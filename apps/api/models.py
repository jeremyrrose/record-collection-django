from django.db import models
from apps.authentication.models import User

# Create your models here.


class Artist(models.Model):
    class Meta:
        verbose_name_plural = "artists"

    name = models.CharField(max_length=255, unique=True)
    hot_100_hits = models.IntegerField()


class Record(models.Model):
    class Meta:
        verbose_name_plural = "records"

    title = models.CharField(max_length=255)
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE, related_name='records')
    release_year = models.IntegerField()
    cover_image = models.URLField(max_length=455)


class Collection(models.Model):
    class Meta:
        verbose_name_plural = "collections"
    
    owner = models.OneToOneField(User, on_delete=models.CASCADE)
    records = models.ManyToManyField(Record)
    public = models.BooleanField(default=False)

    def __str__(self):
        return f'Collection: Owner {self.owner.username}, {self.records.count()} records'


# class Category(models.Model):
#     class Meta:
#         verbose_name_plural = 'categories'

#     name = models.CharField(max_length=100)
#     owner = models.ForeignKey(User, on_delete=models.CASCADE)
#     description = models.TextField(blank=True)
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)

#     def __str__(self):
#         return self.name


# class Recipe(models.Model):

#     owner = models.ForeignKey(User, on_delete=models.CASCADE)
#     category = models.ForeignKey(Category, related_name='recipes', on_delete=models.CASCADE)
#     name = models.CharField(max_length=100)
#     description = models.TextField(blank=True)
#     ingredients = models.TextField()
#     directions = models.TextField()
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)
#     is_public = models.BooleanField(default=False)

#     def __str__(self):
#         return self.name
