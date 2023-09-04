from django.shortcuts import render,HttpResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login
from .import models
from .import serializer as serial
from rest_framework.authtoken.models import Token
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

# Create your views here.
#cant use this function directly as it is

# @api_view(['GET'])
# def api_home(request):
#     student = models.Student.objects.all()#show all data of student table
#     serializer=serial.StudentSerializer(instance=student,many=True)
#     return Response({'status':200,"payload":serializer.data})#serializer=show data in jason format


class StudentAPI(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    def get(request,self):
        student = models.Student.objects.all()
        serializer=serial.StudentSerializer(instance=student,many=True)
        return Response({'status':200,"payload":serializer.data})
    
    def post(self,request):
        #gather data
        data = request.data
        serializer = serial.StudentSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response({"status":200,"msg":"Data Saved"})
        else:
            return Response({"status":403,"msg":"Something bad happend"})
#update data
    def put(self,request,id) :
        student= models.Student.objects.get(id=id) 
        serializer = serial.StudentSerializer(student,data=request.data)  
        if serializer.is_valid():
            serializer.save()
            return Response({"status":200,"msg":" Full data Updated"})
        else:
                return Response({"status":403,"msg":"Something bad happend"})

    def patch(self,request,id):
        student= models.Student.objects.get(id=id) 
        serializer = serial.StudentSerializer(student,data=request.data,partial=True)  
        if serializer.is_valid():
            serializer.save()
            return Response({"status":200,"msg":"Patch data Updated"})
    
        else:
            return Response({"status":403,"msg":"Something bad happend"}) 

    def delete(self,request,id):
        try:
             student = models.Student.objects.get(id=id) 
             student.delete()
             return Response({"delete successfully"})
        except:
            return Response({"something is wrong"})
        
class LoginUser(APIView):
        def post(self,request):
            username = request.data['username']    
            password = request.data['password']
            user = authenticate(request,username=username,password=password)
            if user:
                login(request,user)
                loged_user = User.objects.get(id=user.pk)#to send user details to frontend    
                #make variable
                token,_ = Token.objects.get_or_create(user=loged_user)
                #_=stored value which is not used
                data ={
                    "name":loged_user.first_name,
        
                    "token":str(token)
                }
                return Response({'status':200,"Payload":data})


                



