from django.shortcuts import render, get_object_or_404,redirect
from django.http import HttpResponse
from django.core.mail import send_mail
from django.contrib.admin.views.decorators import staff_member_required
from .forms import *
from django.core.exceptions import ObjectDoesNotExist
from .models import *

# Create your views here.

def Home(request):
    return render(request, 'home.html')

def Donate(request):
    if request.method == 'POST':
        form = DonationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('donate')
    else:
        form = DonationForm()

    return render(request, 'donate.html', {'form': form})

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
        return render(request, 'publication.html', {'error': error_message})
        
def Join(request):
    if request.method=="POST":
        memberdata = member.objects.create(
            full_name = request.POST['full_name'],
            phone_number = request.POST['phone_number'],
            email = request.POST['email'],
            contact_address = request.POST['contact_address'],
            residential_address = request.POST['residential_address'],
            how_know = request.POST['how_know'],
            upload_photo=request.FILES.get('upload_photo'),)

        
        memberdata.save()
        return redirect ('home')
    return render(request,'joinus.html')
    

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = ContactForm()

    return render(request, 'contact.html', {'form': form})

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