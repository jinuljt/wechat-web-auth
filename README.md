微信网页授权获取用户信息封装
=====

对微信网页授权获取用户信息接口的封装

* 生成授权URL
* 获取access_token
* 刷新access_token
* 获取用户信息

微信文档
---
[http://mp.weixin.qq.com/wiki/17/c0f37d5704f0b64713d5d2c37b468d75.html](http://mp.weixin.qq.com/wiki/17/c0f37d5704f0b64713d5d2c37b468d75.html)


使用方式
===

```
from wechat_web_auth import Wechat

wc = Wechat(app_id, secret)

def connect(request):
    url = wc.get_connect_url("http://redirect.url/)
    return redirect(url)

def callback(request):
    resp = wc.get_access_token(self, request.GET.get('code'))
    access_token = resp.access_token
    userinfo = wc.get_userinfo(access_token)
	return HttpResponse("nickname:" + userinfo.nickname)

```
