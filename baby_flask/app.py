#!/usr/bin/env python3

# import Flask class (an instance of this class will be our WSGI application)
# render_template generates HTML dynamically given a template HTML file
from flask import Flask, url_for, render_template
from random import randint

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

	themes = ["sw", "asoiaf"]

	arts = {
		"sw": [
			"https://orig00.deviantart.net/6853/f/2017/275/a/c/star_wars___siege_of_mandalore_by_thetechromancer-dbp1v6o.png",
			"https://orig00.deviantart.net/3b32/f/2017/203/c/1/star_wars___lost_child__ahsoka_tano__by_thetechromancer-dbh9w2n.png",
			"https://orig00.deviantart.net/ce61/f/2015/301/a/b/star_wars___whispers_of_the_past__ahsoka_tano__by_thetechromancer-d7z38st.png",
			"https://orig00.deviantart.net/4a16/f/2015/310/2/f/star_wars___darth_revan_vs__bastila_shan_by_thetechromancer-d9fpt1m.png",
			"https://orig00.deviantart.net/6b64/f/2016/316/9/7/star_wars___peacekeeper__obi_wan_kenobi__by_thetechromancer-dao7hka.png"
		],
		"asoiaf": [
			"https://orig00.deviantart.net/e766/f/2017/319/1/6/trident_by_thetechromancer-dbtvdg9.jpg",
			"https://orig00.deviantart.net/70e0/f/2017/319/f/b/targaryens_by_thetechromancer-dbtvdfw.jpg",
			"https://orig00.deviantart.net/1823/f/2017/319/4/2/stoneheart_by_thetechromancer-dbtvjrk.png",
			"https://orig00.deviantart.net/a389/f/2017/319/f/1/rhaegar_by_thetechromancer-dbtvdfh.jpg"
		]
	}

	backgrounds = {
		"sw": [ "https://steamuserimages-a.akamaihd.net/ugc/251464760146726875/760F72CF39FD7D13B418EC008A92F7B23150BC4A/" ],
		"asoiaf": [ "https://i.pinimg.com/originals/a2/dd/5a/a2dd5ae7059d1a47fbf7ee2bbb3fc0fe.jpg" ]
	}

	try:
		theme = themes[app.config['THEME']]
	except:
		theme = pick_random(themes)

	art = pick_random(arts[theme])
	background = pick_random(backgrounds[theme])

	return render_template('home.html', rand_art=art, background=background)


@app.route('/admin/')
def admin():

	return render_template('admin.html')


def pick_random(v, key=None):
	'''
	takes dictionary or iterable
	if dictionary, picks a random key and then picks random entry from associated value
	if list, picks random entry
	'''
	if type(v) == dict:
		try:
			v = v[key]
		except:
			values = list(v.values())
			v = values[randint(0,len(values)-1)]

	r = v[randint(0,len(v)-1)]
	print(r)
	return r

if __name__ == '__main__':
	app.run()