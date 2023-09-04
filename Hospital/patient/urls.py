from django.urls import path
from.import views
#www.hospital.com/patient

#make variable with same name
app_name='patient'
urlpatterns=[
    # path('<str:page_name>',views.home),  #argument will pass here,<name of parameter from views>
    path('',views.home,name='patient_home'),#function name after views
    path('detail/',views.details),
    path('register/',views.registration,name='patient_registration'),
    path("delete/<int:patient_id>/",views.delete,name="delete_patient"),
    #/<int:patient_id>/=take arguments through url

    path('search/',views.search,name="patient_search"),
    path('edit/<int:patient_id>/',views.edit,name='edit_patient'),
    path('login/',views.login_patient,name='login'),
     path('signup/',views.signup_patient,name='signup'),
      path('logout/',views.logout_patient,name='logout')
]