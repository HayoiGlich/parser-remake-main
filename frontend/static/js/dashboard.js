export async function renderDashboardPage() {
    const data = await getRedmineIssues();  // Запрос к вашему API
    return `
        <h2>Задачи из Redmine</h2>
        <table class="table table-striped">
            <thead>
                <tr>
                    <th>ID</th>
                    <th>Название</th>
                    <th>Статус</th>
                </tr>
            </thead>
            <tbody>
                ${data.map(issue => `
                    <tr>
                        <td>${issue.id}</td>
                        <td>${issue.title}</td>
                        <td>${issue.status}</td>
                    </tr>
                `).join('')}
            </tbody>
        </table>
    `;
}