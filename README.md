# Club Chinois Admin

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


## Getting started
```
# clone the project
git clone https://github.com/LonelVino/world-week.git

# enter the project directory
cd world-week

# install dependency
npm install

# develop
npm run dev
```

## Build Setup

``` bash

# build for test environment
npm run build:stage

# build for production environment
npm run build:prod

# run unit tests
npm run unit

# run e2e tests
npm run e2e

# run all tests
npm test
```

## Advanced
```bash
# preview the release environment effect
npm run preview

# preview the release environment effect + static resource analysis
npm run preview -- --report

# code format check
npm run lint

# code format check and auto fix
npm run lint -- --fix
```

For a detailed explanation on how things work, check out the [guide](http://vuejs-templates.github.io/webpack/) and [docs for vue-loader](http://vuejs.github.io/vue-loader).
