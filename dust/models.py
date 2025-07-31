from django.db import models


class top(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    created = models.DateTimeField()
    modified = models.DateTimeField()

class bottom(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    created = models.DateTimeField()
    modified = models.DateTimeField()

class outer(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    created = models.DateTimeField()
    modified = models.DateTimeField()

class outer(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    created = models.DateTimeField()
    modified = models.DateTimeField()



    def __str__(self):
        return f'게시글 제목:{self.title} - 게시글 내용 - {self.content}'