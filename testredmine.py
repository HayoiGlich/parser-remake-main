from redminelib import Redmine
import json
import re

def expand_serial_numbers(serial_value: str):
    serial_numbers = []

    if not isinstance(serial_value, str) or not serial_value.strip():
        return serial_numbers

    # Разбиваем по запятой или точке с запятой
    parts = re.split(r'[;,]', serial_value)

    for part in parts:
        part = part.strip()

        # Проверяем, является ли часть диапазоном (например, "2-0459 - 2-0465")
        match = re.match(r'(\d+)-(\d+) - \1-(\d+)', part)
        if match:
            prefix, start, end = match.groups()
            serial_numbers.extend([f"{prefix}-{str(num).zfill(len(start))}" for num in range(int(start), int(end) + 1)])
        else:
            # Если просто одиночный номер, добавляем его как есть
            serial_numbers.append(part)

    return serial_numbers

def fetch_and_save_issues(
    api_url: str,
    api_key: str,
    limit: int,
    assigned_to_id: str,
    output_file: str
) -> None:
    redmine = Redmine(api_url, key=api_key)

    def issue_to_dict(issue) -> dict:
        """
        id для серийника в custom_fields = 17
        id для ip в custom_fields = 10
        """
        serial_value = issue.custom_fields[17].value
        serial_numbers = expand_serial_numbers(serial_value) if serial_value else []

        return {
            "id": issue.id,
            "subject": issue.subject,
            "description": issue.description,
            "assigned_to": issue.assigned_to.name if hasattr(issue, "assigned_to") and issue.assigned_to else None,
            "ip": issue.custom_fields[10].value,
            "serial_number": serial_numbers,
        }

    tasks = redmine.issue.filter(limit=limit, assigned_to_id=assigned_to_id)
    issues = [issue_to_dict(task) for task in tasks]

    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(issues, f, ensure_ascii=False, indent=4)

if __name__ == "__main__":
    API_URL = "https://tasks.etecs.ru/"
    API_KEY = "918f793bc080e6a52d795dc3b0058d58f47b303f"
    fetch_and_save_issues(API_URL, API_KEY, limit=int(input("Введите число задач: ")), assigned_to_id='me', output_file="issues.json")
