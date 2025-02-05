document.addEventListener('DOMContentLoaded', () => {
    // Контекстное меню
    const contextMenu = document.querySelector('.context-menu');
    
    // Обработчик правого клика
    document.querySelectorAll('.data-row').forEach(row => {
        row.addEventListener('contextmenu', (e) => {
            e.preventDefault();
            contextMenu.style.display = 'block';
            contextMenu.style.left = `${e.pageX}px`;
            contextMenu.style.top = `${e.pageY}px`;
        });
    });

    // Закрытие контекстного меню
    document.addEventListener('click', () => {
        contextMenu.style.display = 'none';
    });

    // Поиск по таблице
    document.querySelector('.search-input')?.addEventListener('input', function() {
        const filter = this.value.toLowerCase();
        document.querySelectorAll('.data-row').forEach(row => {
            row.style.display = row.textContent.toLowerCase().includes(filter) 
                ? '' 
                : 'none';
        });
    });

    // Выделение всех чекбоксов
    document.getElementById('select-all')?.addEventListener('change', function() {
        const checkboxes = document.querySelectorAll('.data-row input[type="checkbox"]');
        checkboxes.forEach(checkbox => checkbox.checked = this.checked);
    });

    // Пагинация
    document.querySelectorAll('.page-item').forEach(item => {
        item.addEventListener('click', function() {
            document.querySelector('.page-item.active')?.classList.remove('active');
            this.classList.add('active');
        });
    });

    // Логика работы со ссылками
    let linksArray = [];
    
    // Инициализация обработчиков для ссылок
    document.querySelector('.btn-primary')?.addEventListener('click', addLink);
    
    // Динамическое добавление обработчиков удаления
    document.getElementById('linksContainer')?.addEventListener('click', (e) => {
        if(e.target.classList.contains('link-remove')) {
            const index = Array.from(e.target.parentNode.parentNode.parentNode.children)
                .indexOf(e.target.parentNode.parentNode);
            removeLink(index);
        }
    });

    function addLink() {
        const input = document.querySelector('.url-input');
        const url = input.value.trim();
        
        if(url && isValidUrl(url)) {
            linksArray.push(url);
            input.value = '';
            updateLinksDisplay();
        } else {
            alert('Пожалуйста, введите корректный URL');
        }
    }

    function isValidUrl(string) {
        try {
            new URL(string);
            return true;
        } catch (_) {
            return false;
        }
    }

    function updateLinksDisplay() {
        const container = document.getElementById('linksContainer');
        container.innerHTML = linksArray.map((link, index) => `
            <div class="link-item">
                <span>${link}</span>
                <div class="link-actions">
                    <span class="link-remove">×</span>
                </div>
            </div>
        `).join('');
    }

    function removeLink(index) {
        linksArray.splice(index, 1);
        updateLinksDisplay();
    }
});