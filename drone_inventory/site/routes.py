from flask import Blueprint,render_template
from flask_login import login_required




"""
Note that in the above code some arguments are specified the Blueprint object

The first argument, 'site' is the Blueprint's name,
which is used by Flask's routing mechanism.
The second argument, __name__, is the Blueprint's import name,
whicj Flask ues to locate the Blueprint's resource
"""

site = Blueprint('site', __name__, template_folder = 'site_templates')

@site.route('/')
def home():
    return render_template('index.html')

@site.route('/profile')
@login_required
def profile():
    return render_template('profile.html')