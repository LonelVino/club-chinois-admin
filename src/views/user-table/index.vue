<template>
  <div class="app-container">
    <div class="filter-container">
      <el-input v-model="listQuery.name" placeholder="Name" style="width: 200px;" class="filter-item" @keyup.enter.native="handleFilter" />
      
      <el-button v-waves class="filter-item" type="primary" icon="el-icon-search" @click="handleFilter">
        Search
      </el-button>
      <el-button class="filter-item" style="margin-left: 10px;" type="primary" icon="el-icon-edit" @click="handleCreate">
        Add
      </el-button>
      <el-button v-waves :loading="downloadLoading" class="filter-item" type="primary" icon="el-icon-download" @click="handleDownload">
        Export
      </el-button>
      <el-checkbox v-model="showReviewer" class="filter-item" style="margin-left:15px;" @change="tableKey=tableKey+1">
        reviewer
      </el-checkbox>
    </div>

    <el-table
      :key="tableKey"
      v-loading="listLoading"
      :data="list"
      border
      fit
      highlight-current-row
      style="width: 100%;"
      @sort-change="sortChange"
    >
      <el-table-column label="ID" prop="id" sortable="custom" align="center" width="80">
        <template slot-scope="{row}">
          <span>{{ row.id }}</span>
        </template>
      </el-table-column>
      <el-table-column label="Name" width="100px" align="center">
        <template slot-scope="{row}">
          <span>{{ row.name}}</span>
        </template>
      </el-table-column>
      <el-table-column label="isAne" width="100px" align="center">
        <template slot-scope="{row}">
          <span>{{ row.isAne?'Yes':'No' }}</span>
        </template>
      </el-table-column>
      <el-table-column label="isVol" width="100px" align="center">
        <template slot-scope="{row}">
          <span>{{ row.isVol?'Yes':'No' }}</span>
        </template>
      </el-table-column>
      <el-table-column label="isPitch" class-name="status-col" width="100px">
        <template slot-scope="{row}">
          <span>{{ row.isPitch?'Yes':'No' }}</span>
        </template>
      </el-table-column>
      
      <el-table-column label="Score" width="80px">
        <template slot-scope="{row}">
           <span>{{ row.score }}</span>
        </template>
      </el-table-column>

      <el-table-column label="Country" width="100px" sortable="custom" align="center">
        <template slot-scope="{row}">
          <span>{{ row.pays }}</span>
        </template>
      </el-table-column>

      <el-table-column label="Email" class-name="status-col" width="200">
        <template slot-scope="{row}">
          <span>{{ row.email }}</span>          
        </template>
      </el-table-column>

      <el-table-column label="telephone" class-name="status-col" width="200">
        <template slot-scope="{row}">
          <span>{{ row.telephone }}</span>          
        </template>
      </el-table-column>


      <el-table-column label="Loc" class-name="status-col" width="100">
        <template slot-scope="{row}">
          <span>{{ row.loc }}</span>
        </template>
      </el-table-column>
      
      <el-table-column label="Actions" align="center" width="150" class-name="small-padding fixed-width">
        <template slot-scope="{row}">
          <el-button type="primary" size="mini" @click="handleUpdate(row)">
            Edit
          </el-button>
          <el-button v-if="row.status!='deleted'" size="mini" type="danger" @click="confirmDelete(row.id)">
            Delete
          </el-button>
        </template>
      </el-table-column>
    </el-table>

    <pagination v-show="total>0" :total="total" :page.sync="listQuery.page" :limit.sync="listQuery.limit" @pagination="getList" />

    <el-dialog :title="textMap[dialogStatus]" :visible.sync="dialogFormVisible">
      <el-form ref="dataForm" :rules="rules" :model="temp" label-position="left" label-width="70px" style="width: 400px; margin-left:50px;">
        <el-form-item label="Name" prop="name">
          <el-input v-model="temp.name" />
        </el-form-item>
        <el-form-item label="Has played AneRouge?" prop="isAne" label-width="230px">
          <el-radio v-model="temp.isAne" label="1">Yes</el-radio>
          <el-radio v-model="temp.isAne" label="0">No</el-radio>
        </el-form-item>
        <el-form-item label="Has played Volant?" prop="isVol" label-width="230px">
          <el-radio v-model="temp.isVol" label="1">Yes</el-radio>
          <el-radio v-model="temp.isVol" label="0">No</el-radio>
        </el-form-item>
        <el-form-item label="Has played Pitch?" prop="isPitch" label-width="230px">
          <el-radio v-model="temp.isPitch" label="1">Yes</el-radio>
          <el-radio v-model="temp.isPitch" label="0">No</el-radio>
        </el-form-item>
        <el-form-item label="Score" prop="score" label-width="130px">
          <el-input v-model="temp.score" />
        </el-form-item>
        <el-form-item label="Country" prop="pays" label-width="130px">
          <el-input v-model="temp.pays" />
        </el-form-item>
        <el-form-item label="Email" prop="email" label-width="100px">
          <el-input v-model="temp.email" />
        </el-form-item>
        <el-form-item label="Telephone" prop="telephone" label-width="130px">
          <el-input v-model="temp.telephone" />
        </el-form-item>
        <el-form-item label="Location" prop="loc" label-width="100px">
          <el-input v-model="temp.loc" />
        </el-form-item>
      </el-form>
      <div slot="footer" class="dialog-footer">
        <el-button @click="dialogFormVisible = false">
          Cancel
        </el-button>
        <el-button type="primary" v-loading="confirmLoading" @click="dialogStatus==='create'?createData():updateData()">
          Confirm
        </el-button>
      </div>
    </el-dialog>
  </div>
