from OFS.Folder import Folder


def add_school(context):
    """Add school"""
    context._setObject('school', School())


class School(Folder):
    """School"""
    meta_type = "School"


def initialize(context):
    context.registerClass(School, constructors=(add_school,))
