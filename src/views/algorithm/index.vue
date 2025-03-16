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
				<ul class="list-none min-h-80">
					<li></li>
					<li></li>
					<li></li>
					<li></li>
					<li></li>
					<li></li>
				</ul>
			</ElCard>
		</div>
	</div>
</template>

<script setup lang="ts">
import { onMounted, ref } from 'vue'
import { createVideo } from './utils/video'
import { ElForm, ElFormItem, ElSelect, ElOption, ElInput, ElCard, ElSwitch } from 'element-plus'
import { AlgorithmForm } from './utils/interface'
const isAuto = ref<boolean>(true)
const videoRef = ref<HTMLVideoElement | null>()
const form = ref<AlgorithmForm>({
	name: '',
	region: '',
	device: '',
	fps: 45
})

onMounted(() => {
	// createVideo()
})
</script>

<style lang="scss" scoped></style>
