import learndash

from learndash.api_resources.abstract import ListableAPIResource
from learndash.api_resources.abstract import RetrievableAPIResource
from learndash.api_resources.abstract import UpdateableAPIResource
from learndash.api_resources.abstract import NestedAPIResource
from learndash.api_resources.typing import CourseDict
from learndash.api_resources.typing import CourseStepDict
from learndash.api_resources.typing import CoursePrerequisiteDict
from learndash.api_resources.typing import CourseUserDict
from learndash.api_resources.typing import CourseGroupDict


class Course(RetrievableAPIResource[CourseDict], ListableAPIResource[CourseDict]):  # Also deletable, creatable, updateable
    api_path = learndash.path_courses
    
    def steps(self, id=None):
        return CourseSteps(id, parent=self)
    
    def prerequisites(self, id=None):
        return CoursePrerequisites(id, parent=self)

    def users(self, id=None):
        return CourseUser(id, parent=self)
    
    def groups(self, id=None):
        return CourseGroups(id, parent=self)


class CourseSteps(ListableAPIResource[CourseStepDict], UpdateableAPIResource, NestedAPIResource):
    api_path = learndash.path_course_steps

    def instance_url(self):
            # This endpoint accepts updates at it's base endpoint
            return self.class_url()


class CoursePrerequisites(ListableAPIResource[CoursePrerequisiteDict], NestedAPIResource):
    api_path = learndash.path_course_prerequisites


class CourseUser(ListableAPIResource[CourseUserDict], UpdateableAPIResource, NestedAPIResource):
    api_path = learndash.path_course_users

    def instance_url(self):
        # This endpoint accepts updates and deletions at it's base endpoint
        return self.class_url()


class CourseGroups(ListableAPIResource[CourseGroupDict], UpdateableAPIResource, NestedAPIResource): # Also deletable
    api_path = learndash.path_course_groups

    def instance_url(self):
        # This endpoint accepts updates and deletions at it's base endpoint
        return self.class_url()
