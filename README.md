### Проект "Игра в угадывание слова"

![Guess The Word](https://img.shields.io/badge/GuessTheWord-Django-brightgreen)

Проект "Игра в угадывание слова" представляет собой онлайн-игру, в которой один пользователь придумывает слово, а другие участники пытаются отгадать его. Игра начинается с того момента, когда один из участников создает комнату, придумывает слово и открывает её для других игроков. Остальные участники присоединяются к комнате и начинают отгадывать придуманное слово.

Когда слово будет успешно отгадано одним из участников, комната автоматически закрывается. После этого пользователи могут начать новую игру, создав новую комнату, либо присоединиться к уже существующей.

### Установка и запуск

Для установки и запуска проекта выполните следующие инструкции:

1. **Клонирование репозитория:**

```bash
git clone https://github.com/Adik8712/Guess-The-Word.git
cd Guess-The-Word/
```

2. **Создание и активация виртуального окружения:**

```bash
python3 -m venv venv
source venv/bin/activate  # для Linux / macOS
venv\Scripts\activate  # для Windows
```

3. **Установка зависимостей:**

```bash
pip install -r requirements.txt
```

4. **Применение миграций и создание суперпользователя:**

```bash
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
```

5. **Запуск сервера:**

```bash
python manage.py runserver
```

6. **Доступ к приложению:**

После запуска сервера перейдите по адресу [http://localhost:8000](http://localhost:8000) в вашем браузере.

### Структура проекта

```
├── GuessTheWord/
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── main/
│   ├── admin.py
│   ├── migrations/
│   │   └── ...
│   ├── models.py
│   ├── tests.py
│   ├── utils.py
│   ├── views.py
│   └── ...
├── static/
│   ├── css/
│   │   └── main.css
│   ├── image/
│   └── js/
├── templates/
│   ├── base.html
│   ├── index.html
│   ├── login.html
│   ├── main.html
│   ├── registration.html
│   └── room.html
├── .gitignore
├── db.sqlite3
├── manage.py
├── README.md
├── requirements.txt
└── ...
```

### Участники

- Разработчик: Adik
  - GitHub: [Adik8712](https://github.com/Adik8712)
  - Telegram: [AdikPy](https://t.me/AdikPy)

### Лицензия

Этот проект лицензирован по лицензии MIT - см. файл [LICENSE](LICENSE) для получения дополнительной информации.

Не стесняйтесь вносить свой вклад в проект, открывая проблемы или отправляя запросы на объединение изменений (pull requests)! Если у вас возникли проблемы или есть предложения по улучшению, пожалуйста, дайте [мне](https://t.me/AdikPy) знать. Удачного кодирования! 🚀