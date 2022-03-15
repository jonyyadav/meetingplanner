from django.db import models
from datetime import time


# Create your models here.


class Room(models.Model):
    name = models.CharField(max_length=30)
    floor_number = models.IntegerField()
    room_number = models.IntegerField()

    def __str__(self):
        return super().__str__()


class Meeting(models.Model):
    title = models.CharField(max_length=200)
    date = models.DateField()
    start_time = models.TimeField(default=time(9))
    duration = models.IntegerField(default=1)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)

    def __str__(self):
        return super().__str__()


class Person(models.Model):
    name = models.CharField(max_length=30)
    age = models.IntegerField()


class SignUp(models.Model):
    name = models.CharField(max_length=25)
    email = models.CharField(max_length=40)
    password = models.CharField(max_length=10)
