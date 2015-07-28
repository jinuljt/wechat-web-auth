#-*- coding:utf-8 -*-
# created:     Tue Jul 28 21:04:56 2015
# filename:    wechat.py
# author:      juntao liu
# email:       jinuljt@gmail.com
# descritpion:

import json

import requests

from .exceptions import APIException

CONNECT_URL = "https://open.weixin.qq.com/connect/oauth2/authorize?appid=%s&redirect_uri=%s&response_type=code&scope=%s&state=%s#wechat_redirect"
ACCESS_TOKEN_URL = "https://api.weixin.qq.com/sns/oauth2/access_token?appid=%s&secret=%s&code=%s&grant_type=authorization_code"
REFRESH_TOKEN_URL = "https://api.weixin.qq.com/sns/oauth2/refresh_token?appid=%s&grant_type=refresh_token&refresh_token=%s"
USERINFO_URL = "https://api.weixin.qq.com/sns/userinfo?access_token=%s&openid=%s&lang=zh_CN"



def _obj_hook(pairs):
    o = JsonObject()
    for k, v in pairs.iteritems():
        o[str(k)] = v
        return o

class JsonObject(dict):
    def __getattr__(self, attr):
        return self[attr]

    def __setattr__(self, attr, value):
        self[attr] = value


class  Wechat(object):
    def __init__(self, app_id, secret):
        self.app_id = app_id
        self.secret = secret

    def _http_get(self, url):
        try:
            r = requests.get(url, timeout=1)
            j = json.loads(r.content, object_hook=_obj_hook)
        except Exception:
            raise APIException
        return j

    def get_connect_url(self,
                        redirect_url,
                        scope="snsapi_userinfo",
                        state="STATE"):
        return CONNECT_URL%(self.app_id, redirect_url, scope, state)

    def get_access_token(self, code):
        url = ACCESS_TOKEN_URL%(self.app_id, self.secret, code)
        return self._http_get(url)

    def refresh_token(self, refresh_token):
        url = REFRESH_TOKEN_URL%(self.app_id, refresh_token)
        return self._http_get(url)

    def get_userinfo(self, access_token):
        url = USERINFO_URL%(access_token, self.app_id)
        return self._http_get(url)
