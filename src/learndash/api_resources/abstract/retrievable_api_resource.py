from learndash.api_resources.abstract.api_resource import APIResource

class RetrievableAPIResource(APIResource):
    @classmethod
    def retrieve(cls, id):
        url = cls.instance_url(id)
        return cls.request("get", url)
