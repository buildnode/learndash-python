from learndash.api_resources.abstract.api_resource import APIResource
from learndash.exceptions import LearndashException


class ListableAPIResource(APIResource):
    def list(self, **params):
        url = self.class_url()
        resp = self.request("get", url, params)

        if resp.status_code > 299:
            raise LearndashException(resp.text)

        return resp.json()
