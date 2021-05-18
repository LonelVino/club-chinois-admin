'''
/django_api/pitch/views.py
-------------------------
Organize the views of pitch 
'''


import json
from django.http import JsonResponse
from django_api.pitch.models import Pitch

def all_scores(request):
    if request.method == 'GET':
        all_pitchs = list(Pitch.objects.all())
        scores = []
        for i in all_pitchs:
            tmp = {}
            tmp['id'] = i.id
            tmp['name'] = i.name
            tmp['isPart'] = i.isPart
            tmp['isFini'] = i.isFini
            tmp['isFreeze'] = i.isFreeze
            tmp['number'] = i.number
            tmp['number_2'] = i.number_2
            tmp['number_3'] = i.number_3
            tmp['number_4'] = i.number_4
            tmp['number_5'] = i.number_5
            tmp['number_6'] = i.number_6
            tmp['time'] = i.time
            tmp['p_score'] = i.p_score
            tmp['comment'] = i.comment
            scores.append(tmp)
        if len(all_pitchs) >= 0:
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
            Pitch.objects.filter(id=id)[0]
        elif name != '':
            pitch_1 = Pitch.objects.filter(name=name)[0]
        else:
           return JsonResponse({
            'code': 3005,
            'msg': 'Parameters does not meet the requirements!'
        })     

        info = {'id': pitch_1.id, 'name': pitch_1.name, 'isFini': pitch_1.isFini, 
        'isPart': pitch_1.isPart,  'isFreeze': pitch_1.isFreeze, 'number': pitch_1.number, 'number_2': pitch_1.number_2, 
        'number_3': pitch_1.number_3, 'number_4': pitch_1.number_4, 'number_5': pitch_1.number_5, 'number_6': pitch_1.number_6, 
        'p_score': pitch_1.p_score, 'time': pitch_1.time, 'comment': pitch_1.comment}
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
        pitch_1 = Pitch(name=rec['name'], isPart=rec['isPart'], isFini=rec['isFini'], isFreeze=rec['isFreeze'],
        number=rec['number'], number_2 = rec['number_2'], number_3 = rec['number_3'] 
        ,number_4 = rec['number_4'], number_5 = rec['number_5'], number_6 = rec['number_6'],
        time=rec['time'], p_score=rec['p_score'], comment=rec['comment'])
        pitch_1.save()
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
        pitch_1 = Pitch.objects.get(id = rec['id'])
        pitch_1.name=rec['name']
        pitch_1.isPart=rec['isPart']
        pitch_1.isFini=rec['isFini']
        pitch_1.isFreeze=rec['isFreeze']

        pitch_1.number=rec['number']
        pitch_1.number_2 = rec['number_2'] 
        pitch_1.number_3 = rec['number_3'] 
        pitch_1.number_4 = rec['number_4'] 
        pitch_1.number_5 = rec['number_5']
        pitch_1.number_6 = rec['number_6']
        pitch_1.time=rec['time']
        pitch_1.p_score=rec['p_score']
        pitch_1.comment=rec['comment']
        pitch_1.save()
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


def p_score_delete_byId(request):
    try:
        id = request.GET.get('id')
    except:
        pass
    if id:
        print(id)
        Pitch.objects.filter(id=id).delete()
        return JsonResponse({
            'code': 200,
            'msg': 'Delete successfully!',
        })
    else:
        return JsonResponse({
            'code': 404,
            'msg': 'Delete failed!'
        })