<template>
  <div class="app-container">
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
      <el-checkbox v-model="showReviewer" class="filter-item" style="margin-left:15px;" @change="tableKey=tableKey+1">
        show comments
      </el-checkbox>
    </div>

    <div class="note">
      <p class="note-txt">You can only modify one row at a time, not multiple rows of data.</p>
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
      <el-table-column label="ID" prop="id" align="center" width="80">
        <template slot-scope="{row}">
          <span>{{ row.id }}</span>
        </template>
      </el-table-column>
      <el-table-column label="Name" width="200px" align="center">
        <template slot-scope="scope">
          <div v-if="!scope.row.isEdit" @click="handleClick(scope.row)"> {{ scope.row.name }}</div>
          <div v-else>
            <el-input v-model="scope.row.name" @click="handleClick(scope.row)"></el-input>
          </div>
        </template>
      </el-table-column>
      <el-table-column label="number" class-name="status-col" align="center" width="100">
        <template slot-scope="scope">
          <div v-if="!scope.row.isEdit" @click="handleClick(scope.row)"> {{ scope.row.number }}</div>
          <div v-else>
            <el-input v-model="scope.row.number"  type='number'  @click="handleClick(scope.row)"></el-input>
          </div>
        </template>
      </el-table-column>
      <el-table-column label="Score" sortable="custom" width="100px" align="center">
        <template slot-scope="scope">
          <div v-if="!scope.row.isEdit" @click="handleClick(scope.row)"> {{ scope.row.v_score }}</div>
          <div v-else>
            <el-input v-model="scope.row.v_score"  type='number'  @click="handleClick(scope.row)"></el-input>
          </div>
        </template>
      </el-table-column>
      <el-table-column v-if="showReviewer" label="Comments" width="200">
         <template slot-scope="scope">
          <div v-if="!scope.row.isEdit" @click="handleClick(scope.row)"> {{ scope.row.comment }}</div>
          <div v-else>
            <el-input v-model="scope.row.comment" @click="handleClick(scope.row)"></el-input>
          </div>
        </template>
      </el-table-column>

      <el-table-column label="Actions" align="center" width="350" class-name="small-padding fixed-width">
        <template slot-scope="{row}">
          <el-button type="primary" size="mini" @click="handleSubmit(row)">
            Submit
          </el-button>
          <el-button type="warning" size="mini" @click="handleCancle(row)">
            Cancle
          </el-button>
          <el-button type="info" size="mini" @click="handleUpdate(row)">
            Edit in Dialog
          </el-button>
          <el-button v-if="row.status!='deleted'" size="mini" type="danger" @click="confirmDelete(row.id)">
            Delete
          </el-button>
        </template>
      </el-table-column>
    </el-table>
    <div class="test">
      <el-button @click="test_add_only_name()">Add Vol with name</el-button>
    </div>
    <pagination v-show="total>0" :total="total" :page.sync="listQuery.page" :limit.sync="listQuery.limit" @pagination="getList" />

    <el-dialog :title="textMap[dialogStatus]" :visible.sync="dialogFormVisible">
      <el-form ref="dataForm" :rules="rules" :model="temp" label-position="left" label-width="80px" style="width: 400px; margin-left:50px;">
        <el-form-item label="Name" prop="name" required>
          <el-input v-model="temp.name" />
        </el-form-item>
        <el-form-item label="Number" prop="number" required>
          <el-input v-model="temp.number" />
        </el-form-item>
        <el-form-item label="Score" prop="v_score" required>
          <el-input  type="number" v-model="temp.v_score" />
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
import {getScore, getAllScores, addScore, updateScore, deleteScore, test_addScore} from '@/api/vol'
import waves from '@/directive/waves' // waves directive
import { parseTime } from '@/utils'
import Pagination from '@/components/Pagination' // secondary package based on el-pagination



// // arr to obj, such as { CN : "China", US : "USA" }
// const calendarTypeKeyValue = calendarTypeOptions.reduce((acc, cur) => {
//   acc[cur.key] = cur.display_name
//   return acc
// }, {})

