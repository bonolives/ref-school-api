from django.shortcuts import render
from .models import *
from .serializers import *
from rest_framework import generics
from rest_framework.pagination import PageNumberPagination
# Create your views here.

# Custom pagination class (optional)
class CustomPagination(PageNumberPagination):
    page_size = 10  # Number of staff members per page
    page_size_query_param = 'page_size'
    max_page_size = 100
#staff
class StaffView(generics.ListCreateAPIView):# retrieve
    queryset = StaffMember.objects.all()
    serializer_class = StaffMemberSerializer
    pagination_class = CustomPagination
    
class SingleStaffView(generics.RetrieveUpdateAPIView, generics.RetrieveDestroyAPIView): # 
    queryset = StaffMember.objects.all()
    serializer_class = StaffMemberSerializer
    
    #Student
class StudentView(generics.ListCreateAPIView):# retrieve
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    pagination_class = CustomPagination
    
class SingleStudentView(generics.RetrieveUpdateAPIView, generics.RetrieveDestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    
    #Course
class CourseView(generics.ListCreateAPIView):# retrieve
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    pagination_class = CustomPagination

class SingleCourseView(generics.RetrieveUpdateAPIView, generics.RetrieveDestroyAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    
#Department
class DepartmentView(generics.ListCreateAPIView):# retrieve
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer
    pagination_class = CustomPagination

class SingleDepartmentView(generics.RetrieveUpdateAPIView, generics.RetrieveDestroyAPIView):
    queryset = Course.objects.all()
    serializer_class = DepartmentSerializer
    
#Club
class ClubView(generics.ListCreateAPIView):# retrieve
    queryset = Club.objects.all()
    serializer_class = ClubSerializer
    pagination_class = CustomPagination

class SingleClubView(generics.RetrieveUpdateAPIView, generics.RetrieveDestroyAPIView):
    queryset = Club.objects.all()
    serializer_class = ClubSerializer