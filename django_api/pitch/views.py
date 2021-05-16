'''
/django_api/ane/views.py
-------------------------
Organize the views of Ane 
'''

from django.http import JsonResponse
from django_api.pitch.models import Pitch

def all_scores(request):
    if request.method == 'GET':
        all_anes = list(Pitch.objects.all())
        scores = {}
        for i in all_anes:
            scores[i.name] = i.score
        if len(all_anes) >= 0:
            return JsonResponse({'code': 200,'msg': 'Get names successfully!'})
        else:
            return JsonResponse({'code': 200, 'msg': 'Empty table!'})


def add_score(request):
    return JsonResponse({'volant': '踢毽子'}, {'ane_rouge': '华容道'}, {'pitch': '投壶'})