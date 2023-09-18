from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.http import HttpResponse,JsonResponse
from .forms import AccountForm

from .models import District,Branch

from django.shortcuts import render, redirect, get_object_or_404

app_name='credentialsapp'
# Create your views here.

def home(request):
    return render(request,"base.html")
def page(request):
    return render(request,"page.html")

def account_create_view(request):
    form = AccountForm(request.POST or None)
    if form.is_valid():
        form.cleaned_data['materials']
        form.save()
        return render(request,"base.html",{'form':form})

    return render(request, "registerationform.html", {'form':form})
def get_branches(request, district_id):
    branches = Branch.objects.filter(district_id=district_id).values('id','name')
    branch_list=list(branches)
    return JsonResponse(list(branches), safe=False)






def login(request):
    if request.method=='POST':
        username=request.POST['username']
        password = request.POST['password']
        user=auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,"Invalid credentials")
            return HttpResponse("Invalid credentials")
    return render(request,"login.html")
def register(request):
    if request.method=='POST':
        username = request.POST['username']
        password = request.POST['password']
        cpassword = request.POST['password1']
        if password==cpassword:
            if User.objects.filter(username=username).exists():
                messages.info(request,"Username Already exists")
                return redirect('register')


            else:

                user=User.objects.create_user(username=username,password=password)
                user.save();

                return redirect('login')


        else:
            messages.info(request,"Password not matching")
            return redirect('register')
        return redirect('/')
    return render(request,"register.html")
def logout(request):
    auth.logout(request)
    return redirect('/')


