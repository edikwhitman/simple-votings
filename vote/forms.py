from django import forms


class SignInForm(forms.Form):
    user_name = forms.CharField(label="Имя пользователя:")
    user_email = forms.EmailField(label="Email: ")
    password = forms.CharField(widget=forms.PasswordInput, label="Пароль:")
    password_conf = forms.CharField(widget=forms.PasswordInput, label="Подтвердите пароль:")
