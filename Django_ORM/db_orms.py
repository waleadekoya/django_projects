from django.conf import settings
import django

from django_project.settings import INSTALLED_APPS, DATABASES

conf = {
    'INSTALLED_APPS': INSTALLED_APPS,
    'DATABASES': DATABASES,
    'TIME_ZONE': 'UTC'
}

settings.configure(**conf)
django.setup()

from django_project.abinitio_app.models import Company, Language, Programmer

# from here we can interact with the database using Django ORM API
[print(item.comp_name) for item in Company.objects.all()]

[print(item.lang_name) for item in Language.objects.all()]

