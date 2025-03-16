export interface AlgorithmForm {
	name: string
	region: string
	device: string
	fps: number
}

export type VideoList = Record<'name' | 'pth' | 'time' | 'uid', string>
