from django.shortcuts import render


# Create your views here.
def category_view(request):
    return render(request, 'category.html')


def article_view(request):
    return render(request, 'article.html')

def new_view(request):
    return render(request, 'new.html')