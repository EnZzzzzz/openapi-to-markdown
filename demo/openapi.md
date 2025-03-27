---
title: 个人项目
language_tabs:
  - shell: Shell
  - http: HTTP
  - javascript: JavaScript
  - ruby: Ruby
  - python: Python
  - php: PHP
  - java: Java
  - go: Go
toc_footers: []
includes: []
search: true
code_clipboard: true
highlight_theme: darkula
headingLevel: 2
generator: "@tarslib/widdershins v4.0.29"

---

# 个人项目

Base URLs:

# Authentication

# Default

<a id="opIdroot__get"></a>

## GET Root

GET /

> 返回示例

> 200 Response

```json
"string"
```

### 返回结果

|状态码|状态码含义|说明|数据模型|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Successful Response|string|

<a id="opIdclassroom_classroom_post"></a>

## POST Classroom

POST /classroom

> Body 请求参数

```json
{
  "students": [
    {
      "name": "string",
      "age": 0,
      "course": "string"
    }
  ]
}
```

### 请求参数

|名称|位置|类型|必选|中文名|说明|
|---|---|---|---|---|---|
|body|body|[Classroom](#schemaclassroom)| 否 | Classroom|none|

> 返回示例

> 200 Response

```json
"string"
```

### 返回结果

|状态码|状态码含义|说明|数据模型|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Successful Response|string|
|422|[Unprocessable Entity](https://tools.ietf.org/html/rfc2518#section-10.3)|Validation Error|[HTTPValidationError](#schemahttpvalidationerror)|

# 数据模型

<h2 id="tocS_Pet">Pet</h2>

<a id="schemapet"></a>
<a id="schema_Pet"></a>
<a id="tocSpet"></a>
<a id="tocspet"></a>

```json
{
  "id": 1,
  "category": {
    "id": 1,
    "name": "string"
  },
  "name": "doggie",
  "photoUrls": [
    "string"
  ],
  "tags": [
    {
      "id": 1,
      "name": "string"
    }
  ],
  "status": "available"
}

```

### 属性

|名称|类型|必选|约束|中文名|说明|
|---|---|---|---|---|---|
|id|integer(int64)|true|none||宠物ID编号|
|category|[Category](#schemacategory)|true|none||分组|
|name|string|true|none||名称|
|photoUrls|[string]|true|none||照片URL|
|tags|[[Tag](#schematag)]|true|none||标签|
|status|string|true|none||宠物销售状态|

#### 枚举值

|属性|值|
|---|---|
|status|available|
|status|pending|
|status|sold|

<h2 id="tocS_Category">Category</h2>

<a id="schemacategory"></a>
<a id="schema_Category"></a>
<a id="tocScategory"></a>
<a id="tocscategory"></a>

```json
{
  "id": 1,
  "name": "string"
}

```

### 属性

|名称|类型|必选|约束|中文名|说明|
|---|---|---|---|---|---|
|id|integer(int64)|false|none||分组ID编号|
|name|string|false|none||分组名称|

<h2 id="tocS_Tag">Tag</h2>

<a id="schematag"></a>
<a id="schema_Tag"></a>
<a id="tocStag"></a>
<a id="tocstag"></a>

```json
{
  "id": 1,
  "name": "string"
}

```

### 属性

|名称|类型|必选|约束|中文名|说明|
|---|---|---|---|---|---|
|id|integer(int64)|false|none||标签ID编号|
|name|string|false|none||标签名称|

<h2 id="tocS_HTTPValidationError">HTTPValidationError</h2>

<a id="schemahttpvalidationerror"></a>
<a id="schema_HTTPValidationError"></a>
<a id="tocShttpvalidationerror"></a>
<a id="tocshttpvalidationerror"></a>

```json
{
  "detail": [
    {
      "loc": [
        "string"
      ],
      "msg": "string",
      "type": "string"
    }
  ]
}

```

HTTPValidationError

### 属性

|名称|类型|必选|约束|中文名|说明|
|---|---|---|---|---|---|
|detail|[[ValidationError](#schemavalidationerror)]|false|none|Detail|none|

<h2 id="tocS_Classroom">Classroom</h2>

<a id="schemaclassroom"></a>
<a id="schema_Classroom"></a>
<a id="tocSclassroom"></a>
<a id="tocsclassroom"></a>

```json
{
  "students": [
    {
      "name": "string",
      "age": 0,
      "course": "string"
    }
  ]
}

```

Classroom

### 属性

|名称|类型|必选|约束|中文名|说明|
|---|---|---|---|---|---|
|students|[[Student](#schemastudent)]|true|none|Students|none|

<h2 id="tocS_UserIn">UserIn</h2>

<a id="schemauserin"></a>
<a id="schema_UserIn"></a>
<a id="tocSuserin"></a>
<a id="tocsuserin"></a>

```json
{
  "channel": 0,
  "username": "string",
  "password": "string",
  "email": "string",
  "full_name": "string",
  "request_id": "string"
}

```

UserIn

### 属性

|名称|类型|必选|约束|中文名|说明|
|---|---|---|---|---|---|
|channel|integer|false|none|渠道|none|
|username|string|true|none|用户名|none|
|password|string|true|none|用户密码|长度6-8位|
|email|string|true|none|用户邮箱地址|none|
|full_name|string|false|none|用户全名|none|
|request_id|string(uuid4)|false|none|Request Id|none|

#### 枚举值

|属性|值|
|---|---|
|channel|0|
|channel|1|

<h2 id="tocS_Course">Course</h2>

<a id="schemacourse"></a>
<a id="schema_Course"></a>
<a id="tocScourse"></a>
<a id="tocscourse"></a>

```json
"string"

```

### 属性

|名称|类型|必选|约束|中文名|说明|
|---|---|---|---|---|---|
|*anonymous*|string|false|none||none|

<h2 id="tocS_UserOut">UserOut</h2>

<a id="schemauserout"></a>
<a id="schema_UserOut"></a>
<a id="tocSuserout"></a>
<a id="tocsuserout"></a>

```json
{
  "username": "string",
  "email": "string",
  "full_name": "string",
  "request_id": "string"
}

```

UserOut

### 属性

|名称|类型|必选|约束|中文名|说明|
|---|---|---|---|---|---|
|username|string|true|none|用户名|none|
|email|string|true|none|用户邮箱地址|none|
|full_name|string|false|none|用户全名|none|
|request_id|string(uuid4)|false|none|Request Id|none|

<h2 id="tocS_ValidationError">ValidationError</h2>

<a id="schemavalidationerror"></a>
<a id="schema_ValidationError"></a>
<a id="tocSvalidationerror"></a>
<a id="tocsvalidationerror"></a>

```json
{
  "loc": [
    "string"
  ],
  "msg": "string",
  "type": "string"
}

```

ValidationError

### 属性

|名称|类型|必选|约束|中文名|说明|
|---|---|---|---|---|---|
|loc|[anyOf]|true|none|Location|none|

anyOf

|名称|类型|必选|约束|中文名|说明|
|---|---|---|---|---|---|
|» *anonymous*|string|false|none||none|

or

|名称|类型|必选|约束|中文名|说明|
|---|---|---|---|---|---|
|» *anonymous*|integer|false|none||none|

continued

|名称|类型|必选|约束|中文名|说明|
|---|---|---|---|---|---|
|msg|string|true|none|Message|none|
|type|string|true|none|Error Type|none|

<h2 id="tocS_Student">Student</h2>

<a id="schemastudent"></a>
<a id="schema_Student"></a>
<a id="tocSstudent"></a>
<a id="tocsstudent"></a>

```json
{
  "name": "string",
  "age": 0,
  "course": "string"
}

```

Student

### 属性

|名称|类型|必选|约束|中文名|说明|
|---|---|---|---|---|---|
|name|string|true|none|Name|none|
|age|integer|true|none|Age|none|
|course|[Course](#schemacourse)|true|none||none|

