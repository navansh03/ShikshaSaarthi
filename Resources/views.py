from django.shortcuts import render
from .models import Course,Learning,Subject,Video,UserCourse
from django.contrib.auth.decorators import login_required
from django.urls import reverse


# Create your views here.
@login_required
def educational_content(request):
    courses=Course.objects.filter(active='True')    
    return render(request,template_name="Resources/educational_content.html",context={"courses":courses})


def CourseOverview(request,slug):
    # print(slug)
    course=Course.objects.get(slug=slug)
    learnings=Learning.objects.filter(course=course)
    subject=Subject.objects.filter(course=course)
    video=Video.objects.filter(course=course)
    print(video)
    course_id=Course.objects.get(slug=slug)
    try:
        check_enroll=UserCourse.objects.get(user=request.user,course=course_id)
    except UserCourse.DoesNotExist:
        check_enroll=None

    # video=Video.objects.filter(subject=subject).first()
    # print(video)

    context={
        "course":course,
        "video":video,
        "learnings":learnings,
        "subjects":subject,
        'check_enroll':check_enroll,
        # "video":video,
    }
    return render(request,template_name="Resources/course_overview.html",context=context)



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


def Checkout(request,slug):
        course=Course.objects.get(slug=slug)
        course=UserCourse(user=request.user,course=course)
        course.save()
        checkout_url = reverse('checkout', args=['your-slug-value'])
        print(checkout_url)
        

        return render(request,'Resources/checkout_confirmation.html',{'checkout_url': checkout_url})    