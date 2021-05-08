# -*- coding: utf-8 -*-
from allauth.socialaccount.providers.base import ProviderAccount
from allauth.socialaccount.providers.oauth2.provider import OAuth2Provider


class BifrostAccount(ProviderAccount):
    def to_str(self):
        dflt = super(BifrostAccount, self).to_str()
        return self.account.extra_data.get("name", dflt)


class BifrostProvider(OAuth2Provider):
    id = "bifrost"
    name = "Bifrost"
    account_class = BifrostAccount

    def get_default_scope(self):
        return [""]

    def extract_uid(self, data):
        return str(data["id"])

    def extract_common_fields(self, data):
        return dict(
            user_id=data.get("id"),
            id=data.get("id"),
            name=data.get("name"),
            email=data.get("email"),
            username=data.get("email")
        )


provider_classes = [BifrostProvider]
