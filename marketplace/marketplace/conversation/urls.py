from django.urls import path

from . import views as user_view

app_name = 'conversation'

urlpatterns = [
    path('', user_view.inbox, name='inbox'),
    path('new/<int:item_pk>/', user_view.new_conversation, name='new')
]
