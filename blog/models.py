from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    created = models.DateTimeField(null=True)
    modified = models.DateTimeField(null=True)
    uploaded_image = models.ImageField(upload_to = 'images/',
                                       blank=True,)
    uploaded_file = models.FileField(upload_to = 'files/',
                                     blank=True,)



    def __str__(self):
        return f'게시글 제목:{self.title} - 게시글 내용 - {self.content}'

