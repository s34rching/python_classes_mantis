from models.project import Project


def test_add_project(app):
    old_project_list = app.project.get_project_list()
    project = Project(name='some_name12345', description='some_description12345')
    app.project.add_new_project(project.name, project.description)
#    new_project_list = app.project.get_project_list()