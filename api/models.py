from django.db import models

# Create your models here.


class Books(models.Model):
    title = models.CharField(max_length=200)
    authors = models.CharField(max_length=200)
    published_date = models.CharField(max_length=200)
    categories = models.CharField(max_length=200)
    average_rating = models.IntegerField()
    rating_count = models.IntegerField()
    thumbnail = models.CharField(max_length=200)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Books'
        verbose_name_plural = 'Books'