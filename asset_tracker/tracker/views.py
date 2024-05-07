from rest_framework import generics
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from .models import Company, Device, Employee, DeviceAssignment
from .serializers import (
    CompanySerializer, DeviceSerializer, EmployeeSerializer, DeviceAssignmentSerializer
)

from django.contrib.auth import get_user_model

from rest_framework.generics import RetrieveAPIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ('id', 'username')


class UserAPIView(RetrieveAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = UserSerializer

    def get_object(self):
        return self.request.user


# Company Views

class CompanyListCreateView(generics.ListCreateAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer
    permission_classes = [IsAuthenticated]


class CompanyRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer
    permission_classes = [IsAuthenticated, IsAdminUser]


# Device Views

class DeviceListCreateView(generics.ListCreateAPIView):
    queryset = Device.objects.all()
    serializer_class = DeviceSerializer
    permission_classes = [IsAuthenticated]


class DeviceRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Device.objects.all()
    serializer_class = DeviceSerializer
    permission_classes = [IsAuthenticated, IsAdminUser]


class DeviceAssignView(generics.UpdateAPIView):
    queryset = DeviceAssignment.objects.all()
    serializer_class = DeviceAssignmentSerializer
    permission_classes = [IsAuthenticated, IsAdminUser]


# Employee Views

class EmployeeListCreateView(generics.ListCreateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    permission_classes = [IsAuthenticated]


class EmployeeRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    permission_classes = [IsAuthenticated, IsAdminUser]


class EmployeeAssignmentsListView(generics.ListAPIView):
    serializer_class = DeviceAssignmentSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        employee_id = self.kwargs['pk']
        return DeviceAssignment.objects.filter(employee=employee_id)
