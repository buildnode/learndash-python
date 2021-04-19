import learndash
import requests
import threading


class APIRequestor(object):
    """
    """
    def __init__(
        self,
        api_host=None,
        api_version=None,
        api_root=None,
        wordpress_un=None,
        wordpress_pw=None,
    ):
        self.api_host = api_host or learndash.api_host
        self.api_version = api_version or learndash.api_version
        self.api_root = api_root or learndash.api_root
        self.wordpress_un = wordpress_un or learndash.wordpress_un
        self.wordpress_pw = wordpress_pw or learndash.wordpress_pw

        self._thread_local = threading.local()
    
    def request(self, method: str, url: str, data=None, headers=None):

        if getattr(self._thread_local, "session", None) is None:
            self._thread_local.session = requests.Session()
        
        return self._thread_local.session.request(
            method,
            url,
            headers=headers,
            data=data,
        )
