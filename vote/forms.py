from django import forms


class SignInForm(forms.Form):
    user_name = forms.CharField(label="Имя пользователя:")
    user_email = forms.EmailField(label="Email: ")
    password = forms.CharField(label="Пароль:")
    password_conf = forms.CharField(label="Подтвердите пароль:")
