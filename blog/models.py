from django.contrib.auth.models import User
from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100,unique=True,allow_unicode=True)

    def get_url(self):
        return f'/blog/category/{self.slug}'

    def __str__(self):
        return f'{self.name}+{self.slug}'



class Post(models.Model):
    author=models.ForeignKey(User,on_delete=models.SET_NULL,null=True)
    title = models.CharField(max_length=100)
    content = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True,blank=True)
    created = models.DateTimeField(null=True)
    modified = models.DateTimeField(null=True)
    uploaded_image = models.ImageField(upload_to = 'images/',
                                       blank=True,)
    uploaded_file = models.FileField(upload_to = 'files/',
                                     blank=True,)


    def __str__(self):
        return f'게시글 제목:{self.title}-by{self.author} -category:{self.category}'

