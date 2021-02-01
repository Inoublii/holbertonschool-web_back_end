#!/usr/bin/env python3
""" BasicAuth inherits from Auth """
from api.v1.auth.auth import Auth
import base64


class BasicAuth(Auth):
    """ BasicAuth inherits from Auth """

    def extract_base64_authorization_header(self,
                                            authorization_header: str) -> str:
        """
        Returns the Base64 part of the Authorization header for a Basic
        Authentication.
        """
        if authorization_header is None:
            return None
        if type(authorization_header) is not str:
            return None
        if not authorization_header.startswith('Basic '):
            return None
        return authorization_header[6:]

    def decode_base64_authorization_header(
            self, base64_authorization_header: str) -> str:
        """returns the decoded value of a Base64"""

        if (
           not base64_authorization_header or
           not isinstance(base64_authorization_header, str)):
            return None
        try:
            return base64.b64decode(base64_authorization_header).decode(
                'utf-8')
        except Exception as e:
            return None

    def extract_user_credentials(
            self, decoded_base64_authorization_header: str) -> (str, str):
        """Returns email and password from Base64 decoded ."""
        credentials = []
        if decoded_base64_authorization_header is None:
            return None, None
        if type(decoded_base64_authorization_header) is not str:
            return None, None
        if ':' not in decoded_base64_authorization_header:
            return None, None
        credentials = decoded_base64_authorization_header.split(':')
        return (credentials[0], credentials[1])
