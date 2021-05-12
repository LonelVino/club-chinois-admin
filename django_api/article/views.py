'''
/django_api/article/views.py
-------------------------
Organize the views of Article 
'''

from django.http import JsonResponse


def article_name(request):
    return JsonResponse({'articles': ['article_1', 'article_2', 'article_3']})

def article_content(request):    
    return JsonResponse({'article_1': 'This is article 1!'}, {'article_2': 'This is article_2!'}, {'article_3:', 'This is article 3!'})
