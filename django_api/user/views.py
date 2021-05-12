'''
/django_api/users/views.py
-------------------------
Organize the views of User 
'''

import json
from django.http import JsonResponse
from django.core.handlers.wsgi import WSGIRequest

def login(request: WSGIRequest):
    # No validation, pass directly
    if request.method == 'POST':
        received_json_data = json.loads(request.body)
        username = received_json_data['username']
        password = received_json_data['password']
        if (username and password): 
            return JsonResponse(\
                {'code': 200,\
                'message':[{'status': True}]})

def all_user_names(request):
    return JsonResponse({'code': 200,\
        'names': ['William', 'Rod', 'Grant']})

def all_user_infos(request):
    return JsonResponse(\
        {'code': 200,\
        'data': [{'William': {'roles': ['admin'], 'name': 'Information', 'telephone': '1818645872', 'intro': 'Me'}},\
        {'Rod': {'roles': ['admin'], 'name': 'Information', 'telephone': '1818645872', 'intro': 'Me'}},\
        {'Grant': {'roles': ['admin'], 'name': 'Information', 'telephone': '1818645872', 'intro': 'Me'}}]})

def user_name(request):
    return JsonResponse({'code': 200},\
        {'roles': ['admin'], 'name': 'Williams'})

def user_info(request):
    return JsonResponse({'code': 200,\
        'data': {'roles': ['admin'], 'name': 'Information', 'telephone': '1818645872', 'intro': 'Me'}})

def logout():
    # No validation, pass directly
    return JsonResponse({'code': 200,\
        'status': True})