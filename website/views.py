from django.shortcuts import render


def index(request):
    return render(request, 'index.html')


def mainframe(request):
    return render(request, 'mainframe.html')


def contact(request):
    if request.method == "POST":
        first_name = request.POST['firstname']
        last_name = request.POST['lastname']
        email_address = request.POST['emailaddress']
        website_name = request.POST['websitename']
        text_area = request.POST['textarea']
        return render(request, 'contact.html', {'first_name': first_name })
    else:
        return render(request, 'contact.html', {})
