<template>
  <div class="app-container">
    <div class="add-cat">
      <el-button class='cat-add-btn' type='primary' @click='handleAddCategory()'> Add Category</el-button>
    </div>
    <div class="material-table">
       <el-table
        ref="multipleTable"
        v-loading="listLoading"
        :data="cats"
        border
        fit
        highlight-current-row
        class="table"
      >
        <el-table-column prop="id" label="ID" width="50px" align="center" show-overflow-tooltip></el-table-column>
        <el-table-column label="Category" width="200px" align="center" show-overflow-tooltip>
          <template slot-scope="scope">
            <div> {{ scope.row.name }}</div>
          </template>
        </el-table-column>
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

    <el-dialog :visible.sync="dialogFormVisible">
      <el-form :model="catTemp" label-position="left" label-width="150px" style="width: 400px; margin-left:50px;">
        <el-form-item label="Category Name" required>
          <el-input v-model="catTemp.name"/>
        </el-form-item>
      </el-form>

      <div slot="footer" class="dialog-footer">
        <el-button @click="dialogFormVisible = false">
          Cancel
        </el-button>
        <el-button type="primary" @click="dialogStatus==='create'?AddCategory():updateData()">
          Confirm
        </el-button>
      </div>
    </el-dialog>

  </div>
</template>

<script>
import { mapGetters } from 'vuex'
import { getAllCats, addCat, updateCat, deleteCat} from '@/api/material.js'
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
      catLoading: false,
      catTemp: {
        name: '',
      },
      listLoading: false,

      temp: {
        id: 0, name: ''
      },

      // Edit dialog configuration
      dialogFormVisible: false,
      dialogStatus: '',
      confirmLoading: false,
      textMap: {
        update: 'Edit',
        create: 'Create'
      },
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
      this.listLoading = false
    },

    // ------------------------------- ADD ------------------------------------
    handleAddCategory() {
      this.dialogStatus = 'create'
      this.dialogFormVisible = true
      
    },
    AddCategory() {
      addCat(this.catTemp).then(res => {
        this.catLoading = true
        this.dialogFormVisible = false
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
    // ------------------------------- UPDATE ----------------------------------
     handleUpdate(row) {
      this.catTemp = Object.assign({}, row) // copy obj
      this.dialogStatus = 'update'
      this.dialogFormVisible = true
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
        const tempData = Object.assign({}, this.catTemp)
        console.log('tempData:', tempData)
        updateCat(tempData).then(response => {
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
    },


    // --------------------------------- DELETE -------------------------------
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
      deleteCat(index).then(() => {
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


  }
}
</script>


<style lang="scss" scoped>

.add-cat {
  display: flex;
  justify-content: flex-end;
}
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
  .action-btn  {
    margin: 0.3vw 0
  }
}
</style>