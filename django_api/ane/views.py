'''
/django_api/ane/views.py
-------------------------
Organize the views of Ane 
'''

from django.http import JsonResponse


def ane_name(request):
    return JsonResponse({'actvities': ['volant', 'ane-rouge', 'pitch']})

def ane_info(request):
    return JsonResponse({'volant': '踢毽子'}, {'ane_rouge': '华容道'}, {'pitch': '投壶'})