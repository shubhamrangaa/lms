
from custom_users.models import UserProfile
from django.db import models
import uuid

# Create your models here.
class Images(models.Model):
    title = models.CharField(max_length=50,null=True,blank=True)
    image_url = models.CharField(max_length=250,null=True,blank=True)

    def __str__(self):
        return self.title

class Videos(models.Model):
    title = models.CharField(max_length=50,null=True,blank=True)
    video_url = models.CharField(max_length=250,null=True,blank=True)
    def __str__(self):
        return self.title
     
class Keywords(models.Model):
    keyword_name = models.CharField(max_length=50,null=True,blank=True)
    def __str__(self):
        return self.keyword_name
    
class ContentType(models.Model):
    content_type = models.CharField(max_length=50,null=True,blank=True)
    def __str__(self):
        return self.content_type



class Tutorial(models.Model):
    uuid = models.UUIDField(primary_key=True,default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=50,null=True,blank=True)
    description = models.TextField()
    author = models.ForeignKey(UserProfile, on_delete=models.CASCADE,null=True,blank=True) #on delete field?
    updated = models.DateTimeField(auto_now=True,auto_now_add=False)
    timestamp = models.DateTimeField(auto_now=False,auto_now_add=True)
    comments = models.TextField()
    category = models.ForeignKey(ContentType,on_delete=models.CASCADE,null=True,blank=True) #on delete field?
    keywords = models.ManyToManyField(Keywords,null=True,blank=True,related_name='tutorial_keywords') #on delete field?
    images = models.ManyToManyField(Images,null=True,blank=True,related_name='tutorial_images') #o1n delete field?
    videos = models.ManyToManyField(Videos,null=True,blank=True,related_name='tutorial_videos') #on delete field?
    
    def __str__(self):
        return self.title