# -*- coding: utf-8 -*-
from bifrostprovider.provider import BifrostProvider
from allauth.socialaccount.providers.oauth2.urls import default_urlpatterns


urlpatterns = default_urlpatterns(BifrostProvider)
