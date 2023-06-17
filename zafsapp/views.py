from django.shortcuts import render, get_object_or_404,redirect
from django.http import HttpResponse
from django.core.mail import send_mail
from django.contrib.admin.views.decorators import staff_member_required
from PIL import Image
from django.conf import settings
from django.http import JsonResponse
from django.core.exceptions import ObjectDoesNotExist
from .models import *

# Create your views here.

def Home(request):
    return render(request, 'home.html')

def Donate(request):
    return render(request, 'donate.html')

def publication_api(request):
    try:
        # Retrieve the latest publication from the database
        latest_publication = Publication.objects.latest('id')

        # Prepare the publication data
        publication_data = {
            'photo_url': latest_publication.photo.url,
            'title': latest_publication.title,
            'context': latest_publication.context,
        }

        # Pass the publication data to the template for rendering
        return render(request, 'publication.html', {'publication': publication_data})

    except ObjectDoesNotExist:
        error_message = 'No publication found'
        return render(request, 'index.html', {'error': error_message})
        
def Join(request):
    if request.method=="POST":
        memberdata = member.objects.create(
            first_name = request.POST['first_name'],
            middel_name = request.POST['middel_name'],
            last_name = request.POST['last_name'],
            phone_number = request.POST['phone_number'],
            email = request.POST['email'],
            how_know = request.POST['how_know'])

        
        memberdata.save()
        return redirect ('home')
    return render(request,'joinus.html')
    

def Contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        # Additional form validation and processing logic can be added here
        send_mail(
            'Contact Form Submission',
            f'Name: {name}\nEmail: {email}\nMessage: {message}',
            settings.DEFAULT_FROM_EMAIL,
            ['dafamabelnansak@gmail.com'],
            fail_silently=False,
        )
        return render(request, 'contact.html', {'success': True})
    return render(request, 'contact.html')


def Member(request):
    memberdata = member.objects.all()
    context = {'data': memberdata}
    return render(request, 'member.html', context)
    

def team_information(request):
    teams = Team.objects.all()
    return render(request, 'about.html', {'teams': teams})


def gallery(request):
    images = Gallery.objects.all()
    return render(request, 'gallery.html', {'images': images})