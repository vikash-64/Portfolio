from django.db import models

# Create your models here.
class Project(models.Model):
    

    title = models.CharField(max_length=200)
    description = models.CharField(max_length=200 , blank=True , null=True)
    ImgLink = models.URLField(max_length = 500 , blank=True , null=True)
    ProjectLink = models.URLField(max_length = 500 , blank=True , null=True)
