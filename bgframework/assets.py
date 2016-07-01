from django_assets import Bundle, register

js = Bundle(
    'bower/jquery/jquery-2.1.4.min.js',
    'bootstrap/js/bootstrap.min.js',
    'ajaxcsrftoken.js',
    'bgframework.js',
    'ace/ace.min.js',
    'ace/ace-elements.min.js',
    'ace/ace-extra.min.js',
    filters='jsmin', output='gen/packed.js'
)

css = Bundle(
    'bootstrap/css/bootstrap.min.css',
    'ace/ace.css',
    'ace/ace-rtl.min.css',
    'ace/ace-skins.css',
    'bower/font-awesome/css/font-awesome.min.css',
    'base.css',
    filters='cssrewrite', output='gen/packed.css'
)

register('bgframework_js', js)
register('bgframework_css', css)
