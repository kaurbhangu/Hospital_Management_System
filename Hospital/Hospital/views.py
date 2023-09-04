from django .shortcuts import render

def hospital_home(request):
    return render(request,'hospital.html')
