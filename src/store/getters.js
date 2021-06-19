const getters = {
  sidebar: state => state.app.sidebar,
  size: state => state.app.size,
  device: state => state.app.device,

  visitedViews: state => state.tagsView.visitedViews,
  cachedViews: state => state.tagsView.cachedViews,

  cas_id: state => state.user.cas_id,
  name: state => state.user.name,
  role: state => state.user.role,
  score: state => state.user.score,
  isAne: state => state.user.isAne,
  isVol: state => state.user.isVol,
  isPitch: state => state.user.isPitch,

  materials: state => state.material.materials,
  materialByCat: state => state.material.materialByCat,
  categories: state => state.material.categories,
  mats_loading: state => state.material.mats_loading,

  finances: state => state.finance.finances,
  financeByCat: state => state.finance.financeByCat,
  categories: state => state.finance.categories,
  finss_loading: state => state.finance.fins_loading,
  
  permission_routes: state => state.permission.routes,
  errorLogs: state => state.errorLog.logs
}
export default getters
