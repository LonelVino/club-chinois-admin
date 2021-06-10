<template>
  <div class="dashboard-editor-container">
    <github-corner class="github-corner" />
    <div class="files">
      <div class="upload">
        <el-upload
        class="upload-demo"
        drag
        action="https://jsonplaceholder.typicode.com/posts/"
        :on-preview="handlePreview"
        :on-remove="handleRemove"
        :file-list="fileList"
        :auto-upload="false"
        multiple>
        <i class="el-icon-upload"></i>
        <div class="el-upload__text">Drag Your file here or <em> Click to upload </em></div>
        <div class="el-upload__tip" slot="tip">Only CSV file is allowed.</div>
      </el-upload>
      </div>
      <div class="actions">
        <div class="buttons">
          <el-button class="upload-btn" type="primary" @click="Predict()">Predict</el-button>
          <el-button class="upload-btn" type="warning" @click="StopPredict()">Stop</el-button>
        </div>
        <div class="download">
        <el-card shadow="hover">
          <span>sample.csv</span>
          <el-button type='info' @click="DonwloadFile()">Download</el-button>
        </el-card>
      </div>
      </div>
    </div>

    <div class="result" v-if="hasResult">
      <el-table
        ref="multipleTable"
        :key="tableKey"
        v-loading="listLoading"
        :data="table_list"
        border
        fit
        highlight-current-row
        style="width: 100%;"
      >
      <el-table-column label="ID" align="center" width="80">
        <template slot-scope="{row}">
          <span>{{ row.id }}</span>
        </template>
      </el-table-column>
      <el-table-column label="MAC CODE" align="center" width="80">
        <template slot-scope="{row}">
          <span>{{ row.mac_code}}</span>
        </template>
      </el-table-column>
      <el-table-column label="Pitch Angle" align="center">
        <template slot-scope="{row}">
          <span>{{ row.pch_ang }} deg</span>
        </template>
      </el-table-column>
      <el-table-column label="Rotor Speed" align="center">
        <template slot-scope="{row}">
          <span>{{ row.rrt_v }} m/s</span>
        </template>
      </el-table-column>
      <el-table-column label="Hub Temperature" align="center">
        <template slot-scope="{row}">
          <span>{{ row.hub_t }} ºC</span>
        </template>
      </el-table-column>
      <el-table-column label="TARGET" align="center">
        <template slot-scope="{row}">
          <span>{{ row.target }}</span>
        </template>
      </el-table-column>
      </el-table>


      <el-row style="background:#fff;padding:16px 16px 0;margin-bottom:32px;">
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

import axios from 'axios'

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
var ex_list = [
  {id: 1, mac_code: 'WT1', pch_ang: 20.114552, rrt_v: 0, hub_t: 7.6, target: 3.006128},
  {id: 2, mac_code: 'WT3', pch_ang: 92.470001, rrt_v: 0, hub_t: 6.8, target: 3.049276},
  {id: 3, mac_code: 'WT2', pch_ang: -5.021552, rrt_v: 0, hub_t: 17.6, target: 1.026452},
  {id: 4, mac_code: 'WT4', pch_ang: 35.255156, rrt_v: 13.40, hub_t: 18.0, target: 7.611338},
  {id: 5, mac_code: 'WT2', pch_ang: 20.158423, rrt_v: 12.52, hub_t: 12.2, target: 31.61581},
  {id: 6, mac_code: 'WT1', pch_ang: 20.365158, rrt_v: 14.96, hub_t: 21.2, target: 26.32515},
  {id: 7, mac_code: 'WT3', pch_ang: 20.155845, rrt_v: 13.63, hub_t: 10.5, target: 6.354523}
]

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
      hasResult: false
    }
  },
  computed: {
    listLoading() {return false},
    table_list() {return ex_list},
  },
  methods: {
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

    Predict() {
      this.hasResult = true
      console.log(this.hasResult)
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
    }
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
    }
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
