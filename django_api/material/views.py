import json
from django.http import JsonResponse
from django_api.material.models import Product 
from django_api.material.models import Category


# Create your views here.
def one_product(request):   # Select the product according to the id
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
        'description': prod_1.description, 'price': prod_1.price, 'dt_info': prod_1.dt_info,
        'created': prod_1.created, 'updated': prod_1.updated }
        return JsonResponse({
            'code': 200,
            'msg': 'Get information successfully',
            'data': {
                'prod_info': info
            }
        })

def products(request):
    if request.method == 'GET':
        all_products = list(Product.objects.all().values())
        if len(all_products) >= 0:
            return JsonResponse({
                'code': 200,
                'msg': 'get all products successfully',
                'data': {
                    'total': len(all_products),
                    'prod_infos': all_products
                }
            })
        else:
            return JsonResponse({'code': 200, 'msg': 'Empty table!'})

def getProductsByCat(request):
    if request.method == 'GET':
        cat_id = request.GET.get('id', default=0)
        products = list(Product.objects.filter(category_id = cat_id).values())
        if len(products) >= 0:
            return JsonResponse({
                'code': 200,
                'msg': 'get all products successfully',
                'data': {
                    'total': len(products),
                    'prod_infos': products
                }
            })
        else:
            return JsonResponse({'code': 200, 'msg': 'Empty table!'})

def one_category(request):  # Select the product according to the id
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
        if len(all_categories) >= 0:
            return JsonResponse({
                'code': 200,
                'msg': 'get all products successfully',
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

keys = ['category' , 'image', 'quantity', 'description' , 'price' , 'dt_info', 'status', 'created' , 'updated' ]
def add_prod(request):
    if request.method == 'POST':
        received_json_data = json.loads(request.body)
        rec = received_json_data
        cat_1 = Product(name=rec['name'], category=rec['category'], status = rec['status'], 
            image=rec['image'], quantity= rec['quantity'], price = rec['price'],
            dt_info = rec['dt_info'], created=rec['created'], updated=rec['updated'])
        cat_1.save()
        return JsonResponse({
            'code': 200,
            'msg': 'Add Successfully!',
            'data':{
                'name': rec['name']
            }
        })


def update_cat(request):
    pass

def update_prod(request):
    pass

def del_cat(request):
    pass

def del_prod(request):
    pass