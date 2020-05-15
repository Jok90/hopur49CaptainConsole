from django.shortcuts import render
from user import views

# Create your views here.
def index(request):
    return render(request, 'edit/index.html')
