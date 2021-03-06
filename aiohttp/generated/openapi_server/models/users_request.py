# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model_ import Model
from openapi_server import util


class UsersRequest(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, username: str=None):
        """UsersRequest - a model defined in OpenAPI

        :param username: The username of this UsersRequest.
        """
        self.openapi_types = {
            'username': str
        }

        self.attribute_map = {
            'username': 'username'
        }

        self._username = username

    @classmethod
    def from_dict(cls, dikt: dict) -> 'UsersRequest':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The UsersRequest of this UsersRequest.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def username(self):
        """Gets the username of this UsersRequest.


        :return: The username of this UsersRequest.
        :rtype: str
        """
        return self._username

    @username.setter
    def username(self, username):
        """Sets the username of this UsersRequest.


        :param username: The username of this UsersRequest.
        :type username: str
        """

        self._username = username
