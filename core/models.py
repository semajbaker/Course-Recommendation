from django.db import models

class Subject(models.Model):
    title = models.CharField(max_length=100)
    
    def __str__(self):
        return self.title

class Course(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    subject = models.ManyToManyField(Subject)
    
    def __str__(self):
        return self.title

class School(models.Model):
    title = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    courses = models.ManyToManyField(Course)
    
    def __str__(self):
        return self.title

class User(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subjects = models.ManyToManyField(Subject)
    
    def __str__(self):
        return self.name
