from django.shortcuts import render
from main.models import Page
from django.core.mail import send_mail

def main(request):
    #page = Page.objects.filter(alias='main')
    page = Page.objects.get(alias='main')
    return render(request,'index.html', {"page": page})

def page(request, page_name):
    page = Page.objects.get(alias=page_name)
    return render(request,'index.html', {"page": page})


def contact(request):
    print('Contact page')
    if request.method == 'POST':
        username = request.POST.get('username','Null')
        content = request.POST.get('content','Null')
        send_mail(
            'Test email from %s' % username,
            'Message: %s.' % content, 
            'from@example.com',
            ['to@example.com'],
            fail_silently=False,
        )
    return render(request,'contact.html')