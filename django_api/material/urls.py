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
    url('add_cat', views.add_cat, name='AddCat'), 
    url('add_mat', views.add_material, name='addMaterial'), 

    url('update_cat', views.update_cat, name='updateCategory'),     
    url('update_mat', views.update_material, name='updateMaterial'), 
    url('update_quantity', views.update_material_quantity, name='updateMaterial'), 

    url('del_cat', views.del_cat, name='delCategory'),     
    url('del_mat', views.del_material, name='delMaterial'), 
    ]


#TODO:add_product() add_category() update.... delete......