import os

from django.core.wsgi import get_wsgi_application

# project_name_settings = "<project_name's>.settings"
# project_name_settings = "dojo_ninjas_main.settings"
project_name_settings = ""

os.environ.setdefault("DJANGO_SETTINGS_MODULE", project_name_settings)
application = get_wsgi_application()

# Example: from <location of models.py in relation to manage.py> import <model names>
from apps.likes_books.models import Users, Books

# users = [['Jimmy', "Crouch", "barty_couch@gmail.com"], ["Jelly", "Bean", "jb@gmail.com"], ['JAckdon', "brown", "jackB@gmail.com"]]

# for usr in users:
#     user = Users()
#     user.first_name = usr[0]
#     user.last_name = usr[1]
#     user.email = usr[2]
#     user.save()