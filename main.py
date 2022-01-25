from dotenv import load_dotenv
from app.Facebook import Facebook
import os

load_dotenv()

facebook = Facebook(
      facebook_login = str(os.getenv('FACEBOOK_LOGIN')),
      facebook_password = str(os.getenv('FACEBOOK_PASSWORD')),
      delay_for_each_post = int(os.getenv('DELAY_FOR_EACH_POST')),
      skip_if_group_not_found = bool(os.getenv('SKIP_IF_GROUP_NOT_FOUND')),
      debug = bool(os.getenv('DEBUG'))
)

facebook.run()
