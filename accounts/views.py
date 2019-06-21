from django.shortcuts import render
from django_telegram_login.widgets.constants import LARGE, DISABLE_USER_PHOTO
from django_telegram_login.widgets.generator import create_redirect_login_widget

def redirect(request):
    telegram_login_widget = create_redirect_login_widget(
            redirect_url,
            bot_name,
            size=LARGE,
            user_photo = DISABLE_USER_PHOTO
        )

    context = {'telegram_login_widget': telegram_login_widget}
    return render(request, 'telegram_auth/redirect.html', context)

# def index