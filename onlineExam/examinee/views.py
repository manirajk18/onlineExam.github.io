from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from examinee import models
from examiner import models as examiner_model

def newExaminee(request):
    error_msg='Username-already-exists'
    d={}
    try:
        if int(request.GET['err'])==1:
            d['error_msg']=error_msg
    except:
        pass
    return render(request,'examinee/newExaminee.html',d)
    
def examineeRegistration(request):
    e=models.examinee()
    e.username=request.POST['Username']
    e.password=request.POST['Password']
    e.name=request.POST['Name']
    e.rollno=request.POST['Rollno']
    e.email=request.POST['Email']
    e.marks=0
    try:
        if e==models.examinee.objects.get(username=e.username):
            return HttpResponseRedirect('http://localhost:8000/examinee/new-examinee?err=1')
    except:
        pass

    e.save()
    return HttpResponseRedirect('http://localhost:8000/examinee/examinee-login/')

def examineeLogin(request):
    return render(request,'examinee/examineeLogin.html')

def examineeLoginValidate(request):
    UserName=request.POST['Username']
    PassWord=request.POST['Password']
    try:
        valid_user=models.examinee.objects.get(username=UserName,password=PassWord)
        request.session['username']=UserName
        return render(request,'examinee/examineeWelcome.html',{'User':valid_user.name})
    except:
        return HttpResponseRedirect("http://localhost:8000/examinee/examinee-login/")

def examineeLogout(request):
    del request.session['username']
    return HttpResponseRedirect('http://localhost:8000/examinee/examinee-login/')

def decor_examineeLogin(f):
    def modified_f(request):
        if 'username' in request.session.keys():
            return f(request)
        else:
            return HttpResponseRedirect('http://localhost:8000/examinee/examinee-login/')
    return modified_f

@decor_examineeLogin
def examineeExam(request):
    Q=examiner_model.questionbank.objects.all()
    return render(request,'examinee/examineeExam.html',{'Questions':Q})

@decor_examineeLogin
def examineeResult(request):
    total_marks=0
    for i in request:
        for j in examiner_model.questionbank.objects.all():
            if i== j.ans:
                j.mark=1
                total_marks +=1

    return render(request,'examinee/examineeResult.html',{'Total_Marks':total_marks,'User':request.session['username']})
