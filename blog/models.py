from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse



# this is for the user to create a post and note *the user is denoted as author
class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})
    """
     this fuction is made to enabel a user to create a file and after creating it in the form then he is being
     reverse to post-detail  this means you would be redirected to that same post but
     that you have created but this would show you the details of the post
     and you know that the post details does have pk so you just have to put the pk
     but if it is another part you want it to go that has no pk then you just have to
     put the name    return reverse('post-home') then it would be reversed to that place
    """


class Comment(models.Model):
    comment = models.TextField(max_length=200)
    user = models.ForeignKey(User,on_delete= models.CASCADE)
    post = models.ForeignKey(Post,on_delete= models.CASCADE)
    time = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return f'{self.user} - comment'


















