from django import forms

class ContactFormForm(forms.Form):
    customer_email = forms.EmailField(
        label='Correo electrónico',
        widget=forms.EmailInput(attrs={'placeholder': 'Introduce tu correo electrónico'})
    )
    customer_name = forms.CharField(
        max_length=64,
        label='Nombre',
        widget=forms.TextInput(attrs={'placeholder': 'Introduce tu nombre'})
    )
    message = forms.CharField(
        label='Mensaje',
        widget=forms.Textarea(attrs={'placeholder': 'Introduce tu mensaje', 'rows': 4})
    )

