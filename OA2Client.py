#!/usr/bin/env python
# -*- coding: utf-8 -*-



from json import loads as Deserialize
from rauth import OAuth2Service
from typing import Dict, Optional

# OA2Client Class
from OA2Data import *

class OA2Client:
    """Class to generate active OAuth client object to access APIs using OAuth

    Attributes:
    ----------
        client_id : str
            first name of the person
    """

    _SESSION_DATA = {
            'code': 'bar',
            'grant_type': 'client_credentials',
            'redirect_uri': ''
    }

    def __init__(self,
            client_name: str,
            client_id: str,
            client_secret: str,
            base_url: str,
            redirect_uri: str,
            authorize_url: str,
            access_token_url: str,
            session_data: Optional[Dict[str,str]]):
        """Constructs all the necessary attributes for OA2Client object.

        Parameters:
        ----------
            client_name : str
                age of the person
            client_id : str
                first name of the person
            client_secret : str
                family name of the person
            base_url : str
                first name of the person
            redirect_uri : str
                family name of the person
            authorize_url : str
                age of the person
            access_token_url : str
                first name of the person
            session_data : Dict[str,str]
                family name of the person
        """
        self.client_name = client_name
        self.client_id = client_id
        self.client_secret = client_secret
        self.base_url = base_url
        self.redirect_uri = redirect_uri
        self.authorize_url = authorize_url
        self.access_token_url = access_token_url
        self.session_data = session_data

        # Initialize client service
        self._get_service()
        # Retrieve token from service
        self._get_access_token()
        self.access_token = None

    def __repr__(self):
        return f"""OA2Client(
        client_name = {self.client_name},
        client_id = {self.client_id},
        client_secret = {self.client_secret},
        base_url = {self.base_url},
        redirect_uri = {self.redirect_uri},
        authorize_url = {self.authorize_url},
        access_token_url = {self.access_token_url},
        session_data = {self.session_data})"""

    def __str__(self):
        return f"""OA2Client Session Object\nCLIENT: {self.client_name}\nACCESSING: {self.base_url}"""

    def _get_service(self) -> None:
        """Generates service object from OA2Client object attributes
        """
        self.service = OAuth2Service(
            name=self.client_name,
            client_id=self.client_id,
            client_secret=self.client_secret,
            access_token_url=self.access_token_url,
            authorize_url=self.authorize_url,
            base_url=self.base_url,)


    def _get_access_token(self) -> None:
        """Generates access token from OA2Client.service object
        """
        # Init OA2 session from service
        session = self.service.get_auth_session(data=self.session_data, decoder=Deserialize)
        # Retrieve access token from session
        self.access_token = session.access_token


VALID_NAME = "Wesley Nguyen"

TEST_CLIENT = OA2Client(VALID_NAME, CLIENT_ID, CLIENT_SECRET,
                        BASE_URL, REDIRECT_URI, AUTHORIZE_URL,
                        ACCESS_TOKEN_URL, DATA)
