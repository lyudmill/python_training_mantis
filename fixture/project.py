from model.project import Project


class ProjectHelper:
    project_cash = None

    def __init__(self, app):
        self.app = app

    def create(self, project):
        wd = self.app.wd
        self.open_projects_page()
        # init new project creation
        wd.find_element_by_css_selector("input[value='Create New Project']").click()
        # enter project data
        self.fill_project_form(project)
        # submit created project
        wd.find_element_by_css_selector("input[value=\"Add Project\"]").click()
        wd.find_element_by_partial_link_text("Proceed").click()
        self.project_cash = None

    def open_projects_page(self):
        wd = self.app.wd
        if not wd.current_url.endswith("manage_proj_page.php"):
            self.app.open_home_page()
            wd.find_element_by_link_text("Manage").click()
            wd.find_element_by_link_text("Manage Projects").click()

    def delete_project_by_name(self, name):
        wd = self.app.wd
        self.open_projects_page()
        self.select_project_by_name(name)
        wd.find_element_by_css_selector("input[value='Delete Project']").click()
        #confirm
        wd.find_element_by_css_selector("input[value='Delete Project']").click()
        self.project_cash = None

    def select_project_by_name(self, name):
        wd = self.app.wd
        btn = wd.find_element_by_css_selector("input[value='Create New Project']")
        table = btn.find_element_by_xpath("./../../../..")
        table.find_element_by_link_text(name).click()

    """
    def modify_first_project(self, new_project_data):
        self.modify_project_by_index(0, new_project_data)

    def modify_project_by_index(self, index, new_project_data):
        wd = self.app.wd
        self.open_projects_page()
        # open modification form
        self.select_project_by_index(index)
        wd.find_element_by_name("edit").click()
        # fill project form
        self.fill_project_form(new_project_data)
        # submit modified project
        wd.find_element_by_name("update").click()
        self.return_to_projects_page()
        self.project_cash = None

    def modify_project_by_id(self, new_project_data):
        wd = self.app.wd
        self.open_projects_page()
        self.select_project_by_id(new_project_data.id)
        wd.find_element_by_name("edit").click()
        # fill project form
        self.fill_project_form(new_project_data)
        # submit modified project
        wd.find_element_by_name("update").click()
        self.return_to_projects_page()
        self.project_cash = None   
    """

    def fill_project_form(self, project):
        self.change_field("name", project.name)
        self.select_field_by_text("status", project.status)
        self.change_field("description", project.description)
        #self.change_field("view_status", project.view_status)

    def change_field(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def select_field_by_text(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            element = wd.find_element_by_name(field_name)
            element.find_element_by_xpath("//option[contains(.,'%s')]" % text).click()
            wd.find_element_by_name(field_name).send_keys(text)

    def return_to_projects_page(self):
        wd = self.app.wd
        if not wd.current_url.endswith("manage_proj_page.php"):
            wd.find_element_by_link_text("Proceed").click()

    def count(self):
        return len(self.find_project_table_rows())

    def find_project_table_rows(self):
        wd = self.app.wd
        self.open_projects_page()
        btn = wd.find_element_by_css_selector("input[value='Create New Project']")
        table = btn.find_element_by_xpath("./../../../..")
        rows = table.find_elements_by_css_selector("tr")
        return rows[2:]

    def get_project_list(self):
        if self.project_cash is None:
            wd = self.app.wd
            self.open_projects_page()
            self.project_cash = []
            for element in self.find_project_table_rows():
                fields = element.find_elements_by_css_selector("td")
                name_ref = fields[0].find_element_by_tag_name("a")
                project_id = name_ref.get_attribute("href").split("?")[1].split("=")[1]
                name = name_ref.text
                status = fields[1].text
                view_status = fields[3].text
                description = fields[4].text
                self.project_cash.append(Project(name=name, project_id=project_id, status = status, view_status = view_status, description = description))
        return list(self.project_cash)