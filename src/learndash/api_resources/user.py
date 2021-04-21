import learndash
from learndash.api_resources.abstract import ListableAPIResource
from learndash.api_resources.abstract import RetrievableAPIResource
from learndash.api_resources.abstract import UpdateableAPIResource
from learndash.api_resources.abstract import NestedAPIResource

class User(RetrievableAPIResource, ListableAPIResource):
    """
    """

    api_path = learndash.path_users

    def course_progress(self, id=None):
        return UserCourseProgress(id, parent=self)


class UserCourseProgress(ListableAPIResource, NestedAPIResource):
        """
        """
        api_path = learndash.path_user_course_progress
