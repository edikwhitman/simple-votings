from django import forms


class SignInForm(forms.Form):
    user_name = forms.CharField(label="Логин:")
    user_fname = forms.CharField(label="Имя:")
    user_lname = forms.CharField(label="Фамилия:")
    user_email = forms.EmailField(label="Email: ")
    password = forms.CharField(widget=forms.PasswordInput, label="Пароль:")
    password_conf = forms.CharField(widget=forms.PasswordInput, label="Подтвердите пароль:")


class ReportForm(forms.Form):
    link = forms.CharField(label="Ссылка на голосование")
    text = forms.CharField(label="Ваша жалоба", widget=forms.Textarea)
