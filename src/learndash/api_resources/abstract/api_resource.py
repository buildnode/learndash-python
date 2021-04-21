import learndash
import learndash.api_requestor

class APIResource(object):
    """
    """
    api_path = None

    def __init__(self, id=None):
        self.id = id
    
    def class_url(self):
        api_base = learndash.get_api_base()
        if not self.api_path:
            raise Exception('No api path defined.')
        return f'{api_base}/{self.api_path}'
    
    def instance_url(self):
        id = self.id
        if not isinstance(id, int):
            raise Exception(f'Could not determine URL, received an invalid id "{id}".')

        base = self.class_url()
        return f'{base}/{id}'

    def request(self, method, url, data=None, headers=None):
        requestor = learndash.api_requestor.APIRequestor()
        return requestor.request(method, url, data, headers)
