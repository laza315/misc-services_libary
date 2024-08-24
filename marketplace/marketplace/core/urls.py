from django.urls import path
from django.contrib.auth import views as auth_views

from . import views as user_view

from . forms import LoginForm

app_name = 'core'

urlpatterns = [
    path('', user_view.index, name='index'),
    path('contact/', user_view.contact, name='contact'),
    path('signup/', user_view.signup, name='signup'),
    path('login/', auth_views.LoginView.as_view(template_name='core/login.html', authentication_form=LoginForm), name='login')

]