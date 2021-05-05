import learndash

from learndash.api_resources.abstract import ListableAPIResource
from learndash.api_resources.abstract import RetrievableAPIResource
from learndash.api_resources.abstract import UpdateableAPIResource
from learndash.api_resources.abstract import NestedAPIResource
from learndash.api_resources.typing import UserDict
from learndash.api_resources.typing import UserCourseProgressDict
from learndash.api_resources.typing import UserCourseDict
from learndash.api_resources.typing import UserGroupDict
from learndash.api_resources.typing import UserQuizProgressDict

class User(RetrievableAPIResource[UserDict], ListableAPIResource[UserDict]):

    api_path = learndash.path_users

    def course_progress(self, id=None):
        return UserCourseProgress(id, parent=self)

    def courses(self, id=None):
        return UserCourse(id, parent=self)
    
    def groups(self, id=None):
        return UserGroup(id, parent=self)

    def quiz_progress(self, id=None):
        return UserQuizProgress(id, parent=self)


class UserCourseProgress(ListableAPIResource[UserCourseProgressDict], NestedAPIResource):
    api_path = learndash.path_user_course_progress


# class UserCourseProgressSteps(ListableAPIResource, NestedAPIResource):
    

class UserCourse(ListableAPIResource[UserCourseDict], UpdateableAPIResource, NestedAPIResource): # also deletable
    api_path = learndash.path_user_courses

    def instance_url(self):
        # This endpoint accepts updates and deletions at it's base endpoint
        return self.class_url()


class UserGroup(ListableAPIResource[UserGroupDict], UpdateableAPIResource, NestedAPIResource): # also deleteable
    api_path = learndash.path_user_groups

    def instance_url(self):
        # This endpoint accepts updates and deletions at it's base endpoint
        return self.class_url()


class UserQuizProgress(ListableAPIResource[UserQuizProgressDict], NestedAPIResource):
    api_path = learndash.path_user_quiz_progress
