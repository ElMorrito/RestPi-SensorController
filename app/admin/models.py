from flask_admin.model import BaseModelView


class UserModelView(ModelView):
    column_exclude_list = ['password', ]
