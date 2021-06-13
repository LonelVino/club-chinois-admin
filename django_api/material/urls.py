from django.conf.urls import url, include
from . import views


app_name='shop'
urlpatterns = [
    url('category', views.one_category, name='product_list_by_category'),   # category?id
    url('all_categories', views.categories, name='allCatagories'),     
    url('product', views.one_product, name='product_detail'), # product?id
    url('all_prods', views.products, name='allProducts'), 
    url('prods_by_cat', views.getProductsByCat, name='allProductsByCat'), 
    # url(r'^$',views.viarezo_check,name='viarezo_check'),
    # url('secret', views.secret_page, name='secret'),
    ]


#TODO:add_product() add_category() update.... delete......