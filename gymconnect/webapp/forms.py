from django import forms
from .models import Feedback
from .models import ProgressoAluno
from .models import Dados

class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = ['aluno', 'feedback']


class ProgressoForm(forms.ModelForm):
    class Meta:
        model = ProgressoAluno
        fields = ['nome_aluno', 'metrica', 'data', 'progresso_observado']

class LoginForm(forms.Form):
    nome = forms.CharField()
    senha = forms.CharField(widget=forms.PasswordInput)
    tipo = forms.CharField(widget=forms.HiddenInput(), required=False)
    

class CadastroForm(forms.ModelForm):
    class Meta:
        model = Dados
        fields = ['nome', 'senha', 'tipo']
