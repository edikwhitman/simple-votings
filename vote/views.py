import datetime
from os import path

from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import check_password
from django.http import HttpResponseRedirect
from django.shortcuts import render
from vote.forms import SignInForm, ReportForm
from django.contrib.auth.models import User
import hashlib
from vote.models import ReportModel, VoteModel, CheckedVoting
import vote.functions as f_m  # Вспомогательные функции. Вынесены для сокращения кода в views.py


def not_found(request):
    context = f_m.get_base_context(request)
    context['title'] = '404'

    return render(request, '404.html', context)


def index_page(request):
    context = f_m.get_base_context(request)
    context['title'] = 'Главная страница - simple votings'
    context['main_header'] = 'Simple votings'

    return render(request, 'index.html', context)


def vote(request, pk=''):
    context = f_m.get_base_context(request)
    context['title'] = 'Голосование'

    if pk:
        if VoteModel.objects.filter(ref=pk):
            v = VoteModel.objects.filter(ref=pk)[0]

            if request.user.is_anonymous:
                context['done'] = True
            else:
                if CheckedVoting.objects.filter(user=User.objects.filter(username=request.user)[0], voting_id=v):
                    context['done'] = True
                else:
                    context['done'] = False

                if request.method == 'POST' and not context['done']:
                    checked = list(map(int, request.POST.getlist('form')))
                    counts = list(map(int, v.vote_counts.split('\x06')))

                    for i in checked:
                        counts[i - 1] += 1

                    v.vote_counts = '\x06'.join(list(map(str, counts)))
                    v.save()

                    context['done'] = True

                    CheckedVoting(user=User.objects.filter(username=request.user)[0], voting_id=v).save()

            options = v.options.split('\x06')
            percents = list(map(int, v.vote_counts.split('\x06')))
            options_sum = sum(percents)
            if options_sum == 0:
                for i in range(len(percents)):
                    percents[i] = 0
            else:
                x = 100
                for i in range(len(percents) - 1):
                    if percents[i] != 0:
                        percents[i] = int(percents[i] / options_sum * 100)
                        if percents[i] == 0:
                            percents[i] = 1
                        x -= percents[i]
                percents[len(percents) - 1] = x

            options_fin = list()

            for i in range(len(options)):
                options_fin.append({'option': options[i], 'percent': percents[i], 'index': i + 1})

            context['options'] = options_fin
            context['percents'] = percents
            context['options_sum'] = options_sum
            context['vote'] = v
            context['can_edit'] = request.user.id == v.creator_id

            return render(request, 'vote.html', context)
        else:
            return HttpResponseRedirect('/404/')
    else:
        return HttpResponseRedirect('/search_vote/')



@login_required
def profile(request):
    context = f_m.get_base_context(request)
    context['title'] = 'Профиль'
    user = User.objects.filter(username=request.user)[0]
    end = ['.jpg', '.png', '.gif', '.jpeg']
    Image = {'have': False, 'src': 'none'}
    for i in end:
        if path.exists('static/img_profile/' + str(user) + i):
            Image['have'] = True
            Image['src'] = 'img_profile/' + str(user) + i
        else:
            Image['have'] = False
        if Image['have']:
            break
    context['image'] = Image

    return render(request, 'profile.html', context)

def update_votes_db(question, options, type, dt, ref, vote_counts):
    db = VoteModel.objects.filter(ref=ref)
    db.update(question=question, options=options, type=type, closing_time=dt, ref=ref, vote_counts=vote_counts,
                  edited=True)

def fill_votes_db(question, options, type, dt, ref, vote_counts, user_id):
    db = VoteModel(question=question, options=options, type=type, closing_time=dt, ref=ref, vote_counts=vote_counts, creator_id=user_id)
    db.save()


@login_required
def create_vote(request):
    context = f_m.get_base_context(request)
    context['title'] = 'Create a poll'
    if len(request.GET) > 0:
        if VoteModel.objects.get(ref = request.GET.get('ref', 0)).creator_id != request.user.id:
            return HttpResponseRedirect("/404/")
        context['title'] = 'Edit a poll'
        print("Ok, get")
        ref = request.GET.get('ref', 0)
        db = VoteModel.objects.get(ref=ref);
        context['question'] = db.question
        context['type'] = db.type
        context['ref'] = db.ref
        context['options'] = db.options
        context['vote_counts'] = db.vote_counts
        context['closing_date'] = db.closing_time.strftime("%Y-%m-%d")
        context['closing_time'] = db.closing_time.strftime("%H:%M")
        context['edit'] = '1'
    elif len(request.POST) > 0:
        print("Ok, post")
        print("Get Post Request")
        question = request.POST.get('question', 0)
        options = request.POST.get('options', 0)
        type = request.POST.get('type', 0)
        vote_counts = request.POST.get('vote_counts', 0)
        dt = datetime.datetime.strptime(request.POST.get('date') + " " + request.POST.get('time'), '%Y-%m-%d %H:%M')
        hash_link = request.POST.get('hash_link', 0)
        if len(VoteModel.objects.filter(ref = hash_link)) and VoteModel.objects.get(ref = hash_link).creator_id == request.user.id :
            update_votes_db(question, options, type, dt, hash_link, vote_counts)
        else:
            fill_votes_db(question, options, type, dt, hash_link, vote_counts, request.user.id)
    else:
        print("No Request")
    return render(request, 'create_vote.html', context)


