const webpack = require("webpack");
const MiniCssExtractPlugin = require("mini-css-extract-plugin");
const CopyWebpackPlugin = require('copy-webpack-plugin');

module.exports = {
  entry: "./src/index.js",
  module: {
    rules: [
      {
        test: /\.(js|jsx)$/,
        exclude: /node_modules/,
        use: ["babel-loader"]
      },
      {
        test: /\.scss$/,
        use: [MiniCssExtractPlugin.loader, "css-loader", "sass-loader"]
      },
      {
        test: /\.(png|jpg|gif|svg)$/,
        use: [
          'file-loader',
          {
            loader: "image-webpack-loader",
            options: {},
          },
        ],
      }
    ]
  },
  resolve: {
    extensions: ["*", ".js", ".jsx"]
  },
  plugins: [
    new webpack.HotModuleReplacementPlugin(),
    new MiniCssExtractPlugin({filename: "[name].css"}),
    new CopyWebpackPlugin([{ from: './src/assets', to: './app-dist/assets' }])
  ],
  output: {
    path: __dirname + "/app-dist",
    publicPath: "/",
    filename: "bundle.js"
  },
  devServer: {
    contentBase: "./app-dist",
    hot: true
  }
};
