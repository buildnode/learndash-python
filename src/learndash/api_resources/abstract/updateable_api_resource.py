from learndash.api_resources.abstract.api_resource import APIResource

class UpdateableAPIResource(APIResource):
    def update(self, data):
        url = self.instance_url()
        return self.request("patch", url, data)
