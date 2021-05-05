from typing import Generic
from typing import TypeVar

from learndash.api_resources.abstract.api_resource import APIResource
from learndash.exceptions import LearndashException


T = TypeVar('T')

class ListableAPIResource(APIResource, Generic[T]):
    def list(self, **params) -> 'list[T]':
        url = self.class_url()
        resp = self.request("get", url, params)

        if resp.status_code > 299:
            raise LearndashException(resp.text)

        return resp.json()
