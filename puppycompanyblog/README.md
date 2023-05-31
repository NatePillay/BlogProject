in this read me ill describe the steps taken

blog_posts, core and users all connect to the app.py file using Blueprints
each file needs an __init__.py file

__init__ connects blueprints and organisational logic 

core
views.py has home and info view

models.py will hold user model and blog post model

checkout the bootstrap documentation on forms

user_blog_post.html incomplete


html:

python
@app.route('/')
def index():
    some_variable = "Jose"
    letters = list(some_variable)
    return render_template('basic_html', my_variable=some_variable, letters=letters)

html
<html lang="en" dir=""lt">
    <head>
        <meta charset="utf-8">
        <title></title>
    </head>
    <body>
    <h1> Hello! {{my_variable}} </h1>
    <h1>{{letters}} </h1>
 </body>
</html>


