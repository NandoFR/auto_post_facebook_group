import os
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from time import sleep

class Facebook:
      def __init__(self, **kwargs):
            self.facebook_login = kwargs['facebook_login']
            self.facebook_password = kwargs['facebook_password']
            self.delay_for_each_post = kwargs['delay_for_each_post']
            self.skip_if_group_not_found = kwargs['skip_if_group_not_found']
            self.debug = kwargs['debug']

            self.facebook_url = 'https://mbasic.facebook.com'
            self.chrome = webdriver.Chrome(ChromeDriverManager().install())
            self.chrome.maximize_window()
            self.chrome.implicitly_wait(60)
      
      def go_to_facebook(self):
            self.chrome.get(self.facebook_url)
      
      def login_facebook(self):
            self.chrome.find_element(By.XPATH, '//input[@name="email"]').send_keys(self.facebook_login)
            self.chrome.find_element(By.XPATH, '//input[@name="pass"]').send_keys(self.facebook_password)
            self.chrome.find_element(By.XPATH, '//input[@name="login"]').click()

      def close_save_device_page(self):
            if 'save-device' in self.chrome.current_url:
                  self.chrome.find_element(By.XPATH, '//a').click()
      
      def clear_url(self, url):
            if url.find('g') == 0:
                  return url

            two_dots = url.find(':')
            url_final = url[two_dots+3:]
            g_word = url_final.find('/')+1
            return url_final[g_word:]


      def post_in_group_loop(self):
            with open('./data/groups.txt', 'r') as group_file:
                  all_groups = group_file.readlines()
                  for group in all_groups:
                        self.chrome.get(os.path.join(self.facebook_url, self.clear_url(group)))
                        
                        try:
                              self.chrome.find_element(By.XPATH, '//input[@name="view_overview"]').click()
                        except:
                              if self.skip_if_group_not_found:
                                    continue
                              
                              self.chrome.close()
                              raise AssertionError

                        with open('./data/post.txt', 'r') as post_file:
                              all_lines = post_file.readlines()
                              post = ''.join([str(line) for line in all_lines])
                              self.chrome.find_element(By.XPATH, '//textarea[@name="xc_message"]').send_keys(post)
                              post_file.close()
                        
                        files_absolute_path = os.path.abspath('./data/files')
                        for file in os.listdir(files_absolute_path):
                              if '.gitkeep' in file:
                                    continue
                              
                              self.chrome.find_element(By.XPATH, '//input[@name="view_photo"]').click()
                              self.chrome.find_element(By.XPATH, '//input[@name="file1"]').send_keys(os.path.join(files_absolute_path, file))
                              self.chrome.find_element(By.XPATH, '//input[@name="add_photo_done"]').click()

                        if not self.debug:
                              self.chrome.find_element(By.XPATH, '//input[@name="view_post"]').click()
                              
                        sleep(self.delay_for_each_post)
      
      def run(self):
            self.go_to_facebook()
            self.login_facebook()
            self.close_save_device_page()
            self.post_in_group_loop()
            sleep(10)
            self.chrome.close()