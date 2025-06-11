from django.db import models

# Create your models here.


class Department(models.Model):
    department_code = models.CharField(max_length=10, unique=True)
    department_name = models.CharField(max_length=100)
    hod_faculty_id = models.IntegerField()  # FK to Faculty (can also be models.ForeignKey)
    facilities = models.JSONField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.department_name


class Faculty(models.Model):
    user_id = models.IntegerField()  # FK to User Service
    employee_code = models.CharField(max_length=20, unique=True)
    designation = models.CharField(max_length=100)
    department = models.ForeignKey(Department, on_delete=models.CASCADE, related_name='faculties')
    qualification = models.CharField(max_length=100)
    research_interests = models.JSONField()
    publications = models.JSONField()
    is_mentor = models.BooleanField(default=False)
    joining_date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.employee_code


class Student(models.Model):
    user_id = models.IntegerField()  # FK to User Service
    enrollment_number = models.CharField(max_length=20, unique=True)
    program = models.CharField(max_length=100)
    batch = models.CharField(max_length=10)
    current_semester = models.PositiveIntegerField()
    branch = models.CharField(max_length=50)
    cgpa = models.DecimalField(max_digits=4, decimal_places=2)
    total_credits = models.PositiveIntegerField()
    backlog_count = models.PositiveIntegerField()
    registration_status = models.CharField(max_length=50)
    academic_goals = models.JSONField()
    skills_strengths = models.JSONField()
    admission_date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.enrollment_number


class Mentorship(models.Model):
    mentor = models.ForeignKey(Faculty, on_delete=models.CASCADE, related_name='mentorships')
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='mentorships')
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    status = models.CharField(max_length=50)
    goals = models.JSONField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Mentorship ({self.mentor_id} → {self.student_id})"


class AcademicCalendar(models.Model):
    department = models.ForeignKey(Department, on_delete=models.CASCADE, related_name='academic_calendars')
    academic_year = models.CharField(max_length=20)
    semester = models.PositiveIntegerField()
    semester_start = models.DateField()
    semester_end = models.DateField()
    exam_start = models.DateField()
    exam_end = models.DateField()
    important_dates = models.JSONField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.academic_year} - Sem {self.semester}"

