import learndash

from typing import Literal
from typing import TypedDict

from learndash.api_resources.typing import ContentDict
from learndash.api_resources.typing import GuidDict
from learndash.api_resources.typing import MaterialsDict
from learndash.api_resources.typing import TitleDict
from learndash.api_resources.abstract import ListableAPIResource
from learndash.api_resources.abstract import RetrievableAPIResource
from learndash.api_resources.abstract import UpdateableAPIResource
from learndash.api_resources.abstract import NestedAPIResource


class CourseDict(TypedDict):
    id: int
    date: str  # datetime
    date_gmt: str  # datetime
    guid: GuidDict
    modified: str  # datetime
    modified_gmt: str  # datetime 
    slug: str
    status: Literal[
        'publish',
        'future',
        'draft',
        'pending',
        'private',
        'graded',
        'not_graded',
    ]
    type: str
    link: str  # uri
    title: TitleDict
    content: ContentDict
    author: int
    featured_media: int
    menu_order: int
    template: str
    categories: list
    tags: list
    ld_course_category: list
    ld_course_tag: list
    materials_enabled: bool
    materials: MaterialsDict
    certificate: int
    disable_content_table: bool
    lessons_per_page: int
    lesson_per_page_custom: int
    topic_per_page_custom: int
    price_type: Literal['open',
        'closed',
        'free',
        'buynow',
        'subscribe',
    ]
    price_type_paynow_price: str
    price_type_subscribe_price: str
    price_type_closed_price: str
    price_type_closed_custom_button_url: str
    prerequisite_enabled: bool
    prerequisite_compare: Literal[
        'ANY',
        'ALL',
    ]
    prerequisites: list
    points_enabled: bool
    points_access: str
    points_amount: str
    progression_disabled: bool
    expire_access: bool
    expire_access_days: int
    expire_access_delete_progress: bool


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
