# Благотворительный фонд поддержки котиков
### Автор 
- [Вадим Крамаренко](https://github.com/litlmayn "GitHub аккаунт")

### Стэк технологий:
```
Python 3.9
FastApi
SQLAlchelmy
```

Клонировать репозиторий и перейти в него в командной строке:

```
git@github.com:litlmayn/cat_charity_fund.git
```

```
cd cat_charity_fund
```

Cоздать и активировать виртуальное окружение:

```
python3 -m venv venv
```

* Если у вас Linux/macOS

    ```
    source venv/bin/activate
    ```

* Если у вас windows

    ```
    source venv/scripts/activate
    ```

Установить зависимости из файла requirements.txt:

```
python3 -m pip install --upgrade pip
```

```
pip install -r requirements.txt
```
Создать файл настроек окружения:
```
touch .env
```
Заполните его по примеру:
```
DATABASE_URL = sqlite+aiosqlite:///./fastapi.db
SECRET = sochetaniesimvolov
```

Запуск проекта:
```
uvicorn app.main:app --reload
```
### Документация:

Документация находиться по ссылке '/docs'
