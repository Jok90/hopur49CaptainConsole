from django.urls import path
from . import views


urlpatterns = [
    #http://localhost:8000/users/
    path('', views.index, name="user-index"),
    path('create_user', views.create_user, name="create_user"),
    path('loginpage', views.loginpage, name="loginpage"),
    path('<int:id>', views.get_user_by_id, name="user_details"),

]
