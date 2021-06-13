from django.conf.urls import url, include
from . import views


app_name='material'
urlpatterns = [
    url('category', views.one_category, name='product_list_by_category'),   # category?id
    url('all_categories', views.categories, name='allCatagories'),     
    url('material', views.one_material, name='material_detail'), # product?id
    url('all_mats', views.materials, name='allMaterials'), 
    url('mats_by_cat', views.getMaterialsByCat, name='allMaterialsByCat'), 
    # url(r'^$',views.viarezo_check,name='viarezo_check'),
    # url('secret', views.secret_page, name='secret'),
    ]


#TODO:add_product() add_category() update.... delete......