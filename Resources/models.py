from django.db import models

class Course(models.Model):
    name=models.CharField(max_length=30, null =False)
    description= models.CharField(max_length=200,null=True)
    active=models.BooleanField(default=False)
    
    def _str_(self):
        return self.name

class CourseProperty(models.Model):
    description=models.CharField(max_length=20,null=False)
    course=models.ForeignKey(Course,null=False,on_delete=models.CASCADE)

    class Meta:
        abstract= True

class Prerequisites(CourseProperty):
    pass

class Learning(CourseProperty):
    pass





#video model in course

class Video(models.Model):
    title= models.CharField(max_length=100,null=False)
    course=models.ForeignKey(Course,null=False,on_delete=models.CASCADE)
    serial_number=models.IntegerField(null=False)
    video_url=models.CharField(max_length=150,null=False,default=0)
    is_preview=models.BooleanField(default=False)

    def _str_(self):
        return self.title

