from django.shortcuts import render
from rest_framework import generics
from .models import MenuItem
from .serializers import MenuItemSerializer

#List Create APIView can create records with accept post then view them with Get
class MenuItemsView (generics.ListCreateAPIView):

    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer


#Viewing an Item One at a time
class SingleMenuItemView(generics.RetrieveUpdateAPIView, generics.DestroyAPIView):

    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer




