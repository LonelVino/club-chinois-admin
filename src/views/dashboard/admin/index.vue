<template>
  <div class="dashboard-editor-container">
    <github-corner class="github-corner" />
      <el-row gutter="32">
        <el-col :xs="24" :sm="24" :lg="12">
          <TodoList/>
        </el-col>
      </el-row>


      <el-row style="background:#fff;padding:16px 16px 0;margin-bottom:32px; margin-top: 2vw;">
        <line-chart :chart-data="lineChartData" />
      </el-row>

      <el-row :gutter="32">
        <el-col :xs="24" :sm="24" :lg="8">
          <div class="chart-wrapper">
            <raddar-chart />
          </div>
        </el-col>
        <el-col :xs="24" :sm="24" :lg="8">
          <div class="chart-wrapper">
            <pie-chart />
          </div>
        </el-col>
        <el-col :xs="24" :sm="24" :lg="8">
          <div class="chart-wrapper">
            <bar-chart />
          </div>
        </el-col>
      </el-row>
    </div>
  
  </div>
</template>

<script>
import GithubCorner from '@/components/GithubCorner'
import LineChart from './components/LineChart'
import RaddarChart from './components/RaddarChart'
import PieChart from './components/PieChart'
import BarChart from './components/BarChart'
import TodoList from './components/TodoList'
import BoxCard from './components/BoxCard'

import waves from '@/directive/waves' // waves directive

import axios from 'axios'

import introJs from 'intro.js'
import 'intro.js/introjs.css'

var lineChartData = {
  newVisitis: {
    expectedData: [100, 120, 161, 134, 105, 160, 165],
    actualData: [120, 82, 91, 154, 162, 140, 145]
  },
  messages: {
    expectedData: [200, 192, 120, 144, 160, 130, 140],
    actualData: [180, 160, 151, 106, 145, 150, 130]
  },
  purchases: {
    expectedData: [80, 100, 121, 104, 105, 90, 100],
    actualData: [120, 90, 100, 138, 142, 130, 130]
  },
  shoppings: {
    expectedData: [130, 140, 141, 142, 145, 150, 160],
    actualData: [120, 82, 91, 154, 162, 140, 130]
  }
}

export default {
  name: 'DashboardAdmin',
  components: {
    GithubCorner,
    LineChart,
    RaddarChart,
    PieChart,
    BarChart,
    TodoList,
    BoxCard
  },
  data() {
    return {
      fileList: [],
      lineChartData: lineChartData.newVisitis,
      hasResult: false,
      resultLoading: false,

      downloadLoading: false,

      progressNum: 0,
      startTimer: '',
      endTimer: ''
    }
  },
  props: {
    progressStatus: {
      type: Boolean,
      default() {
        return false
      }
    }
  },
  watch: {
    progressNum: function () {
      if (this.progressNum == 99) {
        this.endProgress()
      }
    }
  },
  computed: {
    listLoading() {return false},
  },
  mounted() {
    this.guide()
  },
  methods: {
    guide() {
        introJs()
        .setOptions({
            nextLabel: 'Next',  // 下一个按钮文字
            prevLabel: 'Previous',  // 上一个按钮文字
            skipLabel: 'Skip',    // 跳过按钮文字
            doneLabel: 'Start',// 完成按钮文字
            hidePrev: true,       // 在第一步中是否隐藏上一个按钮
            hideNext: true,       // 在最后一步中是否隐藏下一个按钮
            exitOnOverlayClick: false,  // 点击叠加层时是否退出介绍
            showStepNumbers: false,     // 是否显示红色圆圈的步骤编号
            disableInteraction: true,   // 是否禁用与突出显示的框内的元素的交互，就是禁止点击
            showBullets: false          // 是否显示面板指示点
        }).start()
    },

    DonwloadFile() {
      axios({
        url: 'https://people.sc.fsu.edu/~jburkardt/data/csv/addresses.csv',
        method: 'GET',
        responseType: 'blob',
    }).then((response) => {
        var fileURL = window.URL.createObjectURL(new Blob([response.data]));
        var fileLink = document.createElement('a');

        fileLink.href = fileURL;
        fileLink.setAttribute('download', 'file.pdf');
        document.body.appendChild(fileLink);

        fileLink.click();
    });
    },

    handleDownload() {
      this.downloadLoading = true
      import('@/vendor/Export2Excel').then(excel => {
        const tHeader = ['ID', 'MAC CODE', 'Pitch Angle', 'Rotor Speed', 'Hub Temperature', 'TARGET']
        const filterVal = ['id', 'mac_code', 'pch_ang', 'rrt_v', 'hub_t', 'target']
        const data = this.formatJson(filterVal)
        excel.export_json_to_excel({
          header: tHeader,
          data,
          filename: 'PredictResult'
        })
        this.downloadLoading = false
      })
    },

    Predict() {
      this.startProgress()
    },
    StopPredict() {
      console.log(this.progressNum)
    },
    startProgress () {
      this.startTimer = setInterval(() => {
        this.progressNum ++
        if (this.progressNum > 98) {
            clearInterval(this.startTimer)
        }
      }, 100); 
    },
    endProgress () {
      clearInterval(this.startTimer)
      this.endTimer = setInterval(() => {
        this.progressNum ++
        if (this.progressNum > 99) {
          clearInterval(this.endTimer)
          this.finishProgress()
        }
      }, 10);
    },
    finishProgress () {
      this.hasResult = true
      console.log(this.hasResult)
      this.$emit('finishProgress', false)
    },

    submitUpload() {
      this.$refs.upload.submit();
      tmp_file = {name: 'csc.csv', url: 'http://abc.com'}
      fileList.push(tmp_file)
    },
    handleRemove(file, fileList) {
      tmp_file = {name: 'csc.csv', url: 'http://abc.com'}
      fileList.push(tmp_file)
    },
    handlePreview(file) {
      console.log(file);
    },

    handleSetLineChartData(type) {
      this.lineChartData = lineChartData[type]
    },

    formatJson(filterVal) {
      return this.table_list.map(v => filterVal.map(j => {
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

<style lang="scss" scoped>
.dashboard-editor-container {
  padding: 32px;
  background-color: rgb(240, 242, 245);
  position: relative;

  .github-corner {
    position: absolute;
    top: 0px;
    border: 0;
    right: 0;
  }

  .files {
    margin-bottom: 2vh;
    display: flex;
    flex-direction: row;
    justify-content: center;

    .download {
      display: flex;
      flex-direction: row;
    }

    .actions {
      display: flex;
      flex-direction: column;
      align-content: space-between;
      margin: 0 2vw;
      .buttons {
        margin: 2vw 0;
        .upload-btn {
          margin: 0 1vw;
          transform: scale(1.2);
        }
      }
      .btn-tip {
        font-weight: bold;
        font-family: 'Lucida Sans', 'Lucida Sans Regular', 'Lucida Grande', 'Lucida Sans Unicode', Geneva, Verdana, sans-serif;
        margin: 0 0.5vw;
      }
    }
  }

  .result {
    margin-top: 2vw;
    display: flex;
    flex-direction: column;
    justify-content:flex-start;
  }

  .chart-wrapper {
    background: #fff;
    padding: 16px 16px 0;
    margin-bottom: 32px;
  }
}

@media (max-width:1024px) {
  .chart-wrapper {
    padding: 8px;
  }
}
</style>
