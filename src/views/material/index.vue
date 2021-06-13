<template>
  <div class="app-container">
    <el-row gutter="32" class="cats">
      <el-col :xs="{span: 32}" :sm="{span: 24}" :md="{span: 12}" :lg="{span: 12}" :xl="{span: 6}">
        <el-menu :default-active="activeIndex" class="el-menu" mode="horizontal" @select="handleSelect">
          <div v-for="cat in cats">
            <el-menu-item index="cat.id">{{cat.name}}</el-menu-item>
          </div>
        </el-menu>
      </el-col>
      <el-col :xs="{span: 12}" :sm="{span: 6}" :md="{span: 4}" :lg="{span: 3}" :xl="{span: 6}">
        <el-button class='add-cat-btn' type="primary"  icon="el-icon-circle-plus" @click="handleAddCategory()">Add</el-button>
      </el-col>
    </el-row>
<!-- 
    <div class="filter-container">
      <el-input v-model="listQuery.name" placeholder="Name" style="width: 200px;" class="filter-item" @keyup.enter.native="handleFilter" />
      <el-select v-model="listQuery.status" placeholder="Received" clearable style="width: 90px" class="filter-item">
        <el-option v-for="item in statusOptions" :key="item" :label="item"  :value="item" />
      </el-select>
      <el-button v-waves class="filter-item" type="primary" icon="el-icon-search" @click="handleFilter">
        Search
      </el-button>
      <el-button v-waves class="filter-item" type="primary" icon="el-icon-refresh-right" @click="ResetFilter">
        Reset
      </el-button>
      <el-button class="filter-item" style="margin-left: 10px;" type="primary" icon="el-icon-edit" @click="handleCreate" disabled>
        Add
      </el-button>
      <el-button v-waves :loading="downloadLoading" class="filter-item" type="primary" icon="el-icon-download" @click="handleDownload">
        Export
      </el-button>
    </div> -->

    <div class="material-table">
       <el-table
        ref="multipleTable"
        v-loading="listLoading"
        :data="material_items"
        border
        fit
        highlight-current-row
        class="table"
        @sort-change="sortChange"
      >
        <el-table-column prop="id" label="ID" width="50px" align="center" show-overflow-tooltip></el-table-column>
        <el-table-column label="Product" width="200px" align="center" show-overflow-tooltip>
          <template slot-scope="scope">
            <div> {{ scope.row.name }}</div>
          </template>
        </el-table-column>
        <el-table-column label="Price" align="center" show-overflow-tooltip>
          <template slot-scope="scope">
            <div> {{ scope.row.price }} €</div>
          </template>
        </el-table-column>
        <el-table-column label="Quantity" width="250px" align="center" show-overflow-tooltip>
          <template slot-scope="scope">
            <el-input-number class='number-count' v-model="scope.row.quantity" @change="handleChangeQuantity(scope.row.id, scope.row.quantity)" :min="1" :step="1" ></el-input-number>
          </template>
        </el-table-column>
        <el-table-column label="Total" align="center" show-overflow-tooltip>
          <template slot-scope="scope">
            <div> {{ scope.row.ttl_price }} €</div>
          </template>
        </el-table-column>
        <el-table-column label="Status" width="100px" align="center" show-overflow-tooltip>
          <template slot-scope="scope">
          <el-switch
            v-model="scope.row.status"
            :active-value="1"
            :inactive-value="0"
            active-color="#02538C"
            inactive-color="#B9B9B9"
            @change="handleChangeStatus(scope.row)"
          />
          </template>
        </el-table-column>
        <el-table-column prop="description" label="Description" align="center" show-overflow-tooltip></el-table-column>
        <el-table-column label="Actions" align="center" class-name="small-padding fixed-width">
          <template slot-scope="{row}">
            <el-button v-if="row.status!='deleted'" size="mini" type="danger" @click="confirmDelete(row.id)">
              Remove
            </el-button>
          </template>
        </el-table-column>
      </el-table>
    </div>

    <el-dialog :title="textMap[dialogStatus]" :visible.sync="catDialogVisible">
      <el-input v-model="catTemp.name" />

      <div slot="footer" class="dialog-footer">
        <el-button @click="dialogFormVisible = false">
          Cancel
        </el-button>
        <el-button type="primary" @click="dialogStatus==='create'?createCat():updateCat()">
          Confirm
        </el-button>
      </div>
    </el-dialog>

    <el-dialog :title="textMap[dialogStatus]" :visible.sync="dialogFormVisible">
      <el-form ref="dataForm" :rules="rules" :model="temp" label-position="left" label-width="80px" style="width: 400px; margin-left:50px;">
        <el-form-item label="Name" prop="name" required>
          <el-input v-model="temp.name" disabled />
        </el-form-item>
        <el-form-item label="Category">
          <el-select v-model="temp.category"></el-select>
        </el-form-item>
        <el-form-item label="Status">
          <el-select v-model="temp.status"></el-select>
        </el-form-item>
        <el-form-item label="Price" prop="price"  required>
          <el-input  type="number" v-model="temp.price" />
        </el-form-item>
        <el-form-item label="Quantity" required>
          <el-input  type="number" v-model="temp.quantity" />
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
import {getCat, getAllCats, getMaterial, getAllMaterials, getAllMaterialsByCat} from '@/api/material.js'
import Pagination from '@/components/Pagination' // secondary package based on el-pagination
import waves from '@/directive/waves' // waves directive

