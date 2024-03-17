from http.server import HTTPServer, BaseHTTPRequestHandler;
import sys;

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

        fp = open( 'Students.html' ); 
        page = fp.read();
        fp.close();

        self.send_header( "Content-length", len(page) );
        self.end_headers();
        self.wfile.write( bytes( page, "utf-8" ) );

    def do_POST(self):
      
      if self.path == "/addStudent":
        self.send_response( 200 ); # OK
        self.send_header( "Content-type", "text/html" );

        page ='Student Added'

        self.send_header( "Content-length", len(page) );
        self.end_headers();
        self.wfile.write( bytes( page, "utf-8" ) );

      # else:
      #   self.send_response( 404 );
      #   self.end_headers();
      #   self.wfile.write( bytes( "40411: not found", "utf-8" ) );

      


httpd = HTTPServer( ( 'localhost', int(sys.argv[1]) ), MyHandler );
httpd.serve_forever(); 