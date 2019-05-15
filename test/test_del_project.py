from model.project import Project
import random


def test_del_project(app):
    app.session.login("administrator", "root")
    if len(app.project.get_projects_list()) == 0:
        app.project.create(Project(projectname="testing_new"))
    old_projects = app.project.get_projects_list()
    project = random.choice(old_projects)
    app.project.delete(project.projectname)
    new_projects = app.project.get_projects_list()
    assert len(old_projects) - 1 == len(new_projects)
    old_projects.remove(project)
    assert sorted(old_projects, key=Project.id_or_max) == sorted(new_projects, key=Project.id_or_max)
