from django.forms import ModelForm
from django import forms
from .models import Book, Author


class AuthorForm(ModelForm):
    class Meta:
        model = Author
        fields = ["first_name", "last_name", "birthdate",
                  "biography", "personal_website", "country", "picture"]
        widgets = {
            "birthdate": forms.DateInput(attrs={"type": "date"})
        }
        labels = {
            "first_name": "Nome",
            "last_name": "Apelido",
            "birthdate": "Data de Nascimento",
            "biography": "Biografia",
            "personal_website": "Website",
            "country": "Nacionalidade",
            "picture": "Fotografia"
        }

    def __init__(self, *args, **kwargs):
        super(AuthorForm, self).__init__(*args, **kwargs)
        for name, field in self.fields.items():
            if name == "country":
                field.widget.attrs.update({"class": "form-select mb-3"})
            else:
                field.widget.attrs.update({"class": "form-control mb-3"})


class BookForm(ModelForm):
    class Meta:
        model = Book
        fields = ["title", "authors", "publisher",
                  "genre", "publication_date", "summary", "isbn", "pages", "format", "language", "cover"]
        widgets = {
            'publication_date': forms.DateInput(attrs={"type": "date"})
        }
        labels = {
            "title": "Título",
            "authors": "Autor(es)",
            "publisher": "Editora",
            "genre": "Géneros",
            "publication_date": "Data de Publicação",
            "summary": "Resumo",
            "isbn": "ISBN",
            "pages": "Número de páginas",
            "format": "Formato",
            "language": "Idioma",
            "cover": "Capa"
        }

    def __init__(self, *args, **kwargs):
        super(BookForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            if name == "authors" or name == "publisher" or name == "genre" or name == "format" or name == "language":
                field.widget.attrs.update({"class": "form-select"})
            else:
                field.widget.attrs.update({"class": "form-control"})
