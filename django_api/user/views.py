'''
/django_api/users/views.py
-------------------------
Organize the views of User 
'''

import json
from django.http import JsonResponse
from django.core.handlers.wsgi import WSGIRequest
from django_api.user.models import User

def all_user_names(request):
    if request.method == 'GET':
        all_users = list(User.objects.all())
        names = []
        for i in all_users:
            names.append(i.name)
        if len(names) >= 0:
            return JsonResponse({'code': 200,'msg': 'Get names successfully!'})
        else:
            return JsonResponse({'code': 200, 'msg': 'Empty table!'})

    
def all_user_infos(request):
    if request.method == 'GET':
        all_users = list(User.objects.all())
        return JsonResponse({
            'code': 200,
            'msg': 'get all information successfully',
            'data': {
                'total': len(all_users)
            }
        })

def user_name(request):
    if request.method == 'GET':
        id = request.GET.get('id',default='1')
        user_1 = User.objects.filter(id=id)[0]
        return JsonResponse({
            'code': 200,
            'msg': 'Get name successfully',
            'data': {
                'name': user_1.name
            }
        })

def user_info(request):
    if request.method == 'GET':
        id = request.GET.get('id',default=0)
        name = request.GET.get('name',default='')
        if id != 0:
            user_1 = User.objects.filter(id=id)[0]
        elif name != '':
            user_1 = User.objects.filter(name=name)[0]
        else:
           return JsonResponse({
            'code': 3005,
            'msg': 'Parameters does not meet the requirements!'
        })     

        info = {'id': user_1.id, 'name': user_1.name, 'isAne': user_1.isAne, 'isVol': user_1.isVol, 'isPitch': user_1.isPitch, 'email': user_1.email, 'telephone': user_1.telephone, 'loc': user_1.loc   }
        return JsonResponse({
            'code': 200,
            'msg': 'Get information successfully',
            'data': {
                'info': info
            }
        })

def user_delete_byId(request):
    received_json_data = json.loads(request.body)
    id = received_json_data['id']
    if id:
        User.objects.filter(id=id).delete()
        return JsonResponse({
            'code': 200,
            'msg': 'Delete successfully!'
        })
    else:
        return JsonResponse({
            'code': 404,
            'msg': 'Delete failed!'
        })


def test_add(request):
    # 添加数据
    test1 = User(name='runoob', isAne=1, isVol=1, isPitch=1, email='', telephone='',score=0,loc='')
    test1.save()
    all_users =  User.objects.all()
    if all_users:
        new_add = all_users[0]
        print(new_add.name)
    return JsonResponse({
        'code': 200,
        'msg': 'User add successfully!',
        'data': {
            'id': new_add.id, 'name': new_add.name, 'isAne': new_add.isAne, 'isVol': new_add.isVol, 'isPitch': new_add.isPitch, 'email': new_add.email, 'telephone': new_add.telephone, 'loc': new_add.loc  
        }
    })
