import request from '@/utils/request'

var BASE_URL = '/django_api/finance'
var ADMIN_BASE_URL = '/django_api/finance/admin'


export function getCat(id) {
  return request({
    url:  BASE_URL + '/category?id='+id,
    method: 'get',
  })
}

export function getAllCats() {
  return request({
    url: BASE_URL + '/all_categories',
    method: 'get',
  })
}

export function getFinance(id) {
  return request({
    url:  BASE_URL + '/finance?id='+id,
    method: 'get',
  })
}

export function getAllFinances() {
  return request({
    url: BASE_URL + '/all_fins',
    method: 'get',
  })
}

export function getAllFinancesByCat(cat_id) {
  return request({
    url: BASE_URL + '/fins_by_cat?id=' + cat_id,
    method: 'get',
  })
}


export function addCat(data) {
  return request({
    url: BASE_URL + '/add_cat',
    method: 'post',
    data
  })
}

export function addFinance(data) {
  return request({
    url: BASE_URL + '/add_fin',
    method: 'post',
    data
  })
}

export function updateCat(data) {
  return request({
    url: BASE_URL + '/update_cat',
    method: 'put',
    data
  })
}

export function updateFinance(data) {
  return request({
    url: BASE_URL + '/update_fin',
    method: 'put',
    data
  })
}

export function updateFinancePrice(data) {
  return request({
    url: BASE_URL + '/update_price',
    method: 'put',
    data
  })
}

export function deleteCat(id) {
  return request({
    url: BASE_URL + '/del_cat?id='+id,
    method: 'delete',
  })
}

export function deleteFinance(id) {
  return request({
    url: BASE_URL + '/del_fin?id='+id,
    method: 'delete',
  })
}


// --------------- AMDIN PART -----------------------
