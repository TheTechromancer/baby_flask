#!/usr/bin/python3

# import Flask class (an instance of this class will be our WSGI application)
from flask import Flask

# __name__ is used because depending on if it's started as an application or
# imported as a module, the name will be different.  This is needed so that
# Flask knows where to look for templates, static files, etc.
app = Flask(__name__)

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
@app.route('/')
def hello_world():

	# returns the message we want to display in the user's browser
	return 'Hello there.'