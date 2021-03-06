import json
from django.http import JsonResponse
from django_api.material.models import Product 
from django_api.material.models import Category


# Create your views here.
def one_material(request):   # Select the material according to the id
    if request.method == 'GET':
        id = request.GET.get('id', default=0)
        if id != 0:
            prod_1= Product.objects.filter(id=id)[0]
        else:
            return JsonResponse({
            'code': 3005,
            'msg': 'Parameters does not meet the requirements!'
        })     
        newImage = json.dumps(str(prod_1.image)) 
        #TODO: write this as a map function
        info =  {'id': prod_1.id, 'name': prod_1.name, 'category_id': prod_1.category_id,
        'image': newImage, 'quantity': prod_1.quantity, 'status': prod_1.status,
        'description': prod_1.description, 'price': prod_1.price,
        'created': prod_1.created, 'updated': prod_1.updated }
        return JsonResponse({
            'code': 200,
            'msg': 'Get information successfully',
            'data': {
                'info': info
            }
        })

def materials(request):
    if request.method == 'GET':
        all_materials = list(Product.objects.all().values())
        if len(all_materials) >= 0:
            return JsonResponse({
                'code': 200,
                'msg': 'get all materials successfully',
                'data': {
                    'total': len(all_materials),
                    'info': all_materials
                }
            })
        else:
            return JsonResponse({'code': 200, 'msg': 'Empty table!'})

def getMaterialsByCat(request):
    if request.method == 'GET':
        cat_id = request.GET.get('id', default=0)
        materials = list(Product.objects.filter(category_id = cat_id).values())
        if len(materials) >= 0:
            return JsonResponse({
                'code': 200,
                'msg': 'get all materials successfully',
                'data': {
                    'total': len(materials),
                    'info': materials
                }
            })
        else:
            return JsonResponse({'code': 200, 'msg': 'Empty table!'})

def one_category(request):  # Select the material according to the id
    if request.method == 'GET':
        id = request.GET.get('id', default=0)
        if id != 0:
            cat_1 = Category.objects.filter(id=id)[0]
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
        all_categories = list(Category.objects.all().values())
        all_categories.sort(key=lambda k: k['id'])
        if len(all_categories) >= 0:
            return JsonResponse({
                'code': 200,
                'msg': 'get all materials successfully',
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
        cat_1 = Category(name=rec['name'])
        cat_1.save()
        return JsonResponse({
            'code': 200,
            'msg': 'Add Successfully!',
            'data':{
                'name': rec['name']
            }
        })

keys = ['category' , 'image', 'quantity', 'description' , 'price' ,  'status', 'created' , 'updated' ]
def add_material(request):
    if request.method == 'POST':
        received_json_data = json.loads(request.body)
        rec = received_json_data
        mat_1 = Product(name=rec['name'], category_id=rec['category_id'], status = rec['status'], 
            image=rec['image'], quantity= rec['quantity'], price = rec['price'], description = rec['description'])
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
    cat_1 = Category.objects.get(id = rec['id'])
    cat_1.name=rec['name']
    cat_1.save()
    return JsonResponse({
        'code': 200,
        'msg': 'Update Successfully!',
        'data':{
            'name': rec['name']
        }
    })

def update_material(request):
    received_json_data = json.loads(request.body)
    rec = received_json_data
    prod_1 = Product.objects.get(id = rec['id'])
    prod_1.name=rec['name']; prod_1.category_id=rec['category_id']; prod_1.status = rec['status']; 
    prod_1.image=rec['image']; prod_1.quantity= rec['quantity']; prod_1.price = rec['price']; prod_1.description = rec['description']
    prod_1.save()
    return JsonResponse({
        'code': 200,
        'msg': 'Update Successfully!',
        'data':{
            'name': rec['name']
        }
    })


def update_material_quantity(request):
    received_json_data = json.loads(request.body)
    rec = received_json_data
    prod_1 = Product.objects.get(id = rec['id'])
    prod_1.quantity= rec['quantity'];
    prod_1.save()
    return JsonResponse({
        'code': 200,
        'msg': 'Update Successfully!',
        'data':{
            'quantity': prod_1.quantity
        }
    })

def del_cat(request):
    try:
        id = request.GET.get('id')
    except:
        pass
    if id:
        Category.objects.filter(id=id).delete()
        return JsonResponse({
            'code': 200,
            'msg': 'Delete successfully!',
        })
    else:
        return JsonResponse({
            'code': 404,
            'msg': 'Delete failed!'
        })

def del_material(request):
    try:
        id = request.GET.get('id')
    except:
        pass
    if id:
        Product.objects.filter(id=id).delete()
        return JsonResponse({
            'code': 200,
            'msg': 'Delete successfully!',
        })
    else:
        return JsonResponse({
            'code': 404,
            'msg': 'Delete failed!'
        })