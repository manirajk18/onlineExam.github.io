from django.db import models

# Create your models here.
class examinee(models.Model):
    username=models.CharField(primary_key=True,max_length=20)
    password=models.CharField(max_length=20)
    name=models.CharField(max_length=20)
    rollno=models.IntegerField()
    email=models.CharField(max_length=20)
    marks=models.IntegerField()

    def __str__(self):
        s=self.username+"  "+self.password+"  "+self.name+"  "+str(self.rollno)+"  "+self.email+"  "+str(self.marks)
        return s
    