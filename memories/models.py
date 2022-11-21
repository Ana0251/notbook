from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Memory(models.Model):
    STATUS_TYPE = (('pu', 'عمومی'), ('pr', 'خصوصی'),)
    writer = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    text = models.TextField()
    place = models.CharField(max_length=15)
    history = models.DateTimeField()
    ftravel = models.CharField(max_length=100)
    image = models.ImageField(blank=True, upload_to='images/%Y/%m/%d/')
    create = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)
    type = models.CharField(max_length=2, choices=STATUS_TYPE, default='pr')

    def __str__(self):
        return self.title

    class Meta:
        ordering = ('-create',)


class Profile(models.Model):
    job = models.CharField(max_length=20, blank=True)
    place = models.CharField(max_length=20, blank=True)
    birthday = models.DateField(blank=True)
    avatar = models.ImageField(upload_to='images/%User/%Y/%m/%d/')
    profile = models.OneToOneField(User, on_delete=models.CASCADE)


class Tags(models.Model):
    tag = models.CharField(max_length=10)

    def __str__(self):
        return self.tag


class Interests(models.Model):
    interest = models.OneToOneField(User, on_delete=models.CASCADE)
    tag = models.ManyToManyField(Tags, blank=True)

    def __str__(self):
        return self.interest.username


class Comment(models.Model):
    memory = models.ForeignKey(Memory, on_delete=models.CASCADE, blank=True)
    writer = models.ForeignKey(User, on_delete=models.CASCADE, blank=True)
    comment = models.TextField(max_length=150)
    create = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.writer.username


