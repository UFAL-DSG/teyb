from BaseHTTPServer import BaseHTTPRequestHandler
import SimpleHTTPServer
import SocketServer

import json

PORT = 8001


class HTTPRequestHandler(BaseHTTPRequestHandler):
    def do_POST(self):
        self.send_response(200)
        self.send_header('Content-Type', 'application/json')
        self.end_headers()
        length = int(self.headers.getheader('content-length'))
        data = json.loads(self.rfile.read(length))

        self.wfile.write(json.dumps(
            {
                'data': "OK. Received: %s, dialog key: %s" % (data['data'], data['dialog_key']),
            }))

    do_GET = do_POST



def main():
    Handler = SimpleHTTPServer.SimpleHTTPRequestHandler

    httpd = SocketServer.TCPServer(("", PORT), HTTPRequestHandler)

    print "serving at port", PORT
    httpd.serve_forever()

if __name__ == '__main__':
    main()