const state = {
    materials: [],
    materialByCat: [],
    categories: [],
    mats_loading: false,
  }
  
  const mutations = {
    SET_MATERIALS: (state, prods) => {
      state.materials = prods
    },
    ADD_MATERIALS: (state, product) => {
      state.materials.push(product)
    },
    CLEAR_MATERIALS: (state) => {
      state.materials.splice(0)
    },
    SET_MATERIALS_BYCAT: (state, prods) => {
      state.materialByCat = prods
    },
    ADD_MATERIALS_BYCAT: (state, product) => {
      state.materialByCat.push(product)
    },
    CLEAR_MATERIALS_BYCAT: (state) => {
      state.materialByCat.splice(0)
    },
    SET_CATEGORIES: (state, cats) => {
      state.categories = cats
    },
    ADD_CATEGORY: (state, cat) => {
      state.categories.push(cat)
    },
    CLEAR_CATEGORIES: (state) => {
      state.categories.splice(0)
    },
    CHANGE_MATS_LOADING: (state, status) => {
      state.mats_loading = status
    }
  }
  
  const actions = {
    setMaterials({ commit }, prods) {
      commit('SET_MATERIALS', prods)
    },
    addMaterial({ commit }, product) {
        commit('ADD_MATERIALS', product)
    },
    clearMaterials({ commit }) {
        commit('CLEAR_MATERIALS')
    },
    setMaterialsByCat({ commit }, prods) {
      commit('SET_MATERIALS_BYCAT', prods)
    },
    addMaterialByCat({ commit }, product) {
        commit('ADD_MATERIALS_BYCAT', product)
    },
    clearMaterialsByCat({ commit }) {
        commit('CLEAR_MATERIALS_BYCAT')
    },
    setCategories({ commit }, cats) {
      commit('SET_CATEGORIES', cats)
    },
    addMaterial({ commit }, cat) {
        commit('ADD_CATEGORY', cat)
    },
    clearCategories({ commit }) {
        commit('CLEAR_CATEGORIES')
    },
    changeMatsLoading({ commit }, status) {
        commit('CHANGE_MATS_LOADING', status)
    }
  }
  
  export default {
  namespaced: true,
  state,
  mutations,
  actions
  }
    