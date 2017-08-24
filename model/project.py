from sys import maxsize


class Project:

    def __init__(self, name=None, status=None, view_status=None, description=None, project_id=None):
        self.name = name
        self.status = status
        self.view_status = view_status
        self.description = description
        self.project_id = project_id

    def __repr__(self):
        return "%s:%s; %s; %s" % (self.project_id, self.name, self.status, self.description)

    def __eq__(self, other):
        return (self.project_id is None or other.project_id is None or self.project_id == other.project_id) and self.name == other.name

    def id_or_max(gr):
        if gr.project_id:
            return int(gr.project_id)
        else:
            return maxsize