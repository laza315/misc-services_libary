from django.urls import path

from . import views as user_views

app_name = 'item'

urlpatterns = [
    path('', user_views.items, name='items'),
    path('new/', user_views.new, name='new'),
    path('<int:pk>/', user_views.detail, name='detail'),
    path('<int:pk>/delete/', user_views.delete, name='delete'),
    path('<int:pk>/edit/', user_views.edit, name='edit'),

]
