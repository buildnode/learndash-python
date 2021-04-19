import learndash
from learndash.api_resources.abstract import ListableAPIResource
from learndash.api_resources.abstract import RetrievableAPIResource

class Course(RetrievableAPIResource, ListableAPIResource):
    """
    """
    api_path = learndash.path_courses
