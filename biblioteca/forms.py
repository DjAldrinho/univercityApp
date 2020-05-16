from django import forms

from biblioteca.models import Reserva, Cliente


class ReservaForm(forms.ModelForm):
    class Meta:
        model = Reserva
        fields = "__all__"


class ClienteForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = Cliente
        fields = "__all__"
