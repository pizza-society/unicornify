module.exports = {
	root: true,
	env: {
		node: true
	},
	extends: [
		'eslint:recommended',
		'plugin:vue/vue3-recommended',
		'@vue/typescript/recommended'
	],
	parserOptions: {
		ecmaVersion: 2020
	},
	rules: {
		'no-console': process.env.NODE_ENV === 'production' ? 'warn' : 'off',
		'no-debugger': process.env.NODE_ENV === 'production' ? 'warn' : 'off',
		'comma-dangle': ['error', 'never'],
		'indent': ['error', 'tab'],
		'object-curly-spacing': ['error', 'always'],
		'padded-blocks': [
			'error', { 'blocks': 'never' }
		],
		'quotes': ['error', 'single'],
		'semi': ['error', 'never'],
		'template-curly-spacing': ['error', 'always'],
		'vue/block-spacing': [
			'error', 'never'
		],
		'vue/html-closing-bracket-newline': ['error', {
			'singleline': 'never',
			'multiline': 'never'
		}],
		'vue/html-indent': ['error', 'tab'],
		'vue/html-self-closing': ['error', {
			'html': {
				'void': 'always',
				'normal': 'never',
				'component': 'always'
			}
		}],
		'vue/object-curly-spacing': ['error', 'always'],
		'vue/padding-line-between-blocks': ['error', 'always'],
		'vue/template-curly-spacing': ['error', 'always']
	},
	overrides: [
		{
			files: [
				'**/__tests__/*.{j,t}s?(x)',
				'**/tests/unit/**/*.spec.{j,t}s?(x)'
			],
			env: {
				jest: true
			}
		}
	]
}
