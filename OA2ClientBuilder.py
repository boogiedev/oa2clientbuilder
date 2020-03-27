#!/usr/bin/env python
# -*- coding: utf-8 -*-



from OA2ClientMetaBuilder import *
from OA2Client import *

# OA2Client Concrete Builder Class

class OA2ClientBuilder(OA2ClientMetaBuilder):
    """Concrete Builder for OA2Client object
    """
    def __init__(self):
        self.OA2Client = OA2Client()

    # Client Credentials
    def set_client_name(self, val: str) -> None:
        self.OA2Client.client_name = val
        return self
    def set_client_id(self, val: str) -> None:
        self.OA2Client.client_id = val
        return self
    def set_client_secret(self, val: str) -> None:
        self.OA2Client.client_secret = val
        return self

    # Base & OA2 URLs
    def set_base_url(self, val: str) -> None:
        self.OA2Client.base_url = val
        return self
    def set_redirect_uri(self, val: str) -> None:
        self.OA2Client.redirect_uri = val
        return self
    def set_authorize_url(self, val: str) -> None:
        self.OA2Client.authorize_url = val
        return self
    def set_access_token_url(self, val: str) -> None:
        self.OA2Client.access_token_url = val
        return self

    # OA2.get_auth_session JSON data
    def set_session_data(self, val: Optional[Dict[str,str]]) -> None:
        self.OA2Client.session_data = val
        return self

    # Return Client Object
    def get_active_client(self) -> object:
        return self.OA2Client
