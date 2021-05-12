'''
/django_api/users/views.py
-------------------------
Organize the views of User 
'''

from django.shortcuts import render

from django.http import JsonResponse

def login(username, password):
    # No validation, pass directly
    if (username and password): 
        return JsonResponse({'status': True})

def all_user_names(request):
    return JsonResponse({'names': ['William', 'Rod', 'Grant']})

def user_name(id):
    return JsonResponse({'names': 'William'})

def all_user_infos(request):
    return JsonResponse({'data': [{'William': [{'role': 'Male'}, {'name': 'Information'}, {'telephone': '1818645872'}, {'intro': 'Me'}]},\
        {'Rod': [{'role': 'Male'}, {'name': 'Information'}, {'telephone': '1818645872'}, {'intro': 'Me'}]},\
        {'Grant': [{'role': 'Male'}, {'name': 'Information'}, {'telephone': '1818645872'}, {'intro': 'Me'}]}]})

def user_info(name):
    return JsonResponse({'data': [{'role': 'Male'}, {'name': 'Information'}, {'telephone': '1818645872'}, {'intro': 'Me'}]})

def logout():
    # No validation, pass directly
    return JsonResponse({'status': True})