Underdevelopment FastAPI service that provides secure user management alongside real-time, 7-day historical, and predictive weather data. Built with SQLAlchemy (async ORM), a clean CRUD layer, and asynchronous HTTP calls to an external weather provider with full data validation via Pydantic.
✨ Features

🔐 Secure user management

    User registration and login

    Password hashing (bcrypt/argon2)

    JWT-based authentication & authorization

    Protected routes and per-user data isolation

🌤️ Weather data

    Real-time current conditions

    7-day historical weather

    Predictive (forecast) weather data

    Data fetched asynchronously from an external weather API

    Response validation & normalization before persisting/serving

🧱 Architecture

    FastAPI for routing, DI, and OpenAPI docs

    SQLAlchemy 2.0 async ORM + AsyncSession

    Dedicated CRUD layer separating DB logic from endpoints

    Pydantic schemas for request/response validation

    Async HTTP client (httpx) for external API calls


Находящийся в разработке сервис на FastAPI, который обеспечивает безопасное управление пользователями, а также данные о погоде в реальном времени, за 7 дней (исторические) и прогнозные данные. Построен на SQLAlchemy (асинхронный ORM), с чистым слоем CRUD и асинхронными HTTP-запросами к внешнему погодному провайдеру с полной валидацией данных через Pydantic.
✨ Возможности
🔐 Безопасное управление пользователями

    Регистрация и вход пользователей

    Хеширование паролей (bcrypt/argon2)

    Аутентификация и авторизация на основе JWT

    Защищённые маршруты и изоляция данных по пользователям

🌤️ Данные о погоде

    Текущие условия в реальном времени

    Исторические данные о погоде за 7 дней

    Прогнозные данные о погоде

    Асинхронное получение данных из внешнего погодного API

    Валидация и нормализация ответов перед сохранением/отдачей

🧱 Архитектура

    FastAPI для маршрутизации, внедрения зависимостей (DI) и документации OpenAPI

    SQLAlchemy 2.0 async ORM + AsyncSession

    Выделенный слой CRUD, отделяющий логику работы с БД от эндпоинтов

    Pydantic-схемы для валидации запросов/ответов

<<<<<<< HEAD
    Асинхронный HTTP-клиент (httpx) для вызовов внешнего API
=======
    Асинхронный HTTP-клиент (httpx) для вызовов внешнего API
>>>>>>> d1191b4 (feat: add google auth)
