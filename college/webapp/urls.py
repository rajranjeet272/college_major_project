from django.urls import path
from webapp import views

urlpatterns = [
    path('', views.index),
    path('physics/', views.physics),
    path('chemistry/', views.chemistry),
    path('maths/', views.maths),
    path('it/', views.it),
    path('mechanical/', views.mechanical),
    path('civil/', views.civil),
    path('etc/', views.etc),
    path('pei/', views.pei),
    path('account_log/', views.account_log),
    path('account_sign/', views.account_sign),
    path('account_admin/', views.account_admin),
    path('userdetails/<str:email>', views.userdetails),
    path('edituserdetails/<str:editemail>',views.edituserdetails),
    path('registration/<str:email>', views.registration),
    path('library/', views.library),
    path('bus/', views.bus),
    path('hostels/', views.hostels),
    path('internet/', views.internet),
    path('guesthouse/', views.guesthouse),
    path('healthcenter/', views.healthcenter),
    path('notice/', views.notice),
    path('feedback/', views.feedback),
    path('admindashboard/', views.admindashboard),
    path('admindashboard/students', views.adminstudents),
    path('admindashboard/students/details/<str:email>', views.details),
    path('admindashboard/notices', views.adminnotices),
    path('admindashboard/notices/addnotice', views.addnotice),
    path('admindashboard/notices/details/<int:notice_id>', views.notices_edit),
    path('admindashboard/feedbacks', views.adminfeedbacks),
]

