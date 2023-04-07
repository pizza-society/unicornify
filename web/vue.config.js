const { defineConfig } = require('@vue/cli-service')
module.exports = defineConfig({
	transpileDependencies: true,
	lintOnSave: false,
	chainWebpack: config => {
		config.module
			.rule('vue')
			.use('vue-loader')
			.tap(options => ({
				...options,
				compilerOptions: {
					// treat any tag that starts with lottie- as custom elements
					isCustomElement: tag => tag.startsWith('lottie-')
				}
			}))
	}
})
