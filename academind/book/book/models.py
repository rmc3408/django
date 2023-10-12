from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.urls import reverse

rate_validator_condition = [MinValueValidator(1), MaxValueValidator(10)]

class Country(models.Model):
  name = models.CharField(max_length=20)
  code = models.CharField(max_length=2)

  def __str__(self):
    return f"{self.name}"
  
  class Meta:
    verbose_name_plural = 'Countries'


class Address(models.Model):
  city = models.CharField(max_length=20)
  postal_code = models.CharField(max_length=6)

  def __str__(self):
    return f"{self.city}-{self.postal_code}"
  
  class Meta:
    verbose_name_plural = 'Addresses'


class Author(models.Model):
  first_name = models.CharField(max_length=50)
  last_name = models.CharField(max_length=50)
  address = models.OneToOneField(Address, on_delete=models.CASCADE, null=True)

  def full_name(self):
    return f"{self.first_name} {self.last_name}"
  
  def __str__(self):
    return self.full_name()


class Category(models.Model):
  type = models.CharField(max_length=30)

  def __str__(self):
    return f"{self.type}"
  

class Book(models.Model):
  title = models.CharField(max_length=50)
  rating = models.IntegerField(validators=rate_validator_condition)
  is_bestselling = models.BooleanField(default=False)
  pub_date = models.DateTimeField("date published")

  author = models.ForeignKey(Author, on_delete=models.CASCADE, null=True, related_name='books')
  category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, related_name='books')
  published = models.ManyToManyField(Country, null=True)
   
  slug = models.SlugField(default="", blank=True, null=False, db_index=True) # editable=False

  def __str__(self):
    return f"{self.title} by author {self.author}"
  
  def get_absolute_url(self):
    return reverse("book-details", args=[self.slug])


