import webapp2
from google.appengine.ext import ndb

MAIN_PAGE_HTML = """\
<html>
  <body>
    <form action="/write" method="post">
      <div>Name:<br><input name="name" rows="3" cols="60"></input`></div>
      <div>Note:<br><textarea name="note" rows="3" cols="60"></textarea></div>
      <div><input type="submit" value="write"></div>
    </form>
  </body>
</html>
"""

# Declare the structure of entity
class Note(ndb.Model):
	name = ndb.StringProperty()
	note = ndb.StringProperty()

class MainPage(webapp2.RequestHandler):
	def get(self):
		self.response.headers['Content-Type'] = 'text/html'
		self.response.write(MAIN_PAGE_HTML)

class WriteNote(webapp2.RequestHandler):
	def post(self):
		name = self.request.get("name")
		note = self.request.get("note")
		new_note = Note(name=name,
				note=note)

		new_note_key = new_note.put()

		self.response.headers['Content-Type'] = 'text/html'
		self.response.write('Note has been stored.')

class ReadNote(webapp2.RequestHandler):
	def get(self):
		qry = Note.query() # Retrieve all Account entitites
		
		self.response.headers['Content-Type'] = 'text/html'
		for note in qry:
			self.response.write(note.name+":"+note.note+"<br>")


class ReadNotebyName(webapp2.RequestHandler):
	def get(self):
		name = self.request.get("name")
		qry = Note.query().filter(Note.name == name)

		self.response.headers['Content-Type'] = 'text/html'
		for note in qry:
			self.response.write(note.name+":"+note.note+"<br>")


app = webapp2.WSGIApplication([
	('/', MainPage),
	('/write', WriteNote),
	('/read', ReadNote),
	('/readbyname', ReadNotebyName)
], debug=True)
