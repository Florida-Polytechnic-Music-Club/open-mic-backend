from .flask_server import FlaskServer
from .database_handler import DatabaseHandler

class App():

  def __init__(self):
    self.db_handler = DatabaseHandler()
    self.flask_server = FlaskServer(self.db_handler)

  def start(self):
    server_ip = "0.0.0.0"
    server_port = 8080
    self.flask_server.run(server_ip, server_port, debug=True)

def main():
  app = App()
  app.start()