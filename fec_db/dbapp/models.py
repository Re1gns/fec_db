from django.db import models
from django.utils.html import mark_safe
import random
from django.conf import settings

class ReferenceID(models.Model):
    @classmethod
    def generate_reference_id(cls):
        random_id = random.randint(1000, 9999)
        return f'FEC24{random_id}'
    
class MemberInformation(models.Model):
    SEX_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
    ]
    MARITAL_STATUS_CHOICES = [
        ('S', 'Single'),
        ('M', 'Married'),
        ('W', 'Widow or Widower'),
    ]
    BLOOD_GROUP_CHOICES = [
        ('A', 'A'),
        ('B', 'B'),
        ('AB', 'AB'),
        ('O', 'O'),
    ]
    RHESUS_CHOICES = [
        ('+', 'Positive'),
        ('-', 'Negative'),
    ]
    PROFESSION_SECTOR_CHOICES = [
        ('CS', 'Civil Servant'),
        ('PS', 'Public Servant'),
        ('PRI', 'Private Sector'),
        ('ART', 'Artisan'),
        ('RET', 'Retired'),
        ('STU', 'STUDENT')
    ]
    Fellowship_Group_Choices = [
        ('M', 'Men'),
        ('W', 'Women'),
        ('Y', 'Youth'),
    ]
    Church_Status_Choices = [
        ('A', 'Active'),
        ('D', 'Diaspora')
    ]
    options = [
        ('Y', 'Yes'),
        ('N', 'No'),
    ]

    # Basic Information Fields
    reference_id = models.CharField(max_length=9, default=ReferenceID.generate_reference_id, editable=False)
    timestamp = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='images/', blank=True, null=True)
    surname = models.CharField(max_length=100)
    other_names = models.CharField(max_length=100)
    sex = models.CharField(max_length=1, choices=SEX_CHOICES)
    date_of_birth = models.DateField()
    phone_number = models.CharField(max_length=15)
    whatsapp_number = models.CharField(max_length=15)
    email = models.EmailField()
    home_address = models.TextField()
    house_fellowship_zone = models.CharField(max_length=100)
    next_of_kin = models.CharField(max_length=100)
    next_of_kin_phone_number = models.CharField(max_length=15)
    home_town = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    lga = models.CharField(max_length=100, verbose_name="Local Government Area")
    nationality = models.CharField(max_length=100)
    tribe = models.CharField(max_length=100)
    other_languages = models.CharField(max_length=100)
    close_townmate = models.CharField(max_length=100, verbose_name="Close Townmate")
    townmate_phone_number = models.CharField(max_length=15, verbose_name="Townmate's Phone Number")
    
    # Marital Status Fields
    marital_status = models.CharField(max_length=1, choices=MARITAL_STATUS_CHOICES)
    other_information = models.CharField(max_length=100, blank=True, null=True)
    
    # Health Fields
    blood_group = models.CharField(max_length=2, choices=BLOOD_GROUP_CHOICES)
    rhesus = models.CharField(max_length=1, choices=RHESUS_CHOICES)
    
    # Profession Fields
    profession_sector = models.CharField(max_length=3, choices=PROFESSION_SECTOR_CHOICES)
    employed = models.CharField(max_length=1, choices=options)
    profession = models.CharField(max_length=150, blank=True, null=True)
    place_of_work = models.CharField(max_length=100, blank=True, null=True)
    position_at_work = models.CharField(max_length=100, blank=True, null=True)
    w_year = models.DateField(blank=True, null=True)
    student = models.CharField(max_length=3, choices=options, blank=True, null=True)
    field_of_study = models.CharField(max_length=100, verbose_name="Field or Course of Study", blank=True, null=True)
    school = models.CharField(max_length=150, blank=True, null=True)
    position_in_school = models.CharField(max_length=100, blank=True, null=True)
    s_year = models.DateField(blank=True, null=True)
    
    # Church Information Fields
    baptised = models.CharField(max_length=3, choices=options)
    by_immersion = models.CharField(max_length=3, choices=options)
    denomination = models.CharField(max_length=150)
    church_worker = models.CharField(max_length=3, choices=options)
    units = models.CharField(max_length=200)
    church_group = models.CharField(max_length=150)
    fellowship_group = models.CharField(max_length=5, choices = Fellowship_Group_Choices)
    other_relevant_information = models.TextField(blank=True, null=True)
    name_of_member_closest_to_you = models.CharField(max_length=150)
    when_did_you_become_a_member_of_the_church =models.CharField(max_length=20)
    church_status = models.CharField(max_length=10, choices = Church_Status_Choices)
    leadership_position_held1 = models.CharField(max_length=50, blank=True, null=True)
    year1 = models.DateField(blank=True, null=True)
    leadership_position_held2 = models.CharField(max_length=50, blank=True, null=True)
    year2 = models.DateField(blank=True, null=True)
    leadership_position_held3 = models.CharField(max_length=50, blank=True, null=True)
    year3 = models.DateField(blank=True, null=True)
    leadership_position_held4 = models.CharField(max_length=50, blank=True, null=True)
    year4 = models.DateField(blank=True, null=True)
    leadership_position_held5 = models.CharField(max_length=50, blank=True, null=True)
    year5 = models.DateField(blank=True, null=True)

    #For Children Below 17 Years
    current_class = models.CharField(max_length=150, blank=True, null=True)
    current_class_year = models.DateField(blank=True, null=True)
    current_school = models.CharField(max_length=150, blank=True, null=True)
    current_school_year = models.DateField(blank=True, null=True)

    #Official Use
    comment_on_member = models.TextField(blank=True, null=True)

    def image_tag(self):
        print (self.image.name)
        if self.image:
            image_url = f"{settings.MEDIA_URL}{self.image.name}"
            return mark_safe(f'<img src="{image_url}" width="60" />')
        else:
            return "No_Image"


    def save(self, *args, **kwargs):
        if not self.reference_id:
            self.reference_id = self.generate_reference_id()
        self.surname = self.surname.upper()
        super().save(*args, **kwargs)

    @classmethod
    def generate_reference_id(cls):
        random_id = random.randint(1000, 9999)
        return f'FEC24{random_id}'