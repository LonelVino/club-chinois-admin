import request from '@/utils/request'

var BASE_URL = '/django_api/user'

export function login(data) {
  return request({
    url: BASE_URL + '/login',
    method: 'post',
    data
  })
}

export function getName() {
  return request({
    url: BASE_URL + '/one_name',
    method: 'get',
  })
}

export function getInfo() {
  return request({
    url:  BASE_URL + '/one_info',
    method: 'get',
  })
}


export function getAllNames() {
  return request({
    url: BASE_URL + '/all_names',
    method: 'get',
  })
}

export function getAllInfos() {
  return request({
    url: BASE_URL + '/all_infos',
    method: 'get',
  })
}

export function logout() {
  return request({
    url: BASE_URL + '/logout',
    method: 'post'
  })
}
