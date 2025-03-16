import request from '@/utils/request'
import { AxiosPromise } from 'axios'

// 我是懒狗之不想配置
const baseUrl: string = 'http://8.134.60.171:6001/nuist'

const videoChange = (data: any) => {
	return request({
		baseURL: baseUrl,
		method: 'POST',
		url: '/change',
		data: data
	})
}

export { videoChange }
