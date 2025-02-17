const API_BASE_URL = 'http://localhost:8000';  // Ваш FastAPI-сервер

async function fetchData(endpoint, method = 'GET', data = null) {
    const options = {
        method,
        headers: {
            'Content-Type': 'application/json',
            'Authorization': `Bearer ${localStorage.getItem('token')}`  // Если используется JWT
        }
    };

    if (data) {
        options.body = JSON.stringify(data);
    }

    const response = await fetch(`${API_BASE_URL}${endpoint}`, options);
    return await response.json();
}

// Пример: Получение задач из Redmine через ваш бэкенд
export async function getRedmineIssues() {
    return await fetchData('/api/redmine/issues');
}