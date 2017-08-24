# -*- coding: utf-8 -*-
from models.project import Project

class ProjectHelper:

    def __init__(self, app):
        self.app = app

    def open_main_page(self):
        wd = self.app.wd
        wd.find_element_by_xpath("//a[@class='navbar-brand']").click()

    def open_manage_panel(self):
        wd = self.app.wd
        self.open_main_page()
        wd.find_element_by_xpath("//a[@href='/mantisbt-2.5.1/manage_overview_page.php']").click()

    def add_new_project(self, name, description):
        wd = self.app.wd
        self.open_manage_panel()
        self.open_project_panel()
        wd.find_element_by_xpath("//input[@value='создать новый проект']").click()
        wd.find_element_by_xpath("//input[@id='project-name']").click()
        wd.find_element_by_xpath("//input[@id='project-name']").clear()
        wd.find_element_by_xpath("//input[@id='project-name']").send_keys(name)
        wd.find_element_by_xpath("//textarea[@id='project-description']").click()
        wd.find_element_by_xpath("//textarea[@id='project-description']").clear()
        wd.find_element_by_xpath("//textarea[@id='project-description']").send_keys(description)
        wd.find_element_by_xpath("//input[@value='Добавить проект']").click()
        wd.find_element_by_xpath("//a[@href='/mantisbt-2.5.1/manage_proj_page.php']").click()

    def open_project_panel(self):
        wd = self.app.wd
        wd.find_element_by_xpath("//a[@href='/mantisbt-2.5.1/manage_proj_page.php']").click()

    def get_project_list(self):
        wd = self.app.wd
        self.open_manage_panel()
        self.open_project_panel()
        project_table = wd.find_element_by_css_selector('table.table.table-striped.table-bordered.table-condensed.table-hover')
        project_rows = project_table.find_elements_by_xpath("//tbody//tr")
        project_list = []
        for row in project_rows:
            cells = row.find_elements_by_tag_name('td')
            project_name = cells[0].text
            project_description = cells[4].text
            project_list.append(Project(name=project_name, description=project_description))
        return project_list

