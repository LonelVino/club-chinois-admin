'''
/django_api/vol/views.py
-------------------------
Organize the views of Vol 
'''

import json
from django.http import JsonResponse
from django_api.vol.models import Vol

def all_scores(request):
    if request.method == 'GET':
        all_vols = list(Vol.objects.all())
        scores = []
        for i in all_vols:
            tmp = {}
            tmp['id'] = i.id
            tmp['name'] = i.name
            tmp['number'] = i.number
            tmp['time'] = i.time
            tmp['v_score'] = i.v_score
            tmp['comment'] = i.comment
            scores.append(tmp)
        if len(all_vols) >= 0:
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
            Vol.objects.filter(id=id)[0]
        elif name != '':
            vol_1 = Vol.objects.filter(name=name)[0]
        else:
           return JsonResponse({
            'code': 3005,
            'msg': 'Parameters does not meet the requirements!'
        })     

        info = {'id': vol_1.id, 'name': vol_1.name, 'number': vol_1.number, 'v_score': vol_1.v_score, 'time': vol_1.time, 'comment': vol_1.comment}
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
        vol_1 = Vol(name=rec['name'], number=rec['number'], time=rec['time'], v_score=rec['v_score'], comment=rec['comment'])
        vol_1.save()
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
        vol_1 = Vol.objects.get(id = rec['id'])
        vol_1.name=rec['name']
        vol_1.number=rec['number']
        vol_1.time=rec['time']
        vol_1.v_score=rec['v_score']
        vol_1.comment=rec['comment']
        vol_1.save()
        return JsonResponse({
            'code': 200,
            'msg': 'Update Successfully!',
            'data':{
                'name': rec['name']
            }
        })
    else: 
        return JsonResponse({
            'code': 500,
            'msg': 'Update Failed, incorrect request method!'
        })


def v_score_delete_byId(request):
    try:
        id = request.GET.get('id')
    except:
        pass
    if id:
        print(id)
        Vol.objects.filter(id=id).delete()
        return JsonResponse({
            'code': 200,
            'msg': 'Delete successfully!',
        })
    else:
        return JsonResponse({
            'code': 404,
            'msg': 'Delete failed!'
        })