import json
from django.http import JsonResponse
from django_api.finance.models import Finance 
from django_api.finance.models import FinCategory


# Create your views here.
def one_finance (request):   # Select the finance according to the id
    if request.method == 'GET':
        id = request.GET.get('id', default=0)
        if id != 0:
            fin_1= Finance.objects.filter(id=id)[0]
        else:
            return JsonResponse({
            'code': 3005,
            'msg': 'Parameters does not meet the requirements!'
        })     
        newImage = json.dumps(str(fin_1.image)) 
        #TODO: write this as a map function
        info =  {'id': fin_1.id, 'name': fin_1.name, 'category_id': fin_1.category_id,
        'buyer': fin_1.buyer , 'description': fin_1.description, 'price': fin_1.price,
        'facture': fin_1.facture, 'created': fin_1.created, 'updated': fin_1.updated }
        return JsonResponse({
            'code': 200,
            'msg': 'Get information successfully',
            'data': {
                'info': info
            }
        })

def finances(request):
    if request.method == 'GET':
        all_finances = list(Finance.objects.all().values())
        if len(all_finances) >= 0:
            return JsonResponse({
                'code': 200,
                'msg': 'get all finances successfully',
                'data': {
                    'total': len(all_finances),
                    'info': all_finances
                }
            })
        else:
            return JsonResponse({'code': 200, 'msg': 'Empty table!'})

def getFinanceByCat(request):
    if request.method == 'GET':
        cat_id = request.GET.get('id', default=0)
        finances = list(Finance.objects.filter(category_id = cat_id).values())
        if len(finances) >= 0:
            return JsonResponse({
                'code': 200,
                'msg': 'get all finances successfully',
                'data': {
                    'total': len(finances),
                    'info': finances
                }
            })
        else:
            return JsonResponse({'code': 200, 'msg': 'Empty table!'})

def one_category(request):  # Select the finance according to the id
    if request.method == 'GET':
        id = request.GET.get('id', default=0)
        if id != 0:
            cat_1 = FinCategory.objects.filter(id=id)[0]
        else:
            return JsonResponse({
                'code': 3005,
                'msg': 'Parameters does not meet the requirements!'
            })     

        #TODO: write this as a map function
        info =  {'id': cat_1.id, 'name': cat_1.name}
        return JsonResponse({
            'code': 200,
            'msg': 'Get information of category successfully',
            'data': {
                'cat_info': info
            }
        })

def categories(request):
    if request.method == 'GET':
        all_categories = list(FinCategory.objects.all().values())
        all_categories.sort(key=lambda k: k['id'])
        if len(all_categories) >= 0:
            return JsonResponse({
                'code': 200,
                'msg': 'get all finances successfully',
                'data': {
                    'total': len(all_categories),
                    'cat_infos': all_categories
                }
            })
        else:
            return JsonResponse({'code': 200, 'msg': 'Empty table!'})

def add_cat(request):
    if request.method == 'POST':
        received_json_data = json.loads(request.body)
        rec = received_json_data
        cat_1 = FinCategory(name=rec['name'])
        cat_1.save()
        return JsonResponse({
            'code': 200,
            'msg': 'Add Successfully!',
            'data':{
                'name': rec['name']
            }
        })

keys = ['category' , 'buyer', 'description' , 'price' ,  'facture', 'created' , 'updated' ]
def add_finance(request):
    if request.method == 'POST':
        received_json_data = json.loads(request.body)
        rec = received_json_data
        mat_1 = Finance(name=rec['name'], category_id=rec['category_id'], 
            buyer=rec['buyer'], facture= rec['facture'], price = rec['price'], description = rec['description'])
        mat_1.save()
        return JsonResponse({
            'code': 200,
            'msg': 'Add Successfully!',
            'data':{
                'name': rec['name']
            }
        })


def update_cat(request):
    received_json_data = json.loads(request.body)
    rec = received_json_data
    cat_1 = FinCategory.objects.get(id = rec['id'])
    cat_1.name=rec['name']
    cat_1.save()
    return JsonResponse({
        'code': 200,
        'msg': 'Update Successfully!',
        'data':{
            'name': rec['name']
        }
    })

def update_finance(request):
    received_json_data = json.loads(request.body)
    rec = received_json_data
    fin_1 = Finance.objects.get(id = rec['id'])
    fin_1.name=rec['name']; fin_1.category_id=rec['category_id']; fin_1.description = rec['description'];
    fin_1.buyer=rec['buyer']; fin_1.facture= rec['facture']; fin_1.price = rec['price']; 
    fin_1.save()
    return JsonResponse({
        'code': 200,
        'msg': 'Update Successfully!',
        'data':{
            'name': rec['name']
        }
    })

def update_finance_price(request):
    received_json_data = json.loads(request.body)
    rec = received_json_data
    fin_1 = Finance.objects.get(id = rec['id'])
    fin_1.price= rec['price'];
    fin_1.save()
    return JsonResponse({
        'code': 200,
        'msg': 'Update Successfully!',
        'data':{
            'price': fin_1.price
        }
    })


def del_cat(request):
    try:
        id = request.GET.get('id')
    except:
        pass
    if id:
        FinCategory.objects.filter(id=id).delete()
        return JsonResponse({
            'code': 200,
            'msg': 'Delete successfully!',
        })
    else:
        return JsonResponse({
            'code': 404,
            'msg': 'Delete failed!'
        })

def del_finance(request):
    try:
        id = request.GET.get('id')
    except:
        pass
    if id:
        Finance.objects.filter(id=id).delete()
        return JsonResponse({
            'code': 200,
            'msg': 'Delete successfully!',
        })
    else:
        return JsonResponse({
            'code': 404,
            'msg': 'Delete failed!'
        })