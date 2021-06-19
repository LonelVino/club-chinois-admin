from django.conf.urls import url, include
from . import views


app_name='finance'
urlpatterns = [
    url('category', views.one_category, name='category'),   # category?id
    url('all_categories', views.categories, name='allCatagories'),     
    url('finance', views.one_finance, name='finance_detail'), # product?id
    url('all_fins', views.finances, name='allFinances'), 
    url('fins_by_cat', views.getFinanceByCat, name='getFinanceByCat'), 
    # url(r'^$',views.viarezo_check,name='viarezo_check'),
    # url('secret', views.secret_page, name='secret'),
    url('add_cat', views.add_cat, name='AddCat'), 
    url('add_fin', views.add_finance, name='addFinance'), 

    url('update_cat', views.update_cat, name='updateCategory'),     
    url('update_fin', views.update_finance, name='updateFinance'),
    url('update_price', views.update_finance_price, name='updateFinancePrice'), 

    url('del_cat', views.del_cat, name='delCategory'),     
    url('del_fin', views.del_finance, name='delFinance'), 
    ]


#TODO:add_product() add_category() update.... delete......