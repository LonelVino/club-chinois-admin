const state = {
    finances: [],
    financeByCat: [],
    categories: [],
    fins_loading: false,
  }
  
  const mutations = {
    SET_FINANCES: (state, fins) => {
      state.finances = fins
    },
    ADD_FINANCES: (state, finance) => {
      state.finances.push(finance)
    },
    CLEAR_FINANCES: (state) => {
      state.finances.splice(0)
    },
    SET_FINANCES_BYCAT: (state, fins) => {
      state.financeByCat = fins
    },
    ADD_FINANCES_BYCAT: (state, finance) => {
      state.financeByCat.push(finance)
    },
    CLEAR_FINANCES_BYCAT: (state) => {
      state.financeByCat.splice(0)
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
      state.fins_loading = status
    }
  }
  
  const actions = {
    setFinances({ commit }, fins) {
      commit('SET_FINANCES', fins)
    },
    addFinance({ commit }, finance) {
        commit('ADD_FINANCES', finance)
    },
    clearFinances({ commit }) {
        commit('CLEAR_FINANCES')
    },
    setFinancesByCat({ commit }, fins) {
      commit('SET_FINANCES_BYCAT', fins)
    },
    addFinanceByCat({ commit }, finance) {
        commit('ADD_FINANCES_BYCAT', finance)
    },
    clearFinancesByCat({ commit }) {
        commit('CLEAR_FINANCES_BYCAT')
    },
    setCategories({ commit }, cats) {
      commit('SET_CATEGORIES', cats)
    },
    addFinance({ commit }, cat) {
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
    