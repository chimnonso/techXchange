from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from .forms import *
from django.contrib.auth import get_user_model

User = get_user_model()

# Create your views here.


def register(request):
    form = UserCreateForm()

    context = {'form':form}
    
    return render(request, 'accounts/register.html', context)

class SignupView(CreateView):
    form_class = UserCreateForm
    template_name = 'accounts/register.html'
    success_url = reverse_lazy('accounts:login')


def profile(request, username):
    person = get_object_or_404(User, username=username)
    techs = person.technology_set.all()
    context = {
        "user": person,
        "techs": techs
    }
    print(context)

    return render(request, 'accounts/profile.html', context)