from django.urls import path
from main.views import (
    index, user_registration,
    main_page, user_login, user_logout, room_connection
)


urlpatterns = [
    path('', index, name='index-page'),
    path('sign-up/', user_registration, name='sign-up'),
    path('main/', main_page, name="main-page"),
    path('sign-in/', user_login, name='sign-in'),
    path('sign-out/', user_logout, name='sign-out'),
    path('room/<int:room_id>/', room_connection, name='room')
]
