from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
# from django.contrib.auth.models import User

# Create your models here.


class MovieDB(models.Model):
  name = models.CharField(max_length=100, blank=False)
  rating = models.FloatField(validators=[MinValueValidator(0), MaxValueValidator(10)], blank=False)
  release = models.DateField(blank=False)
  duration = models.DurationField(help_text="value must be in '%d %H:%M:%S.%f' format.", blank=False)
  description = models.TextField(max_length=300, blank=False)

  
  def __str__(self):
    return f"{self.name} | {self.duration}"

  class Meta:
    verbose_name = "Movies"
    unique_together = [("name", "release")]
    ordering = ("-rating", "-release", "name")
