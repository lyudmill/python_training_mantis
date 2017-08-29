from model.project import Project
import random



def test_delete_project_soap(app):
    if app.project.count() == 0:
        app.project.create(Project(name="name for delete"))
    old_projects = app.soap.get_project_list(app.config['webadmin']["username"], app.config['webadmin']["password"])
    project = random.choice(old_projects)
    print(project)
    app.project.delete_project_by_name(project.name)
    new_projects = app.soap.get_project_list(app.config['webadmin']["username"], app.config['webadmin']["password"])
    assert len(old_projects) - 1 == len(new_projects)
    old_projects.remove(project)
    assert sorted(old_projects, key=Project.id_or_max) == sorted(new_projects, key=Project.id_or_max)

def test_delete_project(app):
    if app.project.count() == 0:
        app.project.create(Project(name="name for delete"))
    old_projects = app.project.get_project_list()
    project = random.choice(old_projects)
    print(project)
    app.project.delete_project_by_name(project.name)
    new_projects = app.project.get_project_list()
    assert len(old_projects) - 1 == len(new_projects)
    old_projects.remove(project)
    assert sorted(old_projects, key=Project.id_or_max) == sorted(new_projects, key=Project.id_or_max)
