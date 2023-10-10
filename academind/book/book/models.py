from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

rate_validator_condition = [MinValueValidator(1), MaxValueValidator(5)]

class Book(models.Model):
  title = models.CharField(max_length=50)
  rating = models.IntegerField(validators=rate_validator_condition)
  author = models.CharField(null=True, max_length=30)
  is_bestselling = models.BooleanField(default=False)
  pub_date = models.DateTimeField("date published")

  def __str__(self):
    return f"{self.title} by {self.author}"
      

class Category(models.Model):
  book_id = models.ForeignKey(Book, on_delete=models.CASCADE)
  type = models.CharField(max_length=30)
  votes = models.IntegerField(default=0)