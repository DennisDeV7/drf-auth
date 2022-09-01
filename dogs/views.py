from telnetlib import DO
from dogs.permissions import IsOwnerOrReadOnly
from rest_framework import generics
from .serializers import DogSerializer
from .models import Dog


class DogList(generics.ListCreateAPIView):
    queryset = Dog.objects.all()
    serializer_class = DogSerializer


class DogDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsOwnerOrReadOnly,)
    queryset = Dog.objects.all()
    serializer_class = DogSerializer