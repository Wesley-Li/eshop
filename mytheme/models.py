#coding: utf-8
from django.db import models

# Create your models here.
from django.utils.translation import ugettext_lazy as _
from mezzanine.core.fields import FileField, RichTextField
from mezzanine.core.models import RichText, Orderable, Slugged
from mezzanine.pages.models import Page
from mezzanine.utils.models import upload_to
from django.contrib.auth.models import User
from django.contrib import admin
from django.db.models.signals import post_save

class HomePage(Page, RichText):
    '''
    A page representing the format of the home page
    '''
    heading = models.CharField(max_length=200,
        help_text="The heading under the icon blurbs")
    subheading = models.CharField(max_length=200,
        help_text="The subheading just below the heading")
    featured_works_heading = models.CharField(max_length=200,
        default="Featured Works")
    featured_portfolio = models.ForeignKey("Portfolio", blank=True, null=True,
        help_text="If selected items from this portfolio will be featured "
                  "on the home page.")
    content_heading = models.CharField(max_length=200,
        default="About us!")
    latest_posts_heading = models.CharField(max_length=200,
        default="Latest Posts")

    class Meta:
        verbose_name = _("Home page")
        verbose_name_plural = _("Home pages")

class Slide(Orderable):
    '''
    A slide in a slider connected to a HomePage
    '''
    homepage = models.ForeignKey(HomePage, related_name="slides")
    image = FileField(verbose_name=_("Image"),
        upload_to=upload_to("mytheme.Slide.image", "slider"),
        format="Image", max_length=255, null=True, blank=True)


class IconBlurb(Orderable):
    '''
    An icon box on a HomePage
    '''
    homepage = models.ForeignKey(HomePage, related_name="blurbs")
    icon = FileField(verbose_name=_("Image"),
        upload_to=upload_to("mytheme.IconBlurb.icon", "icons"),
        format="Image", max_length=255)
    title = models.CharField(max_length=200)
    content = models.TextField()
    link = models.CharField(max_length=2000, blank=True,
        help_text="Optional, if provided clicking the blurb will go here.")


class Portfolio(Page):
    '''
    A collection of individual portfolio items
    '''
    class Meta:
        verbose_name = _("Portfolio")
        verbose_name_plural = _("Portfolios")


GENDER_CHOICES = (
('M', '男'),
('F', '女'),
('B','其它'),
)

class UserProfile(models.Model):
    # This field is required.
    user = models.OneToOneField(User,related_name="extraprofile")

    # Other fields here
    date_of_birth = models.DateTimeField("生日",blank=True,null=True,help_text="生日可能有惊喜哦 :-)")
    
    gender = models.CharField("性别",max_length=1, choices=GENDER_CHOICES,blank=True,null=True)
    cell = models.CharField("手机号",max_length=11, blank=True,null=True)
    is_try_group = models.BooleanField("试吃团", default=False)


    #def create_user_profile(sender, instance, created, **kwargs):
    #    if created:
    #        UserProfile.objects.create(user=instance)
   
    #post_save.connect(create_user_profile, sender=User)

