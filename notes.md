# Notatki

## Lab 01

- klient i serwer,
- frontend i backend,
- request i response,
- GET i POST.

## Lab 02

- środowisko wirtualne,
- Git,
- GitHub,
- commit,
- push,
- pull.

## Lab 03

- struktura dokumentu HTML (`<!DOCTYPE>`, `html`, `head`, `body`),
- nagłówki, akapity, listy, linki, obrazy, tabele,
- `div` oraz elementy semantyczne (`header`, `nav`, `main`, `section`, `article`, `footer`),
- strona uruchamiana przez HTTP: `python -m http.server`.

## Lab 04

- DOM — drzewo dokumentu (rodzic / dziecko),
- formularze: `form`, `label`, `input`, `select`, `textarea`, `button`,
- atrybuty `name`, `placeholder`, `required`, `value`,
- GET — dane w adresie (`?query=Solaris`), POST — dane w treści żądania.

## Lab 05

- CSS: selektor elementu, klasy (`.klasa`), id (`#id`), atrybutu (`input[type="text"]`),
- kolory, czcionki, jednostki (`px`, `%`, `rem`),
- box model (`margin`, `border`, `padding`, `box-sizing`),
- dziedziczenie i kaskadowość.

## Lab 06

- Flexbox: `display: flex`, `gap`, `flex-direction`, `justify-content`, `align-items`, `flex-wrap`,
- `flex: 1 1 250px`,
- responsywność i `@media (max-width: ...)`,
- Flexbox Froggy: https://flexboxfroggy.com/#pl

## Lab 07

- `django-admin startproject config .`, `python manage.py startapp biblioteka`,
- projekt (konfiguracja) vs aplikacja (funkcjonalność),
- `manage.py runserver`, `manage.py check`,
- widok = funkcja `request -> HttpResponse`,
- routing: `config/urls.py` -> `include` -> `biblioteka/urls.py` -> widok.

## Lab 08

- szablony w `biblioteka/templates/biblioteka/`,
- `render(request, szablon, context)`,
- `{% extends %}`, `{% block %}`, `{{ zmienna }}`, `{% for %}` / `{% empty %}`, `{% if %}`,
- `{% url 'nazwa' %}` zamiast wpisywania adresów,
- pliki statyczne: `{% load static %}`, `{% static 'biblioteka/css/styles.css' %}`.

---

## Lab 07 — Zadanie 4: adresy dla własnej aplikacji (przykład: Planer nauki)

```text
/tasks/          -> task_list
/tasks/add/      -> task_add
/tasks/5/        -> task_detail
/subjects/       -> subject_list
```

## Lab 08 — Zadanie 5: podział szablonów własnego projektu (przykład: Planer nauki)

```text
base.html          — wspólny header, nav, footer
task_list.html     — lista zadań
task_detail.html   — szczegóły zadania
task_form.html     — formularz dodawania / edycji zadania
subject_list.html  — lista przedmiotów
```
