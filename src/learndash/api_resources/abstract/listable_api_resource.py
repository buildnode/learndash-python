from learndash.api_resources.abstract.api_resource import APIResource

class ListableAPIResource(APIResource):
    def list(self, **params):
        url = self.class_url()
        return self.request("get", url, params)
