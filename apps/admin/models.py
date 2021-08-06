from flask_admin.contrib.sqla import ModelView
from flask_login import current_user
from flask import redirect, url_for


class SecureModelView(ModelView):

    """Base Class for protected views.

    Classes that derive from this class will only be accessible by authenticted users

    """
    # attributes added to secure /admin url paths

    def is_accessible(self):
        return (current_user.is_active and current_user.is_authenticated)

    # def _handle_view(self, name, **kwargs):
    #     if not self.is_accessible():
    #         return redirect(url_for('security.login'))


class UserModelView(ModelView):

    #column_editable_list = ('active',)
    column_exclude_list = ['password', "date_modified"]
    column_list = ['email', 'date_created', 'active']


class SensorModelView(ModelView):

    column_exclude_list = ["date_modified"]
