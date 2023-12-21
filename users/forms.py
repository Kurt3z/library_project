from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm


class CustomUserCreationForm(UserCreationForm):
    password1 = forms.CharField(
        label="Palavra-passe",
        widget=forms.PasswordInput,
        help_text="<p>A sua palavra-passe deve:</p><ul>"
                  "<li>Conter pelo menos 8 caracteres.</li>"
                  "<li>Não ser semelhante a outras informações pessoais.</li>"
                  "<li>Não ser uma palavra-passe comum.</li>"
                  "<li>Conter letras, números e símbolos.</li>"
                  "</ul>"
    )

    password2 = forms.CharField(
        label=" Confirmar Palavra-passe",
        widget=forms.PasswordInput,
        help_text="<p>Insira a mesma palavra-passe.</p>"
    )

    class Meta:
        model = User
        fields = ["first_name", "last_name", "email",
                  "username", "password1", "password2"]
        labels = {
            "first_name": "Nome",
            "last_name": "Apelido",
            "email": "Endereço Email",
            "username": "Nome de Utilizador",
        }

    def __init__(self, *args, **kwargs):
        super(CustomUserCreationForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({"class": "form-control mb-3"})
