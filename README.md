# bgframework
Django background management full-stack framework

# Page Style

This framework use 'ace-admin-template', demo at http://tkliuxing.github.io/ace/ , document at http://tkliuxing.github.io/ace/docs/

# Add-ons Usage

1. Install this package: `pip install bgframework`
2. Create your Django project
3. Install 'bgframework' and 'sekizai' and 'bootstrapform' into your Django settings `INSTALLED_APPS`:
```python
INSTALLED_APPS = [
    # ... django apps
    'sekizai',
    'bootstrapform',
    'bgframework',
    # ... your apps
]
```
4. Add the bgframework context processor:
```
TEMPLATES = [
    {
        ...
        'OPTIONS': {
            'context_processors': [
                ...
                'bgframework.context_processors.context',
                ...
            ],
        },
    },
]
```
5. Migrate database
6. Put the following code into your 'root url file':
```python
from bgframework.add_ons import get_addons_urls, load_bgframework_addons
load_bgframework_addons()

urlpatterns = [
    # ...
]

urlpatterns += [
    url(r'^addons/', include(get_addons_urls(), namespace="addons")),
    url(r'', include('bgframework.urls')),
]
```
7. Use `python manage.py startbgfapp YOUR_APP_NAME` create your apps.
8. Modify `bgf_addons.py` at your app folder.

## Available Settings
1. `APP_NAME` 
    The Site Title of your bgframework interface.
2. `AUTHOR`
    The Site author in login page.
3. `CAN_SIGNUP`

## Templates
```
templates
 |- bgframework
    |- addons.html
    |- base.html
    |- edit_base.html
    |- login.html
    |- logout.html
    |- pagination.html
```

### base.html

* Blocks: `content`, `app_name` and `js`.
* Sekizai block: `beforetitle`, `aftertitle` and `css`.
  You can use sekizai template tag like `{% add_to_block 'css' %}` before `{% load sekizai_tags %}`.
