#!/usr/bin/python

from subprocess import call
from os.path import isfile, isdir
from os import remove
from shutil import rmtree
from json import load, dumps

if isdir('.git'):
    rmtree('.git')

call(['npm', 'init'])
if not isfile('package.json'):
    exit()

with open('package.json', 'r') as f:
    data = load(f)
    data['scripts'] = {
        'build': 'webpack -p --config webpack.config.babel.js',
        'watch': 'webpack-dev-server --hot --inline --config webpack.config.babel.js'
    }

with open('package.json', 'w') as f:
    f.write(dumps(data))

call(['npm', 'install', '--save-dev'] + [
    'autoprefixer',
    'babel-core',
    'babel-loader',
    'babel-plugin-transform-object-rest-spread',
    'babel-plugin-transform-runtime',
    'babel-preset-es2015',
    'babel-preset-es2017',
    'css-loader',
    'cssnano',
    'extract-text-webpack-plugin',
    'file-loader',
    'html-loader',
    'html-webpack-plugin',
    'less',
    'less-loader',
    'optimize-css-assets-webpack-plugin',
    'postcss',
    'postcss-loader',
    'style-loader',
    'url-loader',
    'webpack',
    'webpack-dev-server'
])

remove('README.md')
remove(__file__)
