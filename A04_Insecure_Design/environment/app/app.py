import json
from http.server import BaseHTTPRequestHandler, HTTPServer

# 加载模拟数据库
with open("data.json") as f:
    data = json.load(f)

users = data["users"]

class Handler(BaseHTTPRequestHandler):
    def _send_json(self, code, data):
        self.send_response(code)
        self.send_header("Content-Type", "application/json")
        self.end_headers()
        self.wfile.write(json.dumps(data).encode("utf-8"))

    def do_POST(self):
        if self.path == "/get_secret":
            length = int(self.headers.get("Content-Length", 0))
            body = self.rfile.read(length).decode("utf-8")
            try:
                req = json.loads(body)
            except:
                self._send_json(400, {"error": "invalid json"})
                return

            username = req.get("username")
            # A04 漏洞：未验证身份，任何人都可获取 admin/普通用户 secret
            if username in users:
                self._send_json(200, {
                    "username": username,
                    "role": users[username]["role"],
                    "secret": users[username].get("secret"),
                    "api_key": users[username].get("api_key")
                })
            else:
                self._send_json(404, {"error": "user not found"})
        else:
            self._send_json(404, {"error": "not found"})

    def do_GET(self):
        if self.path == "/":
            self.send_response(200)
            self.send_header("Content-Type", "text/html")
            self.end_headers()
            html = "<h1>Welcome to Insecure Demo</h1><p>Use POST /get_secret</p>"
            self.wfile.write(html.encode("utf-8"))
        else:
            self._send_json(404, {"error": "not found"})

def run(server_class=HTTPServer, handler_class=Handler):
    server_address = ("0.0.0.0", 5000)
    httpd = server_class(server_address, handler_class)
    print("Server running on port 5000")
    httpd.serve_forever()

if __name__ == "__main__":
    run()