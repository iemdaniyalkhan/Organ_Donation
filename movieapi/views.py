from django.shortcuts import render

# Create your views here.

from django.shortcuts import render

from rest_framework import generics
from .serializers import studentSerializer,UserSerializer,Admin_detailsSerializer,organSerializer,requests_madeSerializer
from rec_organ.models import student,user_Details,Admin_details,requests_made,organ





# Create your views here.

class studentAPIView(generics.ListCreateAPIView):
    queryset = student.objects.all()
    serializer_class = studentSerializer

class studentdetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = student.objects.all()
    serializer_class = studentSerializer

class user_DetailsAPIView(generics.ListCreateAPIView):
    queryset = user_Details.objects.all()
    serializer_class = UserSerializer

class user_Detailsdetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = user_Details.objects.all()
    serializer_class = UserSerializer




    

class Admin_detailsAPIView(generics.ListCreateAPIView):
    queryset = Admin_details.objects.all()
    serializer_class = Admin_detailsSerializer

class Admin_detailsdetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Admin_details.objects.all()
    serializer_class = Admin_detailsSerializer








class organAPIView(generics.ListCreateAPIView):
    queryset = organ.objects.all()
    serializer_class = organSerializer

class organdetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = organ.objects.all()
    serializer_class = organSerializer







class requests_madeAPIView(generics.ListCreateAPIView):
    queryset = requests_made.objects.all()
    serializer_class = requests_madeSerializer

class requests_madedetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = requests_made.objects.all()
    serializer_class = requests_madeSerializer





    