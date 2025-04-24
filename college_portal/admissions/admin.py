from django.contrib import admin
from .models import StudentApplication


admin.site.register(StudentApplication)
# admissions/admin.py

from django.contrib import admin
from .models import Faculty

admin.site.register(Faculty)
