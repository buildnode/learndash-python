from learndash.api_resources.abstract.api_resource import APIResource

class ListableAPIResource(APIResource):
    @classmethod
    def list(cls, **params):
        url = cls.class_url()
        return cls.request("get", url, params)
