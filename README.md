# Club Chinois Admin

[![TeamCity CodeBetter](https://img.shields.io/teamcity/codebetter/bt428.svg)![npm](https://img.shields.io/npm/dw/localeval.svg)]() [![npm](https://img.shields.io/npm/v/npm.svg)]() [![Chrome Web Store](https://img.shields.io/chrome-web-store/stars/nimelepbpejjlbmoobocpfnjhihnpked.svg)]()

This project is the administration of Club Chinois

## Features ็นๆง

- **๐vue-cli่ๆๆถ๐**๏ผ่ๆๆถๅฉไฝ ๅฎ่ฃ/ๅธ่ฝฝ็ปไปถๆดๆนไพฟ๏ผ
- **๐ๅคTABๅฏผ่ช**
- ้ขๅๅฑๅฏผ่ช
- `็ปๅฝ/ๆณจ้`
- `ๆ้้ช่ฏ`
- 404้่ฏฏ้กต้ข
- **่กจๆ ผๆฐๆฎ็ดๆฅๅฏผๅบxlsx**

## Preview ๆๆๅพ

### ไธป็้ข

![image-20210520233813212](https://cdn.jsdelivr.net/gh/LonelVino/CDN@1.4.5/ClubChinois/club-chinois-admin-dashboard.png)

### ็ปๅฝ็้ข

![image-20210521001400722](https://cdn.jsdelivr.net/gh/LonelVino/CDN@1.4.5/ClubChinois/club-chinois-admin-login.png)

## Structure of The projects

```
.
โโโ API.md
โโโ build
โโโ config
โโโ dist
โโโ django_api
โย ย  โโโ admin.py
โย ย  โโโ app_1
โย ย  โย ย  โโโ admin.py
โย ย  โย ย  โโโ apps.py
โย ย  โย ย  โโโ migrations
โย ย  โย ย  โโโ models.py
โย ย  โย ย  โโโ tests.py
โย ย  โย ย  โโโ urls.py
โย ย  โย ย  โโโ views.py
โย ย  โโโ apps.py
โย ย  โโโ cas
โย ย  โย ย  (same with the structure of 'ane')
โย ย  โโโ __init__.py
โย ย  โโโ migrations
โย ย  โโโ models.py
โย ย  โโโ urls.py
โย ย  โโโ user
โย ย  โย ย  (same with the structure of 'ane')
โย ย  โโโ views.py
โย ย  โโโ app_3
โโโ django_vue_template
โย ย  โโโ asgi.py
โย ย  โโโ __init__.py
โย ย  โโโ settings.py
โย ย  โโโ urls.py
โย ย  โโโ wsgi.py
โโโ index.html
โโโ manage.py
โโโ package.json
โโโ package-lock.json
โโโ Procfile
โโโ README.md
โโโ requirements.txt
โโโ src
โย ย  โโโ api
โย ย  โย ย  โโโ material.js
โย ย  โย ย  โโโ article.js
โย ย  โย ย  โโโ axios.js
โย ย  โย ย ............
โย ย  โโโ App.vue
โย ย  โโโ assets
โย ย  โย ย  โโโ css
โย ย  โย ย  โโโ imgs
โย ย  โย ย  โโโ svg
โย ย  โโโ components
โย ย  โย ย  โโโ Breadcrumb
โย ย  โย ย  โโโ ErrorLog
โย ย  โย ย  โโโ GithubCorner
โย ย  โย ย  โโโ Hamburger
โย ย  โย ย  โโโ HeaderSearch
โย ย  โย ย  ..........
โย ย  โโโ directive
โย ย  โโโ icons
โย ย  โย ย  โโโ index.js
โย ย  โย ย  โโโ svg
โย ย  โโโ layout
โย ย  โย ย  โโโ components
โย ย  โย ย  โย ย  โโโ Sidebar
โย ย  โย ย  โย ย  โโโ TagsView
โย ย  โย ย  โโโ index.vue
โย ย  โย ย  โโโ mixin
โย ย  โโโ main.js
โย ย  โโโ permission.js
โย ย  โโโ plugins
โย ย  โโโ router
โย ย  โโโ settings.js
โย ย  โโโ store
โย ย  โโโ styles
โย ย  โโโ utils
โย ย  โโโ vendor
โย ย  โโโ views
โย ย      โโโ dashboard
โย ย      โโโ error-page
โย ย      โโโ icons
โย ย      โโโ login
โย ย      โโโ profile
โย ย      โโโ table
โย ย      โโโ user-table
โโโ static
โโโ staticfiles
โโโ test
โย ย  โโโ e2e
โย ย  โโโ unit
โโโ vue.config.js
```

### ็ปๅฝ็้ข

## Run ๅผๅ

```bash
    # clone the project
    git clone https://github.com/LonelVino/club-chinois-admin.git

    # enter the project directory
    cd club-chinois-admin
    
    # ๅฎ่ฃไพ่ต
    npm install
    //or 
    npm install --registry=https://registry.npm.taobao.org


    # ๆฌๅฐๅผๅ ๅผๅฏๆๅก
    npm run dev
```

## Build ๅๅธ

```bash
    # ๅๅธๆต่ฏ็ฏๅข 
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

- ไธ็ไธไผ  CDN
- `ๅค็ฏๅขๅๅธ`
- `Markdown ็ผ่พๅจ` - Article Part
- `ๅจๆไพง่พนๆ `๏ผๆฏๆๅค็บง่ทฏ็ฑ๏ผ(a little bit bugs to be fixed)

## License

MIT License

### Customize configuration

See [Configuration Reference](https://cli.vuejs.org/config/).


