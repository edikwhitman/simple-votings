from django import forms


class SignInForm(forms.Form):
    user_name = forms.CharField(label="Логин:", widget=forms.TextInput(attrs={'class': 'float-right'}))
    user_email = forms.EmailField(label="Email:", widget=forms.TextInput(attrs={'class': 'float-right'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'float-right'}), label="Пароль:")
    password_conf = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'float-right'}),
                                    label="Подтвердите пароль:")


class ReportForm(forms.Form):
    link = forms.CharField(label="Ссылка на голосование:", widget=forms.TextInput(
        attrs={'class': 'float-right form-control'}))
    text = forms.CharField(label="Ваша жалоба:", widget=forms.Textarea(
        attrs={'rows': '5', 'style': 'width: 100%;', 'class': 'form-control', 'placeholder': 'УДОЛИТЕ!!1!'}))
