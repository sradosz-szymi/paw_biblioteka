# Biblioteka

Projekt ćwiczeniowy rozwijany podczas laboratoriów z przedmiotu
**Projektowanie aplikacji webowych**.

## Cel

Celem projektu jest stopniowe poznanie podstaw:

- HTML,
- CSS,
- Django,
- baz danych,
- formularzy,
- operacji CRUD,
- uwierzytelniania użytkowników,
- podstaw API REST.

> Projekt „Biblioteka” jest projektem dydaktycznym i nie może zostać
> wykorzystany jako temat projektu zaliczeniowego.

## Planowane funkcje

- lista książek i szczegóły książki,
- lista autorów,
- dodawanie, edycja i usuwanie danych,
- logowanie użytkowników,
- wypożyczenia.

## Uruchomienie

```bash
python -m venv .venv

# Windows (PowerShell)
.venv\Scripts\Activate.ps1
# Windows (CMD)
.venv\Scripts\activate.bat
# Linux / macOS
source .venv/bin/activate

python -m pip install -r requirements.txt
python manage.py runserver
```

Aplikacja: <http://127.0.0.1:8000/>

Dostępne adresy:

| Adres | Widok | Szablon |
|---|---|---|
| `/` | `home` | `home.html` |
| `/books/` | `book_list` | `book_list.html` |
| `/authors/` | `author_list` | `author_list.html` |
| `/contact/` | `contact` | `contact.html` |
| `/about/` | `about` | `about.html` |

Statyczny prototyp z lab 03–06 znajduje się w katalogu `frontend/`
(otwórz `frontend/index.html` w przeglądarce). Django już go nie używa.

## Autor

Imię Nazwisko
