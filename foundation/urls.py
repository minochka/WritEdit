from django.urls import path

from .views import signup_user, login_user, Home, logout_user, posts_detail, delete, people_list, people_detail, like, dislike, settingi


urlpatterns = [
    # Auth
    path('signup/', signup_user, name='signup'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),

    path('', Home, name='home'),
    path('posts/<int:id>/', posts_detail, name='posts_detail'),
    path('posts/<int:id>/delete/', delete, name='delete'),
    path('posts/<int:id>/like', like, name='like'),
    path('posts/<int:id>/dislike', dislike, name='dislike'),
    path('settingi/', settingi, name='settingi'),

    path('people/', people_list, name='people_list'),
    path('people/<int:id>', people_detail, name='people_detail')
]