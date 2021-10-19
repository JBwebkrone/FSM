var path = require('path');
var webpack = require('webpack');
var BundleTracker = require('webpack-bundle-tracker');

module.exports = {
    context: __dirname,
    mode: "development",
    entry: './fsm_app/static/js/index.js',
    output: {
        path: path.resolve('./fsm_app/static/webpack_bundles/'),
        filename: "[name]-[hash].js",
    },
    plugins: [
        new BundleTracker({filename: './webpack-stats.js'})
    ]
};