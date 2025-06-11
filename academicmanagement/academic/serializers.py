from rest_framework import serializers
from .models import Student, Faculty, Department, Mentorship, AcademicCalendar


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'


class FacultySerializer(serializers.ModelSerializer):
    class Meta:
        model = Faculty
        fields = '__all__'


class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = '__all__'


class MentorshipSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mentorship
        fields = '__all__'


class AcademicCalendarSerializer(serializers.ModelSerializer):
    class Meta:
        model = AcademicCalendar
        fields = '__all__'
