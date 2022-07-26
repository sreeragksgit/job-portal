from django.db import models
from users.models import User
# Create your models here.


class Candidateprofile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE,related_name='candidates')
    profile_pic=models.ImageField(upload_to='profile')
    qualification=models.CharField(max_length=120)
    age=models.PositiveIntegerField(default=17)
    skills=models.CharField(max_length=120,null=True)
    cv=models.FileField(upload_to='cvs',null=True)

