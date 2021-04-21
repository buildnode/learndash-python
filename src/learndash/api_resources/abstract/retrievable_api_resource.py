from learndash.api_resources.abstract.api_resource import APIResource

class RetrievableAPIResource(APIResource):
    def retrieve(self):
        url = self.instance_url()
        return self.request("get", url)
