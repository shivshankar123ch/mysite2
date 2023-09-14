from django.contrib.auth.models import User
from rest_framework import serializers
from .models import *


# User Serializer
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email')

# Register Serializer
class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(validated_data['username'], validated_data['email'], validated_data['password'])

        return user


class LoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'password',]


class Personal_InformationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Personal_Information
        # fields = ('user','name','dob','email')
        fields = "__all__"


class Job_InformationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Job_Information
        fields = "__all__"


class Employee_Education_InformationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee_Education_Information
        fields = "__all__"


class Employee_Old_Service_HistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee_Old_Service_History
        fields = "__all__"

class DeclarationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Declaration
        # fields = ['id', 'name', 'contact', 'linenos', 'language', 'style']
        fields = "__all__"


class Job_InformationSerializer(serializers.ModelSerializer):
    Personal_Information = Personal_InformationSerializer(Personal_Information.objects.filter(user=2),read_only=True,many=True)
    Job_Information = Job_InformationSerializer(Job_Information.objects.filter(user=2),read_only=True)
    Employee_Education_Information = Employee_Education_InformationSerializer(Employee_Education_Information.objects.filter(user=2),read_only=True,many=True)
    Employee_Old_Service_History = Employee_Old_Service_HistorySerializer(Employee_Old_Service_History.objects.filter(user=2),read_only=True,many=True)
    Declaration =DeclarationSerializer(Declaration.objects.filter(user=2),read_only=True,many=True)


    class Meta:
        model = Job_Information
        fields = "__all__"

    
    # def create(self, validated_data):
    #     Personal_Information_data = validated_data.pop('Personal_Information')
    #     Job_Information= Job_Information.objects.create(**validated_data)
    #     for Job_Information_data in Job_Information_data :
    #         Personal_Information.objects.create(Job_Information=Job_Information, **invoice_detail_data )
    #     return Job_Information

# class UserSerializer(serializers.ModelSerializer):
#     profile = ProfileSerializer()

#     class Meta:
#         model = User
#         fields = ['username', 'email', 'profile']

#     def create(self, validated_data):
#         profile_data = validated_data.pop('profile')
#         user = User.objects.create(**validated_data)
#         Profile.objects.create(user=user, **profile_data)
#         return user

# class Combined_Serializer(serializers.ModelSerializer):
    
#     Personal_Information = serializers.SerializerMethodField()
#     Employee_Education_Information = serializers.SerializerMethodField()
    
#     def get_Personal_Information(self, obj):
#         Personal_Information = obj.Personal_Information_set.all()
#         serializer = Personal_InformationSerializer(Personal_Information, many=True)
#         return serializer.data

#     def get_Employee_Education_Information(self, obj):
#         Employee_Education_Information = obj.Employee_Education_Information_set.all()
#         serializer = Employee_Education_InformationSerializer(Employee_Education_Information, many=True)  
#         return serializer.data

   
#     class Meta:
#         model = Personal_Information
#         fields = "__all__"





# class Job_InformationSerializer(serializers.ModelSerializer):

#     class Meta:

#         model = Job_Information

#         fields = '__all__'

       

       

# class Employee_Education_InformationSerializer(serializers.ModelSerializer):

#     class Meta:

#         model = Employee_Education_Information

#         fields = '__all__'

       

# class Personal_InformationSerializer(serializers.ModelSerializer):

#     # job=Job_Information.objects.get(user=2)

#     job = serializers.SerializerMethodField()

#     employee = serializers.SerializerMethodField()

#     user = UserSerializer(required=True)

#     # job=Job_InformationSerializer()

#     # job1= Field(source='get_absolute_url')

   

#     def get_job(self, obj):

#         data = Job_InformationSerializer(Job_Information.objects.filter(user=2), many=True).data

#         return data

   

#     def get_employee(self, obj):

#         data = Employee_Education_InformationSerializer(Employee_Education_Information.objects.filter(user=2), many=True).data

#         return data

   

#     class Meta:

#         model = Personal_Information

#         # fields = "__all__"

#         fields=['user','job','employee']




# class CreateUserSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = User
#         fields = ['email', 'username', 'password']
#         extra_kwargs = {'password': {'write_only': True}}

#     def create(self, validated_data):
#         user = User(
#             email=validated_data['email'],
#             username=validated_data['username']
#         )
#         user.set_password(validated_data['password'])
#         user.save()
#         return user