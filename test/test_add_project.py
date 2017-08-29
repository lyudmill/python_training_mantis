# -*- coding: utf-8 -*-
from model.project import Project


def test_add_project_soap(app, data_project):
    project = data_project
    old_projects = app.soap.get_project_list(app.config['webadmin']["username"], app.config['webadmin']["password"])
    app.project.create(project)
    new_projects = app.soap.get_project_list(app.config['webadmin']["username"], app.config['webadmin']["password"])
    old_projects.append(project)
    assert sorted(old_projects,key=Project.id_or_max) ==sorted(new_projects,key=Project.id_or_max)


def test_add_project(app, data_project):
    project = data_project
    old_projects = app.project.get_project_list()
    app.project.create(project)
    new_projects = app.project.get_project_list()
    old_projects.append(project)
    assert sorted(old_projects,key=Project.id_or_max) ==sorted(new_projects,key=Project.id_or_max)
