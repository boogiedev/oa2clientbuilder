#!/usr/bin/env python
# -*- coding: utf-8 -*-



from __future__ import annotations
from abc import ABC, abstractmethod, abstractproperty
from typing import Dict

# OA2Client Abstract Builder Class

class OA2ClientMetaBuilder(ABC):
    """Abstract Builder Interface for OA2Client object
    """

    # Client Credentials
    @abstractmethod
    def set_client_name(val: str) -> None:
        """Set the Client Name
        """
    @abstractmethod
    def set_client_id(val: str) -> None:
        """Set the Client ID
        """
    @abstractmethod
    def set_client_secret(val: str) -> None:
        """Set the Client Secret
        """

    # Base & OA2 URLs
    @abstractmethod
    def set_base_url(val: str) -> None:
        """Set the Base URL for API
        """
    @abstractmethod
    def set_redirect_uri(val: str) -> None:
        """Set the Redirect URI for OA2
        """
    @abstractmethod
    def set_authorize_url(val: str) -> None:
        """Set the Authorization URL for API OA2
        """
    @abstractmethod
    def set_access_token_url(val: str) -> None:
        """Set the Access Token URL for API OA2
        """

    # OA2.get_auth_session JSON data
    @abstractmethod
    def set_session_data(val: Optional[Dict[str,str]]) -> None:
        """Set the Session JSON data
        """

    # Return Client Object
    @abstractmethod
    def get_active_client() -> :
        """Return Active OA2Client Object
        """
