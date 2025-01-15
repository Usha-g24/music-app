const webpack = require('webpack');

module.exports = {
  mode: 'development', // or 'production'
  plugins: [
    new webpack.DefinePlugin({
      'process.env.NODE_ENV': JSON.stringify('development'),
    }),
  ],
  // other configurations...
};
