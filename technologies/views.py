from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .forms import *
from .models import Technology, Contact
# from PIL import pillow

# Create your views here.


def handle_uploaded_file(img):
    image = Image.open(img)
    new_image = image.thumbnail((400, 400))
    return new_image


def create_technology(request):
    form = TechnologyForm()

    if request.method == 'POST':
        form = TechnologyForm(request.POST, request.FILES)

        if form.is_valid():
            new_tech = form.save(commit=False)
            new_tech.posted_by = request.user
            new_tech.save()
            messages.add_message(request, messages.SUCCESS, 'Technology Added Successfully')
            return redirect('index')



    context = {'form': form}

    return render(request, 'technologies/create.html', context)


def detail(request, tech_id):
    tech = get_object_or_404(Technology, pk=tech_id)

    context = {'tech': tech}

    return render(request, 'technologies/detail.html', context=context)


def get_technologies(request):

    techs = Technology.objects.all()

    context = {'techs':techs}
    return render(request, 'technologies/technologies.html', context)


def contacts(request, tech_id):
    
    form = ContactForm
    if request.method == 'POST':
        tech = get_object_or_404(Technology, pk=tech_id)

        form = ContactForm(request.POST)

        if form.is_valid():
            contact = form.save(commit=False)
            contact.technology = tech
            contact.save()
            print("Workinf inside")
            messages.add_message(request, messages.SUCCESS, 'Request sent successfully. We will get back to you soon :)')

            return redirect('technology:detail', tech_id)
    context = {'form':form, 'tech_id': tech_id}

    return render(request, 'technologies/contact.html', context)



