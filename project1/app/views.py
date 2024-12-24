from django.shortcuts import render, redirect
from .forms import CourseForm, LessonForm, TurForm, GulForm


def add_course(request):
    if request.method == 'POST':
        form = CourseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('course_list')
    else:
        form = CourseForm()
    return render(request, 'add_course.html', {'form': form})


def add_lesson(request):
    if request.method == 'POST':
        form = LessonForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lesson_list')
    else:
        form = LessonForm()
    return render(request, 'add_lesson.html', {'form': form})


def add_tur(request):
    if request.method == 'POST':
        form = TurForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('tur_list')
    else:
        form = TurForm()
    return render(request, 'add_tur.html', {'form': form})


def add_gul(request):
    if request.method == 'POST':
        form = GulForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('gul_list')
    else:
        form = GulForm()
    return render(request, 'add_gul.html', {'form': form})
