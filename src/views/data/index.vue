<template>
	<div class="w-full flex justify-center">
		<div class="w-11/12">
			<div class="mt-2 flex justify-between">
				<div>
					<ElButton type="primary">文件上传</ElButton>
					<ElButton type="danger">批量删除</ElButton>
				</div>
				<div>
					<ElInput class="w-60 mr-2" v-model="videoName" size="large" placeholder="请输入视频名称" :suffix-icon="Search"></ElInput>
					<ElButton>搜索</ElButton>
				</div>
			</div>
			<ElTable :data="tableData" height="400" class="mt-4 w-full" key="videoTable">
				<ElTableColumn type="selection" width="55" />
				<ElTableColumn prop="date" label="视频名称" width="180" align="center" />
				<ElTableColumn prop="name" label="上传时间" width="180" align="center" />
				<ElTableColumn prop="address" label="清晰度" align="center" />
				<ElTableColumn prop="address" label="视频大小" align="center" />
				<ElTableColumn label="操作" align="center">
					<template #default>
						<ElButton type="danger" size="small">删除</ElButton>
						<ElButton type="primary" size="small">查看详情</ElButton>
					</template>
				</ElTableColumn>
			</ElTable>
			<ElPagination class="mt-2 float-right" background layout="prev, pager, next" :total="1000" />
		</div>
	</div>
</template>

<script setup lang="ts">
import { ref, onMounted } from 'vue'
import { ElTable, ElTableColumn, ElButton, ElInput, ElPagination } from 'element-plus'
import { Search } from '@element-plus/icons-vue'
const videoName = ref<string>()

const tableData = ref<any[]>([
	{
		date: '2016-05-03',
		name: 'Tom',
		address: 'No. 189, Grove St, Los Angeles'
	},
	{
		date: '2016-05-02',
		name: 'Tom',
		address: 'No. 189, Grove St, Los Angeles'
	},
	{
		date: '2016-05-04',
		name: 'Tom',
		address: 'No. 189, Grove St, Los Angeles'
	},
	{
		date: '2016-05-01',
		name: 'Tom',
		address: 'No. 189, Grove St, Los Angeles'
	},
	{
		date: '2016-05-08',
		name: 'Tom',
		address: 'No. 189, Grove St, Los Angeles'
	},
	{
		date: '2016-05-06',
		name: 'Tom',
		address: 'No. 189, Grove St, Los Angeles'
	},
	{
		date: '2016-05-07',
		name: 'Tom',
		address: 'No. 189, Grove St, Los Angeles'
	}
])

onMounted(() => {
	window.addEventListener('resize', event => {
		console.log(window.innerHeight)
	})
})
</script>

<style lang="scss" scoped></style>
