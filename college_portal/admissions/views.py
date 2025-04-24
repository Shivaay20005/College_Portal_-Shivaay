from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import StudentApplicationForm
from .models import Faculty, StudentApplication

# ------------------- Home & Static Pages -------------------

def home(request):
    return render(request, 'admissions/home.html')

def about(request):
    return render(request, 'admissions/about.html')

def contact(request):
    return render(request, 'admissions/contact.html')

def admissions(request):
    return render(request, 'admissions/admissions.html')


# ------------------- Student Login & Dashboard -------------------

def student_login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        dob = request.POST.get('dob')  # Format should match what's stored

        try:
            student = StudentApplication.objects.get(email=email, date_of_birth=dob)
            request.session['student_id'] = student.id
            return redirect('student_dashboard')
        except StudentApplication.DoesNotExist:
            messages.error(request, "❌ Invalid credentials. Please try again.")

    return render(request, 'admissions/login.html')


def student_dashboard(request):
    student_id = request.session.get('student_id')
    if not student_id:
        return redirect('student_login')

    try:
        student = StudentApplication.objects.get(id=student_id)
        return render(request, 'admissions/student_dashboard.html', {'student': student})
    except StudentApplication.DoesNotExist:
        messages.error(request, "❌ Student not found.")
        return redirect('student_login')


# ------------------- Application Form -------------------

def apply(request):
    if request.method == 'POST':
        form = StudentApplicationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/apply/?submitted=true')
        else:
            messages.error(request, "❌ Please fix the errors below.")
    else:
        form = StudentApplicationForm()

    submitted = request.GET.get('submitted') == 'true'
    return render(request, 'admissions/apply.html', {
        'form': form,
        'submitted': submitted
    })


# ------------------- Faculty Page -------------------
# admissions/views.py
from django.shortcuts import render
from .models import Faculty
from collections import defaultdict

def faculty(request):
    departments = defaultdict(list)
    for member in Faculty.objects.all():
        departments[member.department].append(member)
    return render(request, 'admissions/faculty.html', {'departments': dict(departments)})



def apply_view(request):
    return render(request, 'admission/apply.html')  # Ensure apply.html exists





# ------------------- Contact Page -------------------
def contact(request):
    return render(request, 'admissions/contact.html')
# ------------------- About Page -------------------
def about(request):
    return render(request, 'admissions/about.html')
from django.shortcuts import render
from datetime import datetime

def admission_form(request):
    # Assuming you get the student's details here
    submission_date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')  # Current date-time
    return render(request, 'admission_form.html', {'submission_date': submission_date})
