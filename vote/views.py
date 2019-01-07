import datetime

from django.shortcuts import render


def get_base_context():
    context = {
        'menu': [
            {'link': '/', 'text': 'Главная'},
        ],
        'current_time': datetime.datetime.now(),
    }
    return context


def index_page(request):
    context = get_base_context()
    context['title'] = 'Главная страница - simple votings'
    context['main_header'] = 'Simple votings'
    return render(request, 'index.html', context)


def vote(request):
    context = get_base_context()
    context['title'] = 'Голосование'

    return render(request, 'vote.html', context)


def create_vote(request):
    context = get_base_context()
    context['title'] = 'Создание голосования'

    return render(request, 'create_vote.html', context)
