
# Flask Login Using Token Authentication

Flask Based API for the Sign-Up & Login using the Token Authentication


## API Reference

### Sign-Up

```http
  POST /signup/
```

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `username` | `string` | **Required**. Name For The User |
| `email` | `string` | **Required**. Email Of The User |
| `password` | `string` | **Required**. Password Of The User |


#### Response

```http
{
  "token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyIjoiZ291cmF2dnYiLCJleHAiOjE2NzM3NzkwNzN9.I9XAXnjAIIHwSgKC0XiiSVftU1fF-e8Vw5BUIoWvPes"
}
```

#### Headers

```httpdate

status : 200 OK
date : Sun, 15 Jan 2023 10:07:53 GMT
content-type : application/json
content-length : 147
connection : close

```
### Login
```http
  POST /login/
```
| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `username` | `string` | **Required**. Name For The User |
| `email` | `string` | **Required**. Email Of The User |
| `password` | `string` | **Required**. Password Of The User |


#### Response

```http
{
  "token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyIjoiZ291cmF2dnYiLCJleHAiOjE2NzM3NzkzMTN9.6L19HehsNn9eXEIS2r0ryWZcO685xTtxnowkazFm64A"
}

```

#### Headers

```httpdate

status : 200 OK
date : Sun, 15 Jan 2023 10:11:53 GMT
content-type : application/json
content-length : 147
connection : close
```



### Token Validation

```http
  GET /protected/
```
| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `Token` | `string` | **Required**. Token  |



#### Response

```http
Welcome {User.userame}

```

#### Headers

```httpdate

status : 200 OK
date : Sun, 15 Jan 2023 10:14:37 GMT
content-type : text/html; charset=utf-8
content-length : 16
connection : close
```



## Support

For support, email souravvmishra@gmail.com 

