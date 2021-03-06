#coding: utf-8

from django import forms
import captcha
from mezzanine.accounts.forms import ProfileForm

class MyForm(forms.Form): 
    wni_captcha = captcha.fields.CaptchaField()

#import mezzanine
from cartridge.shop.utils import make_choices

GENDER_CHOICES = (
('M', '男'),
('F', '女'),
('B','其它'),
)
from models import UserProfile
#from django.db import models
class MyProfileForm(ProfileForm):
    #required_css_class = 'required'
    #class Meta:
        #model = UserProfile
        #fields = ("first_name", "last_name", "email", "username")
        #exclude = ("is_try_group",)
    date_of_birth = forms.DateTimeField(help_text="生日可能有惊喜哦 :-)")
    #gender = forms.ChoiceField("性别",choices=make_choices(GENDER_CHOICES))
    gender = forms.ChoiceField(choices=GENDER_CHOICES)
    cell = forms.CharField()
    profile_captcha = captcha.fields.CaptchaField(label="验证码")
