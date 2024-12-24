
from django.db import models

class Course(models.Model):  # Kurslar modeli
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name


class Lesson(models.Model):  # Darslar modeli
    title = models.CharField(max_length=100)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    content = models.TextField()

    def __str__(self):
        return self.title


class Tur(models.Model):  # Gullar turlari modeli
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Gul(models.Model):  # Gullar modeli
    name = models.CharField(max_length=100)
    tur = models.ForeignKey(Tur, on_delete=models.CASCADE)
    color = models.CharField(max_length=50)

    def __str__(self):
        return self.name

