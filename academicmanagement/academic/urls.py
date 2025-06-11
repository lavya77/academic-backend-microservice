from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    StudentViewSet, FacultyViewSet, DepartmentViewSet,
    MentorshipViewSet, AcademicCalendarViewSet
)

router = DefaultRouter()
router.register(r'students', StudentViewSet)
router.register(r'faculty', FacultyViewSet)
router.register(r'departments', DepartmentViewSet)
router.register(r'mentorships', MentorshipViewSet)
router.register(r'academic-calendar', AcademicCalendarViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
