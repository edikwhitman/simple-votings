from django import forms


class SignInForm(forms.Form):
    user_name = forms.CharField(label="Логин:", widget=forms.TextInput(attrs={'class': 'float-right'}))
    user_fname = forms.CharField(label="Имя:", widget=forms.TextInput(attrs={'class': 'float-right'}))
    user_lname = forms.CharField(label="Фамилия:", widget=forms.TextInput(attrs={'class': 'float-right'}))
    user_email = forms.EmailField(label="Email:", widget=forms.TextInput(attrs={'class': 'float-right'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'float-right'}), label="Пароль:")
    password_conf = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'float-right'}),
                                    label="Подтвердите пароль:")


class ReportForm(forms.Form):
    link = forms.CharField(label="Ссылка на голосование:")
    text = forms.CharField(label="Ваша жалоба:", widget=forms.Textarea)
