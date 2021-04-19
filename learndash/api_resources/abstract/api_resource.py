import learndash
import learndash.api_requestor

class APIResource(object):
    """
    """
    api_path = None
    
    @classmethod
    def class_url(cls):
        api_base = learndash.get_api_base()
        if not cls.api_path:
            raise Exception('No api path defined.')
        return f'{api_base}/{cls.api_path}'
    
    @classmethod
    def instance_url(cls, id: int):
        base = cls.class_url()
        return f'{base}/{id}'

    @classmethod
    def request(cls, method, url, data=None, headers=None):
        requestor = learndash.api_requestor.APIRequestor()
        print(f'Requesting ({method}) {url}')
        return requestor.request(method, url, data, headers)
