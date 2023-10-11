from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.urls import reverse

rate_validator_condition = [MinValueValidator(1), MaxValueValidator(10)]

class Author(models.Model):
  first_name = models.CharField(max_length=50)
  last_name = models.CharField(max_length=50)

  def __str__(self):
    return f"{self.first_name} {self.last_name}"


class Category(models.Model):
  type = models.CharField(max_length=30)

  def __str__(self):
    return f"{self.type.upper()}"
  

class Book(models.Model):
  title = models.CharField(max_length=50)
  rating = models.IntegerField(validators=rate_validator_condition)
  author = models.ForeignKey(Author, on_delete=models.CASCADE, null=True, related_name='books')
  category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, related_name='books')
  is_bestselling = models.BooleanField(default=False)
  pub_date = models.DateTimeField("date published")
  slug = models.SlugField(default="", blank=True, null=False, db_index=True) # editable=False

  def __str__(self):
    return f"{self.title} by author {self.author}"
  
  def get_absolute_url(self):
    return reverse("book-details", args=[self.slug])


