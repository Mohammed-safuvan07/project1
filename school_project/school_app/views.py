from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from school_app. models import students
# Create your views here.
def register(request):
    if request.method == "POST":
        # firstname = request.POST['first_name']
        # lastname = request.POST['last_name']
        username = request.POST['username']
        mail = request.POST['email']
        password1 = request.POST['password']
        password2 = request.POST['c_password']

        if password1 == password2:
            user = User.objects.create_user(username=username,email=mail, password=password1)
            user.save()
        return redirect('class_det')
    return render(request,'register.html')

def class_det(request):
    # info = clsdetails.objects.all()
    # if request.method == 'GET':
    #     class_name = request.GET.get('class_name',' ')
    #     strength = request.GET.get('class_strength',' ')
    #     section = request.GET.get('section',' ')
    #     values = clsdetails(class_name=class_name,list_of_student=strength,section=section)
    #     values.save()
    #     print('class section')
        # return redirect('student_det')

    return render(request,'classes.html')

def student_det(request):
    return render(request,'student.html')

def details(request):
    info = students.objects.all()
    if request.method == 'GET':
        student_name = request.GET.get('student_name',' ')
        age = request.GET.get('age',' ')
        father_name = request.GET.get('father_name',' ')
        phone_number = request.GET.get('phone_number',' ')
        values = students(student_name=student_name,student_age=age,father_name=father_name,phone_number=phone_number)
        values.save()
    return render(request,'detail.html',{'value':info})