from django.shortcuts import render


def home(request):
    context = {
        "books_count": 3,
        "authors_count": 2,
    }
    return render(request, "biblioteka/home.html", context)


def book_list(request):
    books = [
        {
            "title": "Solaris",
            "author": "Stanisław Lem",
            "year": 1961,
            "available": True,
        },
        {
            "title": "Lalka",
            "author": "Bolesław Prus",
            "year": 1890,
            "available": False,
        },
        {
            "title": "Hobbit",
            "author": "J.R.R. Tolkien",
            "year": 1937,
            "available": True,
        },
    ]

    return render(request, "biblioteka/book_list.html", {"books": books})


def author_list(request):
    authors = [
        {"name": "Stanisław Lem", "nationality": "polski"},
        {"name": "Bolesław Prus", "nationality": "polski"},
        {"name": "J.R.R. Tolkien", "nationality": "angielski"},
    ]
    return render(request, "biblioteka/author_list.html", {"authors": authors})


def contact(request):
    return render(request, "biblioteka/contact.html")


def about(request):
    return render(request, "biblioteka/about.html")

def author_list(request):
    return render(
        request,
        "biblioteka/author_list.html",
    )

def contact(request):
    return render(
        request,
        "biblioteka/contact.html",
    )