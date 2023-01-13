from pickle import TRUE
from django.db import models
from django.urls import reverse 

class Post(models.Model):
  
    title = models.CharField(verbose_name='название', max_length=100)
    desc = models.TextField(verbose_name='описание', null=True, blank=True)
    image = models.ImageField(verbose_name='картинка')
    created_at = models.DateTimeField(verbose_name='создание', auto_now_add=True)
    update_at = models.DateTimeField(verbose_name='обнавление', auto_now=True)
   

    def __str__(self):
        return f'{self.title}'

    def get_absolute_url(self):
        return reverse('index')


    
  


class Comment(models.Model):
    desc = models.TextField(verbose_name='описание', null=True, blank=True)
    post = models.ForeignKey(Post, related_name='coments' ,on_delete=models.CASCADE)
    created_at = models.DateTimeField(verbose_name='создание', auto_now_add=True)

    def __str__(self):
        return f'{self.desc}'

    def get_absolute_url(self):
        return reverse('index')