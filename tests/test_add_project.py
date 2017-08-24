from models.project import Project


def test_add_project(app, json_projects):
    project = json_projects
    old_project_list = app.project.get_project_list()
    app.project.add_new_project(project.name, project.description)
    new_project_list = app.project.get_project_list()
    old_project_list.append(project)
    assert sorted(old_project_list, key = Project.return_name) == sorted(new_project_list, key = Project.return_name)