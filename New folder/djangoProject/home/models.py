

# Create your models here.
from django.db import models
class Books(models.Model):
    category = models.CharField(max_length=100)
    name=models.CharField(max_length=100)
    author=models.CharField(max_length=100)
    edition=models.IntegerField(max_length=100)
    # publish_date=models.DateField(max_length=100)
    image=models.URLField(max_length=100)
    summary=models.TextField(help_text='short description')

    # class Meta:
    #      ordering =['category']