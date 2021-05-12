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
            return JsonResponse({'status': True})

def all_user_names():
    return JsonResponse({'names': ['William', 'Rod', 'Grant']})

def all_user_infos():
    return JsonResponse({'data': [{'William': [{'role': 'Male'}, {'name': 'Information'}, {'telephone': '1818645872'}, {'intro': 'Me'}]},\
        {'Rod': [{'role': 'Male'}, {'name': 'Information'}, {'telephone': '1818645872'}, {'intro': 'Me'}]},\
        {'Grant': [{'role': 'Male'}, {'name': 'Information'}, {'telephone': '1818645872'}, {'intro': 'Me'}]}]})

def user_name(id):
    return JsonResponse({'names': 'William'})

def user_info(name):
    return JsonResponse({'data': [{'role': 'Male'}, {'name': 'Information'}, {'telephone': '1818645872'}, {'intro': 'Me'}]})

def logout():
    # No validation, pass directly
    return JsonResponse({'status': True})