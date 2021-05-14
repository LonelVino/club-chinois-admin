# Club Chinois API Documents

## 0.Introduction

###  0.1 Base path

```
https://world-week-test.herokuapp.com/django_api  生产环境
无  测试环境
无  Mock 服务
```

### 0.2调用说明

#### 0.2.1 请求

所有的请求方式（Method）均与动词相关：

- `GET`：获取资源
- `POST`：创建资源
- `PUT`：更新资源
- `PATCH`：更新资源的一个属性
- `DELETE`：删除资源
- `OPTIONS`：获取客户端能对资源做什么操作的信息

##### （1）参数传入方式

如无特别说明，`GET` 请求参数需要放到 Url Query String 中：

```awk
GET https://world-week-test.herokuapp.com/django_api/users?pagesize=20
```

`POST/PUT/PATCH` 请求参数建议使用 JSON 格式将参数放到请求体中：

```json
PUT https://world-week-test.herokuapp.com/django_api/users/1
Content-Type: application/json
{
  "id": 1,
  "category": {
    "game": "ane-rouge",
    "id": 1
  },
  "role": "admin",
  "name": "Williams",
  "telephone": '+33........',
  "score": 12,
  "email": 'williams@student-cs.fr',
  "loc": '4CE001'
}
```

#### 0.2.2 响应

成功响应中包含实体资源内容，如：

```json
[
  {
    "a": "xxx",
    "b": "xxx"
  },
  {
    "c": "xxx",
    "d": "xxx"
   }
]
```

### 0.3 错误

使用标准 HTTP 响应码（Status Code）来表示 API 请求。

通常，状态码：

- `2xx` 代表成功响应
- `4xx` 代表失败响应，并给出失败原因
- `5xx` 代表宠物商店服务端内部错误

## 状态码说明

