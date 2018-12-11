import datetime

from django.shortcuts import render


def get_base_context():
    context = {
        'menu': [
            {'link': '/', 'text': 'Главная'},
            {'link': '/test', 'text': 'Несуществующая'},
        ],
        'current_time': datetime.datetime.now(),
    }
    return context


def index_page(request):
    context = get_base_context()
    context['title'] = 'Главная страница - simple votings'
    context['main_header'] = 'Simple votings'
    return render(request, 'index.html', context)
