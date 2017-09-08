from django_assets import Bundle, register

js = Bundle(
    'bower/jquery/dist/jquery.min.js',
    'bower/bootstrap/dist/js/bootstrap.min.js',
    'ajaxcsrftoken.js',
    'ace2/ace.js',
    'ace2/ace-elements.js',
    'ace2/ace-extra.js',
    'bgframework.js',
    filters='jsmin', output='bgframework/packed.js'
)

css_base = Bundle(
    'bower/bootstrap/dist/css/bootstrap.min.css',
    'bower/font-awesome/css/font-awesome.min.css',
    filters='cssrewrite', output='bgframework/base.css'
)

css_ace = Bundle(
    'ace2/ace.css',
    'ace2/ace-part2.css',
    'ace2/ace-skins.css',
    'ace2/ace-rtl.css',
    filters='cssmin,cssrewrite', output='bgframework/packed-ace.css'
)

css = Bundle(
    css_base,
    css_ace,
    'base.css',
    filters='cssrewrite', output='bgframework/packed.css'
)

register('bgframework_js', js)
register('bgframework_css', css)
