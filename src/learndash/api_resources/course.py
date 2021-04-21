import learndash
from learndash.api_resources.abstract import ListableAPIResource
from learndash.api_resources.abstract import RetrievableAPIResource
from learndash.api_resources.abstract import UpdateableAPIResource
from learndash.api_resources.abstract import NestedAPIResource

class Course(RetrievableAPIResource, ListableAPIResource): # Also deletable, creatable, updateable
    api_path = learndash.path_courses
    
    def steps(self, id=None):
        return CourseSteps(id, parent=self)
    
    def prerequisites(self, id=None):
        return CoursePrerequisites(id, parent=self)

    def users(self, id=None):
        return CourseUser(id, parent=self)
    
    def groups(self, id=None):
        return CourseGroups(id, parent=self)


class CourseSteps(ListableAPIResource, UpdateableAPIResource, NestedAPIResource):
    api_path = learndash.path_course_steps

    def instance_url(self):
            # This endpoint accepts updates at it's base endpoint
            return self.class_url()


class CoursePrerequisites(ListableAPIResource, NestedAPIResource):
    api_path = learndash.path_course_prerequisites


class CourseUser(ListableAPIResource, UpdateableAPIResource, NestedAPIResource):
    api_path = learndash.path_course_users

    def instance_url(self):
        # This endpoint accepts updates and deletions at it's base endpoint
        return self.class_url()


class CourseGroups(ListableAPIResource, UpdateableAPIResource, NestedAPIResource): # Also deletable
    api_path = learndash.path_course_groups

    def instance_url(self):
        # This endpoint accepts updates and deletions at it's base endpoint
        return self.class_url()
