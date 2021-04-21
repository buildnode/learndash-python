import learndash
from learndash.api_resources.abstract import ListableAPIResource
from learndash.api_resources.abstract import RetrievableAPIResource
from learndash.api_resources.abstract import UpdateableAPIResource
from learndash.api_resources.abstract import NestedAPIResource

class Course(RetrievableAPIResource, ListableAPIResource):
    """
    """

    api_path = learndash.path_courses

    def users(self, id=None):
        return CourseUser(id, parent=self)


class CourseUser(ListableAPIResource, UpdateableAPIResource, NestedAPIResource):
        """
        """
        api_path = learndash.path_course_users

        def instance_url(self):
            # This endpoint accepts updates and deletions at it's base endpoint
            return self.class_url()
