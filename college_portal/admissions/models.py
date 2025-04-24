from django.db import models

class StudentApplication(models.Model):
    # 🎓 Basic Information
    full_name = models.CharField(max_length=100)
    gender_choices = [('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')]
    gender = models.CharField(max_length=10, choices=gender_choices)
    date_of_birth = models.DateField()
    blood_group = models.CharField(max_length=10, blank=True, null=True)
    nationality = models.CharField(max_length=50)
    religion = models.CharField(max_length=50)
    caste_category_choices = [('General', 'General'), ('OBC', 'OBC'), ('SC', 'SC'), ('ST', 'ST')]
    caste_category = models.CharField(max_length=10, choices=caste_category_choices)

    # 🏠 Contact Details
    mobile_number = models.CharField(max_length=15)
    email = models.EmailField(unique=True)
    parent_mobile_number = models.CharField(max_length=15)
    parent_email = models.EmailField()
    present_address = models.TextField()
    permanent_address = models.TextField()

    # 👨‍👩‍👧 Parent/Guardian Info
    father_name = models.CharField(max_length=100)
    father_occupation = models.CharField(max_length=100, blank=True, null=True)
    father_contact = models.CharField(max_length=15, blank=True, null=True)
    mother_name = models.CharField(max_length=100)
    mother_occupation = models.CharField(max_length=100, blank=True, null=True)
    mother_contact = models.CharField(max_length=15, blank=True, null=True)
    guardian_name = models.CharField(max_length=100, blank=True, null=True)
    guardian_relation = models.CharField(max_length=100, blank=True, null=True)

    # 📚 Academic Info
    last_school_name = models.CharField(max_length=100)
    last_class_passed = models.CharField(max_length=100)
    year_of_passing = models.PositiveIntegerField()
    board_name = models.CharField(max_length=100)
    marks_obtained = models.FloatField()
    percentage = models.FloatField()
    subjects_studied = models.TextField()

    # 🏫 Course & Admission Info
    course_applying_for_choices = [
        ('BTECH', 'B.Tech'),
        ('MTECH', 'M.Tech'),
        ('BCA', 'BCA'),
        ('MCA', 'MCA'),
        ('MBA', 'MBA'),
        ('BBA', 'BBA'),
        ('BSC', 'B.Sc.')
    ]
    course_applying_for = models.CharField(max_length=10, choices=course_applying_for_choices)
    branch = models.CharField(max_length=100)
    medium_of_instruction_choices = [('English', 'English'), ('Hindi', 'Hindi')]
    medium_of_instruction = models.CharField(max_length=10, choices=medium_of_instruction_choices)
    academic_year = models.CharField(max_length=20)
    admission_category_choices = [('General', 'General'), ('Reserved', 'Reserved')]
    admission_category = models.CharField(max_length=10, choices=admission_category_choices)

    # 📁 Documents
    profile_picture = models.ImageField(upload_to='profile_pictures/')
    signature = models.ImageField(upload_to='signatures/')
    aadhar_card = models.FileField(upload_to='aadhar_cards/')

    # 📅 Additional Info
    hostel_required = models.BooleanField(default=False)
    transport_required = models.BooleanField(default=False)
    scholarship_applied = models.BooleanField(default=False)

    # Timestamp
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.full_name}"






# admissions/models.py
from django.db import models

class Faculty(models.Model):
    DEPARTMENT_CHOICES = [
        ('Physics', 'B.Sc. Physics'),
        ('Chemistry', 'B.Sc. Chemistry'),
        ('Electronics', 'B.Sc. Electronics'),
        ('Math', 'B.Sc. Mathematics'),
        ('CS', 'Computer Science'),
        ('BioMed', 'Biomedical Science'),
        ('Botany', 'Botany'),
        ('Zoology', 'Zoology'),
        ('BCom', 'B.Com'),
    ]

    name = models.CharField(max_length=100)
    department = models.CharField(max_length=50, choices=DEPARTMENT_CHOICES)
    photo = models.ImageField(upload_to='faculty_photos/')
    designation = models.CharField(max_length=100, default='Assistant Professor')
    experience = models.PositiveIntegerField()
    email = models.EmailField()
    contact = models.CharField(max_length=20, blank=True, null=True)

    def __str__(self):
        return self.name
