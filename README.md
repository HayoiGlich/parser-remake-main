project-root/
├── backend/                  # Основная папка бэкенда
│   ├── app/                  
│   │   ├── __init__.py
│   │   ├── main.py           # Точка входа FastAPI
│   │   ├── config.py         # Конфигурация приложения
│   │   ├── database/         # Работа с БД
│   │   │   ├── __init__.py
│   │   │   ├── models.py     # SQLAlchemy модели
│   │   │   └── crud.py       # Операции с БД
│   │   ├── redmine/          # Интеграция с Redmine
│   │   │   ├── __init__.py
│   │   │   ├── client.py     # API клиент для Redmine
│   │   │   └── schemas.py    # Pydantic модели для данных
│   │   ├── routers/          # Роутеры FastAPI
│   │   │   ├── __init__.py
│   │   │   ├── issues.py     # Роуты для работы с issues
│   │   │   └── reports.py    # Генерация отчетов
│   │   ├── printing/         # Генерация PDF
│   │   │   ├── __init__.py
│   │   │   └── pdf_generator.py
│   │   └── utils/            # Вспомогательные модули
│   │       ├── __init__.py
│   │       └── security.py   # Аутентификация
├── frontend/                 # Клиентская часть
│   ├── static/
│   │   ├── js/              # Переименовать в scripts/
│   │   │   ├── dashboard.js 
│   │   │   └── api.js       # API взаимодействие с бэкендом
│   │   └── styles/
│   │       └── styles.css
│   └── templates/           # HTML шаблоны
│       ├── auth.html
│       └── index.html
├── migrations/              # Миграции БД (Alembic)
│   └── versions/
├── tests/                   # Тесты
│   ├── __init__.py
│   └── test_redmine.py      # Переместить сюда из корня
├── .env.example             # Шаблон переменных окружения
├── .gitignore               # Обновить для новой структуры
├── requirements.txt         # Зависимости Python
├── Dockerfile               # Контейнеризация
└── README.md                # Описание проекта