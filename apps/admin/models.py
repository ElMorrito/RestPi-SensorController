from flask_admin.contrib.sqla import ModelView


class UserModelView(ModelView):

    column_editable_list = ('active',)
    column_exclude_list = ['password', ]
