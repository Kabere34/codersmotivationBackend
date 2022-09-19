from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
  # Boolean fiels to select the type of account
   is_admin = models.BooleanField(default=False)
   is_staff= models.BooleanField(default=False)

   def __str__(self):
    return self.username

class Category(models.Models):
  category=models.CharField(max_length=20)

  def __str__(self):
    return self.category

class Post(models.Model):
  category=models.ForeignKey(Category,on_delete=models.CASCADE)
  title=models.CharField(max_length=20)
  image=models.CloudinaryField('image')
  video=models.CloudinaryField('video')
  content=models.TextField()
  timePosted=models.DateTimeField(auto_now_add=True)
  likes = models.IntegerField(default=0)
  author=models.ForeignKey(User, on_delete=models.CASCADE, null=True)


class Like(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class Comment(models.Model):
  post=models.ForeignKey(Post, on_delete=models.CASCADE,related_name='comments')
  name=models.CharField(max_length=80)
  email=models.EmailField()
  body=models.TextField()
  created_on=models.DateTimeField(auto_now_add=True)
  active=models.BooleanField(default=False)

  class Meta:
    ordering=['created_on']

  def _str_(self):
    return 'Comment{} by  {}'.format(self.body,self.name)



