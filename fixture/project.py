from model.project import Project
from selenium.webdriver.support.select import Select


class ProjectHelper:

    def __init__(self, app):
        self.app = app

    def open_page_projects(self):
        wd = self.app.wd
        if not wd.current_url.endswith("/manage_proj_create_page.php"):
            wd.find_element_by_link_text("Manage").click()
            wd.find_element_by_link_text("Manage Projects").click()

    def create(self, project):
        wd = self.app.wd
        self.open_page_projects()
        wd.find_element_by_xpath("//input[@value='Create New Project']").click()
        self.fill_contact_form(project)
        wd.find_element_by_xpath("//input[@value='Add Project']").click()
        self.return_to_projects_page()
        self.project_cache = None

    def delete(self, project_name):
        wd = self.app.wd
        self.open_page_projects()
        self.open_project_page(project_name)
        wd.find_element_by_xpath("//input[@value='Delete Project']").click()
        wd.find_element_by_xpath("//input[@value='Delete Project']").click()
        self.project_cache = None

    def fill_contact_form(self, project):
        self.change_field_value("name", project.projectname)
        self.change_select_field_value("status", project.status)
        self.change_checkbox_value("inherit_global", project.global_categories)
        self.change_select_field_value("view_state", project.view_status)
        self.change_field_value("description", project.description)

    def change_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def change_select_field_value(self, select_name, value):
        wd = self.app.wd
        if value is not None:
            wd.find_element_by_name(select_name).click()
            Select(wd.find_element_by_name(select_name)).select_by_visible_text(value)

    def change_checkbox_value(self, checkbox_name, bool_value):
        wd = self.app.wd
        if bool_value == "X":
            wd.find_element_by_name(checkbox_name).click()

    def open_project_page(self, project_name):
        wd = self.app.wd
        wd.find_element_by_link_text(project_name).click()

    def return_to_projects_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("Proceed").click()

    project_cache = None

    def get_projects_list(self):
        if self.project_cache is None:
            wd = self.app.wd
            self.open_page_projects()
            self.project_cache = []
            list_row_1 = wd.find_elements_by_css_selector("tr.row-1")
            list_row_2 = wd.find_elements_by_css_selector("tr.row-2")
            list_projects = list_row_1 + list_row_2
            for element in list_projects:
                cells = element.find_elements_by_tag_name("td")
                projectname = cells[0].text
                if projectname != "General":
                    self.project_cache.append(Project(projectname=projectname))
        return list(self.project_cache)
