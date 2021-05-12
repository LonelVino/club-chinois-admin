'''
/django_api/activity/views.py
-------------------------
Organize the views of Activity 
'''

from django.http import JsonResponse


def activity_name(request):
    return JsonResponse({'actvities': ['volant', 'ane-rouge', 'pitch']})

def activity_info(request):
    return JsonResponse({'volant': '踢毽子'}, {'ane_rouge': '华容道'}, {'pitch': '投壶'})