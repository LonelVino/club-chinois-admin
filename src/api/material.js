import request from '@/utils/request'

var BASE_URL = '/django_api/material'
var ADMIN_BASE_URL = '/django_api/material/admin'


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

export function getMaterial(id) {
  return request({
    url:  BASE_URL + '/material?id='+id,
    method: 'get',
  })
}

export function getAllMaterials() {
  return request({
    url: BASE_URL + '/all_mats',
    method: 'get',
  })
}

export function getAllMaterialsByCat(cat_id) {
  return request({
    url: BASE_URL + '/mats_by_cat?id=' + cat_id,
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

export function addMaterial(data) {
  return request({
    url: BASE_URL + '/add_mat',
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

export function updateMaterial(data) {
  return request({
    url: BASE_URL + '/update_mat',
    method: 'put',
    data
  })
}

export function updateMaterialQuantity(data) {
  return request({
    url: BASE_URL + '/update_quantity',
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

export function deleteMaterial(id) {
  return request({
    url: BASE_URL + '/del_mat?id='+id,
    method: 'delete',
  })
}


// --------------- AMDIN PART -----------------------
