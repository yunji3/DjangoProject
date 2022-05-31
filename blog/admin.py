from django.contrib import admin # 장고에서 admin 툴을 사용하겠다.
from .models import ArticleModel
from .models import CategoryModel# 우리가 생성한 모델을 가져오는데(user-models.py), 그 중에 UserModel를 가져오겠다.

# Register your models here.
admin.site.register(ArticleModel)
admin.site.register(CategoryModel)