| 状态码 | 描述                                                         |
| :----- | :----------------------------------------------------------- |
| 200    | 更新/获取资源成功                                            |
| 201    | 创建资源成功                                                 |
| 204    | 删除资源成功                                                 |
| 400    | 业务错误，具体参见下方业务错误代码                           |
| 401    | 认证失败，请返回 [认证](https://demo.doc.coding.io/#认证) 检查参数是否有误 |
| 403    | 无权限调用接口，如：未开通 API 功能                          |
| 404    | 资源不存在                                                   |
| 405    | 接口请求方式 `Method` 有误                                   |
| 422    | 请求参数校验失败                                             |
| 429    | 触达限流限制                                                 |
| 500    | 服务器应用发生了错误                                         |
| 502    | 服务器无法连接                                               |
| 503    | 服务器暂不可用                                               |
| 504    | 服务器连接超时                                               |

## 业务错误说明

状态码 `4xx` 的业务错误可通过编码来分别处理不同的处理逻辑，响应将通过 JSON 形式返回，其中包括业务错误码 `code` 和错误原因 `message`，例如：

```json
{
  "code": 3001,
  "type": "ERROR",
  "message": "用户名已被占用，请更改后重新提交"
}
```

业务错误码 `code` 说明如下：

- 状态码 400

| 错误码 | 描述                             |
| :----- | :------------------------------- |
| 3000   | 用户名或密码错误                 |
| 3001   | 用户名已被占用，请更改后重新提交 |

## API REFERENCE

### 1. User

#### 1.1 用户列表

> 列出所有用户的信息

```apl
GET {{BASE_URL}}/users?pagesize=20&page=1
```

##### (1) 请求 Request

**`Query`**

```apl
{
	"pagesize": 20,  \\ [int] 限制每页返回数量 （最大限制：100, 默认值：20;  
	"page": 1  \\ [int] 页码, 默认值：1;   
}
```

##### (2) 响应 Response

**成功示例** 

```json
状态码：200；  [Array]  数组形式返回所有用户信息
--------------------------------------------
[
  	{
      "id": 1,
      "role": "admin", //权限
      "name": "Williams", //姓名
      "isAne": 0, //是否玩过Ane0rouge
      "isVol": 0, //是否玩过volant
      "isPitch": 0, //是否玩过投壶
      "telephone": '+33........', //手机号
      "score": 12, //总得分
      "email": 'williams@student-cs.fr', //邮箱
      "loc": '4CE001'  //宿舍
  	},
    .......
]
```

**失败示例**

```json
状态码：2003, 参数有误; 
-----------------------
{
	'code': 2003,
	'type': "ERROR",
	"message": 'pagesize 必须大于 0'
}
```

#### 1.2 新增用户

```apl
POST {{BASE_URL}}/users
```

##### (1) 请求 Request

**`Body`**

```json
{
    "name": "Williams",  // 姓名
    "telephone": '+33........', // 电话号码
    "email": 'williams@student-cs.fr',  //邮箱地址
    "loc": '4CE001'  // 住宿地址
}
```

##### (2) 响应 Response

**成功示例**

```json
创建成功
--------------------------------
{
  "id": 1,
  "role": "admin", //权限
  "name": "Williams", //姓名
  "isAne": 0, //是否玩过Ane0rouge
  "isVol": 0, //是否玩过volant
  "isPitch": 0, //是否玩过投壶
  "telephone": '+33........', //手机号
  "score": 12, //总得分
  "email": 'williams@student-cs.fr', //邮箱
  "loc": '4CE001'  //宿舍
},
```

**失败示例**

```json
输入参数有误
------------------------
{
    "code": 2000,
    "type": "ERROR".
    "message": 'name 必填'
}
```

#### 1.3 用户信息

#### 1.3.1 根据用户ID获取

>  获取指定ID的用户详情

```apl
GET {{BASE_URL}/users/{userId}
```

##### (1) 请求 Request

**`HEADER`**

-----

`Accept`  [string]     返回数据媒体类型

- 可选值： `apllication/json`, `application/xml`
- 默认值： `apllication/json`,  `string`

`路由参数`

-------

`userId` [int]   用户 ID

##### （2）响应 Response

**成功示例**

```apl
详状态码：200； 用户详情成功返回
----------------------
{
  "id": 1,
  "role": "admin", //权限
  "name": "Williams", //姓名
  "isAne": 0, //是否玩过Ane0rouge
  "isVol": 0, //是否玩过volant
  "isPitch": 0, //是否玩过投壶
  "telephone": '+33........', //手机号
  "score": 12, //总得分
  "email": 'williams@student-cs.fr', //邮箱
  "loc": '4CE001'  //宿舍
},
```

**失败示例**

```json
状态码：400；输入参数有误
------------------------
{
    "code": 400,
    "type": "ERROR".
    "message": 'ID用户不存在'
}
```

#### 1.3.2 根据用户姓名查找信息

>  获取指定姓名的用户详情

```apl
GET {{BASE_URL}/users/{username}
```

##### (1) 请求 Request

**`HEADER`**

-------------

`路由参数`

-------

s`username` [string]   用户姓名

##### （2）响应 Response

**成功示例**

```apl
详状态码：200； 用户详情成功返回
----------------------
{
  "id": 1,
  "role": "admin", //权限
  "name": "Williams", //姓名
  "isAne": 0, //是否玩过Ane0rouge
  "isVol": 0, //是否玩过volant
  "isPitch": 0, //是否玩过投壶
  "telephone": '+33........', //手机号
  "score": 12, //总得分
  "email": 'williams@student-cs.fr', //邮箱
  "loc": '4CE001'  //宿舍
},
```

**失败示例**

```json
状态码：400；输入参数有误
------------------------
{
    "code": 400,
    "type": "ERROR".
    "message": '用户名 用户不存在'
}
```



#### 1.4 更新用户信息

```apl
PUT {{BASE_URL}}/users/{{userId}}
```

##### （1）请求Request

**`路由参数`**

-----

`userId`  [string]    用户ID

**`BODY`** 

```json
{
  "role": "admin", //权限
  "name": "Williams", //姓名
  "isAne": 0, //1：玩过Ane0rouge，0 otherwise
  "isVol": 0, //1：玩过volant，0 otherwise
  "isPitch": 0, //1:玩过投壶，0 otherwise
  "telephone": '+33........', //手机号
  "score": 12, //总得分
  "email": 'williams@student-cs.fr', //邮箱
  "loc": '4CE001'  //宿舍
}
```

##### （2）响应 Response

**成功示例**

```
状态码：200；更新成功
------------
用户信息
```

**失败示例**

```json
状态码：2001； 传入参数有误
--------------
{
    "code": 2001,
    "type": "ERROR",
    "message": "isVol 必须为 int"
}
```

#### 1.5 删除用户

```apl
DELETE /users/{userId}
```

##### (1)请求 Request

`路由参数`

------

`userId` [string]  用户ID

##### （2）响应 Response

**成功示例**

```json
状态码：200，删除成功
-------------------
{
	"code":0,
	"type":"SUCCESS",
	"message":""
}
```

**失败示例** 

```json
状态码：400，删除失败
```

### 2.Ane得分情况

#### 2.1 用户得分列表

```
GET {{BASE_URL}}/scores?isFini=0
```

##### （1）请求 Reqiest

**`Query`** 

```json
{
    'isFini': 0, // 0: 返回未完成的所有用户，1：返回已完成，2：返回所有
}
```

##### （2）响应 Response

```json
状态码：200，请求成功
---------------------
{
	比赛信息
}
```

```
状态码：2004， 参数有误
----------------------
{
	"code": 2004,
	"type": "ERROR",
	"message": "isFini 不存在，必须为 0 & 1 & 2"
}
```



#### 2.2新建用户得分

```
POST {{BASE_URL}}/scores
```

##### （1）请求 Request

```json
{
	"userId": 1, // 用户ID
	"isFini": 0, // 0: 未完成游戏，1：已完成游戏
	"time": 25, // 完成游戏所用时间，单位：秒；若未完成，则为0
}
```

##### （2）响应 Response

```json
状态码：200，新建成功
------------------
{
	"id"：1, //得分id,
	"userId": 1, //用户ID，
	"isFini": 1, // 0: 未完成游戏，1：已完成游戏
    "time": 25, // 完成游戏所用时间，单位：秒；若未完成，则为0
    "create_time": 2021-5-20，
    "update_time": 2021-5-20,
    "delete_time": null
}
```

### 2.3 查询某一用户得分

```apl
GET {{BASE_URL}}/scores/{userId}
```

##### (1)请求 Request

**`路由参数`**

----------

`userId`   [int]    用户ID

##### （2）响应 Response

```json
状态码：200， 成功查询并且返回
--------------------------------
{
	"id"：1, //得分id,
	"userId": 1, //用户ID，
	"isFini": 1, // 0: 未完成游戏，1：已完成游戏
    "time": 25, // 完成游戏所用时间，单位：秒；若未完成，则为0
    "create_time": 2021-5-20，
    "update_time": 2021-5-20,
    "delete_time": null
}
```

#### 2.4 更新得分信息

```apl
PUT {{BASE_URL}}/scores/{{scoreId}}
```

##### （1）请求Request

**`路由参数`**

-----

`scoreId`  [string]    得分ID

**`BODY`** 

```json
{
    "id"：1, //得分id,
    "userId": 1, //用户ID，
    "isFini": 1, // 0: 未完成游戏，1：已完成游戏
    "time": 25, // 完成游戏所用时间，单位：秒；若未完成，则为0
    "create_time": 2021-5-20，
    "update_time": 2021-5-20,
    "delete_time": null
}
```

##### （2）响应 Response

**成功示例**

```
状态码：200；更新成功
------------
用户信息
```

**失败示例**

```json
状态码：2001； 传入参数有误
--------------
{
    "code": 2001,
    "type": "ERROR",
    "message": "isVol 必须为 int"
}
```

#### 2.5 删除得分情况

```apl
DELETE /scores/{scoreId}
```

##### (1)请求 Request

`路由参数`

------

`scoreId` [string]  得分ID

##### （2）响应 Response

**成功示例**

```json
状态码：200，删除成功
-------------------
{
	"code":0,
	"type":"SUCCESS",
	"message":""
}
```

**失败示例** 

```json
状态码：400，删除失败
```

### 3.Volant得分情况

### 4.Pitch得分情况

### 5.会话

#### 5.1 登录

```apl
POST {{BASE_URL}/login}
```

##### (1)请求 Request

```
{
	'username':"coding",
	"password": "123456",
	"remember_me": true
}
```

##### (2)响应 Response

```json

```

### 5.2 注册

```apl
POST {{BASE_URL}}/register
```

```

```

### 5.3登出

```apl
GET {{BASE_URL}}/logout
```

