from django.shortcuts import render
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from .models import Product
from .serilizers import ProductSerializer

class ProductList (APIView):
    """
    List all products or create new one
    """
    def get(self, request):
        queryset = Product.objects.all()
        serializer=ProductSerializer(queryset, many=True).data
        return Response(serializer, status=status.HTTP_200_OK)
    
    def post(self, request):
        serializer=ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ProductDetail (APIView):
    """
    Retrieve, update or delete a product instance.
    """
    def get(self, request, pk):
        queryset=get_object_or_404(Product, pk=pk)
        serializer=ProductSerializer(queryset)
        return Response(serializer.data)
    
    def put(self, request, pk):
        instance=get_object_or_404(Product, pk=pk)
        serializer=ProductSerializer(instance, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        instance=get_object_or_404(Product, pk=pk)
        instance.delete()
        return Response({'messag':'the object has been deleted!'}, status=status.HTTP_200_OK)
