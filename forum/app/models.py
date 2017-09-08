from django.db import models

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
    cfn = models.ForeignKey( )