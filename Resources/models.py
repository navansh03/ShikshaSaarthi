from django.db import models
from users.models import CustomUser

class Course(models.Model):
    name=models.CharField(max_length=30, null =False)
    slug=models.CharField(max_length=50,null=False,unique=True)
    description= models.CharField(max_length=200,null=True)
    active=models.BooleanField(default=False)
    
    def __str__(self):
        return f"{self.name}"

class CourseProperty(models.Model):
    description=models.CharField(max_length=20,null=False)
    course=models.ForeignKey(Course,null=False,on_delete=models.CASCADE)

    class Meta:
        abstract= True

class Prerequisites(CourseProperty):
    pass

class Learning(CourseProperty):
    pass

class Subject(models.Model):
    course=models.ForeignKey(Course,on_delete=models.CASCADE)
    name=models.CharField(max_length=100,null=False)

    def __str__(self):
        return f"{self.name}"



#video model in course

class Video(models.Model):
    title= models.CharField(max_length=100,null=False)
    course=models.ForeignKey(Course,null=False,on_delete=models.CASCADE)
    subject=models.ForeignKey(Subject,null=True,on_delete=models.CASCADE,default=0)
    slug2=models.CharField(max_length=100,null=True)
    serial_number=models.IntegerField(null=False,unique=True,default=999)
    video_number=models.IntegerField(null=False,default=0)
    video_url=models.CharField(max_length=150,null=False,default=0)
    is_preview=models.BooleanField(default=False)




class UserCourse(models.Model):
    user=models.ForeignKey(CustomUser,on_delete=models.CASCADE)
    course=models.ForeignKey(Course,  on_delete=models.CASCADE)
    date=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.first_name ,self.course.name}"
    


class Contact(models.Model):
    name=models.CharField(max_length=200)
    email=models.EmailField()
    subject=models.TextField()
    
    def __str__(self):
        return f"{self.name}"



