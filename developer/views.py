from django.shortcuts import render
from developer.models import Developer


# Create your views here.
def index(request):
    return render(request, 'developer/index.html', context={'developers': Developer.objects.all().order_by('name')})

