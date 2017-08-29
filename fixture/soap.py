from suds.client import Client
from suds import WebFault

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
        r = self.client.service.mc_projects_get_user_accessible(username, password)
#        r = self.client.service.mc_enum_status("administrator", "password")
#        Some conversion ...
        return r