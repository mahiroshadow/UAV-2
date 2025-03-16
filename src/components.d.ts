// 全局组件类型声明
import TableComponent from '@/components/Table/index.vue'
import FormConfig from '@/components/FormConfig/index.vue'
import FormConfigDialog from '@/components/FormConfigDialog.vue'
import SearchForm from '@/components/SearchForm.vue'

declare module '@vue/runtime-core' {
	export interface GlobalComponents {
		LeTable: typeof TableComponent
		LeFormConfig: typeof FormConfig
		LeFormConfigDialog: typeof FormConfigDialog
		LeSearchForm: typeof SearchForm
	}
}
export {}
