from django.forms import ModelForm
from django import forms

from .models import Publisher, Genre, Country


class CountryForm(ModelForm):
    class Meta:
        model = Country
        exclude = ["created"]
        labels = {
            "name": "País",
            "code": "Código",
            "flag": "Bandeira"
        }

    def __init__(self, *args, **kwargs):
        super(CountryForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({"class": "form-control mb-3"})


class GenreForm(ModelForm):
    class Meta:
        model = Genre
        exclude = ["created"]
        labels = {
            "caption": "Género"
        }

    def __init__(self, *args, **kwargs):
        super(GenreForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({"class": "form-control mb-3"})


class PublisherForm(ModelForm):
    class Meta:
        model = Publisher
        exclude = ["created"]
        labels = {
            "name": "Editora",
            "email": "Endereço Email",
            "website": "Website",
            "logo": "Logótipo"
        }

    def __init__(self, *args, **kwargs):
        super(PublisherForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({"class": "form-control mb-3"})
