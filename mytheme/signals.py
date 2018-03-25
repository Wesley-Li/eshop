#!/usr/bin/env python
#coding: utf-8

from django.db.models.signals import post_save
#from django.dispatch import dispatcher
from django.contrib.auth.models import User
#from django.core.mail import mail_admins,SMTPConnection
from cartridge.shop.models import DiscountCode
from uuid import uuid4
#from django.conf import settings #import act_logger
from mezzanine.conf import settings
import datetime
from django.dispatch import Signal
import copy

discount_on_signup = Signal(providing_args=["instance"])

def wni_user_register(instance,**kwargs):
    #settings.use_editable()
    tmp_detail = copy.deepcopy(settings.REG_DISCOUNT_DETAIL)
    for tmp_count in tmp_detail:
        tmp_dis = DiscountCode(active=1,code=str(uuid4()),valid_to=datetime.datetime.now()+datetime.timedelta(days=tmp_count.pop("validdays")),**tmp_count)
        try:
            tmp_dis.save()
            tmp_dis.validusers.add(instance)
        except Exception,e:
            settings.act_logger.log(40,"discount on signin error:%s" % str(e))

discount_on_signup.connect(wni_user_register, dispatch_uid="user_reg")

"""
def user_post_save(sender, instance, signal, *args, **kwargs):  
    tmp_dis = DiscountCode(title="15元优惠",active=1,discount_deduct=10.00,code=str(uuid4()),min_purchase=50.00,uses_remaining=100,description="朋友，订单金额满100元起用！")
    try:
        tmp_dis.save()
    except Exception,e:
        settings.act_logger.log(40,"discount on signin error:%s" % str(e))
  
post_save.connect(user_post_save, sender=User, dispatch_uid="USER.SAVE")
"""
"""
mysql> select * from  shop_discountcode limit 1;
+----+-------------+--------+-----------------+------------------+----------------+---------------------+----------+---------+--------------+---------------+----------------+--------------------------
--------------+
| id | title       | active | discount_deduct | discount_percent | discount_exact | valid_from          | valid_to | code    | min_purchase | free_shipping | uses_remaining | description
              |
+----+-------------+--------+-----------------+------------------+----------------+---------------------+----------+---------+--------------+---------------+----------------+--------------------------
--------------+
|  1 | 10元优惠    |      1 |           10.00 |             NULL |           NULL | 2014-11-05 09:52:00 | NULL     | ajust10 |        20.00 |             0 |             10 | 朋友，订单金额满10元起用！             |

+----+-------------+--------+-----------------+------------------+----------------+---------------------+----------+---------+--------------+---------------+----------------+--------------------------
--------------+
1 row in set (0.00 sec)

mysql>
"""

