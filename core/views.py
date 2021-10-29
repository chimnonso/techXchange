from django.shortcuts import render

from technologies.models import Technology

# Create your views here.


def index(request):

    techs = Technology.objects.all()[:4]

    context = {
        'techs': techs
    }

    return render(request, 'core/index.html', context)