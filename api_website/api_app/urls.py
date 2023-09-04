from django.urls import path
from.import views



urlpatterns=[

    # path('',views.api_home)
    #for classlevel method
    path("",views.StudentAPI.as_view()),
    #url for update,put
    path('put/<int:id>/',views.StudentAPI.as_view()),
    path('patch/<int:id>/',views.StudentAPI.as_view()),
    path('delete/<int:id>/',views.StudentAPI.as_view()),
    path('login/',views.LoginUser.as_view())
]