#!/usr/bin/env python3
""" BasicAuth inherits from Auth """
from api.v1.auth.auth import Auth
import base64
from typing import TypeVar
from models.user import User


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
        return tuple(decoded_base64_authorization_header.split(':', 1))

    def user_object_from_credentials(
            self, user_email: str, user_pwd: str) -> TypeVar('User'):
        """ returns the User instance based on his email and password """
        if (
           not user_email or
           not isinstance(user_email, str) or
           not user_pwd or
           not isinstance(user_pwd, str)
           ):
            return None
        objs = User().search({"email": user_email})
        if not objs:
            return None
        if not objs[0].is_valid_password(user_pwd):
            return None
        return objs[0]

    def current_user(self, request=None) -> TypeVar('User'):
        """ overloads Auth and retrieves instance of a request """
        if not request:
            return None
        auth_header = request.headers["Authorization"]
        authorization_header = extract_base64_authorization_header(auth_header)
        dec_header = decode_base64_authorization_header(auth_header)
        credentials = extract_user_credentials(dec_header)
        return user_object_from_credentials(credentials[0], credentials[1])