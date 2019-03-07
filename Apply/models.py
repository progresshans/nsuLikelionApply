from django.db import models
from django.contrib.auth.models import User
# from .models import Apply

class Apply(models.Model):
    apply_name = models.CharField(max_length=45)
    apply_schoolNum = models.CharField(max_length=45)
    apply_phone = models.CharField(max_length=45)
    apply_department = models.CharField(max_length=45)
    apply_location = models.CharField(max_length=45)
    apply_email = models.CharField(max_length=45)
    apply_question1 = models.TextField()
    apply_question2 = models.TextField()
    apply_question3 = models.TextField()
    apply_question4 = models.TextField()
    apply_question5 = models.TextField()
    apply_total = models.IntegerField(default=0)
    apply_avg = models.FloatField(default=0.0)
    objects = models.Manager()

class Evaluation(models.Model):
    apply_point1 = models.IntegerField(default=0)
    apply_point2 = models.IntegerField(default=0)
    apply_point3 = models.IntegerField(default=0)
    apply_point4 = models.IntegerField(default=0)
    apply_point5 = models.IntegerField(default=0)
    apply_point_total = models.IntegerField(default=0)
    apply_point_avg = models.FloatField(default=0)
    apply_point_comment = models.TextField(max_length=200)
    apply_id = models.ForeignKey(Apply, on_delete=models.CASCADE)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    objects = models.Manager()

# Create your models here.