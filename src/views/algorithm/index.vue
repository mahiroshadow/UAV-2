<template>
	<div class="w-full h-full flex">
		<video ref="videoRef" class="object-fill h-full w-2/3 mt-4" autoplay controls muted preload="auto"></video>
		<div class="w-1/3 h-full p-4">
			<ElCard>
				<template #header>
					<div class="text-lg">
						<span>参数设置</span>
					</div>
				</template>
				<div class="p-2">
					<ElForm :model="form" label-width="auto" style="max-width: 600px">
						<ElFormItem label="算法选择">
							<ElSelect v-model="form.region" placeholder="请选择目标算法">
								<ElOption label="目标检测" value="shanghai" />
								<ElOption label="密度估计" value="beijing" />
							</ElSelect>
						</ElFormItem>
						<ElFormItem label="推流帧率">
							<ElInput v-model="form.fps" disabled />
						</ElFormItem>
						<ElFormItem label="推流设备">
							<ElSelect v-model="form.device" placeholder="请选择设备">
								<ElOption label="GPU" value="shanghai" />
								<ElOption label="CPU" value="beijing" />
							</ElSelect>
						</ElFormItem>
					</ElForm>
				</div>
			</ElCard>
			<ElCard class="mt-2">
				<template #header>
					<div class="text-lg flex justify-between align-middle">
						<div>视频列表</div>
						<div>自动播放<ElSwitch v-model="isAuto"></ElSwitch></div>
					</div>
				</template>
				<ul class="list-none min-h-80 w-full text-lg p-0 overflow-y-auto">
					<li
						v-for="(video, index) in videoList"
						@click="choose(index)"
						class="mt-4 w-full flex justify-around items-center cursor-pointer rounded-md"
						:style="
							selected == index
								? {
										backgroundColor: '#DCDCDC',
										transition: 'background-color .5s ease-out'
								  }
								: { backgroundColor: 'white', transition: 'background-color .5s ease-out' }
						"
					>
						<span>{{ video.name }}</span>
						<span>{{ video.time }}</span>
					</li>
				</ul>
			</ElCard>
		</div>
	</div>
</template>

<script setup lang="ts">
import mpegts from 'mpegts.js'
import { createVideo, destroyVideo } from './utils/video'
import { videoChange } from '@/api/algorithm'
import { onMounted, ref } from 'vue'
import { AlgorithmForm, type VideoList } from './utils/interface'
import { ElForm, ElFormItem, ElSelect, ElOption, ElInput, ElCard, ElSwitch } from 'element-plus'

const videoList = ref<VideoList[]>([
	{ name: '南大街前半段', pth: 'model/test.mp4', time: '01:10', uid: 'home' },
	{ name: '南大街后半段', pth: 'model/test1.mp4', time: '01:14', uid: 'home1' }
])
const selected = ref<number>(0)
const isAuto = ref<boolean>(true)
const form = ref<AlgorithmForm>({
	name: '',
	region: '',
	device: '',
	fps: 45
})
const videoRef = ref<HTMLVideoElement | null>()
const flvPlayer = ref<ReturnType<typeof mpegts.createPlayer> | null>()
const choose = (idx: number) => {
	selected.value = idx
	const { pth, uid } = videoList.value[idx]
	const data = { pth, device: 'cuda:0', uid }
	videoChange(data)
	if (flvPlayer.value) {
		console.log('销毁')
		destroyVideo(flvPlayer.value)
	}
	flvPlayer.value = createVideo(videoRef.value!, `http://121.43.36.206:6003/live?port=1936&app=live&stream=${videoList.value[idx].uid}`)
}

onMounted(() => {})
</script>

<style lang="scss" scoped></style>
