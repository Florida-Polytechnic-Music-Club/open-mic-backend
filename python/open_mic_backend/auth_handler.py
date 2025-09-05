from .database_handler import DatabaseHandler
from .constants import ERR_INVALID_EMAIL_MSG, ERR_INVALID_JSON_MSG, ERR_EMAIL_NOT_FOUND
import re

EMAIL_REGEX = re.compile(
  r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
)

def is_valid_email(email: str) -> bool:
  return EMAIL_REGEX.match(email) is not None


class AuthHandler():
  
  def __init__(self):
    self.database_handler = DatabaseHandler()


  def loginAtempt(self, login_data):
    email = ""
    try:
      email = login_data["email"].lower()
    except KeyError:
      return False, {"error_msg": ERR_INVALID_JSON_MSG}, 400
    
    # Check if email is valid
    if not is_valid_email(email):
        return False, {"error_msg": ERR_INVALID_EMAIL_MSG}, 400

    # Fetch User Name from Database
    user_data = {"name": "bob"} # user_data = db_handler.getNameFromEmail(email_str)
    # If email does not match a existing user in the database
    if user_data == None:
      return False, {"error_msg": ERR_EMAIL_NOT_FOUND}, 404

    rsp_msg = {
      **user_data
    }    
    return True, rsp_msg, 200
  