export default {
  name: 'PitchTable',
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
        name: undefined,
      },
      showReviewer: true,

      temp: {
        id: undefined,
        name: 'None',
        number: 0,
        v_score: 0,
        time: 0,
        comment: ''
      },

      // Edit dialog configuration
      dialogFormVisible: false,
      dialogStatus: '',
      textMap: {
        update: 'Edit',
        create: 'Create'
      },

      rules: {
        name: [{ required: true, message: 'name is required', trigger: 'blur' }],
        number: [{  required: true, message: 'number is required and should be a number', trigger: 'blur' }],
        time: [{  required: true, message: 'time is required and should be a number', trigger: 'blur' }],
        v_score: [{ required: true, message: 'score is required  and should be a number', trigger: 'blur' }]
      },
      downloadLoading: false
    }
  },
  created() {
    this.getList()
  },
  methods: {
    // Implmement edit in the table
    handleClick(row) {
      // 动态设置数据并通过这个数据判断显示方式
      if (row.isEdit) {
        this.$delete(row, 'isEdit')
      } else {
        this.$confirm('Note! You can only modify one row at a time, not multiple rows of data!', 'Warning', {
          confirmButtonText: 'Confirm',
          cancelButtonText: 'Cancle',
          type: 'warning'
        }).then(()=>{
          this.$set(row, 'isEdit', true);
        })
      }
    },
    handleSubmit(row) {
      this.$delete(row, 'isEdit')
      this.inlineUpdateData(row)
    },
    handleCancle(row) {
      this.getList()
    },

    getList() {
      this.listLoading = true
      getAllScores(this.listQuery).then(response => {
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
      if (this.listQuery.name != undefined && this.listQuery.name != "" ) {
        for (var i = 0; i < this.list.length; i++) {
          if (this.list[i].name == this.listQuery.name) {
            new_array.push(this.list[i])
          }
        }
        this.list = new_array
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
      console.log(prop, order)
      this.tmp_list = this.list
      this.list.sort(this.compare("v_score"));
      console.log(this.list)
    },

    resetTemp() {
      this.temp = {
        id: undefined,
        name: 'None',
        number: 0,
        v_score: 0,
        time: 0,
        comment: ''
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
          this.temp.number = parseInt(this.temp.number)
          this.temp.time = parseInt(this.temp.time)
          this.temp.v_score = parseInt(this.temp.v_score)
          console.log('ADD SCORE FORM: ', this.temp)
          addScore(this.temp).then(response => {
            // Just to simulate the time of the request
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
          tempData.number = parseInt(tempData.number)
          tempData.time = parseInt(tempData.time)
          tempData.v_score = parseInt(tempData.v_score)
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
    inlineUpdateData(row) {
      const tempData = Object.assign({}, row)
      tempData.number = parseInt(tempData.number)
      tempData.time = parseInt(tempData.time)
      tempData.v_score = parseInt(tempData.v_score)
      console.log('TEMPDATA:', tempData)
      updateScore(tempData).then(() => {
        this.confirmLoading = true
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
        this.$notify({
          title: 'Failed to update',
          message: 'Update Failed' + err,
          type: 'warning',
          duration: 2000
        })
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
        const tHeader = ['ID', 'name', 'number', 'Score', 'Comments']
        const filterVal = ['id', 'name', 'number', 'v_score', 'comment']
        const data = this.formatJson(filterVal)
        excel.export_json_to_excel({
          header: tHeader,
          data,
          filename: 'volant-volant-table'
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

    test_add_only_name() {
      const request_body = {
        name: 'Haonan'
      }
      test_addScore(request_body).then(response => {
        // Just to simulate the time of the request
        this.$message({
          message: 'TEST, ADD ' + response.data.name + "'s Score Successfully!",
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
    }
  }
}
</script>



<style scoped>
.note {
  display: flex;
  flex-direction: column;
  justify-content: start;
}
.note-txt {
  font-weight: bold;
  color:rgb(226, 134, 13);
  font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
  font-size: 14px;
  margin: 0.2vw;
  display: flex;
  justify-content: flex-start;
}
</style>