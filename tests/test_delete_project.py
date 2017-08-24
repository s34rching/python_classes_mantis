from models.project import Project
import random

def test_delete_project(app):
    if len(app.project.get_project_list()) == 0:
        project = Project(name="emptiness", description="emptiness")
        app.project.add_new_project(project.name, project.description)
    old_project_list = app.project.get_project_list()
    index = random.randrange(len(old_project_list))
    random_group = old_project_list[index]
    app.project.delete_project(index)
    new_project_list = app.project.get_project_list()
    old_project_list.remove(random_group)
    assert sorted(old_project_list, key = Project.return_name) == sorted(new_project_list, key = Project.return_name)