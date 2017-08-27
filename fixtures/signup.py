# -*- coding: utf-8 -*-

import re


class SignupHelper:

    def __init__(self, app):
        self.app = app

    def new_user(self, username, email, password):
        wd = self.app.wd
        wd.get(self.app.baseUrl + "signup_page.php")
        wd.find_element_by_name("username").send_keys(username)
        wd.find_element_by_name("email").send_keys(username + "@localhost")
        wd.find_element_by_xpath("//input[@value='Зарегистрироваться']").click()

        mail = self.app.mail.get_mail(username, password, "[MantisBT] Account Registration")
        url = self.extract_confirmation_url(mail)

        wd.get(url)
        wd.find_element_by_name("password").send_keys(password)
        wd.find_element_by_name("password_confirm").send_keys(password)
        wd.find_element_by_xpath("//imput[@value='Update User']").click()

    def extract_confirmation_url(self, text):
        return re.search("http://.*$", text).group(0)