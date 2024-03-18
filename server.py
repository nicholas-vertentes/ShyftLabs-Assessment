from http.server import HTTPServer, BaseHTTPRequestHandler;
import sys;
import json;
import sqlite3;
import database;

db = database.Database(reset=True);
db.create_tables();

class MyHandler( BaseHTTPRequestHandler ):
    def do_GET(self):
      if self.path == "/":
        self.send_response( 200 ); # OK
        self.send_header( "Content-type", "text/html" );

        fp = open( 'index.html' ); 
        page = fp.read();
        fp.close();

        self.send_header( "Content-length", len(page) );
        self.end_headers();
        self.wfile.write( bytes( page, "utf-8" ) );

      if self.path == "/script.js":
        self.send_response( 200 ); # OK
        self.send_header( "Content-type", "text/javascript" );

        fp = open( 'script.js' ); 
        page = fp.read();
        fp.close();

        self.send_header( "Content-length", len(page) );
        self.end_headers();
        self.wfile.write( bytes( page, "utf-8" ) );

      if self.path == "/style.css":
        self.send_response( 200 ); # OK
        self.send_header( "Content-type", "text/css" );

        fp = open( 'style.css' ); 
        page = fp.read();
        fp.close();

        self.send_header( "Content-length", len(page) );
        self.end_headers();
        self.wfile.write( bytes( page, "utf-8" ) );

      if self.path == "/HomePage.html":
        self.send_response( 200 ); # OK
        self.send_header( "Content-type", "text/html" );

        fp = open( 'HomePage.html' ); 
        page = fp.read();
        fp.close();

        self.send_header( "Content-length", len(page) );
        self.end_headers();
        self.wfile.write( bytes( page, "utf-8" ) );

      if self.path == "/Students.html":
        self.send_response( 200 ); # OK
        self.send_header( "Content-type", "text/html" );

        page = """<body>
                    <h1 style="text-align: center;">
                      Student Form
                    </h1>
                    <div class="studentForm">
                      <div>
                        <label for="firstName">First Name:</label>
                        <input type="text" placeholder="John" id="firstName">
                      </div>
                      <div>
                        <label for="lastName">Last Name:</label>
                        <input type="text" placeholder="Smith" id="lastName">
                      </div>
                      <div>
                        <label for="birthday">Birthday:</label>
                        <input type="date" id="birthday">
                      </div>
                      <button id="studentFormSubmit"> Submit </button>"""

        rows = db.connection.execute("SELECT * FROM Students").fetchall()
        for row in rows:
          page += '<div>'
          page += str(row)
          page += '</div>'

          page +=  """</div>
                    </body>
                  </html>"""


        self.send_header( "Content-length", len(page) );
        self.end_headers();
        self.wfile.write( bytes( page, "utf-8" ) );

    def do_POST(self):
      if self.path == "/addStudent":
        content_length = int(self.headers['Content-Length'])
        body = self.rfile.read(content_length)

        try:
          json_data = json.loads(body.decode('utf-8'))
          # print(json_data)
        except json.JSONDecodeError as e:
          print('Error decoding JSON:', e)
          self.send_error(400, message='Error decoding JSON')
          return

        try:
          db.addStudent(json_data['firstName'], json_data['lastName'], json_data['birthday'])

          self.send_response(200)
          self.send_header("Content-type", "text/html")
          self.end_headers()
          self.wfile.write(bytes('Student Added', 'utf-8'))

        except sqlite3.Error as e:
          print('DatabaseError:', e)
          self.send_error(500, message='Failed to add student')
          return


      # else:
      #   self.send_response( 404 );
      #   self.end_headers();
      #   self.wfile.write( bytes( "40411: not found", "utf-8" ) );

      


httpd = HTTPServer( ( 'localhost', int(sys.argv[1]) ), MyHandler );
httpd.serve_forever(); 