export default {
  name: 'MaterialTable',
  components: { Pagination },
  directives: { waves },
  data() {
    return {
      cats: null,
      cat_id: 1,
      activeIndex: '1',

      material: null,
      material_items: null,
      listLoading: false,
      showReviewer: false,

      statusOptions: [0, 1],
      listQuery: {
        name: undefined,
        status: undefined,
      },

      catTemp: {
        name: '',
      },
      temp: {
        name: '',
        quantity: 0,
        price: 0,
        description: '',
        image: '',
        status: 0,
        category: '',
      },

      // Edit dialog configuration
      catDialogVisible: false,
      dialogFormVisible: false,
      dialogStatus: '',
      confirmLoading: false,
    }
  },
  computed: {
    ...mapGetters([
      'materials',
      'materialByCat',
      'categories',
      'mats_loading'
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
      this.$store.dispatch('material/setCategories', this.cats)
      //TODO:use aysnc/await to replace the settimeout
      getAllMaterials().then(response => {
        this.material_items = response.data.info
        this.$store.dispatch('material/setMaterials', this.material_items)
        setTimeout(() => {
          this.getProdbyId()
          this.listLoading = false
        }, 1500);
      }).catch(err => {
        console.error(err)
      })
    },

    getMatByCat(row) {
      //TODO: Pagination
      this.cat_id = row.id
      getAllMaterialsByCat(this.cat_id).then(response => {
        const matsByCat = response.data.info
        this.$store.dispatch('material/setMaterialsByCat', matsByCat)
      }).catch(err => {
        console.error(err)
      })
    },
    
    compare(p) {
      return function(m,n){
        var a = m[p];
        var b = n[p];
        return b - a; //升序
      }
    },
    sortChange(data) {
      const { prop, order } = data
      this.tmp_list = this.list
      this.list.sort(this.compare("a_score"));
      console.log(this.list)
    },

    handleSelect(key, keyPath) {
      console.log(key, keyPath);
    },

    handleChangeQuantity(id, quantity) {
      const payload = {'id': id,'quantity': quantity}
      updateCartItem(payload).then(res => {
        console.log(res)
      }).catch(err => {
        console.error(err)
      })
    },

    confirmDelete(index) {
      this.$confirm('This operation will delete this information forever, are you sure?', 'Note', {
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
      deleteCartItem(index).then(() => {
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

    confirmDeleteAll() {
      this.$confirm('This operation will delete this information forever, are you sure?', 'Note', {
          confirmButtonText: 'Confirm',
          cancelButtonText: 'Cancle',
          type: 'warning'
        }).then(() => {
          this.handleDeleteAll(this.cart.id)
        }).catch(() => {
          this.$message({
            type: 'info',
            message: 'Delete cancled'
          });
        });
    },
    handleDeleteAll(index) {
      console.log('INDEX:', index)
      deleteCart(index).then(() => {
        this.$notify({
          title: 'Success',
          message: 'Delete All Successfully',
          type: 'success',
          duration: 2000
        })
        this.getList()
      }).catch(err => {
        this.$notify({
          title: 'Failed',
          message: 'Delete All failed',
          type: 'danger',
          duration: 2000
        })
      })
    },
  }
}
</script>

<style lang="scss">
.el-menu {
  display: flex;
  flex-direction: row;
  font-weight: bold;
  font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
}
</style>

<style lang="scss" scoped>
.add-cat-btn {
  transform: scale(1.2);
}
.material-table {
  padding: 0.5vw 0.5vw;
  margin-bottom: 1vw;
  border-radius: 2%;
  display: flex;
  align-items: center;
  font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
}
</style>