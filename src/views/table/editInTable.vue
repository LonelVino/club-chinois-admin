<template>
    <div class="table">
        <el-button type="primary"
                 @click="submit()">提交修改</el-button>
        <el-table ref="multipleTable"
                :data="tableData"
                stripe
                @selection-change="handleSelectionChange">
        <el-table-column type="selection"
                        is-checked
                        width="60"
                        align="center" />
        <el-table-column type="index"
                        width="80"
                        label="序号"
                        align="center" />
        <el-table-column prop="name"
                        label="姓名"
                        align="center" />
        <el-table-column prop="address"
                        label="地址"
                        align="center">
            <template slot-scope="{row,$index}">
            <el-form v-show="showEdit[$index]"
                    :model="row">
                <el-form-item prop="address">
                <el-input v-model="row.address"
                            size="small"
                            name="value" />
                </el-form-item>
            </el-form>
            <span v-show="!showEdit[$index]">{{ row.address }}</span>
            </template>
        </el-table-column>
        <el-table-column label="操作"
                        align="center">
            <template slot-scope="{ row, $index }">
            <el-button v-if="!showBtn[$index]"
                        type="primary"
                        size="mini"
                        @click.native="handleEdit($index, row)">编辑</el-button>
            <el-button v-if="showBtn[$index]"
                        type="primary"
                        size="mini"
                        @click.native="handleCancel($index, row)">取消</el-button>
            </template>
        </el-table-column>
        </el-table>
    </div>
</template>



<script>
// 接口api
import Vue from "vue";
export default {
  data() {
    return {
      tableData: [
        {
          date: "2016-05-02",
          name: "王小虎",
          address: "上海市普陀区金沙江路 1518 弄",
        },
        {
          date: "2016-05-04",
          name: "王小虎",
          address: "上海市普陀区金沙江路 1517 弄",
        },
        {
          date: "2016-05-01",
          name: "王小虎",
          address: "上海市普陀区金沙江路 1519 弄",
        },
        {
          date: "2016-05-03",
          name: "王小虎",
          address: "上海市普陀区金沙江路 1516 弄",
        },
      ],
      multipleSelection: [],
      showEdit: [], // 显示编辑框
      showBtn: [], // 显示操作按钮
      submitData:[],
    };
  },

  methods: {
    // 获取选中行的这一条数据
    handleSelectionChange(val) {
      this.multipleSelection = val;
    },
    // 切换选中
    toggleSelection(rows) {
      if (rows) {
        rows.forEach((row) => {
      this.$refs.multipleTable.toggleRowSelection(row);
        });
      } else {
        this.$refs.multipleTable.clearSelection();
      }
    },

    // 点击编辑
    handleEdit(index, row) {
    // 先将要编辑的原始值赋值给新加的参数originalAddress ，便于编辑时数据还原
      row.originalAddress = row.address;
      this.$refs.multipleTable.toggleRowSelection(row);
      this.showEdit[index] = true;
      this.showBtn[index] = true;
      this.$set(this.showEdit, row, true);
      this.$set(this.showBtn, row, true);
    },

    // 取消编辑
    handleCancel(index, row) {
      row.address = row.originalAddress;
      this.$refs.multipleTable.toggleRowSelection(row);
      this.showEdit[index] = false;
      this.showBtn[index] = false;
      this.$set(this.showEdit, row, false);
      this.$set(this.showBtn, row, false);
    },

    // 从选中的行中取出修改的参数和值
    handleQuery(row) {
      this.multipleSelection.map((i, index) => {
        i.show = false;
        Vue.set(this.multipleSelection, index, i);
        this.submitData.push({
          address: this.multipleSelection[index].address,
        });
      });
      // 取出所有选中修改的参数后还原表格所有操作按钮的状态
      this.tableData.map((i, index) => {
        i.show = false;
        this.showEdit[index] = false;
        this.showBtn[index] = false;
        this.$set(this.showEdit, row, false);
        this.$set(this.showBtn, row, false);
      });
    },
    // 提交修改参数
    submit() {
      if (this.multipleSelection.length < 1) {
        this.$message({
          message: "请至少选择一条数据！",
          type: "warning",
          duration: 3 * 1000,
        });
      } else {
        this.handleQuery();
        console.log(this.submitData)
         // 清除所有选中
        this.$refs.multipleTable.clearSelection();
      }
    },
  },
};
</script>