from django import forms
from .models import Course, Lesson, Tur, Gul

class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ['name', 'description']


class LessonForm(forms.ModelForm):
    class Meta:
        model = Lesson
        fields = ['title', 'course', 'content']


class TurForm(forms.ModelForm):
    class Meta:
        model = Tur
        fields = ['name']


class GulForm(forms.ModelForm):
    class Meta:
        model = Gul
        fields = ['name', 'tur', 'color']
