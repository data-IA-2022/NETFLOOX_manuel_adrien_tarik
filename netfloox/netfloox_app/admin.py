from django.contrib import admin
from netfloox_app.models import AuthUser

from netfloox_app.models import TableListFilms
# run python manage.py inspectdb > models.py
admin.site.register(AuthUser)
admin.site.register(TableListFilms)

