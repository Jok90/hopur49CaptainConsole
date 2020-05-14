from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'checkout/index.html')

def contact_info(request):
    return render(request, 'checkout/contact_info.html')

def payment_info(request) :
    return render(request, 'checkout/payment_info.html')

def review_info(request) :
    return render(request, 'checkout/review_info.html')

def confirmation(request) :
    return render(request, 'checkout/confirmation.html')


