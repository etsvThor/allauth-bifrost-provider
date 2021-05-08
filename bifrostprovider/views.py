# -*- coding: utf-8 -*-
import requests

from allauth.socialaccount import app_settings
from bifrostprovider.provider import BifrostProvider
from allauth.socialaccount.providers.oauth2.views import (
    OAuth2Adapter,
    OAuth2CallbackView,
    OAuth2LoginView,
)


class BifrostOAuth2Adapter(OAuth2Adapter):
    provider_id = BifrostProvider.id
    supports_state = True

    settings = app_settings.PROVIDERS.get(provider_id, {})
    provider_base_url = "https://bifrost.thor.edu"

    access_token_url = "{0}/oauth/token".format(provider_base_url)
    authorize_url = "{0}/oauth/authorize".format(provider_base_url)
    profile_url = "{0}/api/user".format(provider_base_url)

    def complete_login(self, request, app, token, response):
        headers = {'Authorization': f'Bearer {token.token}'}
        resp = requests.get(
            self.profile_url, headers=headers
        )
        extra_data = resp.json()

        return self.get_provider().sociallogin_from_response(request, extra_data)


oauth2_login = OAuth2LoginView.adapter_view(BifrostOAuth2Adapter)
oauth2_callback = OAuth2CallbackView.adapter_view(BifrostOAuth2Adapter)
