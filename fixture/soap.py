from suds.client import Client
from suds import WebFault


class SoapHelper:

    def __init__(self, app):
        self.app = app

    def can_login(self, username, password):
        client = self.client_link()
        try:
            client.service.mc_login(username, password)
            return True
        except WebFault:
            return False

    def can_project(self, username, password):
        client = self.client_link()
        try:
            list = client.service.mc_projects_get_user_accessible(username, password)
            return list
        except WebFault:
            return False

    def client_link(self):
        return Client("http://localhost/mantisbt-1.2.20/api/soap/mantisconnect.php?wsdl")
