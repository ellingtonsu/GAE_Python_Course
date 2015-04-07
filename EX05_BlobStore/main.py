import webapp2
from google.appengine.api import users
from google.appengine.ext import blobstore

UPLOAD_HTML = """\
<html>
  <body>
    <form action="%s" method="post" enctype="multipart/form-data">
    	Upload File: 	<input type="file" name="file"><br>
    					<input type="submit" name="submit" value="Submit"> 
    </form>
  </body>
</html>
"""

class MainPage(webapp2.RequestHandler):
	def get(self):
		user = users.get_current_user()
		if user:
			self.response.headers['Content-Type'] = 'text/html'
			self.response.write('<h1>Welcome to myS3, %s</h1>' % user.nickname())
			self.response.write('	<form method="post"> \
										<button formaction="/upload" type="submit">Upload</button> \
									</form>')
			self.response.write('	<form method="get"> \
										<button formaction="/list" type="submit">List</button> \
									</form>')
			self.response.write('<a href="%s">Logout</a>' % users.create_logout_url(self.request.url))
		else:
			self.redirect(users.create_login_url(self.request.url))

class Upload(webapp2.RequestHandler):
	def post(self):
		upload_url = blobstore.create_upload_url('/myS3/upload')
		#upload_url = blobstore.create_upload_url_async('/myS3/upload')
		self.response.headers['Content-Type'] = 'text/html'
		self.response.write('<h1>Select File for Upload</h1>')
		self.response.write(UPLOAD_HTML % upload_url)
		self.response.write('<a href="%s">Main Page</a>' %('/'))

class List(webapp2.RequestHandler):
	def get(self):
		self.response.headers['Content-Type'] = 'text/html'
		self.response.write('<h1>Your myS3 file list</h1>')
		self.response.write('<form method="post"><TABLE BORDER="1">')
		self.response.write('<TR><TD>Filename</TD><TD>Time</TD><TD>Action</TD></TR>')	

		qry = blobstore.BlobInfo.all()
		for blobinfo in qry:
			self.response.write('<TR>')	
			self.response.write('<TD>%s</TD>' % blobinfo.filename)
			self.response.write('<TD>%s</TD>' % str(blobinfo.creation))
			self.response.write('<TD>')
			self.response.write('<button name="resource" value="%s" formaction="/myS3/download" type="submit">Download</button>' % str(blobinfo.key()))
			self.response.write('<button name="resource" value="%s" formaction="/myS3/delete" type="submit">Delete</button>' % str(blobinfo.key()))
			self.response.write('</TD>')
			self.response.write('</TR>')
		
		self.response.write('</TABLE></form>')
		self.response.write('<a href="%s">Main Page</a>' %('/'))

app = webapp2.WSGIApplication([
	('/', MainPage),
	('/upload', Upload),
	('/list', List),
], debug=True)