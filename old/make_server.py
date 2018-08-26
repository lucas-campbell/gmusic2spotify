from http.server import BaseHTTPRequestHandler, HTTPServer
#server class, subclass of BaseHTTPRequestHandler
class MyServer(BaseHTTPRequestHandler):
    def _set_headers(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        
    def do_GET(self):
        self._set_headers()
        self.wfile.write(bytes("<html><body><h1>yes hello this is server</h1></body></html>", "utf-8"))
            
    def do_POST(self):
        print('incoming http: ', self.path)
        content_length = int(self.headers['Content-Length']) # <--- Gets the size of data
        post_data = self.rfile.read(content_length) # <--- Gets the data itself
        self.send_response(200)
#function to create the actual server, BaseHTTPRequestHandler could also be used as handler_class
def set_up_server(server_class=HTTPServer, handler_class=MyServer, port=8888):
    server_address = ('', port)
    le_server = server_class(server_address, MyServer)
    print('server starting')
    le_server.serve_forever()
    
if __name__ == "__main__":
    from sys import argv
    if len(argv) == 2 and argv[1] == "myServer":
        set_up_server()
    else:
        set_up_server(handler_class=BaseHTTPRequestHandler)
