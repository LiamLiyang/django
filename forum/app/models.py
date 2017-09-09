from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Classification(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'tb_classifcation'


class Sitck(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    additional_content = models.TextField()
    cfn = models.ForeignKey(Classification)
    user = models.ForeignKey(User)
    like = models.PositiveIntegerField()
    access = models.PositiveIntegerField()
    rectime = models.DateTimeField()
    last_access = models.DateTimeField()

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'tb_sitck'
