# -*- coding: utf-8 -*-
#
# Copyright (c) 2024 -- All rights reserved.
# Author: Md Washim Akram <washimakram1631@gmail.com>
#
# This file is part of the exmyb project.

###############################################################################

"""
Bookstores
==========
"""
from django.shortcuts import render
from .models import BookModel
from .serializers import BooksModelSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.decorators import api_view
from rest_framework.views import APIView
# We can also import APIView from decorators
# from rest_framework.decorators import APIView


# Creating a home function to rendering home.html file
def home(request):
    return render(request, 'books/home.html')


# Creating BooksModelViewSet class for CRUD Opreations.
# First Way By Using ModelViewSet Module
class BooksModelViewSet(ModelViewSet):
    queryset = BookModel.objects.all()
    serializer_class = BooksModelSerializer
    #if you want to aunthentication and authorization kind of thing, then remove comment below or line 22 and 23
    # authentication_classes = [JWTAuthentication]
    # permission_classes = [IsAuthenticated]
    

#Second Way By using ListCreateAPIView and RetrieveUpdateDestroyAPIView
class BooksListCreateAPIView(ListCreateAPIView):
    queryset = BookModel.objects.all()
    serializer_class = BooksModelSerializer
    #if you want to aunthentication and authorization kind of thing, then remove comment below or line 30 and 31
    # authentication_classes = [JWTAuthentication]
    # permission_classes = [IsAuthenticated]

class BooksRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = BookModel.objects.all()
    serializer_class = BooksModelSerializer
    #if you want to aunthentication and authorization kind of thing, then remove comment below or line 37 and 38
    # authentication_classes = [JWTAuthentication]
    # permission_classes = [IsAuthenticated]


#Third Way by Using APIView Class
class BooksAPIView(APIView):
    def get_by_object(self, id):
        try:
            book = BookModel.objects.get(id=id)
        except BookModel.DoesNotExist:
            book = None
        return book
    
    def get(self, request, pk=None, format=None):
        id = pk
        if id is not None:
            book = self.get_by_object(id)
            if book is None:
                return Response({'msg':'Provided Book Id is not available'})
            serializer = BooksModelSerializer(book)
            return Response(serializer.data)
        books = BookModel.objects.all()
        serializer = BooksModelSerializer(books, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = BooksModelSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Data Created'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk, format=None):
        id = pk
        book = self.get_by_object(id=id)
        if book is None:
            return Response({'msg':'Provided Book Id is not available'})
        serializer = BooksModelSerializer(book, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Complete Updated Success'})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk, format=None):
        id = pk
        book = self.get_by_object(id)
        if book is None:
            return Response({'msg':'Provided Book Id is not available'})
        serializer = BooksModelSerializer(book, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Partial Updated Success'})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        id = pk
        book = self.get_by_object(id)
        if book is None:
            return Response({'msg':'Provided Book Id is not available'})
        book.delete()
        return Response({'msg':'Data Deleted'})


# Fourth Way Function Based APIView
def get_by_object(id):
        try:
            book = BookModel.objects.get(id=id)
        except BookModel.DoesNotExist:
            book = None
        return book

@api_view(['GET','POST','PUT','PATCH','DELETE'])
def BooksFBAPIView(request, pk=None):
    if request.method == 'GET':
        if pk is not None:
            book = get_by_object(pk)
            if book is None:
                return Response({'msg':'Provided Book Id is not available'})
            serializer = BooksModelSerializer(book)
            return Response(serializer.data)
        books = BookModel.objects.all()
        serializer = BooksModelSerializer(books, many=True)
        return Response(serializer.data)


    elif request.method == 'POST':
        serializer = BooksModelSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Data Created'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'PUT':
        if pk is not None:
            book = get_by_object(pk)
            if book is None:
                return Response({'msg':'Provided Book Id is not available'})
        serializer = BooksModelSerializer(book, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Complete Updated Success'})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            
    elif request.method == 'PATCH':
        if pk is not None:
            book = get_by_object(pk)
            if book is None:
                return Response({'msg':'Provided Book Id is not available'})
        serializer = BooksModelSerializer(book, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Partial Updated Success'})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        if pk is not None:
            book = get_by_object(pk)
            if book is None:
                return Response({'msg':'Provided Book Id is not available'})
        book.delete()
        return Response({'msg':'Data Deleted'})