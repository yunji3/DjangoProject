from django.db import models

# Create your models here.


class CategoryModel(models.Model):
    pass
    class Meta:
        db_table = "category"

    name = models.CharField(max_length=20, null=False)
    description = models.CharField(max_length=256, default='')

class ArticleModel(models.Model):
    class Meta:
        db_table = "article"

    title = models.CharField(max_length=20, null=False)
    category = models.ForeignKey(CategoryModel, on_delete=models.CASCADE)
    content = models.CharField(max_length=256, default='')
