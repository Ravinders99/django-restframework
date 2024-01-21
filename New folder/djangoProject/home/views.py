from django.shortcuts import render

# Create your views here.
from .models import Books
from .serializer import BooksSerializer
from rest_framework import viewsets, permissions
class BooksViewSet(viewsets.ModelViewSet):
    queryset = Books.objects.all()
    serializer_class =BooksSerializer
    permission_classes = [permissions.IsAuthenticated]
