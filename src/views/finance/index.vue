<template>
  <div class="app-container">
    <el-row class="cats">
      <el-col :xs="{span: 32}" :sm="{span: 24}" :md="{span: 12}" :lg="{span: 12}" :xl="{span: 6}">
        <el-menu class='cat-menu' :default-active="activeIndex" mode="horizontal" @select="handleSelect" v-loading="catLoading">
          <div v-for="cat in cats">
            <el-menu-item index="cat.id">{{cat.name}}</el-menu-item>
          </div>
        </el-menu>
      </el-col>
      <el-col :xs="{span: 12}" :sm="{span: 6}" :md="{span: 4}" :lg="{span: 3}" :xl="{span: 6}">
        <el-button class='add-cat-btn' type="primary"  icon="el-icon-circle-plus" @click="handleAddCategory()">Add</el-button>
      </el-col>
    </el-row>

    <div class="filter-container">
      <el-input v-model="listQuery.name" placeholder="Name" style="width: 200px;" class="filter-item" @keyup.enter.native="handleFilter" />
      <el-button v-waves class="filter-item" type="primary" icon="el-icon-search" @click="handleFilter">
        Search
      </el-button>
      <el-button v-waves class="filter-item" type="primary" icon="el-icon-refresh-right" @click="ResetFilter">
        Reset
      </el-button>
      <el-button class="filter-item" style="margin-left: 10px;" type="primary" icon="el-icon-edit" @click="handleCreate">
        Add
      </el-button>
      <el-button v-waves :loading="downloadLoading" class="filter-item" type="primary" icon="el-icon-download" @click="handleDownload">
        Export
      </el-button>
    </div>

    <div class="finance-table">
       <el-table
        ref="multipleTable"
        v-loading="listLoading"
        :data="finance_items"
        border
        fit
        highlight-current-row
        class="table"
        @sort-change="sortChange"
      >
        <el-table-column prop="id" label="ID" width="50px" align="center" show-overflow-tooltip></el-table-column>
        <el-table-column label="Item" width="200px" align="center" show-overflow-tooltip>
          <template slot-scope="scope">
            <div> {{ scope.row.name }}</div>
          </template>
        </el-table-column>
        <el-table-column label="Buyer" align="center" show-overflow-tooltip>
          <template slot-scope="scope">
            <div> {{ scope.row.buyer }}</div>
          </template>
        </el-table-column>
        <el-table-column label="Price" width="250px" align="center" show-overflow-tooltip>
          <template slot-scope="scope">
            <el-input-number class='number-count' v-model="scope.row.price" @change="handleChangePrice(scope.row.id, scope.row.price)" :min="1" :step="1" ></el-input-number>
          </template>
        </el-table-column>
        <el-table-column label="Facture" width="100px" align="center" show-overflow-tooltip>
          <template slot-scope="scope">
            <div> {{ scope.row.facture }}</div>
          </template>
        </el-table-column>
        <el-table-column prop="description" label="Description" align="center" show-overflow-tooltip></el-table-column>
        <el-table-column label="Actions" align="center" class-name="small-padding fixed-width">
          <template slot-scope="{row}">
            <el-button class='action-btn' size="mini" type="warning" @click="handleUpdate(row)">
              Update
            </el-button>
            <el-button class='action-btn' size="mini" type="danger" @click="confirmDelete(row.id)">
              Remove
            </el-button>
          </template>
        </el-table-column>
      </el-table>
    </div>

    <el-dialog :visible.sync="catDialogVisible">
      <el-form :model="catTemp" label-position="left" label-width="150px" style="width: 400px; margin-left:50px;">
        <el-form-item label="Category Name" required>
          <el-input v-model="catTemp.name"/>
        </el-form-item>
      </el-form>

      <div slot="footer" class="dialog-footer">
        <el-button @click="catDialogVisible = false">
          Cancel
        </el-button>
        <el-button type="primary" @click="AddCategory()">
          Confirm
        </el-button>
      </div>
    </el-dialog>

    <el-dialog :title="textMap[dialogStatus]" :visible.sync="dialogFormVisible">
      <el-form ref="dataForm" :model="temp" label-position="left" label-width="120px" style="width: 400px; margin-left:50px;">
        <el-form-item label="Name" prop="name" required>
          <el-input v-model="temp.name" />
        </el-form-item>
        <el-form-item label="Category">
          <el-select v-model="temp.category_id" >
            <el-option
              v-for="item in cats"
              :key="item.id"
              :label="item.name"
              :value="item.id">
            </el-option>
          </el-select>

        </el-form-item>
        <el-form-item label="Buyer" required>
          <el-input  v-model="temp.buyer" />
        </el-form-item>
        <el-form-item label="Price" prop="price"  required>
          <el-input  type="number" v-model="temp.price" />
        </el-form-item>
        <el-form-item label="facture" required>
          <el-input  v-model="temp.facture" />
        </el-form-item>
        <el-form-item label="Description">
          <el-input v-model="temp.description" />
        </el-form-item>
      </el-form>

      <div slot="footer" class="dialog-footer">
        <el-button @click="dialogFormVisible = false">
          Cancel
        </el-button>
        <el-button type="primary" @click="dialogStatus==='create'?createData():updateData()">
          Confirm
        </el-button>
      </div>
    </el-dialog>

  </div>
