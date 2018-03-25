#!/usr/bin/env python
#coding: utf-8
import os
import utils
DEBUG = True

# Make these unique, and don't share it with anybody.
SECRET_KEY = "4cd92059-caa4-4d6c-a1b9-a5efebd80fa403801cbf-aa0c-4f49-a27b-1133c3e7d3999bb27760-3c46-4270-b375-00cf2124b80f"
NEVERCACHE_KEY = "ae266154-741b-4fef-8ac4-8bc69990e957c2122f76-3b47-4618-86b7-b9a886e675062d07a550-a1e3-438e-8101-95e44876ce77"


cell_captcha_map = {}

DATABASES = {
    "default": { 
        # Ends with "postgresql_psycopg2", "mysql", "sqlite3" or "oracle".
        "ENGINE": "django.db.backends.mysql",
        # DB name or path to database file if using sqlite3.
        "NAME": "efood",
        # Not used with sqlite3.
        "USER": "root",
        # Not used with sqlite3.
        "PASSWORD": "root",
        # Set to empty string for localhost. Not used with sqlite3.
        "HOST": "",
        # Set to empty string for default. Not used with sqlite3.
        "PORT": "",
    }
}

APPEND_SLASH = True

EMAIL_FAIL_SILENTLY = False
#SHOP_ORDER_FROM_EMAIL='autoreply@sina.cn'
SHOP_ORDER_FROM_EMAIL='admin@efoodin.com'
SHOP_ORDER_EMAIL_SUBJECT='感谢您的订单！'
SHOP_ORDER_EMAIL_BCC='efoodin@sina.com'

#EMAIL_HOST_USER = 'YOURGMAILADDRESS'
#EMAIL_USE_TLS = True
#EMAIL_HOST = 'smtp.gmail.com'
#EMAIL_HOST_PASSWORD = 'yourpassword'
#EMAIL_PORT = 587

#EMAIL_HOST = 'smtp.sina.com.cn'
EMAIL_HOST = '127.0.0.1'
EMAIL_HOST_USER = 'admin@efoodin.com'
#EMAIL_HOST_PASSWORD = 'WeiChun#1'
#EMAIL_PORT = 465
EMAIL_PORT = None
EMAIL_USE_TLS = False

SHOP_USE_RATINGS=False
BLOG_USE_FEATURED_IMAGE = True
SHOP_CHECKOUT_ACCOUNT_REQUIRED = True
ACCOUNTS_PROFILE_FORM_EXCLUDE_FIELDS = ('last_name','first_name')
ACCOUNTS_PROFILE_FORM_CLASS='mytheme.forms.MyProfileForm'
SHOP_HANDLER_BILLING_SHIPPING='mytheme.wnicheckout.wni_billship_handler'

AUTH_PROFILE_MODULE = "mytheme.UserProfile"
EXTRA_MODEL_FIELDS = (
    (
        "cartridge.shop.models.Product.saled",
        "IntegerField",
        ("Saled",),
        {"blank": True, "default": 0},
    ),
    (
        "cartridge.shop.models.Order.prefer_time",
        'CharField',#"DateTimeField",
        ("配送时间",),
        {"default":"立即送餐","max_length":30},
       #{"blank": True, "null": True},
    ),
    
    (
        "cartridge.shop.models.DiscountCode.description",
        "TextField",
        ('使用说明',),
        {"blank": True, "null": True},
    ),
    (
        "cartridge.shop.models.Product.recnum",
        "IntegerField",
        ("推荐指数",),
        {"blank": True, "default": 0},
    ),
                      )

if os.name != 'nt':
    SHOP_CURRENCY_LOCALE = 'zh_CN'
"""    
DEVICE_USER_AGENTS = (
    ("mobile", ("Android", "BlackBerry", "iPhone")),
    ("desktop", ("Windows", "Macintosh", "Linux")),
)
DEVICE_DEFAULT = "desktop"
"""
DEBUG_TOOLBAR_CONFIG = {'JQUERY_URL':''}
_ = lambda s: s
SHOP_OPTION_TYPE_CHOICES = ((1, u'尺寸'), (2, u'颜色'),(3,u'配送范围'))
SHOP_ORDER_STATUS_CHOICES = ((1, u'未处理'), (2, u'已完毕'),(3,u'派送中'))
SHOP_PRODUCT_SORT_OPTIONS = ((u'按推荐指数', '-recnum'),(u'最近添加的', '-date_added'), ('Highest rated', '-rating_average'), ('价格从低到高', 'unit_price'), ('价格从高到低', '-unit_price'))

FREE_SHIPPING_TOTAL=58
logger = utils.Logger.createLogger('efoodin',fd='./logs/server.log')

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
        'LOCATION': '127.0.0.1:11211',
    }
}
ALLOWED_HOSTS = ['.efoodin.com']