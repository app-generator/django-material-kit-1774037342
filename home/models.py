# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

# Create your models here.

class UserProfile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    #__PROFILE_FIELDS__

    #__PROFILE_FIELDS__END

    def __str__(self):
        return self.user.username
    
    class Meta:
        verbose_name        = _("UserProfile")
        verbose_name_plural = _("UserProfile")

#__MODELS__
class Card_Type(models.Model):

    #__Card_Type_FIELDS__
    description = models.CharField(max_length=255, null=True, blank=True)

    #__Card_Type_FIELDS__END

    class Meta:
        verbose_name        = _("Card_Type")
        verbose_name_plural = _("Card_Type")


class Aspect(models.Model):

    #__Aspect_FIELDS__
    is_fraction = models.BooleanField()
    color = models.CharField(max_length=255, null=True, blank=True)
    color_alt = models.CharField(max_length=255, null=True, blank=True)
    logo = models.CharField(max_length=255, null=True, blank=True)

    #__Aspect_FIELDS__END

    class Meta:
        verbose_name        = _("Aspect")
        verbose_name_plural = _("Aspect")


class Base_Set(models.Model):

    #__Base_Set_FIELDS__
    code = models.CharField(max_length=255, null=True, blank=True)
    description = models.CharField(max_length=255, null=True, blank=True)

    #__Base_Set_FIELDS__END

    class Meta:
        verbose_name        = _("Base_Set")
        verbose_name_plural = _("Base_Set")


class Rarity(models.Model):

    #__Rarity_FIELDS__
    description = models.CharField(max_length=255, null=True, blank=True)

    #__Rarity_FIELDS__END

    class Meta:
        verbose_name        = _("Rarity")
        verbose_name_plural = _("Rarity")


class Card(models.Model):

    #__Card_FIELDS__
    base_set = models.ForeignKey(base_set, on_delete=models.CASCADE)
    card_number = models.IntegerField(null=True, blank=True)
    is_unique = models.BooleanField()
    full_name = models.CharField(max_length=255, null=True, blank=True)
    name = models.CharField(max_length=255, null=True, blank=True)
    title = models.CharField(max_length=255, null=True, blank=True)
    card_type = models.ForeignKey(card_type, on_delete=models.CASCADE)
    cost = models.IntegerField(null=True, blank=True)
    aspect_primary = models.ForeignKey(aspect, on_delete=models.CASCADE)
    aspect_secondary = models.ForeignKey(aspect, on_delete=models.CASCADE)
    aspect_faction = models.ForeignKey(aspect, on_delete=models.CASCADE)
    rarity = models.ForeignKey(rarity, on_delete=models.CASCADE)

    #__Card_FIELDS__END

    class Meta:
        verbose_name        = _("Card")
        verbose_name_plural = _("Card")



#__MODELS__END
