from models.project import Project


def test_add_project(app, json_projects, config):
    project = json_projects
    old_project_list = app.soap.get_project_list(config['webadmin']['username'], config['webadmin']['password'])
    app.project.add_new_project(project.name, project.description)
    new_project_list = app.soap.get_project_list(config['webadmin']['username'], config['webadmin']['password'])
    old_project_list.append(project)
    assert sorted(old_project_list, key = Project.return_name) == sorted(new_project_list, key = Project.return_name)