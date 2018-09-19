---
title: django-redis配置
date: 2018-06-01 15:22:51
tags:
categories: Django
---

# Django-setting配置Redis储存session

```
# redis配置
CACHES= {
    'default':{
        "BACKEND": 'django_redis.cache.RedisCache',
        "LOCATION": "redis://127.0.0.1:6379/2",
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
            "PASSWORD": "",
        }
    }
}

# 储存session设置
SESSION_ENGING = "django.contrib.session.backends.cache"
SESSION_CACHE_ALIAS = "default"
```