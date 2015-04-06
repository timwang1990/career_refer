# from django.db import models
#
# # Create your models here.
# class Reporter(models.Model):
#     full_name = models.CharField(max_length=70)
#
#     def __str__(self):              # __unicode__ on Python 2
#         return self.full_name
#
# class Article(models.Model):
#     pub_date = models.DateField()
#     headline = models.CharField(max_length=200)
#     content = models.TextField()
#     reporter = models.ForeignKey(Reporter)
#
#     def __str__(self):              # __unicode__ on Python 2
#         return self.headline
#
# class Employee(models.Model):
#     name = models.CharField(max_length=50)
#     reporters = models.ManyToManyField(Reporter)
#
#     def __str__(self):              # __unicode__ on Python 2
#         return self.name
#
# class User(models.Model):
#     username = models.CharField(max_length=50)
#     password = models.CharField(max_length=50)
#     #headImg = models.FileField(upload_to='./upload/')
#
#     def __str__(self):
#         return self.username
