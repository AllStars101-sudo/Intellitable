from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator 
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.

class Home(models.Model):
    home_content = models.TextField()

class UserInputFormModel(models.Model):
    id=models.AutoField(primary_key=True)
    username=models.CharField(default=0,max_length=225)
    password=models.CharField(default=0,max_length=225)
    subjectname1=models.CharField(default=0, max_length=255)
    subject1exam1=models.PositiveIntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(100)])
    subject1exam2=models.PositiveIntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(100)])
    subject1exam3=models.PositiveIntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(100)])
    subject1exam4=models.PositiveIntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(100)])
    subject1exam5=models.PositiveIntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(100)])
    subjectname2=models.CharField(default=0, max_length=255)
    subject2exam1=models.PositiveIntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(100)])
    subject2exam2=models.PositiveIntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(100)])
    subject2exam3=models.PositiveIntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(100)])
    subject2exam4=models.PositiveIntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(100)])
    subject2exam5=models.PositiveIntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(100)])
    subjectname3=models.CharField(default=0, max_length=255)
    subject3exam1=models.PositiveIntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(100)])
    subject3exam2=models.PositiveIntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(100)])
    subject3exam3=models.PositiveIntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(100)])
    subject3exam4=models.PositiveIntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(100)])
    subject3exam5=models.PositiveIntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(100)])
    subjectname4=models.CharField(default=0, max_length=255)
    subject4exam1=models.PositiveIntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(100)])
    subject4exam2=models.PositiveIntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(100)])
    subject4exam3=models.PositiveIntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(100)])
    subject4exam4=models.PositiveIntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(100)])
    subject4exam5=models.PositiveIntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(100)])
    subjectname5=models.CharField(default=0, max_length=255)
    subject5exam1=models.PositiveIntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(100)])
    subject5exam2=models.PositiveIntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(100)])
    subject5exam3=models.PositiveIntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(100)])
    subject5exam4=models.PositiveIntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(100)])
    subject5exam5=models.PositiveIntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(100)])
    objects=models.Manager()