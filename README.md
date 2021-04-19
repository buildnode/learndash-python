# LearnDash Python Library

The LearnDash Python Library provides a simple wrapper for a LearnDash API.

## Documentation

See the [LearnDash API V2 Docs](https://developers.learndash.com/rest-api/v2/).

## Usage

```python
import learndash
learndash.api_host = https://my-learndash-website.com

# Auth is provided via wordpress user credentials when needed
import os
learndash.wordpress_un = os.environ.get('WORDPRESS_UN')
learndash.wordpress_pw = os.environ.get('WORDPRESS_PW')

# list Courses
courses_resp = learndash.Course.list()

print(courses_resp.json())

# retrieve specific Course
course_resp = learndash.Course.retrieve(12)

print(course_resp.json())
```

## Configuring API Paths

The LearnDash Wordpress plugin allows admins to configure the paths for each API resource. By default, this library will use the LearnDash plugin's default paths, but you can reconfigure those paths:

```python
import learndash
learndash.path_courses = 'courses'  # Leave out slashes
```

## Dependencies

Requires the requests library.
