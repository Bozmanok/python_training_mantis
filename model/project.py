from sys import maxsize


class Project:

    def __init__(self, projectname=None, status=None, global_categories=None, view_status=None, description=None, id=None):
        self.projectname = projectname
        self.status = status
        self.global_categories = global_categories
        self.view_status = view_status
        self.description = description
        self.id = id

    def __repr__(self):
        return "%s:%s" % (self.id, self.projectname)

    def __eq__(self, other):
        return (self.id is None or other.id is None or self.id == other.id) and \
               (self.projectname is None or other.projectname is None or self.projectname == other.projectname) and \
               (self.status is None or other.status is None or self.status == other.status) and \
               (self.view_status is None or other.view_status is None or self.view_status == other.view_status) and \
               (self.description is None or other.description is None or self.description == other.description)

    def id_or_max(self):
        if self.projectname:
            return self.projectname
        else:
            return maxsize
