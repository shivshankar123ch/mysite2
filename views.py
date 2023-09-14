from django.views.decorators.csrf import requires_csrf_token
from django.contrib.auth import authenticate, login
from django.utils.decorators import method_decorator
from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.http import Http404
from django.contrib import messages
from rest_framework.views import APIView
from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.permissions import AllowAny, IsAdminUser,IsAuthenticated
from rest_framework.decorators import api_view, permission_classes
from .serializers import UserSerializer, RegisterSerializer,LoginSerializer,Personal_InformationSerializer,Job_InformationSerializer,Employee_Education_InformationSerializer,Employee_Old_Service_HistorySerializer,DeclarationSerializer
# from .forms import AuthenticationForm
from urllib import response
from .models import *
# Create your views here.

# Register API
class RegisterAPI(generics.GenericAPIView):
    serializer_class = RegisterSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({
        "user": UserSerializer(user, context=self.get_serializer_context()).data,
        # "token": AuthToken.objects.create(user)[1]
        })


@api_view(['POST'])
def login(request):
    response = Response()
    print(response)
    if request.method == "POST":
        username = request.POST.get('username')
        print(username)
        passsword = request.POST.get('passsword')
       
        if User.objects.filter(username=username,passsword=passsword).exists():

            data = User.objects.get(username=username,passsword=passsword)
            print(data)
            if username is None:
                response.data = {
                    'message':'username is wroung',
                    'status':200
                },
                return Response

            elif passsword is None:
                response.data = {
                    'message':'passsword is wrong',
                    'status':200
                    

                },
                return Response

        else:

            return Response

# # Personal_Information API
# class Personal_InformationList(APIView):
#     permission_classes = [IsAuthenticated]

#     def get(self, request, format=None):
#         snippets = Personal_Information.objects.all()
#         serializer = Personal_InformationSerializer(snippets, many=True)
#         return Response(serializer.data)

#     def post(self, request, format=None):
#         serializer = Personal_InformationSerializer(data=request.data)

#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST,message=sueccfully)



