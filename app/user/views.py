from flask import Blueprint, render_template, request

user_views = Blueprint('user', __name__, template_folder='../../templates')

@user_views.route("/user/login", methods=['GET', 'POST'])
def user_login():
    if request.method == "POST":
        # handling post method
        # authentication
        return redirect('somewhere')

    # handle get method

    return render_template('login.html', **locals())
