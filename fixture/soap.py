#Check in the file C:\xampp\php\php.ini
# extension=php_soap.dll  is uncommented

from suds.client import Client
from suds import WebFault
from model.project import Project


class SoapHelper:
    def __init__(self, app):
        self.app = app
        self.client = Client("http://localhost/mantisbt-1.2.19/api/soap/mantisconnect.php?wsdl")

    def can_login(self, username, password):
        try:
            self.client.service.mc_login(username, password)
            return True
        except WebFault:
            return False

    def get_project_list(self, username, password):
        soap_project_list = self.client.service.mc_projects_get_user_accessible(username, password)
        project_list = []
        for project_data in soap_project_list:
            project_list.append(Project(project_id=project_data.id, name=project_data.name, status = project_data.status,
                                        view_status = project_data.enabled, description = project_data.description))
        return project_list