def sign_up(request):
    context = f_m.get_base_context(request)
    context['title'] = 'Регистрация'
    context['errors'] = []

    if request.method == 'POST':
        f = SignInForm(request.POST)

        if f.is_valid():
            u_n = f.data['user_name']
            u_em = f.data['user_email']
            u_pw = f.data['password']
            u_pw_c = f.data['password_conf']

            if not f_m.is_existing_user(User.objects.all(), u_n):
                if u_pw == u_pw_c:
                    new_user = User.objects.create_user(username=u_n, email=u_em, password=u_pw)
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

    return render(request, 'registration/sign_up.html', context)


@login_required
def report(request):
    context = f_m.get_base_context(request)
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
        context['ref'] = request.GET.get('ref', '')

    context['form'] = f

    return render(request, 'report.html', context)


def search_page(request):
    context = f_m.get_base_context(request)
    context['title'] = 'Поиск'
    votings = VoteModel.objects.all()
    checked_votings = CheckedVoting.objects.filter(user=request.user.id)

    if len(request.GET) > 0:
        request_str = str(request.GET.get('q')).lower()
        author = request.GET.get('author')

        if author is not None:
            if f_m.is_existing_user(User.objects.all(), author):
                author = User.objects.get(username=author)
                votings = VoteModel.objects.filter(creator=author.id)
            else:
                votings = []

        r_words = request_str.split()
        show_votings = {}
        votings_score = []

        score_init_value = f_m.search_get_init_val(request_str, author)

        for voting in votings:
            score = score_init_value

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

        for voting in votings:
            voting.is_new = f_m.is_new_voting(checked_votings, voting)

        context['votings'] = votings
        context['result'] = len(votings)
        context['mode'] = 1

    else:
        for voting in votings:
            voting.is_new = f_m.is_new_voting(checked_votings, voting)

        votings = reversed(votings)

        context['votings'] = votings
        context['mode'] = 0

    return render(request, 'search.html', context)


@login_required
def report_status(request):
    context = f_m.get_base_context(request)
    context['title'] = 'Статус жалобы'
    context['reports'] = ReportModel.objects.filter(author=request.user)

    return render(request, 'report_status.html', context)


def contacts(request):
    context = f_m.get_base_context(request)

    return render(request, 'contact.html', context)


def support(request):
    context = f_m.get_base_context(request)

    return render(request, 'support.html', context)


@login_required
def my_votings(request):
    context = f_m.get_base_context(request)
    context['title'] = 'My votings'

    if VoteModel.objects.filter(creator=User.objects.filter(username=request.user)[0]):
        context['votings'] = VoteModel.objects.filter(creator=User.objects.filter(username=request.user)[0])

    return render(request, 'my_votings.html', context)


@login_required
def votings_i_answered(request):
    context = f_m.get_base_context(request)
    context['title'] = 'Votings i answered'

    if CheckedVoting.objects.filter(user=User.objects.filter(username=request.user)[0]):
        context['votings'] = CheckedVoting.objects.filter(user=User.objects.filter(username=request.user)[0])

    return render(request, 'votings_i_answered.html', context)


@login_required
def profile_edit(request):
    context = f_m.get_base_context(request)
    context['title'] = 'Edit profile'

    user = User.objects.filter(username=request.user)[0]
    if request.method == 'POST':
        if request.POST.get('email', False):
            user.email = request.POST.get('email')
            user.save()
            context['success'] = 'Email успешно изменен'
        if request.POST.get('old_pswd', False):
            if user.check_password(request.POST.get('old_pswd')):
                if request.POST.get('new_pswd') == request.POST.get('conf_pswd'):
                    user.set_password(request.POST.get('new_pswd'))
                    user.save()
                    context['success'] = 'Пароль успешно изменен'
                else:
                    context['error'] = 'Новые пароли не совпадают'
            else:
                context['error'] = 'Старый пароль неверный'

    return render(request, 'profile_edit.html', context)
