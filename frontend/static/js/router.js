const routes = {
    '/': '<h1>Добро пожаловать!</h1>',
    '/dashboard': renderDashboardPage,  // Функция из dashboard.js
    '/reports': renderReportsPage       // Функция из reports.js
};

async function handleRouting() {
    const path = window.location.hash.substr(1) || '/';
    const app = document.getElementById('app');
    
    if (routes[path]) {
        app.innerHTML = await routes[path]();
    } else {
        app.innerHTML = '<h1>404</h1>';
    }
}

window.addEventListener('hashchange', handleRouting);
window.addEventListener('load', handleRouting);