from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse



# Create your models here.
class Post(models.Model):
    subject = models.CharField(max_length=100)
    question = models.TextField()
    date_posted= models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User,on_delete=models.CASCADE)
   
    def __str__(self):
        return self.question
    def get_absolute_url(self):
        return reverse('post-detail',kwargs={'pk': self.pk})

class Answer(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='answers')
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    answer = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    approved_answer = models.BooleanField(default=False)

    def approve(self):
        self.approved_answer = True
        self.save()

    def __str__(self):
        return self.author.username
    def get_absolute_url(self):
        return reverse('post-detail',kwargs={'pk': self.pk})