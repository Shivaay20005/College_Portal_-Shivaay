from django import forms
from .models import StudentApplication

class StudentApplicationForm(forms.ModelForm):
    class Meta:
        model = StudentApplication
        fields = '__all__'
        widgets = {
            # 🎓 Basic Information
            'full_name': forms.TextInput(attrs={'placeholder': 'Your full name', 'class': 'form-input'}),
            'gender': forms.Select(attrs={'class': 'form-select'}),
            'date_of_birth': forms.DateInput(attrs={'type': 'date', 'class': 'form-input'}),
            'blood_group': forms.TextInput(attrs={'placeholder': 'Blood group (optional)', 'class': 'form-input'}),
            'nationality': forms.TextInput(attrs={'placeholder': 'Your nationality', 'class': 'form-input'}),
            'religion': forms.TextInput(attrs={'placeholder': 'Your religion', 'class': 'form-input'}),
            'caste_category': forms.Select(attrs={'class': 'form-select'}),

            # 🏠 Contact Details
            'mobile_number': forms.TextInput(attrs={'placeholder': 'Your mobile number', 'class': 'form-input'}),
            'email': forms.EmailInput(attrs={'placeholder': 'email@example.com', 'class': 'form-input'}),
            'parent_mobile_number': forms.TextInput(attrs={'placeholder': 'Your parent\'s mobile number', 'class': 'form-input'}),
            'parent_email': forms.EmailInput(attrs={'placeholder': 'parent_email@example.com', 'class': 'form-input'}),
            'present_address': forms.Textarea(attrs={'placeholder': 'Your present address', 'class': 'form-textarea'}),
            'same_address': forms.CheckboxInput(attrs={'class': 'form-checkbox'}),

            # 👨‍👩‍👧 Parent/Guardian Info
            'father_name': forms.TextInput(attrs={'placeholder': 'Your father\'s name', 'class': 'form-input'}),
            'father_occupation': forms.TextInput(attrs={'placeholder': 'Father\'s occupation (optional)', 'class': 'form-input'}),
            'father_contact': forms.TextInput(attrs={'placeholder': 'Father\'s contact number (optional)', 'class': 'form-input'}),
            'mother_name': forms.TextInput(attrs={'placeholder': 'Your mother\'s name', 'class': 'form-input'}),
            'mother_occupation': forms.TextInput(attrs={'placeholder': 'Mother\'s occupation (optional)', 'class': 'form-input'}),
            'mother_contact': forms.TextInput(attrs={'placeholder': 'Mother\'s contact number (optional)', 'class': 'form-input'}),
            'guardian_name': forms.TextInput(attrs={'placeholder': 'Guardian\'s name (optional)', 'class': 'form-input'}),
            'guardian_relation': forms.TextInput(attrs={'placeholder': 'Guardian\'s relation (optional)', 'class': 'form-input'}),

            # 📚 Academic Info
            'last_school_name': forms.TextInput(attrs={'placeholder': 'Last school name', 'class': 'form-input'}),
            'last_class_passed': forms.TextInput(attrs={'placeholder': 'Last class passed', 'class': 'form-input'}),
            'year_of_passing': forms.NumberInput(attrs={'placeholder': 'Year of passing', 'class': 'form-input'}),
            'board_name': forms.TextInput(attrs={'placeholder': 'Board name', 'class': 'form-input'}),
            'marks_obtained': forms.NumberInput(attrs={'placeholder': 'Marks obtained', 'class': 'form-input'}),
            'percentage': forms.NumberInput(attrs={'placeholder': 'Percentage', 'class': 'form-input'}),
            'subjects_studied': forms.Textarea(attrs={'placeholder': 'Subjects studied', 'class': 'form-textarea'}),

            # 🏫 Course & Admission
            'course_applying_for': forms.Select(attrs={'class': 'form-select'}),
            'branch': forms.TextInput(attrs={'placeholder': 'Course branch', 'class': 'form-input'}),
            'medium_of_instruction': forms.Select(attrs={'class': 'form-select'}),
            'academic_year': forms.TextInput(attrs={'placeholder': 'Academic year', 'class': 'form-input'}),
            'admission_category': forms.Select(attrs={'class': 'form-select'}),

            # 📁 Documents
            'profile_picture': forms.ClearableFileInput(attrs={'class': 'form-input'}),
            'signature': forms.ClearableFileInput(attrs={'class': 'form-input'}),
            'aadhar_card': forms.ClearableFileInput(attrs={'class': 'form-input'}),

            # 📅 Additional Info
            'hostel_required': forms.CheckboxInput(attrs={'class': 'form-checkbox'}),
            'transport_required': forms.CheckboxInput(attrs={'class': 'form-checkbox'}),
            'scholarship_applied': forms.CheckboxInput(attrs={'class': 'form-checkbox'}),
        }
