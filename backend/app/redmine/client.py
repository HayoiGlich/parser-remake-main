from redminelib import Redmine

# Класс для работы с Redmine через API
class RedmineAPI:
    def __init__(self, api_url, api_key, issue):
        self.redmine = Redmine(api_url, key=api_key)
        self.id = issue.id
        self.subject = issue.subject
        self.description = issue.description
        self.ip = issue.custom_fields[10].value
        self.assigned_to = issue.assigned_to

    

