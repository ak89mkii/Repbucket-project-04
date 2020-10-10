from django.db import models

SETTINGS = (
    ('B', 'Morning'),
    ('L', 'Noon'),
    ('D', 'Night')
)

LEVELINGS = (
    ('B', 'Morning'),
    ('L', 'Noon')
)

class Talent(models.Model):
    skill = models.CharField(max_length=100)
    setting = models.CharField(
        max_length=1,
        choices=SETTINGS,
        default=SETTINGS[0][0]
    )
    leveling = models.CharField(
        max_length=1,
        choices=LEVELINGS,
        default=LEVELINGS[0][0]
    )
    image = models.CharField(max_length=1000)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
