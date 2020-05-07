from django import forms

from .models import Post


class PostForm(forms.ModelForm):  # estamos dizendo que esse form e´um modelform, para que o django aplique suas propriedades.

    class Meta:
        model = Post  # dizendo qual modelo deverá ser usado para criar esse formulario
        fields = ('title', 'text',)  # os campos que entrarão no nosso formulário.
