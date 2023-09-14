from django.urls import path
from .views import RegisterAPI
from . import views 
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('', views.index, name='index'),
    path('api/register/', RegisterAPI.as_view(), name='register'),
    path('api/login/', views.login, name='login'),#preectise
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    # path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

#perms user=1,2,3 list get
    path('persional/', views.Personal_InformationList.as_view()),

#ALL DETAILS GETLIST
    path('all_detail/', views.alldetailList.as_view()),
    
#single get post
    path('job/', views.Job_InformationList.as_view()),
    path('employee/', views.Employee_Education_InformationList.as_view()),
    path('services/', views.Employee_Old_Service_HistoryList.as_view()),
    path('declration/', views.DeclarationList.as_view()),
#crud prectise
    path('declration/<int:pk>/', views.DeclarationDetail.as_view()),
    path('persional/<int:pk>/', views.Personal_InformationDetail.as_view()),



    path('api/persinal2/', views.persinal2, name='persinal2'),#preectise


]