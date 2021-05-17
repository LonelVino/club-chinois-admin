'''
/django_api/users/views.py
-------------------------
Organize the views of User 
'''

import json
from django.http import JsonResponse
from django.core.handlers.wsgi import WSGIRequest
from django_api.user.models import User
from django_api.cas.models import Cas

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
        all_infos = []
        for user in all_users:
            tmp_user = {}
            tmp_user['id'] = user.id; tmp_user['name'] = user.name; tmp_user['isAne'] = user.isAne;  tmp_user['isVol'] = user.isVol;  tmp_user['isPitch'] = user.isPitch;
            tmp_user['score'] = user.score; tmp_user['email'] = user.email; tmp_user['telephone'] = user.telephone; tmp_user['loc'] = user.loc;
            all_infos.append(tmp_user)
        return JsonResponse({
            'code': 200,
            'msg': 'get all information successfully',
            'data': {
                'total': len(all_users),
                'infos': all_infos
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
            User.objects.filter(id=id)[0]
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


def add_info(request):
    if request.method == 'POST':
        received_json_data = json.loads(request.body)
        rec = received_json_data
        user_1 = User(name=rec['name'], isAne=rec['isAne'], isVol=rec['isVol'], isPitch=rec['isPitch'], 
        score=rec['score'],telephone=rec['telephone'], email=rec['email'], loc=rec['loc'])
        user_1.save()
        return JsonResponse({
            'code': 200,
            'msg': 'Add Successfully!',
            'data':{
                'name': rec['name']
            }
        })

def update_info(request):
    if request.method == 'PUT':
        received_json_data = json.loads(request.body)
        rec = received_json_data
        user_1 = User(name=rec['name'], isAne=rec['isAne'], isVol=rec['isVol'], isPitch=rec['isPitch'], telephone=rec['telephone'],
        email=rec['email'], loc=rec['loc'])
        user_1.save()
        return JsonResponse({
            'code': 200,
            'msg': 'Update Successfully!',
            'data':{
                'name': rec['name']
            }
        })


def user_delete_byId(request):
    try:
        id = request.GET.get('id')
    except:
        pass
    if id:
        print(id)
        User.objects.filter(id=id).delete()
        return JsonResponse({
            'code': 200,
            'msg': 'Delete successfully!',
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
