from django.core.wsgi import get_wsgi_application

application = get_wsgi_application()

try:
    from whitenoise.django import DjangoWhiteNoise

    application = DjangoWhiteNoise(application)
except:
    pass
