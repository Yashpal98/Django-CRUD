from django.db import models
from multiselectfield import MultiSelectField

# Create your models here.

gender_choice = [
    ('Male', 'Male'),
    ('Female', 'Female')
]

hobby_choice = [
    ('Cricket', 'Cricket'),
    ('Movies', 'Movies'),
    ('Songs', 'Songs'),
    ('Football', 'Football')
]

class Person(models.Model):
    name = models.CharField(max_length=55)
    gender = models.CharField(max_length=11,choices=gender_choice, null=False, blank=False, default='')
    hobby = MultiSelectField(choices=hobby_choice)

    # objects = PersonQuerySet().as_manager()

    def __str__(self):
        return self.name
    