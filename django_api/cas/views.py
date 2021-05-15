'''
/django_api/cas/views.py
-------------------------
Organize the views of Cas 
'''

import json
from json.decoder import JSONDecodeError
from django.http import JsonResponse
from django.core.handlers.wsgi import WSGIRequest
from django_api.cas.models import Cas

def registry(request: WSGIRequest):
    # No validation, pass directly
    if request.method == 'POST':
        req = request.body.decode("utf-8").replace("'", '"')
        received_json_data = json.loads(req)
        username = received_json_data['username']
        password = received_json_data['password']
        isDuplicated = (len(Cas.objects.filter(username=username)) > 0)
        print(isDuplicated)
        if isDuplicated:
            return JsonResponse({
                'code': 3006,
                'msg': username + ' has been used, please select a new username..'
            })
        else:        
            cas_1 = Cas(username=username, password=password, role = 'editor')
            cas_1.save()
            if (username and password): 
                return JsonResponse({
                    'code': 200,
                    'msg': 'Registry Successfully!',
                    'data':{
                        'username': username,
                        'password': password,
                    }
                })
            else:
                return JsonResponse({
                    'code': 3005,
                    'msg': 'Parameters does not meet the requirements!'
                })


def login(request: WSGIRequest):
    # No validation, pass directly
    if request.method == 'POST':
        received_json_data = json.loads(request.body)
        usr = received_json_data['username']
        pwd = received_json_data['password']
        all_cas = Cas.objects.all()
        cas_1 = list(Cas.objects.filter(username=usr))[0]
        if cas_1:
            cas_info = {'id': cas_1.id, 'username': cas_1.username, 'role': cas_1.role}
            if cas_1.password == pwd:
                return JsonResponse({
                    'code': 200,
                    'msg': 'Login Successfully!',
                    'data': cas_info
                    })
            else:
                return JsonResponse({
                'code': 3002,
                'msg': 'Login Failed, incorrect password!',
                })
        else:
            return JsonResponse({
                'code': 3001,
                'msg': 'Login Failed, the username does not exist!',
                })

def logout(request):
    # No validation, pass directly
    return JsonResponse({
        'code': 200,\
        'msg': 'Log out successfully!'
        })



def get_all_cas(request):
    all_cas = Cas.objects.all()
    all_cas_info = []
    for cas in all_cas:
        tmp_cas = {'id': cas.id, 'username': cas.username, 'password': cas.password, 'role': cas.role}
        all_cas_info.append(tmp_cas)
    if all_cas:
        print('all_cas:', all_cas, '\n list(all_cas):', list(all_cas) )
        return JsonResponse({
            'code': 200,
            'msg': 'Get all cas successfully!',
            'data': {
                'total': len(all_cas),
                'all_cas': all_cas_info
            }
        })
    else:
        return JsonResponse({
            'code': 3000,
            'msg': 'No cas, the table is empty!'
        })


def get_role(request):
    if request.method == 'GET':
        id = request.GET.get('cas_id',default='1')
        cas1 = Cas.objects.filter(id=id)[0]
        return JsonResponse({
            'code': 200,
            'msg': 'Get role successfully!!',
            'data': {
                'role': cas1.role
            }
        })
