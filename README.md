# django_vue_template

> A Vue.js project

## Structure of Django
```
|--+django_vue_template (django root)
|  |---setting.py
|  |---wsgi.py
|  |---// more //
|  +-------------
|
|--+django app
|  |
|  |--models.py
|  |--views.py
|  |--// more //
|  +------------
|
|  // run vue-init in server root //
|  // you will have vue root folder here //
|--+vue root
|  |
|  |--package.json
|  |--index.html
|  |--src folder
|  |--static folder
|  |--// more //
|  +------------
|
|---manage.py
|---// more //

```

## Build Setup

``` bash
# install dependencies
npm install

# serve with hot reload at localhost:8080
npm run dev

# build for production with minification
npm run build

# build for production and view the bundle analyzer report
npm run build --report

# run unit tests
npm run unit

# run e2e tests
npm run e2e

# run all tests
npm test
```

For a detailed explanation on how things work, check out the [guide](http://vuejs-templates.github.io/webpack/) and [docs for vue-loader](http://vuejs.github.io/vue-loader).
