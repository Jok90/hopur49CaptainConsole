from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path, include
from . import views

urlpatterns = [
    # http://localhost:8000/login

    path('signup/', views.register, name='signup'),
    path('', LoginView.as_view(template_name='login/index.html'), name='login'),
    path('logout', LogoutView.as_view(next_page='login'), name='logout')
    # path('wtf', include('django.contrib.auth.urls')
    # )
    # path('login/', include('django.contrib.auth.urls')),

]