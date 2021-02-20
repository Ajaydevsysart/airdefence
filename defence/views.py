from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.models import auth,User
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
@login_required
def home(request):
    return render(request,'defence/main.html')

@login_required
def profileadm(request):
    return render(request,'defence/profileadm.html')

@login_required
def profileseo(request):
    return render(request,'defence/profileseo.html')

@login_required
def canteenprofile(request):
    return render(request,'defence/canteenprofile.html')


def canteen(request):
    return render(request,'defence/canteentest.html')

@login_required
def exam(request):
    return render(request,'defence/exam.html')

@login_required
def approvels(request):
    return render(request,'defence/approvels.html')

@login_required
def addfood(request):
    return render(request,'defence/addfood.html')

@login_required
def appointments(request):
    return render(request,'defence/appoinments.html')

@login_required
def notification(request):
    return render(request,'defence/notification.html')

@login_required
def seoexam(request):
    return render(request,'defence/seoexam.html')

@login_required
def canteenexam(request):
    return render(request,'defence/canteenexam.html')

@login_required
def adddoctor(request):
    return render(request,'defence/adddoctor.html')

def index(request):
    return render(request,'defence/index.html')

@login_required
def admhome(request):
         return render(request,'defence/admhome.html')

@login_required
def event(request):
    return render(request,'defence/events.html')

@login_required
def admevent(request):
    return render(request,'defence/admevent.html')

@login_required
def seoevent(request):
    return render(request,'defence/seoevent.html')

@login_required
def canteenevent(request):
    return render(request,'defence/canteenevent.html')


@login_required
def healthadm(request):
    return render(request,'defence/healthadm.html')

@login_required    
def healthseo(request):
    return render(request,'defence/healthseo.html')

@login_required
def healthcanteen(request):
    return render(request,'defence/healthcanteen.html')

@login_required
def health(request):
    return render(request,'defence/health.html')

@login_required
def seohome(request):
    return render(request,'defence/Seohome.html')

@login_required
def canteenleave(request):
    return render(request,'defence/canteenleave.html')

@login_required
def leaveadm(request):
    return render(request,'defence:leaveadm.html')


def seo(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)
        if user is not None and user.id==2:
            auth.login(request,user)
            return redirect('seohome')
        else:
            messages.info(request,'invalid entry')
            return redirect('seo')
    else:

        return render(request,'defence/Login_as_Seo.html')


def adm(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)
        if user is not None and user.id==1:
            auth.login(request,user)
            return redirect('admhome')
        else:
            messages.info(request,'invalid entry')
            return redirect('adm')
    else:

        return render(request,'defence/Login_as_Admin.html')

@login_required
def userprofile(request):
    return render(request,'defence/userprofile.html')

@login_required
def canteenhm(request):
    return render(request,'defence/canteenhm.html')

@login_required
def userleave(request):
    return render(request,'defence/userleave.html')

@login_required
def leaveseo(request):
    return render(request,'defence/leaveseo.html')





def canteenlg(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)
        if user is not None and user.id==3:
            auth.login(request,user)
            return redirect('canteenhm')
        else:
            messages.info(request,'invalid entry')
            return redirect('canteenlg')
    else:

        return render(request,'defence/Login_as_Canteen.html')