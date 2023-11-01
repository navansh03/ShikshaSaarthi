from django.shortcuts import render
from .models import Course
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required
def educational_content(request):
    courses=Course.objects.filter(active='True')    
    return render(request,template_name="Resources/educational_content.html",context={"courses":courses})


def CourseOverview(request,slug):
    # print(slug)
    course=Course.objects.get(slug=slug)
    context={
        "course":course,
        # "video":video
    }
    return render(request,template_name="Resources/course_overview.html",context=context)


def VideoPlayer(request,slug,video_number):
    video=video.objects.get(slug=slug)
    video2=video.objects.get(video_number)
    
    context={
        "video":video,
        "video" : video2
    }
    return render(request,template_name="Resources/video_player.html",context=context)


def job_listings(request):
    return render(request,template_name='Resources/job_listings.html')


def gov_documentations(request):
    return render(request,template_name='Resources/gov_documentations.html')

def mentor(request):
    return render(request,template_name='Resources/mentor.html')

def news(request):
    return render(request,template_name='Resources/news.html')

def contact_us(request):
    return render(request,template_name='Resources/contact_us.html')


