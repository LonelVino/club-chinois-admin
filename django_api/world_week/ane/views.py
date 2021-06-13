'''
/django_api/ane/views.py
-------------------------
Organize the views of Ane 
'''

import json
from django.http import JsonResponse
from django_api.world_week.ane.models import Ane

def all_scores(request):
    if request.method == 'GET':
        all_anes = list(Ane.objects.all())
        scores = []
        for i in all_anes:
            tmp = {}
            tmp['id'] = i.id
            tmp['name'] = i.name
            tmp['isPart'] = i.isPart
            tmp['hasInd'] = i.hasInd
            tmp['isFini'] = i.isFini
            tmp['isFreeze'] = i.isFreeze
            tmp['time'] = i.time
            tmp['start_time'] = i.start_time
            tmp['end_time'] = i.end_time
            tmp['step'] = i.step
            tmp['status'] = i.status
            tmp['a_score'] = i.a_score
            tmp['comment'] = i.comment
            scores.append(tmp)
        if len(all_anes) >= 0:
            return JsonResponse({
                'code': 200,
                'msg': 'get all information successfully',
                'data': {
                    'total': len(scores),
                    'infos': scores
                }
            })
        else:
            return JsonResponse({'code': 200, 'msg': 'Empty table!'})

def one_score(request):
    if request.method == 'GET':
        id = request.GET.get('id',default=0)
        name = request.GET.get('name',default='')
        if id != 0:
            Ane.objects.filter(id=id)[0]
        elif name != '':
            ane_1 = Ane.objects.filter(name=name)[0]
        else:
            return JsonResponse({
            'code': 3005,
            'msg': 'Parameters does not meet the requirements!'
        })     

        info = {'id': ane_1.id, 'name': ane_1.name, 'start_time': ane_1.start_time, 'end_time': ane_1.end_time,
        'isPart': ane_1.isPart, 'hasInd': ane_1.hasInd,'isFini': ane_1.isFini, 'isFreeze': ane_1.isFreeze, 'status': ane_1.status,
        'a_score': ane_1.a_score, 'time': ane_1.time,'step': ane_1.step, 'comment': ane_1.comment}
        return JsonResponse({
            'code': 200,
            'msg': 'Get information successfully',
            'data': {
                'info': info
            }
        })

def add_score(request):
    if request.method == 'POST':
        received_json_data = json.loads(request.body)
        rec = received_json_data
        ane_1 = Ane(name=rec['name'], isPart=rec['isPart'],  hasInd=rec['hasInd'], start_time=rec['start_time'], end_time=rec['end_time'],
        isFini=rec['isFini'], isFreeze=rec['isFreeze'], time=rec['time'], status=rec['status'],
        step=rec['step'], a_score=rec['a_score'], comment=rec['comment'])
        ane_1.save()
        return JsonResponse({
            'code': 200,
            'msg': 'Add Successfully!',
            'data':{
                'name': rec['name']
            }
        })

def update_score(request):
    if request.method == 'PUT':
        received_json_data = json.loads(request.body)
        rec = received_json_data
        ane_1 = Ane.objects.get(id = rec['id'])
        ane_1.name=rec['name']
        ane_1.isPart=rec['isPart']
        ane_1.hasInd=rec['hasInd']
        ane_1.isFini=rec['isFini']
        ane_1.isFreeze=rec['isFreeze']
        ane_1.time=rec['time']
        ane_1.start_time = rec['start_time']
        ane_1.end_time = rec['end_time']
        ane_1.step=rec['step']
        ane_1.status = rec['status']
        ane_1.a_score=rec['a_score']
        ane_1.comment=rec['comment']
        ane_1.save()
        return JsonResponse({
            'code': 200,
            'msg': 'Update Successfully!',
            'data':{
                'name': rec['name']
            }
        })

def a_score_delete_byId(request):
    try:
        id = request.GET.get('id')
    except:
        pass
    if id:
        print(id)
        Ane.objects.filter(id=id).delete()
        return JsonResponse({
            'code': 200,
            'msg': 'Delete successfully!',
        })
    else:
        return JsonResponse({
            'code': 404,
            'msg': 'Delete failed!'
        })
