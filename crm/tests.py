from django.test import TestCase

# Create your tests here.
import os

if __name__ == '__main__':
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "PerfectCRM.settings")
    import django
    django.setup()

    from crm import models

    t = models.UserProfile.objects.all().first().roles.all().first().menus.all()
    print(t)