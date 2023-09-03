''' Candidate directory Model '''

from django.db import models
import random
import uuid
import string
import os

from django.conf import settings


def random_string_generator(size=10, chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))


def unique_key_generator(instance):
    size = random.randint(30, 45)
    key = random_string_generator(size=size)
    return key


def get_filename_ext(filepath):
    base_name = os.path.basename(filepath)
    name, ext = os.path.splitext(base_name)
    return name, ext


def upload_image_path(instance, filename):
    new_filename = random.randint(1,3910209312)
    name, ext = get_filename_ext(filename)
    final_filename = '{new_filename}{ext}'.format(new_filename=new_filename, ext=ext)
    return "images/{final_filename}".format(
            final_filename=final_filename
            )


def upload_file_path(instance, filename):
    new_filename =unique_key_generator(instance)
    name, ext = get_filename_ext(filename)
    final_filename = '{new_filename}{ext}'.format(new_filename=new_filename,ext=ext)
    return "files/{final_filename}".format(
        final_filename=final_filename
        )


class Eventdetails(models.Model):
    event = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        db_table = 'event_details'

    def __str__(self):
        return self.event


class Jobrequisition(models.Model):
    job_position = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        db_table = "job_position"

    def __str__(self):
        return self.job_position


class Persona(models.Model):
    persona = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        db_table = "persona"

    def __str__(self):
        return self.persona


class Screeningmode(models.Model):
    screening_mode = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        db_table = "screening_mode"

    def __str__(self):
        return self.screening_mode


class Gender(models.Model):
    gender = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        db_table = "gender"

    def __str__(self):
        return self.gender


class Maritalstatus(models.Model):
    marital_status = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        db_table = "marital_status"

    def __str__(self):
        return self.marital_status


class Employeedirectory(models.Model):
    referred_by = models.CharField(max_length=255, blank=True, null=True)
    referred_by_other = models.CharField(max_length=250, blank=True, null=True)
    address_line = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        db_table = "employee_directory"

    def __str__(self):
        return self.referred_by


class City(models.Model):
    city = models.CharField(max_length=255, blank=True, null=True)
    pincode = models.DecimalField(max_digits=6, decimal_places=0, blank=True, null=True)

    class Meta:
        db_table = "city"

    def __str__(self):
        return self.city


class Experiencelevel(models.Model):
    experience_level = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        db_table = "experience_level"

    def __str__(self):
        return self.experience_level


class Educationlevel(models.Model):
    education_level = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        db_table = "educational_level"

    def __str__(self):
        return self.education_level


class Educationqualification(models.Model):
    education_qualification = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        db_table = "education_qualification"

    def __str__(self):
        return self.education_qualification


class Educationspecialization(models.Model):
    education_specialization = models.CharField(max_length=255, blank=True, null=True)
    education_specialization_other = models.TextField(blank=True, null=True)

    class Meta:
        db_table = "education_specialization"

    def __str__(self):
        return self.education_specialization


class Source(models.Model):
    education_institution = models.CharField(max_length=255, blank=True, null=True)
    education_institution_other = models.TextField(blank=True, null=True)

    class Meta:
        db_table = "source"

    def __str__(self):
        return self.education_institution


class Sourcetype(models.Model):
    source_type = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        db_table = "source_type"

    def __str__(self):
        return self.source_type


class Reasonforchange(models.Model):
    reason_for_change = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        db_table = "reason_for_change"

    def __str__(self):
        return self.reason_for_change


class Candidatedirectory(models.Model):
    event = models.ForeignKey(Eventdetails, on_delete=models.SET_NULL, null=True, blank=True)
    job_position = models.ForeignKey(Jobrequisition, on_delete=models.SET_NULL, null=True, blank=True)

    first_name = models.CharField(max_length=255, blank=True, null=True)
    last_name = models.CharField(max_length=255, blank=True, null=True)
    email = models.CharField(max_length=50, blank=True, null=True)

    persona = models.ForeignKey(Persona, on_delete=models.SET_NULL, null=True, blank=True)
    screening_mode = models.ForeignKey(Screeningmode, on_delete=models.SET_NULL, null=True, blank=True)
    gender = models.ForeignKey(Gender, on_delete=models.SET_NULL, null=True, blank=True)

    recruiter_alert = models.CharField(max_length=50, blank=True, null=True)
    role = models.CharField(max_length=255, blank=True, null=True)
    contact_no_primary = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    contact_no_alternate = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)

    years_of_experience = models.DecimalField(
        max_digits=4, decimal_places=2, blank=True, null=True)
    current_employer = models.CharField(max_length=255, blank=True, null=True)
    current_designation = models.CharField(max_length=255, blank=True, null=True)
    current_monthly_salary = models.IntegerField(blank=True, null=True)
    expected_monthly_salary = models.IntegerField(blank=True, null=True)
    notice_period = models.CharField(max_length=255, blank=True, null=True)

    photo_path = models.ImageField(upload_to=upload_image_path, null=True, blank=True)
    resume_path = models.FileField(upload_to=upload_file_path, null=True, blank=True)

    marital_status = models.ForeignKey(Maritalstatus, on_delete=models.SET_NULL, null=True, blank=True)
    employee_directory = models.ForeignKey(Employeedirectory, on_delete=models.SET_NULL, null=True, blank=True)
    city = models.ForeignKey(City, on_delete=models.SET_NULL, null=True, blank=True)
    experience_level = models.ForeignKey(Experiencelevel, on_delete=models.SET_NULL, null=True, blank=True)
    educational_level = models.ForeignKey(Educationlevel, on_delete=models.SET_NULL, null=True, blank=True)
    equ_qualification = models.ForeignKey(Educationqualification, on_delete=models.SET_NULL, null=True, blank=True)
    equ_specialization = models.ForeignKey(Educationspecialization, on_delete=models.SET_NULL, null=True, blank=True)
    source = models.ForeignKey(Source, on_delete=models.SET_NULL, null=True, blank=True)
    source_type = models.ForeignKey(Sourcetype, on_delete=models.SET_NULL, null=True, blank=True)
    reason_for_change = models.ForeignKey(Reasonforchange, on_delete=models.SET_NULL, null=True, blank=True)

    login_time = models.DateTimeField(blank=True, null=True)
    logout_time = models.DateTimeField(blank=True, null=True)

    ip_address = models.CharField(max_length=15, blank=True, null=True)
    geo_location = models.CharField(max_length=50, blank=True, null=True)
    created_date = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    created_by = models.IntegerField(blank=True, null=True)
    modified_date = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    modified_by = models.IntegerField(blank=True, null=True)
    status = models.IntegerField(default=1)

    class Meta:
        db_table = 'candidate_directory'

    def __str__(self):
        return self.first_name

    constraints = [
        models.UniqueConstraint(fields=['first_name', 'last_name'], name='unique appversion')
    ]