class Job_InformationList(APIView):
  
    def get(self, request, format=None):
        snippets = Job_Information.objects.all()
        serializer = Job_InformationSerializer(snippets, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = Job_InformationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class Employee_Education_InformationList(APIView):
  
    def get(self, request, format=None):
        snippets = Employee_Education_Information.objects.all()
        serializer = Employee_Education_InformationSerializer(snippets, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = Employee_Education_InformationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class Employee_Old_Service_HistoryList(APIView):
  
    def get(self, request, format=None):
        snippets = Employee_Old_Service_History.objects.all()
        serializer = Employee_Old_Service_HistorySerializer(snippets, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = Employee_Old_Service_HistorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class DeclarationList(APIView):

    def get(self, request, format=None):
        snippets = Declaration.objects.all()
        serializer = DeclarationSerializer(snippets, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = DeclarationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class DeclarationDetail(APIView):

    def get_object(self, pk):
        try:
            return Declaration.objects.get(pk=pk)
        except Declaration.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = DeclarationSerializer(snippet)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = DeclarationSerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        snippet = self.get_object(pk)
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")


from rest_framework import status

class Personal_InformationList(APIView):
    # permission_classes = [IsAuthenticated]
    def get(self, request, format=None):
        req = self.request
        print('hghghtht',req)
        user_id = req.query_params.get('user_id')
        print(user_id)
        user_id =  req.query_params.get('user_id')

        persionaldetail = Personal_Information.objects.filter(user=user_id)
        print('persionaldetail',Personal_Information.name)
        serializer = Personal_InformationSerializer(persionaldetail, many=True)
        
        job = Job_Information.objects.filter(user=user_id)
        job_serializer = Job_InformationSerializer(job, many=True)

        employee = Employee_Education_Information.objects.filter(user=user_id)
        employee_serializer = Employee_Education_InformationSerializer(employee, many=True)

        history = Employee_Old_Service_History.objects.filter(user=user_id)
        history_serializer = Employee_Old_Service_HistorySerializer(history, many=True)


        dec = Declaration.objects.filter(user=user_id)
        dec_serializer = DeclarationSerializer(dec, many=True)

        # return Response(serializer.data+job_serializer.data+employee_serializer.data+history_serializer.data+dec_serializer.data)
        
        
        return Response({ "status": "success","data": [], "persionaldetail": serializer.data, "job": job_serializer.data,"employee": employee_serializer.data,"history": history_serializer.data,"dec": dec_serializer.data})
       
        # response = files_serializer.data + dirs_serializer.data 
        # return Response(serializer.data)


    def post(self, request, format=None):
        serializer = Personal_InformationSerializer(data=request.data)
        # print(serializer)

        # serializer = Employee_Old_Service_HistorySerializer(data=request.data)
        # serializer = DeclarationSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
        job_serializer = Job_InformationSerializer(data=request.data)

        if job_serializer.is_valid():
            job_serializer.save()   

        employee_serializer = Employee_Education_InformationSerializer(data=request.data)
        if employee_serializer.is_valid():
            employee_serializer.save()   


        old_employee_serializer = Employee_Old_Service_HistorySerializer(data=request.data)
        if old_employee_serializer.is_valid():
            old_employee_serializer.save()   

        dec_serializer = DeclarationSerializer(data=request.data)
        if dec_serializer.is_valid():
            dec_serializer.save()   
            
            
            return Response(serializer.data,job_serializer.data,employee_serializer.data,old_employee_serializer.data,dec_serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


        #     return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
        # else:
        #     return Response({"status": "error", "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)



class Personal_InformationDetail(APIView):

    def get_object(self, pk):
        try:
            return Personal_Information.objects.get(pk=pk)
        except Personal_Information.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer =Personal_InformationSerializer(snippet)
        job_serializer = Job_InformationSerializer(snippet)
        employee_serializer = Employee_Education_InformationSerializer(snippet)

        serializer = Employee_Old_Service_HistorySerializer(snippet)
        serializer = DeclarationSerializer(snippet)
        return Response(serializer.data,job_serializer.data,employee_serializer.data,old_employee_serializer.data,dec_serializer.data)

    def put(self, request, pk, format=None):
        
        snippet = self.get_object(pk)
        print(snippet)
        serializer = Personal_InformationSerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        # response = {"status": "True", "message": "updat sucessfully","data": serializer.data}

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        snippet = self.get_object(pk)
        print('skjdoisjflk',snippet)
        snippet.delete()
        response = {"status": "True", "message": "delete sucessfully","data": serializer.data}

        return Response(response,status=status.HTTP_204_NO_CONTENT)

from django.http import HttpResponse, JsonResponse


@api_view(['POST'])
def persinal2(request):
    response = Response()
    id = request.POST.get('id')
    name = request.POST.get('name')
    dob = request.POST.get('dob')

    
    personalinformation_id = Personal_Information.objects.filter(id=id)
    print(personalinformation_id)
    
    data = Personal_Information.objects.create(name=name,dob=dob)
    print(data)
  
    
    if name is None:
        response.data = {
            'message':'username is wroung',
            'status':200
        },
        return Response

    elif dob is None:
        response.data = {
            'message':'passsword is wrong',
            'status':200
            

        },
        return Response

    else:

        return Response



import json


class alldetailList(APIView):
    # permission_classes = [IsAuthenticated]
    def get(self, request, format=None):
    
        persionaldetail = Personal_Information.objects.all()
        print('persionaldetail',Personal_Information.name)
        serializer = Personal_InformationSerializer(persionaldetail, many=True, context={'request': request})
        
        job = Job_Information.objects.all()
        job_serializer = Job_InformationSerializer(job, many=True)

        employee = Employee_Education_Information.objects.all()
        employee_serializer = Employee_Education_InformationSerializer(employee, many=True)

        history = Employee_Old_Service_History.objects.all()
        history_serializer = Employee_Old_Service_HistorySerializer(history, many=True)


        dec = Declaration.objects.all()
        dec_serializer = DeclarationSerializer(dec, many=True)


        # json_data = json.dumps(serializer.data)
        # print(json_data)
        
        # for k in range(len(json_data)):
        #     print('hghghghg',k)
        
        # Deserialization
      

        # return Response(serializer.data+job_serializer.data+employee_serializer.data+history_serializer.data+dec_serializer.data)
        

        return Response({ "status": "200","message": "success","data":serializer.data,"persionaldetail": serializer.data, "job": job_serializer.data,"employee": employee_serializer.data,"history": history_serializer.data,"dec": dec_serializer.data})



        # response = files_serializer.data + dirs_serializer.data 
        # return Response(k)
       

    def post(self, request, format=None):
        serializer = Personal_InformationSerializer(data=request.data)
        # print(serializer)

        # serializer = Employee_Old_Service_HistorySerializer(data=request.data)
        # serializer = DeclarationSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
        job_serializer = Job_InformationSerializer(data=request.data)

        if job_serializer.is_valid():
            job_serializer.save()   

        employee_serializer = Employee_Education_InformationSerializer(data=request.data)
        if employee_serializer.is_valid():
            employee_serializer.save()   


        old_employee_serializer = Employee_Old_Service_HistorySerializer(data=request.data)
        if old_employee_serializer.is_valid():
            old_employee_serializer.save()   

        dec_serializer = DeclarationSerializer(data=request.data)
        if dec_serializer.is_valid():
            dec_serializer.save()   
            
            
            return Response(serializer.data,job_serializer.data,employee_serializer.data,old_employee_serializer.data,dec_serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

