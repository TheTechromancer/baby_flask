# import Flask class (an instance of this class will be our WSGI application)
# render_template generates HTML dynamically given a template HTML file
from flask import Flask, url_for, render_template

# __name__ is used because depending on if it's started as an application or
# imported as a module, the name will be different.  This is needed so that
# Flask knows where to look for templates, static files, etc.
# instance_relative_config tells flask to use instance/config.py if available
app = Flask(__name__, instance_relative_config=True)
app.config.from_object('config')	# load /config.py
app.config.from_pyfile('config.py') # overwrite with instance/config.py if it exists

app_name = "Baby Flask"


# the route() decorator tells Flask which URL should trigger the function
# but there is more to it!  You can make certain parts of the URL dynamic
# and attach multiple rules to a function
# examples: 
#	@app.route('/user/<username>')
#	def show_user_profile(username):
#	    # show the user profile for that user
#	    return 'User %s' % username
#
#	@app.route('/post/<int:post_id>')
#	def show_post(post_id):
#	    # show the post with the given id, the id is an integer
#	    return 'Post %d' % post_id
#
# the <variable> part is passed as a keyword argument to the function
# e.g., username='ObiWanKenobi'

# our /templates directory parallels our routes

@app.route('/')
def home():

	return render_template('home.html')

	# returns the message we want to display in the user's browser
	return 'Hello there.\n<a href={}>{}</a>'.format(url_for('admin'), 'admin')

@app.route('/admin/')
def admin():

	return render_template('admin.html')

if __name__ == '__main__':
	app.run()