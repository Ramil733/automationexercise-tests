# AQA для [Automation Exercise](https://automationexercise.com)

## 🎯 Покрытие

- **UI**([link](https://automationexercise.com/test_cases)): аутентификация, регистрация, корзина, оформление заказа, поиск товаров, бренды, отзывы, подписка, форма обратной связи
- **API**([link](https://automationexercise.com/api_list)): товары, бренды, пользователи (создание, обновление, удаление, проверка логина, получение данных)
- **Негативные сценарии**: неверные учётные данные, отсутствующие параметры, неподдерживаемые HTTP-методы

## 🛠 Стек

- **Python 3.9+**
- **Playwright** — UI-автоматизация
- **Pytest** — раннер тестов
- **Requests** — API-тестирование
- **Allure** — отчётность
- **Postman + Newman** — API-коллекция
- **GitHub Actions** — CI/CD

## 🚀 Запуск
```bash
https://github.com/Ramil733/automationexercise-tests
cd aqa-playwright-portfolio
```

```bash
python3 -m venv venv
source venv/bin/activate
```

```bash
pip install -r requirements.txt
```

```bash
playwright install chromium
```

##  Запустить тесты

**Все тесты:**
```bash
pytest
```

**Только UI:**
```bash
pytest tests/ui -v
```

**Только API:**
```bash
pytest tests/api -v
```

**Конкретный тест по имени:**
```bash
pytest -k "test_login" -v
```

**В видимом браузере:**
```bash
pytest tests/ui -v --headed --slowmo 500
```

## 📊 Allure-отчёт
**Сгенерировать и посмотреть отчёт:**

```bash
pytest --alluredir=./allure-results
allure serve ./allure-results
```

##  Postman-коллекция
**Json для импорта:**
https://github.com/Ramil733/automationexercise-tests/tree/main/postman/forImport
