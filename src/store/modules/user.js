import { login, logout, getName, getInfo, getAllNames, getAllInfos } from '@/api/user'
import router, { resetRouter } from '@/router'

const state = {
  name: '',
  avatar: '',
  introduction: '',
  roles: []
}

const mutations = {
  SET_INTRODUCTION: (state, introduction) => {
    state.introduction = introduction
  },
  SET_NAME: (state, name) => {
    state.name = name
  },
  SET_AVATAR: (state, avatar) => {
    state.avatar = avatar
  },
  SET_ROLES: (state, roles) => {
    state.roles = roles
  }
}

const actions = {
  // user login
  login({ commit }, userInfo) {
    const { username, password } = userInfo
    return new Promise((resolve, reject) => {
      login({ username: username.trim(), password: password }).then(response => {
        const { data } = response
        resolve()
      }).catch(error => {
        reject(error)
      })
    })
  },

  // get one user name
  getName({ commit, state }) {
    return new Promise((resolve, reject) => {
      getName().then(response => {
        const { data } = response
        resolve(data)
      }).catch(error => {
        reject(error)
      })
    })
  },

  // get one user info
  getInfo({ commit, state }) {
    return new Promise((resolve, reject) => {
      getInfo().then(response => {
        const { data } = response

        if (!data) {
          reject('Verification failed, please Login again.')
        }
        const { intro, name, roles, telephone } = data
        console.log('intro, name, roles, telephone:', intro, name, roles, telephone)
        // roles must be a non-empty array
        if (!roles || roles.length <= 0) {
          reject('getInfo: roles must be a non-null array!')
        }

        commit('SET_ROLES', roles)
        commit('SET_NAME', name)
        commit('SET_AVATAR', telephone)
        commit('SET_INTRODUCTION', intro)
        resolve(data)
        return data
      }).catch(error => {
        reject(error)
      })
    })
  },

  // get all users' infos
  getAllInfos() {
    return new Promise((resolve, reject) => {
      getAllInfos().then(response => {
        const {data} = response
        console.log('all infos:', data)
        resolve()
      }).catch(error => {
        reject(error)
      })
    })
  },

  // get all users' names
  getAllNames() {
    return new Promise((resolve, reject) => {
      getAllNames().then(response => {
        const {data} = response
        console.log('All Names are:', data)
        resolve()
      }).catch(error => {
        reject(error)
      })
    })
  },

  // user logout
  logout({ commit, state, dispatch }) {
    return new Promise((resolve, reject) => {
      logout().then(() => {
        commit('SET_ROLES', [])
        resetRouter()

        // reset visited views and cached views
        // to fixed https://github.com/PanJiaChen/vue-element-admin/issues/2485
        // dispatch('tagsView/delAllViews', null, { root: true })

        resolve()
      }).catch(error => {
        reject(error)
      })
    })
  },

  // dynamically modify permissions
  async changeRoles({ commit, dispatch }, role) {

    const { roles } = await dispatch('getInfo')

    resetRouter()

    // generate accessible routes map based on roles
    const accessRoutes = await dispatch('permission/generateRoutes', roles, { root: true })
    // dynamically add accessible routes
    router.addRoutes(accessRoutes)

    // reset visited views and cached views
    dispatch('tagsView/delAllViews', null, { root: true })
  }
}

export default {
  namespaced: true,
  state,
  mutations,
  actions
}