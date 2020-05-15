from django.shortcuts import render
from django.contrib.auth.models import User as DjangoUser
from user.models import User
from django.shortcuts import render, get_object_or_404, redirect
from user.forms.forms import UserCreateForm
from django.contrib.auth.forms import UserCreationForm
import logging

# Create your views here.
def index(request):

    if request.method == 'POST':
        logging.debug('FOR HINGADDDD!!!! body: %s' % request.body)
        pass

    return render(request, 'login/index.html')



def register(request):
    UserCreationForm
    logging.error('======>  for inni register')
    if request.method == 'POST':
        form = UserCreateForm(data=request.POST)
        logging.error('======>  fekk post request')

        if form.is_valid():
            user = form.save()
            django_user = DjangoUser.objects.create_user(user.username, user.email,
                                                         form.cleaned_data['password'] )
            return redirect('user-index')
    else:
        form = UserCreateForm()

    return render(request, 'signup/index.html', {
        'form': form
    })

