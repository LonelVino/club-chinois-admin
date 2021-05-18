<template>
  <div class="app-container">
    <div class="filter-container">
      <el-input v-model="listQuery.name" placeholder="Name" style="width: 200px;" class="filter-item" @keyup.enter.native="handleFilter" />
      <el-select v-model="listQuery.isFini" placeholder="isFini" clearable style="width: 90px" class="filter-item">
        <el-option v-for="item in isFiniOptions" :key="item" :label="item"  :value="item" />
      </el-select>
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
      <el-checkbox v-model="showReviewer" class="filter-item" style="margin-left:15px;" @change="tableKey=tableKey+1">
        show comments
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
      align="center"
    >
      <el-table-column label="ID" prop="id" align="center" width="80" >
        <template slot-scope="{row}">
          <span>{{ row.id }}</span>
        </template>
      </el-table-column>
      <el-table-column label="Name" width="200px" align="center">
        <template slot-scope="{row}">
          <span>{{ row.name }}</span>
        </template>
      </el-table-column>
      <el-table-column label="isFini" class-name="status-col" align="center" width="100">
        <template slot-scope="{row}">
          <span>{{ row.isFini }}</span>
        </template>
      </el-table-column>
      <el-table-column label="Time" class-name="status-col" align="center" width="100">
        <template slot-scope="{row}">
          <span>{{ row.time }}</span> s
        </template>
      </el-table-column>
      <el-table-column label="Score" width="100px" sortable="custom" align="center">
        <template slot-scope="{row}">
          <span>{{ row.a_score }}</span>
        </template>
      </el-table-column>
      <el-table-column v-if="showReviewer" label="Comments" width="200">
        <template slot-scope="{row}">
          <span style="color:red;">{{ row.comment }}</span>
        </template>
      </el-table-column>

      <el-table-column label="Actions" align="center" width="230" class-name="small-padding fixed-width">
        <template slot-scope="{row}">
          <el-button type="primary" size="mini" @click="handleUpdate(row)">
            Edit
          </el-button>
          <el-button size="mini" type="danger" @click="confirmDelete(row.id)">
            Delete
          </el-button>
        </template>
      </el-table-column>
    </el-table>

    <pagination v-show="total>0" :total="total" :page.sync="listQuery.page" :limit.sync="listQuery.limit" @pagination="getList" />
    <el-dialog :title="textMap[dialogStatus]" :visible.sync="dialogFormVisible">
      <el-form ref="dataForm" :rules="rules" :model="temp" label-position="left" label-width="80px" style="width: 400px; margin-left:50px;">
        <el-form-item label="Name" prop="name" required>
          <el-input v-model="temp.name" />
        </el-form-item>
        <el-form-item label="isFini?">
          <el-switch v-model="temp.isFini"></el-switch>
        </el-form-item>
        <el-form-item label="Time" prop="time"  required>
          <el-input  type="number" v-model="temp.time" />
        </el-form-item>
        <el-form-item label="Score" prop="a_score" required>
          <el-input  type="number" v-model="temp.a_score" />
        </el-form-item>
        <el-form-item label="Comment">
          <el-input  v-model="temp.comment" />
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
import {getScore, getAllScores, addScore, updateScore, deleteScore} from '@/api/ane'
import waves from '@/directive/waves' // waves directive
import { parseTime } from '@/utils'
import Pagination from '@/components/Pagination' // secondary package based on el-pagination


