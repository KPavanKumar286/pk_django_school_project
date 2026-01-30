from django.shortcuts import render, redirect
from .models import Teacher
# Create your views here.

def teacher_list(request):
    print('teacher_list:', request.method)
    teachers = Teacher.objects.all()
    return render(request, 'index.html', {'allteacher': teachers})

def add_teacher(request):
    print('add_teacher:', request.method)
    if request.method == 'POST':
        name = request.POST.get('name')
        subject = request.POST.get('subject')
        contact = request.POST.get('contact')
        email = request.POST.get('email')
        image = request.FILES.get('image')

        teacher = Teacher(
            name = name,
            subject = subject,
            contact = contact,
            email = email,
            image = image if image else None
        )
        teacher.save()
        return redirect('all-teachers')
    return render(request, 'index.html')


def update_teacher(request, id):
    print('update_teacher:', request.method)
    if request.method == 'POST':
        name = request.POST.get('name')
        subject = request.POST.get('subject')
        contact = request.POST.get('contact')
        email = request.POST.get('email')
        image = request.FILES.get('image')

        teacher = Teacher(
            id=id,
            name = name,
            subject = subject,
            contact = contact,
            email = email,
            image = image if image else None
        )
        teacher.save()
        return redirect('all-teachers')
    return render(request, 'index.html', {'teacher':teacher})


def delete_teacher(request, id):
    print('delete_teacher:', request.method)
    teacher = Teacher.objects.filter(id=id)
    teacher.delete()

    return redirect('all-teachers')