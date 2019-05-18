from model.project import Project
import string
import random


def random_projectname(prefix, maxlen):
    symbols = string.ascii_letters
    return prefix + "".join(random.choice(symbols) for i in range(random.randrange(maxlen)))


def test_add_new_project(app):
    projectname = random_projectname("projectname_", 10)
    project = Project(projectname)
    username = "administrator"
    password = "root"
    app.session.login(username, password)
    old_projects = []
    new_projects = []
    for name in app.soap.can_project(username, password):
        old_projects.append(name['name'])
    app.project.create(project)
    for name in app.soap.can_project(username, password):
        new_projects.append(name['name'])
    assert len(old_projects) + 1 == len(new_projects)
    old_projects.append(project.projectname)
    assert sorted(old_projects) == sorted(new_projects)
