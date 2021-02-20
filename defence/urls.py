from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('home', views.home,name='home'),
    path('exam',views.exam,name='exam'),
    path('health',views.health,name='health'),
    path('canteen',views.canteen,name='canteen'),
    path('userleave',views.userleave,name='userleave'),
    path('event',views.event,name='event'), 
    path('userprofile',views.userprofile,name='userprofile'),
    path('adm',views.adm,name='adm'),
    path('admhome',views.admhome,name='admhome'),
    path('profileadm',views.profileadm,name='profileadm'),
    path('admevent',views.admevent,name='admevent'),
    path('healthadm',views.healthadm,name='healthadm'),
    path('approvels',views.approvels,name='approvels'),
    path('leaveadm',views.leaveadm,name='leaveadm'),
    path('appointments',views.appointments,name='appointments'),
    path('notification',views.notification,name='notification'),
    path('seo',views.seo,name='seo'),
    path('seohome',views.seohome,name='seohome'),
    path('leaveseo',views.leaveseo,name='leaveseo'),
    path('seoevent',views.seoevent,name='seoevent'),
    path('healthseo',views.healthseo,name='healthseo'),
    path('profileseo',views.profileseo,name='profileseo'),
    path('seoexam',views.seoexam,name='seoexam'),
    path('adddoctor',views.adddoctor,name='adddoctor'),
    path('canteenprofile',views.canteenprofile,name='canteenprofile'), 
    path('healthcanteen',views.healthcanteen,name='healthcanteen'),
    path('canteenlg',views.canteenlg,name='canteenlg'),
    path('canteenhm',views.canteenhm,name='canteenhm'),
    path('canteenevent',views.canteenevent,name='canteenevent'),
    path('canteenexam',views.canteenexam,name='canteenexam'),
    path('canteenleave',views.canteenleave,name='canteenleave'),
    path('addfood',views.addfood,name='addfood'),
   
   
   
     
]