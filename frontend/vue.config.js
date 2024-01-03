const { defineConfig } = require('@vue/cli-service')
module.exports = defineConfig({
  publicPath: '/static/dist/',
  outputDir: '/stock/static/dist',
  indexPath: '/stock/templates/base_vue.html',
  transpileDependencies: true,
  configureWebpack: {
    devServer: {
      devMiddleware: {
        writeToDisk: true
      }
    }
  }
});
