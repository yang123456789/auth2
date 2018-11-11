## 本项目使用方法如下:
```
1.clone代码
    git clone git@github.com:yang123456789/auth2.git
```
```
2.执行命令
    python3 manage.py migrate
    python3 manage.py createsuperuser
    python3 manage.py runserver
```
```
4.登录admin
http://localhost:8000/admin
输入用户名和密码
```
```
5.注册一个应用
http://localhost:8000/o/applications/
name随便写
Client Type填confidential
Authorization Grant Type填 Resource owner password-based
```
```
6.使用curl获取access token
curl -X POST -d "grant_type=password&username=<user_name>&password=<password>" -u"<client_id>:<client_secret>" http://localhost:8000/o/token/
```

```
本项目只是一个demo，如果想要做成一个完整的服务就需要，在其基础上依据业务进行修改。
```
