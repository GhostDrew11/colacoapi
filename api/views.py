from .models import Soda
from .serializers import UserSerializer, SodaSerializer
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User


# Create your views here.

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class SodaViewSet(viewsets.ModelViewSet):
    queryset = Soda.objects.all()
    serializer_class = SodaSerializer


