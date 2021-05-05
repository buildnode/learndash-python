from typing import TypedDict


class GuidDict(TypedDict):
    rendered: str  # uri


class TitleDict(TypedDict):
    rendered: str


class ContentDict(TypedDict):
    rendered: str
    protected: bool


class MaterialsDict(TypedDict):
    rendered: str


class CourseDict(TypedDict):
    """
    https://developers.learndash.com/rest-api/v2/v2-courses/#schema
    """
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



class CourseStepDict(TypedDict):
    """
    https://developers.learndash.com/rest-api/v2/v2-course-steps/#schema
    """
    # TODO: create based on api documentation above


class CoursePrerequisiteDict(TypedDict):
    """
    https://developers.learndash.com/rest-api/v2/v2-course-prerequisites/#schema
    """
    # TODO: create based on api documentation above


class CourseUserDict(TypedDict):
    """
    https://developers.learndash.com/rest-api/v2/v2-course-users/#schema
    """
    # TODO: create based on api documentation above


class CourseGroupDict(TypedDict):
    """
    https://developers.learndash.com/rest-api/v2/v2-course-groups/#schema
    """
    # TODO: create based on api documentation above


class UserDict(TypedDict):
    """
    Not defined in the API, but present in the actual API.
    """


class UserCourseProgressDict(TypedDict):
    """
    https://developers.learndash.com/rest-api/v2/v2-user-course-progress/#schema
    """
    # TODO: create based on api documentation above


class UserCourseDict(TypedDict):
    """
    https://developers.learndash.com/rest-api/v2/v2-user-courses/#schema
    """
    # TODO: create based on api documentation above


class UserGroupDict(TypedDict):
    """
    https://developers.learndash.com/rest-api/v2/v2-user-groups/#schema
    """
    # TODO: create based on api documentation above


class UserQuizProgressDict(TypedDict):
    """
    https://developers.learndash.com/rest-api/v2/v2-user-quiz-progress/#schema
    """
    # TODO: create based on api documentation above
