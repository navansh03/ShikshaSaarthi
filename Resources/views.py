from django.shortcuts import render
from .models import Course
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required
def educational_content(request):
    courses=Course.objects.all()
    return render(request,template_name="Resources/educational_content.html",context={"courses":courses})


def CourseOverview(request, slug ):
    # print(slug)
    course=Course.objects.get(slug=slug)
    context={
        "course":course
    }
    return render(request,template_name="Resources/course_overview.html",context=context)


def VideoPlayer(request,slug):
    video=video.objects.get(slug=slug)
    context={
        "video":video
    }
    return render(request,template_name="Resources/video_player.html",context=context)

