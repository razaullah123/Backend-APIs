from django.db import models

# Create your models here


class Category(models.Model):
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['title']


class Car(models.Model):
    title = models.CharField(max_length=255,null=True,blank=True)
    color = models.CharField(max_length=255,)
    model = models.IntegerField()
    register_num = models.IntegerField()
    category = models.ForeignKey(Category, on_delete=models.PROTECT, related_name='cars')

    def __str__(self):
        return self.color

    class Meta:
        ordering = ['color']




