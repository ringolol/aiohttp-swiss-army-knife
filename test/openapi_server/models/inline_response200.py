# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model_ import Model
from openapi_server import util


class InlineResponse200(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, name: str=None):
        """InlineResponse200 - a model defined in OpenAPI

        :param name: The name of this InlineResponse200.
        """
        self.openapi_types = {
            'name': str
        }

        self.attribute_map = {
            'name': 'name'
        }

        self._name = name

    @classmethod
    def from_dict(cls, dikt: dict) -> 'InlineResponse200':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The inline_response_200 of this InlineResponse200.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def name(self):
        """Gets the name of this InlineResponse200.


        :return: The name of this InlineResponse200.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this InlineResponse200.


        :param name: The name of this InlineResponse200.
        :type name: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")

        self._name = name