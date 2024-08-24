from django.urls import path

from . import views as user_view

app_name = 'dashboard'

urlpatterns = [
    path('', user_view.index, name='index')
]
