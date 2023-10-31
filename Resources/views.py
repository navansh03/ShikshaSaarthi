from django.shortcuts import render
from .models import Course


# Create your views here.

def educational_content(request):
    courses=Course.objects.all()
    return render(request,template_name="educational_content.html",context={"courses":courses})

