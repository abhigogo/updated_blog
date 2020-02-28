from django.urls import reverse
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.shortcuts import redirect

# Create your models here.
class user_profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    profile_image = models.ImageField('Profile Image',upload_to='profile_images',blank=True)

    def __str__(self):
        return self.user.username

class post(models.Model):
    title = models.CharField('Title',max_length=100)
    text = models.TextField('Text')
    created_date = models.DateTimeField('Created Date',default=timezone.now())
    published_date = models.DateTimeField('Published Date',blank=True,null=True)

    def get_absolute_url(self):
        return reverse('postlist')

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def approved_comments(self):
        return self.comments.filter(approved_comment = True)

    def __str__(self):
        return self.title

class  comment(models.Model):
    post = models.ForeignKey(post,on_delete=models.CASCADE,related_name="comments")
    name = models.CharField('Name',max_length=200)
    text = models.TextField('Text')
    posted_date = models.DateTimeField('Date Posted',default=timezone.now())
    approved_comment = models.BooleanField('Approved',default=False)

    def get_absolute_url(self):
        return redirect('postlist')


    def approve_comment(self):
        self.approved_comment = True
        self.save()

    def __str__(self):
        return self.text



