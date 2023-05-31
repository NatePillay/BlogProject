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

this is JINJA templating syntax and injecting

{{varaible}} syntax
control flow syntax - for and if
using {% %} syntax

<ul> #unordered list
    {% for item in mylist %}   #mylist variable passed into html template
    <li> {{item}} </li>  #list items, you make your own item mylist will be equal to the variable created in python
    {% endfor %}
</ul>

template inheritance

in a base.html file
we create reusable aspects, in base file we set up a block
{%block content%}
xxx
xxx
{% endblock %}

in inheriting files we use
{% extend "base.html" %}

{%block content%}
xxx
xxx
{% endblock %}






in a py file

@app.route('/')
def index():
    return render_template('home.html')


@app.route('/puppy/<name>')
def pup_name(name):
    return render_template('puppy.html', name=name)


html
#create a nav bar


git 