export default {
  name: 'AneTable',
  components: { Pagination },
  directives: { waves },
  filters: {
    statusFilter(status) {
      const statusMap = {
        published: 'success',
        draft: 'info',
        deleted: 'danger'
      }
      return statusMap[status]
    },
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
        isFini: undefined,
        name: undefined,
      },
      isFiniOptions: ['true', 'false'],
      showReviewer: true,
      temp: {
        id: undefined,
        name: 'None',
        isFini: 0,
        a_score: 0,
        time: 0,
        comment: '',
      },

      dialogFormVisible: false,
      dialogStatus: '',
      textMap: {
        update: 'Edit',
        create: 'Create'
      },
      rules: {
        name: [{ required: true, message: 'name is required', trigger: 'blur' }],
        time: [{  required: true, message: 'time is required and should be a number', trigger: 'blur' }],
        a_score: [{ required: true, message: 'score is required  and should be a number', trigger: 'blur' }]
      },
      downloadLoading: false
    }
  },
  created() {
    this.getList()
  },
  methods: {
    getList() {
      this.listLoading = true
      getAllScores().then(response => {
        // Just to simulate the time of the request
        this.list = response.data.infos
        this.tmp_list = response.data.infos
        setTimeout(() => {
          this.listLoading = false
        }, 1.5 * 1000)
      })
    },
    //TODO: Pagination 
    handleFilter() {
      var new_array = []
      this.list = this.tmp_list
      console.log(this.listQuery, this.list)
      if (this.listQuery.isFini != undefined  && (this.listQuery.name != undefined && this.listQuery.name != "" )) {
        for (var i = 0; i < this.list.length; i++) {
          var cor2isFini = (this.list[i].isFini === true && this.listQuery.isFini == 'true') || (this.list[i].isFini === false && this.listQuery.isFini == 'false')
          if ((this.list[i].name == this.listQuery.name) && cor2isFini) {
            new_array.push(this.list[i])
          }
        }
        this.list = new_array
        console.log('FILTER ACCORDING TO BOTH THE NAME AND ISFINI.....')        
      } else if (this.listQuery.name != undefined && this.listQuery.name != "" ) {
        for (var i = 0; i < this.list.length; i++) {
          if (this.list[i].name == this.listQuery.name) {
            new_array.push(this.list[i])
          }
        }
        this.list = new_array
        console.log('FILTER ACCORDING TO THE NAME.....')
      } else if (this.listQuery.isFini != undefined) {
        for (var i = 0; i < this.list.length; i++) {
          if ((this.list[i].isFini == true && this.listQuery.isFini == 'true') || (this.list[i].isFini == false && this.listQuery.isFini == 'false')) {
            new_array.push(this.list[i])
          } 
        }
        this.list = new_array
        console.log('FILTER ACCORDING TO ISFINI.....')
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
    handleModifyStatus(row, status) {
      this.$message({
        message: '操作Success',
        type: 'success'
      })
      row.status = status
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

    resetTemp() {
      this.temp = {
        id: undefined,
        name: 'None',
        isFini: 0,
        a_score: 0,
        time: 0,
        comment: '',
        pays: 'None'
      }
    },
    handleCreate() {
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
          this.temp.isFini = (this.temp.isFini == true) ? 1 : 0 
          this.temp.time = parseInt(this.temp.time)
          this.temp.a_score = parseInt(this.temp.a_score)
          addScore(this.temp).then(response => {
            // Just to simulate the time of the request
            console.log(response)
            this.$message({
              message: 'ADD ' + response.data.name + "'s Score Successfully!",
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
    handleUpdate(row) {
      this.temp = Object.assign({}, row) // copy obj
      this.dialogStatus = 'update'
      this.dialogFormVisible = true
      this.$nextTick(() => {
        this.$refs['dataForm'].clearValidate()
      })
    },
    updateData() {
      this.$refs['dataForm'].validate((valid) => {
        if (valid) {
          const tempData = Object.assign({}, this.temp)
          tempData.isFini = (tempData.isFini == true || tempData.isFini == 1) ? 1 : 0 
          tempData.time = parseInt(tempData.time)
          tempData.a_score = parseInt(tempData.a_score)
          updateScore(tempData).then(response => {
            this.$message({
              message: 'UPDATE ' + response.data.name + "'s Score Successfully!",
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
      deleteScore(index).then(res => {
        this.$notify({
          title: 'Success',
          message: 'Delete Successfully',
          type: 'success',
          duration: 2000
        })
        this.getList()
      }).catch(e => {
        console.error(e)
        this.$message({
          type: 'danger',
          message: 'Delete failed, ' + e
        });      
      })
    },
    handleDownload() {
      this.downloadLoading = true
      import('@/vendor/Export2Excel').then(excel => {
        const tHeader = ['ID', 'name', 'isFinished', 'Time', 'Score', 'Country', 'Comments']
        const filterVal = ['id', 'name', 'isFini', 'time', 'a_score', 'pays', 'comment']
        const data = this.formatJson(filterVal)
        excel.export_json_to_excel({
          header: tHeader,
          data,
          filename: 'ane-rouge-table'
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
