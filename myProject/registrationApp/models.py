from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.
class PeopleReg(models.Model):
    first_name = models.CharField(max_length=50)
    middle_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    age = models.IntegerField(
        default=5,
        validators=[
            MaxValueValidator(100),
            MinValueValidator(0)
        ]
     )
    # renames the instances of the model
    # with their title name
    def __str__(self):
        return self.first_name

