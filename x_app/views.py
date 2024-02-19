from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect

# Create your views here.
from x_app.forms import LoginRegister, StudentForm, Admin1Form
from x_app.models import Student, Admin1


def home(request):
    return render(request,'index.html')
def new(request):
    return render(request,'dashb.html')
def Student_login(request):
    login_form=LoginRegister()
    student_form= StudentForm()

    if request.method=="POST":
        login_form = LoginRegister(request.POST)
        student_form = StudentForm(request.POST,request.FILES)

        if login_form.is_valid() and student_form.is_valid():
            user2=login_form.save(commit=False)
            user2.is_student=True
            user2.save()
            user1=student_form.save(commit=False)
            user1.user_1=user2
            user1.save()

    return render(request, 'form.html', {'login_form': login_form, 'student_form': student_form})

def Admin1_login(request):
    login_form=LoginRegister()
    admin1_form= Admin1Form()
    if request.method=="POST":
        login_form = LoginRegister(request.POST)
        admin1_form = Admin1Form(request.POST)

        if login_form.is_valid() and admin1_form.is_valid():
            user2=login_form.save(commit=False)
            user2.is_admin1=True
            user2.save()
            user1=admin1_form.save(commit=False)
            user1.user_2=user2
            user1.save()

    return render(request, 'form1.html', {'login_form': login_form, 'admin1_form': admin1_form})

def stu_base(request):
    data =Student.objects.get(user_1=request.user)
    return render(request,'student/stu_base.html',{'data':data})

def adm_base(request):
    data =Admin1.objects.get(user_2=request.user)
    return render(request,'admin1/adm_base.html',{'data':data})
def Login_view(request):
    if request.method == "POST":
        username = request.POST.get('uname')
        password = request.POST.get('pass')
        user = authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            if user.is_student:
                return redirect('stu_base')
            elif user.is_admin1:
                return redirect('adm_base')
        else:
            messages.info(request, 'invalid credentials')
    return render(request, 'login.html')









