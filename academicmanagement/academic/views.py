from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from .models import Student, Faculty, Department, Mentorship, AcademicCalendar
from .serializers import (
    StudentSerializer, FacultySerializer, DepartmentSerializer,
    MentorshipSerializer, AcademicCalendarSerializer
)


class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


class FacultyViewSet(viewsets.ModelViewSet):
    queryset = Faculty.objects.all()
    serializer_class = FacultySerializer


class DepartmentViewSet(viewsets.ModelViewSet):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer


class MentorshipViewSet(viewsets.ModelViewSet):
    queryset = Mentorship.objects.all()
    serializer_class = MentorshipSerializer


class AcademicCalendarViewSet(viewsets.ModelViewSet):
    queryset = AcademicCalendar.objects.all()
    serializer_class = AcademicCalendarSerializer

