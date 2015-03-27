import webapp2

class MainPage(webapp2.RequestHandler):
	def get(self):
		self.response.headers['Content-Type'] = 'text/html'
		self.response.write('Hello, Apple<br>')
		self.response.write('<img src="/images/apple.jpg">')


app = webapp2.WSGIApplication([
	('/', MainPage),
], debug=True)
