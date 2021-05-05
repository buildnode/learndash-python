from typing import Literal
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


class CapabilitiesDict(TypedDict):
    rendered: str


class ExtraCapabilitiesDict(TypedDict):
    rendered: str


class AvatarURLsDict(TypedDict):
    rendered: str


class MetaDict(TypedDict):
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
    id: int
    type: str

class CoursePrerequisiteDict(TypedDict):
    """
    https://developers.learndash.com/rest-api/v2/v2-course-prerequisites/#schema
    """
    id: int
    type: str
    date: str # datetime
    date_gmt: str # datetime
    guid: object
    link: str # uri
    modified: str # datetime
    modified_gmt: str #datetime
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
    password:str
    permalink_template: str
    generated_slug: str
    title: TitleDict
    content: ContentDict
    author: int
    featured_media: int
    comment_status: str
    ping_status: str
    menu_order: int
    template: str
    categories: list
    tags: list
    ld_course_category: list
    ld_course_tag: list

class CourseUserDict(TypedDict):
    """
    https://developers.learndash.com/rest-api/v2/v2-course-users/#schema
    """
    id: int
    username: str
    name: str
    first_name: str
    last_name: str
    email: str # email
    url: str # url
    description: str
    link: str # uri
    locale: Literal[
        'en_US',
        'de_DE',
        'en_GB',
        'es_ES',
        'fr_FR'
    ]
    nickname: str
    slug: str
    registered_date: str # datetime
    roles: list
    password: str
    capabilities: CapabilitiesDict
    extra_capabilities: ExtraCapabilitiesDict
    avatar_urls: AvatarURLsDict
    meta: MetaDict


class CourseGroupDict(TypedDict):
    """
    https://developers.learndash.com/rest-api/v2/v2-course-groups/#schema
    """
    id: int
    date: str # datetime
    date_gmt: str # datetime
    guid: GuidDict
    link: str # uri 
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
    password: str
    parent: int
    title: TitleDict
    content: ContentDict
    author: int
    featured_media: int
    template: str
    categories: list
    tags: list
    ld_group_category: list
    ld_group_tag: list


class UserDict(TypedDict):
    """
    Not defined in the API, but present in the actual API.
    """


class UserCourseProgressDict(TypedDict):
    """
    https://developers.learndash.com/rest-api/v2/v2-user-course-progress/#schema
    """
    course: int
    progress_status: Literal[
        'not-started',
        'in-progress',
        'completed'
    ]
    last_step: int
    steps_completed: int
    steps_total: int
    date_started: str # datetime
    date_completed: str # datetime


class UserCourseDict(TypedDict):
    """
    https://developers.learndash.com/rest-api/v2/v2-user-courses/#schema
    """
    id: int
    date: str # datetime
    date_gmt: str # datetime
    guid: GuidDict
    link: str # uri
    modified: str # datetime
    modified_gmt: str # datetime
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
    password: str
    permalink_template: str
    generated_slug: str
    title: TitleDict
    content: ContentDict
    author: int
    featured_media: int
    comment_status: Literal[
        'open',
        'closed'
    ]
    ping_status: Literal[
        'open',
        'closed'
    ]
    menu_order: int
    template: str
    categories: list
    tags: list
    ld_course_category: list
    ld_course_tag: list


class UserGroupDict(TypedDict):
    """
    https://developers.learndash.com/rest-api/v2/v2-user-groups/#schema
    """
    id: int
    date: str # datetime
    date_gmt: str # datetime
    guid: GuidDict
    link: str # uri
    modified: str # datetime
    modified_gmt: str # datetime
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
    password: str
    parent: int
    title: TitleDict
    content: ContentDict
    author: int
    featured_media: int
    template: str
    categories: list
    tags: list
    ld_course_category: list
    ld_course_tag: list

class UserQuizProgressDict(TypedDict):
    """
    https://developers.learndash.com/rest-api/v2/v2-user-quiz-progress/#schema
    """
    quiz: int
    course: int
    lesson: int
    topic: int
    user: int
    percentage: float
    timespent: float
    has_graded: bool
    started: str # datetime
    completed: str # datetime
    points_scored: int
    points_total: int
    statistic: int