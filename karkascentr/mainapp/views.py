from django.shortcuts import render


# # Create your views here.
def home(request):
    context = {
        'title': 'Строительство домов',
        'keywords': 'строителство домов, дома под ключ в Брянске, каркасные дома, дома из газобетона'
    }
    return render(request, 'mainapp/home.html', context)
#

def contacts(request):
    return render(request, 'mainapp/contacts.html')
