from django.shortcuts import render, get_object_or_404, redirect
from user.forms.forms import UserCreateForm, UserUpdateForm
from django.contrib.auth.models import User as DjangoUser
from user.models import User
import logging

from user.forms.forms import UserCreateForm
# Create your views here.

def index(request):
    return render(request, 'user/index.html', context={'users': User.objects.all().order_by('name')})

def create_user(request):
    if request.method == 'POST':
        form = UserCreateForm(data=request.POST)

        if form.is_valid():
            user = form.save()
            django_user = DjangoUser.objects.create_user(user.username, user.email,
                                                         form.cleaned_data['password'] )
            return redirect('user-index')
    else:
        form = UserCreateForm()

    return render(request, 'user/create_user.html', {
        'form': form
    })

def loginpage(request):
    return render(request, 'user/loginpage.html', {
    })

def get_user_by_id(request, id):
    return render(request, 'user/user_details.html', {
        'user': get_object_or_404(User, email=request.user.email)
    })

def update_user(request, id):
    logging.error("-------asdasdasd------")
    instance = get_object_or_404(User, email=request.user.email)
    if request.method == 'POST':
        form = UserUpdateForm(data=request.POST, instance=instance)
        if form.is_valid():
            form.save()
            return redirect('user_details', id=id)
    else:
        logging.error("-------asdasdasd------")
        form = UserUpdateForm(instance=instance)
    return render(request, 'user/update_user.html', {
        'form': form,
        'id': id
    })