</template>

<script>
import { mapGetters } from 'vuex'
import { getAllCats, getAllFinances, getAllFinancesByCat, 
addCat, addFinance, updateFinance, updateFinancePrice, deleteFinance} from '@/api/finance.js'
import Pagination from '@/components/Pagination' // secondary package based on el-pagination
import waves from '@/directive/waves' // waves directive

export default {
  name: 'FinanceTable',
  components: { Pagination },
  directives: { waves },
  data() {
    return {
      cats: null,
      cat_id: 1,
      activeIndex: '1',
      catLoading: false,
      catTemp: {
        name: '',
      },

      finance: null,
      finance_items: null,
      tmp_list: null,
      listLoading: false,
      showReviewer: false,
      listQuery: {
        name: undefined,
        status: undefined,
      },

      temp: {
        id: 0, name: '', facture:'', price: 0,
        description: '', buyer: '', category_id: '',
      },

      // Edit dialog configuration
      catDialogVisible: false,
      dialogFormVisible: false,
      dialogStatus: '',
      confirmLoading: false,
      textMap: {
        update: 'Edit',
        create: 'Create'
      },

      downloadLoading: false,

      rules: {
        name: [{ required: true, message: 'name is required', trigger: 'blur' }],
      },
    }
  },
  computed: {
    ...mapGetters([
      'finances',
      'financeByCat',
      'categories',
      'fins_loading'
    ]),
  },
  created() {
    this.getList()
  },
  methods: {
    async getList() {
      this.listLoading = true
      var res = await getAllCats()
      console.log(res.data.cat_infos)
      this.cats = res.data.cat_infos
      this.$store.dispatch('finance/setCategories', this.cats)
      //TODO:use aysnc/await to replace the settimeout
      getAllFinances().then(response => {
        this.finance_items = response.data.info
        console.log(this.finance_items)
        this.$store.dispatch('finance/setFinances', this.finance_items)
        this.listLoading = false
      }).catch(err => {
        console.error(err)
      })
    },

    getFinByCat(row) {
      //TODO: Pagination
      this.cat_id = row.id
      getAllFinancesByCat(this.cat_id).then(response => {
        const finsByCat = response.data.info
        this.$store.dispatch('finance/setFinancesByCat', finsByCat)
      }).catch(err => {
        console.error(err)
      })
    },
    
    // ------------------------------------ FILTER -------------------------------
    compare(p) {
      return function(m,n){
        var a = m[p];
        var b = n[p];
        return b - a; //升序
      }
    },
    sortChange(data) {
      const { prop, order } = data
      this.tmp_list = this.finance_items
      this.finance_items.sort(this.compare("a_score"));
      console.log(this.finance_items)
    },

    handleSelect(key, keyPath) {
      console.log(key, keyPath);
    },

    //TODO: Pagination 
    handleFilter() {
      var new_array = []
      this.finance_items = this.tmp_list
      console.log(this.listQuery, this.list)
      if (this.listQuery.name != "" ) {
        for (var i = 0; i < this.finance_items.length; i++) {
          if (this.finance_items[i].name == this.listQuery.name) {
            new_array.push(this.finance_items[i])
          }
        }
        this.finance_items = new_array
        console.log('FILTER ACCORDING TO THE NAME.....')
      } else  {
        this.getList()
        this.$message({
          type:'info',
          message: 'NO FILTER'
        })
      }
    console.log('AFTER FILTERING, THE LIST IS: ', this.list)
    },
    ResetFilter() {
      this.getList()
    },
    // ------------------------------- ADD ------------------------------------
    handleAddCategory() {
      this.resetTemp()
      this.dialogStatus = 'create'
      this.catDialogVisible = true
      
    },
    AddCategory() {
      addCat(this.catTemp).then(res => {
        this.catLoading = true
        this.catDialogVisible = false
        this.$message({
          message: 'ADD Category Successfully!',
          type: 'success'
        })
        this.getList()
        this.catLoading = false
      }).catch(err => {
        this.$message({
          message: 'ADD Category failed!',
          type: 'danger'
        })
        this.catLoading = false
      })
      this.catTemp = {name:''}
    },
    resetTemp() {
      this.temp = {
        id: undefined, name: 'None', buyer: '', price: 0,
        description: '', facture: '', category_id: 0,
      }
    },
    handleCreate() {
      console.log(this.cats)
      this.resetTemp()
      this.dialogStatus = 'create'
      this.dialogFormVisible = true
      this.$nextTick(() => {
        this.$refs['dataForm'].clearValidate()
      })
    },
    createData() {
      this.$refs['dataForm'].validate((valid) => {
        if (valid) {
          addFinance(this.temp).then(response => {
            this.$message({
              message: 'ADD ' + response.data.name + "'s Category Successfully!",
              type: 'success'
            })
            this.listLoading = true
            this.dialogFormVisible = false
            setTimeout(() => {
              this.getList()
            }, 1.5 * 1000)
          }).catch (e => {
            console.error(e)
            this.$message({
              message: 'ADD Score failed!',
              type: 'danger'
            })
          })
          this.resetTemp()
        }
      })
    },
    // ------------------------------- UPDATE ----------------------------------
    handleChangePrice(id, price) {
      const payload = {'id': id,'price': price}
      updateFinancePrice(payload).then(res => {
        console.log(res)
      }).catch(err => {
        console.error(err)
      })
    },

     handleUpdate(row) {
      this.temp = Object.assign({}, row) // copy obj
      console.log(this.temp)
      this.dialogStatus = 'update'
      this.dialogFormVisible = true
      this.$nextTick(() => {
        this.$refs['dataForm'].clearValidate()
      })
    },
    updateData() {
      this.$confirm('Are you sure to submit? Once you submitted, the operation cannot be undone!', 'Note', {
          confirmButtonText: 'Confirm',
          cancelButtonText: 'Cancle',
          type: 'warning'
        }).then(() => {
          this.confirmUpdate()
        }).catch(() => {
          this.$message({
            type: 'info',
            message: 'Update cancled'
          });          
        });
    },
    confirmUpdate() {
      this.$refs['dataForm'].validate((valid) => {
        if (valid) {
          const tempData = Object.assign({}, this.temp)
          console.log('tempData:', tempData)
          updateFinance(tempData).then(response => {
            this.$message({
              message: 'UPDATE Successfully!',
              type: 'success'
            })
            this.listLoading = true
            this.dialogFormVisible = false
            setTimeout(() => {
              this.getList()
            }, 1.5 * 1000)
          }).catch (e => {
            console.error(e)
            this.$message({
              message: 'UPDATE Score failed!',
              type: 'danger'
            })
          })
        }
        this.resetTemp()
      })
    },


    // --------------------------------- DELETE -------------------------------
    confirmDelete(index) {
      this.$confirm('This operation will delete this inforfinion forever, are you sure?', 'Note', {
          confirmButtonText: 'Confirm',
          cancelButtonText: 'Cancle',
          type: 'warning'
        }).then(() => {
          this.handleDelete(index)
        }).catch(() => {
          this.$message({
            type: 'info',
            message: 'Delete cancled'
          });
        });
    },
    handleDelete(index) {
      console.log('INDEX:', index)
      deleteFinance(index).then(() => {
        this.$notify({
          title: 'Success',
          message: 'Delete Successfully',
          type: 'success',
          duration: 2000
        })
        this.getList()
      }).catch(err => {
        this.$notify({
          title: 'Failed',
          message: 'Delete failed',
          type: 'danger',
          duration: 2000
        })
      })
    },


    // ----------------------Others-------------------
    handleDownload() {
      this.downloadLoading = true
      import('@/vendor/Export2Excel').then(excel => {
        const tHeader = ['ID', 'name', 'Price', 'Quantity', 'Description', 'status']
        const filterVal = ['id', 'name','price', 'quantity', 'description', 'status']
        const data = this.forfinJson(filterVal)
        excel.export_json_to_excel({
          header: tHeader,
          data,
          filename: 'ane-rouge-table'
        })
        this.downloadLoading = false
      })
    },
  }
}
</script>


<style lang="scss" scoped>

.cat-menu {
  display: flex !important;
  flex-direction: row !important;
  font-weight: bold !important;
  font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif !important;
}

.filter-container {
  margin-top: 1vw;
}

.add-cat-btn {
  transform: scale(1.2);
}
.finance-table {
  padding: 0.5vw 0.5vw;
  margin-bottom: 1vw;
  border-radius: 2%;
  display: flex;
  align-items: center;
  font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
  .action-btn  {
    margin: 0.3vw 0
  }
}
</style>