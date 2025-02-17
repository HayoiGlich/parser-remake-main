export async function renderReportsPage() {
    return `
        <h2>Генерация отчетов</h2>
        <button class="btn btn-primary" onclick="generateExcel()">Создать Excel</button>
        <button class="btn btn-success" onclick="generateDocx()">Создать DOCX</button>
    `;
}

// Генерация Excel
window.generateExcel = async () => {
    const response = await fetch(`${API_BASE_URL}/api/reports/excel`, {
        headers: {
            'Authorization': `Bearer ${localStorage.getItem('token')}`
        }
    });
    const blob = await response.blob();
    const url = window.URL.createObjectURL(blob);
    const a = document.createElement('a');
    a.href = url;
    a.download = 'report.xlsx';
    a.click();
};

// Генерация DOCX (аналогично)
window.generateDocx = async () => { ... };