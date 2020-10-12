from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

SETTINGS = (
    ('Easy', 'Easy'),
    ('Medium', 'Medium'),
    ('Hard', 'Hard')
)

LEVELINGS = (
    ('Active', 'Active'),
    ('Standby', 'Standby')
)

COLORS = (
    ('text-white bg-primary', 'Blue'),
    ('text-white bg-secondary', 'Grey'),
    ('text-white bg-success', 'Green'),
    ('text-white bg-danger', 'Red'),
    ('text-white bg-warning', 'Yellow'),
    ('text-white bg-info', 'Aqua'),
    ('bg-light', 'White'),
    ('text-white bg-dark', 'Dark Grey')
)

class Talent(models.Model):
    skill = models.CharField(max_length=100)
    setting = models.CharField(
        max_length=20,
        choices=SETTINGS,
        default=SETTINGS[0][0]
    )
    leveling = models.CharField(
        max_length=20,
        choices=LEVELINGS,
        default=LEVELINGS[0][0]
    )
    image = models.CharField(max_length=1000)
    color = models.CharField(
        max_length=30,
        choices=COLORS,
        default=COLORS[0][0]
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.skill

    def get_absolute_url(self):
        return reverse('index')

