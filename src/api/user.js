import request from '@/utils/request'

var CAS_BASE_URL = '/django_api/cas'

var BASE_URL = '/django_api/user'

export function register(data) {
  return request({
    url: CAS_BASE_URL + '/register',
    method: 'post',
    data
  })
}

export function login(data) {
  return request({
    url: CAS_BASE_URL + '/login',
    method: 'post',
    data
  })
}

export function logout() {
  return request({
    url: CAS_BASE_URL + '/logout',
    method: 'post'
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
