from .flask_server import FlaskServer

class App():

  def __init__(self):
    self.flask_server = FlaskServer()

  def start(self, debug_mode=False):
    server_ip = "0.0.0.0"
    server_port = 8080
    self.flask_server.run(server_ip, server_port, debug=debug_mode)

def main():
  app = App()
  app.start()