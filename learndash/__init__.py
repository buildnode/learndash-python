api_host = None
api_root = '/wp-json/ldlms'
api_version = 2

def get_api_base():
    if not api_host:
        raise Exception('No api_host has been set')
    return f'{api_host}{api_root}/v{api_version}'

max_network_retried = 5

# We authorize requests to the LearnDash API using a set of Wordpress admin account credentials
wordpress_un = ''
wordpress_pw = ''

# All of these paths can be reconfigured in Wordpress, and should be updated here.
path_assignments = 'sfwd-assignment'  # what is sfwd and why is it only on some of these?
path_courses = 'sfwd-courses'
path_course_steps = 'steps'
path_course_prerequisites = 'prerequisites'
path_course_users = 'users'
path_course_groups = 'groups'
path_essays = 'sfwd-essays'
path_groups = 'groups'
path_group_courses = 'courses'
path_group_leaders = 'leaders'
path_group_users = 'users'
path_lessons = 'sfwd-lessons'
path_price_types = 'price-types'
path_questions = 'sfwd-question'
path_question_types = 'question-types'
path_quizzes = 'sfwd-quiz'  # in api docs as "quizzes", in wordpress conf as "exam"
path_quiz_statistics = 'statistics'
path_quiz_statistics_questions = 'questions'
path_topics = 'sfwd-topic'
path_user_course_progress = 'course-progress'
# path_user-course-progress-steps = ''  # in the api docs, not in the wordpress conf
path_user_courses = 'courses'
path_user_groups = 'groups'
path_user_quiz_progress = 'course-progress'

from learndash.api_resources import *
