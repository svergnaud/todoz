from django.db import models


# Create your models here.

class Category(models.Model):
    #id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class ToDoEntry(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    done = models.BooleanField(default=False)
    creation_date = models.DateField(auto_now_add=True)
    last_modified = models.DateField(auto_now=True)

    class Meta:
        verbose_name = 'Elément de la todo'
        verbose_name_plural = 'Eléments de la todo'
        ordering = ['creation_date', ]

    def __str__(self):
        return self.name
