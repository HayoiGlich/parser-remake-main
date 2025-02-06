document.addEventListener('DOMContentLoaded', function() {
    // Инициализация
    initTabs();
    initModals();
    initPagination();
    initFilters();
    initAuth();
});

function initTabs() {
    document.querySelectorAll('.tab').forEach(tab => {
        tab.addEventListener('click', () => {
            document.querySelector('.tab.active').classList.remove('active');
            tab.classList.add('active');
            
            document.querySelector('.content-section.active').classList.remove('active');
            document.getElementById(tab.dataset.tab).classList.add('active');
        });
    });
}

function initModals() {
    // Логика модальных окон
    const modals = {
        addLicense: document.getElementById('addLicenseModal'),
        addProduct: document.getElementById('addProductModal')
    };

    // Открытие/закрытие модалок
    document.querySelectorAll('[data-modal]').forEach(btn => {
        btn.addEventListener('click', () => {
            const modalId = btn.dataset.modal;
            if (modals[modalId]) {
                modals[modalId].classList.add('show');
            }
        });
    });

    // Закрытие по клику вне окна
    window.addEventListener('click', (e) => {
        if (e.target.classList.contains('modal')) {
            e.target.classList.remove('show');
        }
    });
}

function initPagination() {
    // Логика пагинации
    document.querySelectorAll('.page-item').forEach(item => {
        item.addEventListener('click', async () => {
            const page = item.dataset.page;
            await loadData(page);
        });
    });
}

async function loadData(page = 1) {
    try {
        const response = await fetch(`/api/licenses?page=${page}`);
        const data = await response.json();
        updateTable(data);
    } catch (error) {
        console.error('Ошибка загрузки данных:', error);
    }
}

function updateTable(data) {
    // Обновление таблицы
}

function initFilters() {
    // Логика фильтрации
}

function initAuth() {
    // Логика авторизации
    document.getElementById('logoutBtn').addEventListener('click', () => {
        fetch('/logout', { method: 'POST' })
            .then(() => window.location.href = '/auth');
    });
}

// Подтверждение действий
function confirmAction(message, callback) {
    if (confirm(message)) {
        callback();
    }
}