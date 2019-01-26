import datetime


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


def is_new_voting(checked_votings_list, voting):
    for item in checked_votings_list:
        if item.voting_id.id == voting.id:
            return False

    return True


def is_existing_user(users_list, username):
    for user in users_list:
        if user.username == username:
            return True

    return False


def search_get_init_val(request_str, author):
    if (author == None) or (request_str != "none"):
        return 0
    elif request_str == 'none':
        return 1


