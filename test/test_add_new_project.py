from model.project import Project


def test_add_new_project(app):
    project = Project(projectname="testing32")
    app.session.login("administrator", "root")
    old_projects = app.project.get_projects_list()
    app.project.create(project)
    new_projects = app.project.get_projects_list()
    assert len(old_projects) + 1 == len(new_projects)
    old_projects.append(project)
    assert sorted(old_projects, key=Project.id_or_max) == sorted(new_projects, key=Project.id_or_max)
