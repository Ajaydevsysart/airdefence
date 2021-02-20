from django.shortcuts import render,redirect
from uaccount import urls
from django.views.generic.edit import CreateView
from uaccount.models import User
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.auth.models import auth
from django.contrib.auth import authenticate,login
from django.contrib.auth.decorators import login_required
from .models import extendeduser
from .forms import CustomUsercreationForm,extendeduserForm




@login_required
def addairman(request):
    if request.method=="POST":
        form=CustomUsercreationForm(request.POST)
        extend_form=extendeduserForm(request.POST)

        if form.is_valid() and extend_form.is_valid:
            user=form.save()

            extend=extend_form.save(commit=False)
            extend.user=user

            extend.save()

            username=form.cleaned_data['username']
            password=form.cleaned_data['password1']
            user=authenticate(username=username,password=password)
            login(request,user)
            return redirect('admhome')
    else:
        form=CustomUsercreationForm()
        extend_form=extendeduserForm()

    context={'form':form,'extend_form':extend_form}
    return render(request,'defence/airmanform.html',context)        





def user(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            messages.info(request,'invalid entry')
            return redirect('uaccount:user')   
    else:
        return render(request,'defence/Login_as_User.html')


