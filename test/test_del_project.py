from model.project import Project
import random


def test_del_project(app):
    username = "administrator"
    password = "root"
    old_projects = []
    new_projects = []
    app.session.login(username, password)
    if len(app.soap.can_project(username, password)) == 0:
        app.project.create(Project(projectname="testing_new"))
    for name in app.soap.can_project(username, password):
        old_projects.append(name['name'])
    project = random.choice(old_projects)
    app.project.delete(project)
    for name in app.soap.can_project(username, password):
        new_projects.append(name['name'])
    assert len(old_projects) - 1 == len(new_projects)
    old_projects.remove(project)
    assert sorted(old_projects) == sorted(new_projects)
