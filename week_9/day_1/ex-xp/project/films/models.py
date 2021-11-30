from django.db import models

# Create your models here.
class Country(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Country"

class Category(models.Model):
    name = models.CharField(max_length=50)


    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Category"


class Director(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)

    def __str__(self):
        return self.first_name + ' ' + self.last_name

class Film(models.Model):
    title = models.CharField(max_length=100)
    release_date = models.DateTimeField(auto_now_add=True)
    created_in_country = models.ForeignKey(Country, on_delete = models.PROTECT)
    available_in_countries  = models.ManyToManyField(Country, related_name = "available_in_countries")
    category  = models.ManyToManyField(Category )
    director  = models.ManyToManyField(Director)

    def __str__(self):
        return self.title
