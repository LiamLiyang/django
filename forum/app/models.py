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
    like = models.PositiveIntegerField(default=0)
    access = models.PositiveIntegerField(default=0)
    rectime = models.DateTimeField(auto_now=True)
    last_access = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'tb_sitck'

    def count(self):
        """
        查询贴子总数
        :return:
        """
        if self._result_cache is not None and not self._iter:
            return len(self._result_cache)
        return self.query.get_count(using=self.db)


class Comment(models.Model):
    sitck = models.ForeignKey(Sitck)
    comment_body = models.TextField()

    def __str__(self):
        return self.comment_body[:20]


    class Meta:
        db_table = 'tb_comment'


