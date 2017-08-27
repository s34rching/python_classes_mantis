from suds.client import Client
from suds import WebFault
from fixtures.project import Project


class SoapHelper:

    def __init__(self, app):
        self.app = app

    def can_login(self, username, password):
        client = Client("http://localhost/mantisbt-2.5.1/api/soap/mantisconnect.php?wsdl")
        try:
            client.service.mc_login(username, password)
            return True
        except WebFault:
            return False

    def get_project_list(self, username, password):
        projects = []
        client = Client("http://localhost/mantisbt-2.5.1/api/soap/mantisconnect.php?wsdl")
        try:
            project_list = client.service.mc_projects_get_user_accessible(username, password)
            for project in project_list:
                name = project[1]
                description = project[7]
                projects.append(Project(name=name, description=description))
            return projects
        except WebFault:
            return False