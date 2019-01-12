import datetime

from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render
from vote.forms import SignInForm, ReportForm, SearchForm
from django.contrib.auth.models import User

from vote.models import ReportModel, VoteModel, CheckedVotings


def get_base_context(request):
    auth = []

    if request.user.is_authenticated:
        auth.append({'link': '/logout', 'text': 'Выйти'})
    else:
        auth.append({'link': '/login', 'text': 'Войти'})
        auth.append({'link': '/sign_up', 'text': 'Регистрация'})

    context = {
        'menu': [
            {'link': '/', 'text': 'Главная'},
            {'link': '/create_vote', 'text': 'Создание голосования'},
            {'link': '/report', 'text': 'Пожаловаться'},
            {'link': '/search_vote', 'text': 'Поиск'},
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


def vote(request, pk=''):
    context = get_base_context(request)
    context['title'] = 'Голосование'

    return render(request, 'vote.html', context)


@login_required
def create_vote(request):
    context = get_base_context(request)
    context['title'] = 'Создание голосования'

    return render(request, 'create_vote.html', context)


def sign_up(request):
    context = get_base_context(request)
    context['title'] = 'Регистрация'
    context['errors'] = []
    if request.method == 'POST':
        f = SignInForm(request.POST)

        if f.is_valid():
            u_n = f.data['user_name']
            u_fn = f.data['user_fname']
            u_ln = f.data['user_lname']
            u_em = f.data['user_email']
            u_pw = f.data['password']
            u_pw_c = f.data['password_conf']

            user_exists = 0
            users = User.objects.all()
            for user in users:
                if user.get_username() == u_n:
                    user_exists = 1
                    break

            if not user_exists:
                if u_pw == u_pw_c:
                    new_user = User.objects.create_user(username=u_n, email=u_em, password=u_pw,
                                                        first_name=u_fn, last_name=u_ln)
                    new_user.save()
                    return HttpResponseRedirect('/login/')
                else:
                    context['errors'].append("Введенные пароли не совпадают")
            else:
                context['errors'].append("Пользователь с таким логином уже существует")

            context['form'] = f
        else:
            context['form'] = f
    else:
        f = SignInForm()
        context['form'] = f

    return render(request, 'registration/sign_in.html', context)


@login_required
def report(request):
    context = get_base_context(request)
    context['title'] = 'Создание жалобы'

    context['success'] = False

    if request.method == 'POST':
        f = ReportForm(request.POST)

        if f.is_valid():
            new_report = ReportModel(text=f.data['text'], link=f.data['link'], author=request.user)
            new_report.save()

            f = ReportForm()
            context['success'] = True
    else:
        f = ReportForm()

    context['form'] = f

    return render(request, 'report.html', context)


@login_required
def search_page(request):
    context = get_base_context(request)
    context['title'] = 'Поиск'
    votings = VoteModel.objects.all()

    if request.method == 'POST':
        f = SearchForm(request.POST)

        if f.is_valid():
            request_str = f.data['request_str'].lower()
            r_words = request_str.split()

            show_votings = {}
            votings_score = []

            for voting in votings:
                score = 0
                for word in r_words:
                    if (voting.question.lower()).find(word) != -1:
                        score += 1
                if score > 0:
                    if show_votings.get(str(score), -1) == -1:
                        show_votings[str(score)] = list()
                    show_votings[str(score)].append(voting)

            keys = show_votings.keys()
            for key in keys:
                votings_score.append(int(key))

            votings = []
            votings_score.sort(reverse=True)

            for score in votings_score:
                for item in show_votings[str(score)]:
                    votings.append(item)

            context['votings'] = votings

    else:
        f = SearchForm()
        checked_votings = CheckedVotings.objects.filter(user=request.user.id)

        for voting in votings:
            voting.is_new = True
            for item in checked_votings:
                if item.voting_id.id == voting.id:
                    voting.is_new = False

        votings = reversed(votings)

        context['votings'] = votings

    context['form'] = f

    return render(request, 'search.html', context)


def report_status(request):
    context = get_base_context(request)
    context['title'] = 'Статус жалобы'

    context['reports'] = ReportModel.objects.filter(author=request.user)

    return render(request, 'report_status.html', context)
