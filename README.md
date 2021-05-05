# LearnDash Python Library

**Warning, early alpha. Most functionality is missing.** The LearnDash Python Library provides a simple wrapper for a LearnDash API.

## Documentation

See the [LearnDash API V2 Docs](https://developers.learndash.com/rest-api/v2/).

## Installation

```bash
pip install learndash
```

## Usage

```python
import learndash
learndash.api_host = https://my-learndash-website.com

# Auth is provided via wordpress user credentials when needed
import os
learndash.wordpress_un = os.environ.get('WORDPRESS_UN')
learndash.wordpress_pw = os.environ.get('WORDPRESS_PW')

# list Courses
courses = learndash.Course().list()
print(courses)

# retrieve specific Course
course = learndash.Course(12).retrieve()
print(course)

# add user to a course
course_id = 1
learndash.Course(1).users().update({'user_ids': [course_id]})
```

## Supported Resources

The Learndash V2 API is still in beta, and this library is still in development. Supported resources and examples are listed below.

- [ ] Course
    - [x] Retrieve    
    `learndash.Course(1).retrieve()`
    - [x] List    
    `learndash.Course().list()`
- [x] Course Step
    - [x] List    
    `learndash.Course(1).steps().list()`
    - [x] Update    
    `learndash.Course(1).steps().update({})`
- [x] Course Prerequisite
    - [x] List    
    `learndash.Course(1).prerequisites().list()`
- [x] Course User
    - [x] List    
    `learndash.Course(1).users().list()`
    - [x] Update    
    `learndash.Course(1).users().update({'user_ids': []})`
- [x] Course Group
    - [x] List    
    `learndash.Course(1).groups().list()`
    - [x] Update    
    `learndash.Course(1).groups().update()`
- [ ] User
    - [x] Retrieve    
    `learndash.User(1).retrieve()`
    - [x] List    
    `learndash.User().list()`
- [x] User Course Progress
    - [x] List    
    `learndash.User(1).course_progress().list()`
- [x] User Course
    - [x] List    
    `learndash.User(1).courses().list()`
    - [x] Update    
    `learndash.User(1).courses().update({'user_ids': []})`
- [x] User Group
    - [x] List    
    `learndash.User(1).groups().list()`
    - [x] Update    
    `learndash.User(1).groups().update({})`
- [x] User Quiz Progress
    - [x] List    
    `learndash.User(1).quiz_progress().list()`

## Configuring API Paths

The LearnDash Wordpress plugin allows admins to configure the paths for each API resource. By default, this library will use the LearnDash plugin's default paths, but you can reconfigure those paths.

### How To Configure

Simply import the learndash module and overwrite the default path for an endpoint.

```python
import learndash
learndash.path_courses = 'courses'  # Leave out slashes
```

### Configurable Paths

All configurable paths and their default values are below. From [`learndash/__init__.py`](/src/learndash/__init__.py).

```python
path_assignments = 'sfwd-assignment'
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
path_quizzes = 'sfwd-quiz'
path_quiz_statistics = 'statistics'
path_quiz_statistics_questions = 'questions'
path_topics = 'sfwd-topic'
path_users = 'users'
path_user_course_progress = 'course-progress'
path_user_courses = 'courses'
path_user_groups = 'groups'
path_user_quiz_progress = 'course-progress'
```

## Dependencies

Requires the requests library.
