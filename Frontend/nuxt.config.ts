// https://v3.nuxtjs.org/api/configuration/nuxt.config

export default defineNuxtConfig({

    srcDir: './src',
    css: [
        'ant-design-vue/dist/antd.css',
        '@/assets/customized.css',
    ],
    buildModules: [
        '@nuxtjs/google-fonts'
    ],
    googleFonts: {
        families: {
            Montserrat: true,
        }
    },

})
