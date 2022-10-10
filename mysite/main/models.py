from enum import auto
from turtle import tilt
from django.db import models
from django.shortcuts import render
import main

# Create your models here.
# inheritanse
class Post(models.Model):
    titel =models.CharField(max_length=20)
    content= models.TextField()


class Comment(models.Model):
    text=models.TextField()
    commentdate=models.DateField(auto_now=True)
    visible =models.BooleanField()

class Category(models.Model):
    catName=models.CharField(max_length=20)
    catDesc=models.TextField()


 