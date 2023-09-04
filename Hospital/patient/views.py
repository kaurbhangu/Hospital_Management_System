from django.shortcuts import render,redirect,HttpResponse
from.import models
from django.db.models import Q
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User


# Create your views here.
# pages={
#     'about':'patient/about.html',
#     'contact':'patient/contact.html',
#     'detail':'patient/detail.html',
#     'patient':'patient/patient.html'
# }

# def home(request,page_name):
#     try:
#         page_path=pages[page_name]
#         return render(request,page_path)
#     except:
#         return HttpResponse("Error 404")
# def home(request):
#     name='Kanika'
#     data = {
#         "my_name":name,
#         'Subjects':['Lab','Medicine','Injections'],
#         'dict':{
#             'key1':'value1',
#             'key2':'value2'
#         }
#     }
#     return render(request,'patient/patient.html',context=data)

def home(request):
    if 'user' in request.session.keys():
         print(request.session.keys())
         #take all records from table
         patients_data=models.Patient.objects.all()
         data={
            'patients':patients_data
         }
         return render(request,'patient/patient.html',context=data)
    return redirect('patient:login')
 
def details(request):
  
    #make dict to send data in frontend

    return render(request,'patient/detail.html')

def login_patient(request):
      if request.POST:
            username=request.POST['username']
            password=request.POST['password']
            user = authenticate(request,username=username,password=password)

            if user is not None:
                  login(request,user)
                  user=User.objects.get(id=user.pk) #can fetch main record
                  request.session['user']=user.pk #store user in session
                    #send details in frontend with the help of variable
                  
                  return redirect('hospital_home_page')
      return render(request,'patient/login.html')
def logout_patient(request) :
      logout(request)
      return redirect('hospital_home_page')


          

          

def signup_patient(request):
         if request.POST:
               first_name = request.POST['first_name']
               last_name=request.POST['last_name']
               username=request.POST['username']
               email=request.POST['email']
               password=request.POST['password']
               confirm_password=request.POST['confirm_password']

               if User.objects.filter(username=username).exists():
                     return render(request,'patient/signup.html',context={'username_error':'Username already exist'})
               elif User.objects.filter(email=email).exists():
                     return render(request,'patient/signup.html',context={'email_error':"Email already exist"})
               elif password!=confirm_password:
                     return render(request,'patient/signup.html',context={'password_error':"password do not match"})
               else:
                     user = User.objects.create_user(username=username,email=email,password=password,first_name=first_name,last_name=last_name)
                     user.is_active = True
                     user.save()
                     return redirect('hospital_home_page')
         return render(request,'patient/signup.html')
         
def registration(request):
        #get data
        if request.POST:
            first_name = request.POST['first_name']
            last_name = request.POST['last_name']
            age = request.POST['age']
            email = request.POST['email']
            disease = request.POST['disease']
            #make object of patient
            models.Patient.objects.create(first_name=first_name,Last_name=last_name,age=age,email=email,disease=disease)
            # patient=models.Patient()
            # patient.first_name = first_name
            # patient.last_name = last_name
            # patient.age = age
            # patient.email = email
            # patient.disease=disease
            # patient.save()#to save data
            
        return render(request,'patient/success.html')

#create view for delete
def delete(request,patient_id):
     patient=models.Patient.objects.get(id=patient_id)#get take only one recorde
     patient.delete()
     return redirect('patient:patient_home')

def edit(request,patient_id):
     patient=models.Patient.objects.get(id=patient_id)
     # #get patient
     if request.POST:
            first_name = request.POST['first_name']
            last_name = request.POST['last_name']
            age = request.POST['age']
            email = request.POST['email']
            disease = request.POST['disease']

            patient.first_name = first_name
            patient.last_name = last_name
            patient.age = age
            patient.email = email
            patient.disease=disease
            patient.save()

            return redirect('patient:patient_home')

     data={
          'heading':'Update Details',
          'patient': patient#send to frontend
     }
     return render(request,'hospital.html',context=data)#go to hospital home page


def search(request):
     if request.GET:
          user_input = request.GET['user_search']
          related_patients = models.Patient.objects.filter(Q(first_name__icontains=user_input) | Q(Last_name__icontains=user_input) | Q(age__icontains=user_input) | Q(disease__icontains=user_input)).all()
          return render(request,'patient/patient.html',context ={'patients':related_patients})
     

   



       
 
