# Club Chinois Admin

[![TeamCity CodeBetter](https://img.shields.io/teamcity/codebetter/bt428.svg)![npm](https://img.shields.io/npm/dw/localeval.svg)]() [![npm](https://img.shields.io/npm/v/npm.svg)]() [![Chrome Web Store](https://img.shields.io/chrome-web-store/stars/nimelepbpejjlbmoobocpfnjhihnpked.svg)]()

This project is the administration of Club Chinois

## Features 特性

- **👍vue-cli脚手架👍**（脚手架助你安装/卸载组件更方便）
- **👉多TAB导航**
- 面包屑导航
- `登录/注销`
- `权限验证`
- 404错误页面
- **表格数据直接导出xlsx**

## Preview 效果图

### 主界面

![image-20210520233813212](https://cdn.jsdelivr.net/gh/LonelVino/CDN@1.4.5/ClubChinois/club-chinois-admin-dashboard.png)

### 登录界面

![image-20210521001400722](https://cdn.jsdelivr.net/gh/LonelVino/CDN@1.4.5/ClubChinois/club-chinois-admin-login.png)

## Structure of The projects

```
.
├── API.md
├── build
├── config
├── dist
├── django_api
│   ├── admin.py
│   ├── ane
│   │   ├── admin.py
│   │   ├── apps.py
│   │   ├── migrations
│   │   ├── models.py
│   │   ├── tests.py
│   │   ├── urls.py
│   │   └── views.py
│   ├── apps.py
│   ├── cas
│   │   (same with the structure of 'ane')
│   ├── __init__.py
│   ├── migrations
│   ├── models.py
│   ├── pitch
│   │   (same with the structure of 'ane')
│   ├── urls.py
│   ├── user
│   │   (same with the structure of 'ane')
│   ├── views.py
│   └── vol
│   │   (same with the structure of 'ane')
├── django_vue_template
│   ├── asgi.py
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── index.html
├── manage.py
├── package.json
├── package-lock.json
├── Procfile
├── README.md
├── requirements.txt
├── src
│   ├── api
│   │   ├── ane.js
│   │   ├── article.js
│   │   ├── axios.js
│   │  ............
│   ├── App.vue
│   ├── assets
│   │   ├── css
│   │   ├── imgs
│   │   └── svg
│   ├── components
│   │   ├── Breadcrumb
│   │   ├── ErrorLog
│   │   ├── GithubCorner
│   │   ├── Hamburger
│   │   ├── HeaderSearch
│   │   ..........
│   ├── directive
│   ├── icons
│   │   ├── index.js
│   │   ├── svg
│   ├── layout
│   │   ├── components
│   │   │   ├── Sidebar
│   │   │   └── TagsView
│   │   ├── index.vue
│   │   └── mixin
│   ├── main.js
│   ├── permission.js
│   ├── plugins
│   ├── router
│   ├── settings.js
│   ├── store
│   ├── styles
│   ├── utils
│   ├── vendor
│   └── views
│       ├── dashboard
│       ├── error-page
│       ├── icons
│       ├── login
│       ├── profile
│       ├── table
│       └── user-table
├── static
├── staticfiles
├── test
│   ├── e2e
│   └── unit
├── vue.config.js
```

### 登录界面

## Run 开发

```bash
    # clone the project
    git clone https://github.com/LonelVino/club-chinois-admin.git

    # enter the project directory
    cd club-chinois-admin
    
    # 安装依赖
    npm install
    //or 
    npm install --registry=https://registry.npm.taobao.org


    # 本地开发 开启服务
    npm run dev
```

## Build 发布

```bash
    # 发布测试环境 
    npm run build
```

Or:

```bash

# build for test environment
npm run build:stage

# build for production environment
npm run build:prod

```

## Unit Test

```bash

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

### Customize configuration

See [Configuration Reference](https://cli.vuejs.org/config/).

## TODO List

- 七牛上传 CDN
- `多环境发布`
- `Markdown 编辑器` - Article Part
- `动态侧边栏`（支持多级路由）(a little bit bugs to be fixed)

## License

MIT License

### Customize configuration

See [Configuration Reference](https://cli.vuejs.org/config/).


