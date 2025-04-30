
from django.urls import path
from .views import studentAPIView,studentdetail,user_DetailsAPIView,user_Detailsdetail,organAPIView,organdetail

urlpatterns = [
    
    path('apiss/', studentAPIView.as_view()),
    path('apiss/<int:pk>/', studentdetail.as_view()),
    path('api_user/', user_DetailsAPIView.as_view()),
    path('api_user/<int:pk>/', user_Detailsdetail.as_view()),
    path('api_organ/', organAPIView.as_view()),
    path('api_organ/<int:pk>/', organdetail.as_view()),
   
   

]
