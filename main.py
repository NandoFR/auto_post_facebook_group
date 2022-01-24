from dotenv import load_dotenv
import os
from Bot import Bot

load_dotenv()

bot = Bot(
      facebook_login = str(os.getenv('facebook_email_or_phone')),
      facebook_password = str(os.getenv('facebook_password')),
      delay_for_each_post = int(os.getenv('delay_for_each_post')),
      skip_if_group_not_found = bool(os.getenv('skip_if_group_not_found')),
      delete_group_from_list_after_posting = bool(os.getenv('delete_group_from_list_after_posting')),
      tentatives_before_crashing = int(os.getenv('tentatives_before_crashing'))
)
