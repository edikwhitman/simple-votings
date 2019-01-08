import datetime

from django.shortcuts import render
from vote.forms import SignInForm
from django.contrib.auth.models import User


def get_base_context(request):
    auth = []

    if request.user.is_authenticated:
        auth.append({'link': '/logout', 'text': 'Выйти'})
    else:
        auth.append({'link': '/login', 'text': 'Войти'})
        auth.append({'link': '/signin', 'text': 'Регистрация'})

    context = {
        'menu': [
            {'link': '/', 'text': 'Главная'},
        ],
        'current_time': datetime.datetime.now(),
        'auth': auth,
    }
    return context


def index_page(request):
    context = get_base_context(request)
    context['title'] = 'Главная страница - simple votings'
    context['main_header'] = 'Simple votings'
    return render(request, 'index.html', context)


def vote(request):
    context = get_base_context(request)
    context['title'] = 'Голосование'

    return render(request, 'vote.html', context)


def create_vote(request):
    context = get_base_context(request)
    context['title'] = 'Создание голосования'

    return render(request, 'create_vote.html', context)


def signin(request):
    context = get_base_context(request)

    context['errors'] = []

    if request.method == 'POST':
        f = SignInForm(request.POST)

        if f.is_valid():
            u_n = f.data['user_name']
            u_em = f.data['user_email']
            u_pw = f.data['password']
            u_pw_c = f.data['password_conf']

            if u_pw == u_pw_c:
                new_user = User.objects.create_user(username=u_n, email=u_em, password=u_pw)
                new_user.save()
            else:
                context['errors'].append("Введенные пароли не совпадают")

            context['form'] = f
        else:
            context['form'] = f
    else:
        f = SignInForm()
        context['form'] = f

    return render(request, 'registration/sign_in.html', context)