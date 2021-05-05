from typing import Generic
from typing import TypeVar

from learndash.api_resources.abstract.api_resource import APIResource
from learndash.exceptions import LearndashException


T = TypeVar('T')

class RetrievableAPIResource(APIResource, Generic[T]):
    def retrieve(self) -> T:
        url = self.instance_url()
        resp = self.request("get", url)

        if resp.status_code > 299:
            raise LearndashException(resp.text)

        return resp.json()
