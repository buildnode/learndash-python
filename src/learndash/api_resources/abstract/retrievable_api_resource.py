from learndash.api_resources.abstract.api_resource import APIResource
from learndash.exceptions import LearndashException


class RetrievableAPIResource(APIResource):
    def retrieve(self):
        url = self.instance_url()
        resp = self.request("get", url)

        if resp.status_code > 299:
            raise LearndashException(resp.text)

        return resp.json()
