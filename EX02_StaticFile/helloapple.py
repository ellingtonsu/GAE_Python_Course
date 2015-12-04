import webapp2

class MainPage(webapp2.RequestHandler):
	def get(self):
		self.response.headers['Content-Type'] = 'text/html'
		self.response.write('<script src="/javascripts/dialog.js"></script>')
		self.response.write('Hello, Apple<br>')
		self.response.write('<img src="/images/apple.jpg"><br>')
		self.response.write('<button onclick="inputName(\'demos\')">Try it</button>')
		self.response.write('<p id="demos"></p>')

app = webapp2.WSGIApplication([
	('/', MainPage),
], debug=True)