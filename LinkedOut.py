import os
import webapp2
import jinja2
from random_blobs import randomize, blubs, blobs
from google.appengine.ext import db

template_dir = os.path.join(os.path.dirname(__file__), 'templates')
jinja_env = jinja2.Environment(loader = jinja2.FileSystemLoader(template_dir),
							   autoescape = True)

class Handler(webapp2.RequestHandler):
	def write(self, *a, **kw):
		self.response.out.write(*a, **kw)

	def render_str(self, template, **params):
		t = jinja_env.get_template(template)
		return t.render(params)

	def render(self, template, **kw):
		self.write(self.render_str(template, **kw))

class MainPage(Handler):
	pass

class RandomPage(Handler):
	def get(self):
		if self.request.get('blod') == 'blod':
			self.redirect('/blod')
		else:
			self.render("randomize.html", blob=randomize(blubs), 
				    blub=randomize(blubs), 
				    darrenanderson=randomize(blobs), 
				    nomad=randomize(blobs))

class Blod(Handler):
	def get(self):
		posts = db.GqlQuery('select * from Post order by created desc')
		render('blod.html', posts=posts)

class NewPost(Handler):
	def render_page(self, subject='', content='', error=''):
		self.render('newpost.html', subject=subject, content=content, error=error)

	def get(self):
		self.render_page()

	def post(self):
		subject = self.request.get('subject')
		content = self.request.get('content')

		if subject or content:
			if (not subject) or (not content):
				self.render_page(subject, content, 'subject and content, please!')
			else:
				p = Post(subject=subject, content=content)
				p.put()
				key = str(p.key().id())
				self.redirect('/blod/%s' % key)
		else:
			self.render_page()

class PostHandler(Handler):
	def get(self, post_id):
		post = Post.get_by_id(int(post_id))
		if post:
			self.render('post.html', post=post)

class Post(db.Model):
	subject = db.StringProperty(required = True)
	content = db.TextProperty(required = True)
	created = db.DateTimeProperty(auto_now_add = True)

app = webapp2.WSGIApplication([
	('/', MainPage),
    ('/random', RandomPage),
    ('/blod', Blod),
    ('/blod/newpost', NewPost),
    ('/blod/([0-9]+)', PostHandler)
], debug=True)