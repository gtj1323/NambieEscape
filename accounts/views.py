from django.shortcuts import render, redirect, HttpResponse
from django_telegram_login.widgets.constants import LARGE, DISABLE_USER_PHOTO
from django_telegram_login.widgets.generator import create_redirect_login_widget, create_redirect_login_widget
from django.conf import settings
from django_telegram_login.authentication import verify_telegram_authentication
from django_telegram_login.errors import NotTelegramDataError, TelegramDataIsOutdatedError

bot_name = settings.TELEGRAM_BOT_NAME
bot_token = settings.TELEGRAM_BOT_TOKEN
redirect_url = settings.TELEGRAM_LOGIN_REDIRECT_URL

def index(request):
    # Initially, the index page may have no get params in URL
    # For example, if it is a home page, a user should be redirected from the widget
    if not request.GET.get('hash'):
        return HttpResponse('Handle the missing Telegram data in the response.')
    try:
        result = verify_telegram_authentication(bot_token=bot_token, request_data=request.GET)
    except TelegramDataIsOutdatedError:
        return HttpResponse('Authentication was received more than a day ago.')
    except NotTelegramDataError:
        return HttpResponse('The data is not related to Telegram!')
    # Or handle it as you wish. For instance, save to DB.
    return HttpResponse('Hello, ' + result['first_name'] + '!')

def login(request):
    telegram_login_widget = create_redirect_login_widget(
            redirect_url,
            bot_name,
            size=LARGE,
            # user_photo = DISABLE_USER_PHOTO
        )

    context = {'telegram_login_widget': telegram_login_widget}
    return render(request, 'accounts/login.html', context)