</template>

<script>
import {getAllInfos, addInfo, updateInfo, deleteInfo} from '@/api/user'
import waves from '@/directive/waves' // waves directive
import { parseTime } from '@/utils'
import Pagination from '@/components/Pagination' // secondary package based on el-pagination


export default {
  name: 'UserTable',
  components: { Pagination },
  directives: { waves },

  filters: {
    statusFilter(status) {
      const statusMap = {
        deleted: 'danger'
      }
      return statusMap[status]
    },
    typeFilter(type) {
      return calendarTypeKeyValue[type]
    }
  },

  data() {
    return {
      tableKey: 0,
      list: null,
      tmp_list: null,
      total: 0,
      listLoading: true,
      listQuery: {
        page: 1,
        limit: 20,
        name: undefined,
      },

      statusOptions: ['deleted'],
      showReviewer: false,

      temp: {
        id: undefined,
        name: 'None',
        isAne: 0,
        isVol: 0,
        isPitch: 0,
        score: 0,
        email: '',
        telephone: '',
        loc: '',
        pays: 'None'
      },

      dialogFormVisible: false,
      dialogStatus: '',
      textMap: {
        update: 'Edit',
        create: 'Create'
      },
      
      rules: {
        name: [{ required: true, message: 'name is required', trigger: 'blur' }],
        isAne: [{ required: true, message: 'If has played AneRouge is required', trigger: 'change' }],
        isVol: [{ required: true, message: 'If has played Volant is required', trigger: 'change' }],
        isPitch: [{ required: true, message: 'If has played Pitch is required', trigger: 'change' }],
      },
      downloadLoading: false,
      confirmLoading: false,

    }
  },
  created() {
    this.getList()
  },
  methods: {
    getList() {
      this.listLoading = true

      getAllInfos().then(response => {
        // Just to simulate the time of the request
        console.log('response.data.infos:',response.data.infos)
        this.list = response.data.infos
        this.tmp_list =  response.data.infos
        setTimeout(() => {
          this.listLoading = false
        }, 1.5 * 1000)
      })
    },
    //TODO: Pagination 
    handleFilter() {
      this.listQuery.page = 1
      this.getList()
    },

    handleModifyStatus(row, status) {
      this.$message({
        message: '操作Success',
        type: 'success'
      })
      row.status = status
    },

    sortChange(data) {
      const { prop, order } = data
      if (prop === 'id') {
        this.sortByID(order)
      }
    },
    sortByID(order) {
      if (order === 'ascending') {
        this.listQuery.sort = '+id'
      } else {
        this.listQuery.sort = '-id'
      }
      this.handleFilter()
    },

    resetTemp() {
      this.temp = {
        id: undefined,
        name: '',
        isAne: 0,
        isVol: 0,
        isPitch: 0,
        score: 0,
        email: '',
        telephone: '',
        loc: '',
        pays: ''
      }
    },

    handleCreate() {
      console.log('dialogStatus:', this.dialogStatus)
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
          addInfo(this.temp).then(() => {
            this.confirmLoading = true
            this.list.unshift(this.temp)
            this.dialogFormVisible = false
            this.confirmLoading = false
            this.$notify({
              title: 'Success',
              message: 'Created Successfully',
              type: 'success',
              duration: 2000
            })
          }).catch( err => {
            console.error(err)
          })
        }
      })
    },
    handleUpdate(row) {
      console.log('dialogStatus:', this.dialogStatus)
      this.temp = Object.assign({}, row) // copy obj
      this.temp.timestamp = new Date(this.temp.timestamp)
      this.dialogStatus = 'Update'
      this.dialogFormVisible = true
      this.$nextTick(() => {
        this.$refs['dataForm'].clearValidate()
      })
    },
    updateData() {
      this.$refs['dataForm'].validate((valid) => {
        if (valid) {
          const tempData = Object.assign({}, this.temp)
          tempData.timestamp = +new Date(tempData.timestamp) // change Thu Nov 30 2017 16:41:05 GMT+0800 (CST) to 1512031311464
          updateInfo(tempData).then(() => {
            this.confirmLoading = true
            const index = this.list.findIndex(v => v.id === this.temp.id)
            this.list.splice(index, 1, this.temp)
            this.dialogFormVisible = false
            this.confirmLoading = false
            this.$notify({
              title: 'Success',
              message: 'Update Successfully',
              type: 'success',
              duration: 2000
            })
          }).catch(err => {
            console.error(err)
          })
        }
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
      deleteInfo(index).then(() => {
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
    handleDownload() {
      this.downloadLoading = true
      import('@/vendor/Export2Excel').then(excel => {
        const tHeader = ['ID', 'name', 'has Ane', 'has Pitch', 'has Volant', 'Score', 'Email', 'Tel', 'Country']
        const filterVal = ['id', 'name', 'isAne', 'isPitch', 'isVolant', 'score', 'email', 'telephone', 'pays']
        const data = this.formatJson(filterVal)
        excel.export_json_to_excel({
          header: tHeader,
          data,
          filename: 'table-list'
        })
        this.downloadLoading = false
      })
    },
    formatJson(filterVal) {
      return this.list.map(v => filterVal.map(j => {
        if (j === 'timestamp') {
          return parseTime(v[j])
        } else {
          return v[j]
        }
      }))
    },
  }
}
</script>
