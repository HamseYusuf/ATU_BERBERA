from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    publication_date = models.DateField()
    price = models.DecimalField(max_digits=6 , decimal_places=2)

    def __str__(self):
        return self.title

class Post(models.Model):
    title  = models.CharField(max_length=100)
    content = models.TextField()
    image = models.ImageField(upload_to="post_images/" ,  blank = True , null = True)

    def __str__(self):
        return self.title

    