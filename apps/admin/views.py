from flask_admin.contrib.sqla import ModelView
from flask_admin.base import AdminIndexView
from flask_login import current_user
from flask import redirect, url_for, request


class SecureModelView(ModelView):

    """Base Class for protected views.

    Classes that derive from this class will only be accessible by authenticted users
    """
    # attributes added to secure /admin url paths

    def is_accessible(self):
        return current_user.is_authenticated

    def inaccessible_callback(self, name, **kwargs):
        # redirect to login page if user doesn't have access
        return redirect(url_for('auth.login', next=request.url))
    # def _handle_view(self, name, **kwargs):
    #     if not self.is_accessible():
    #         return redirect(url_for('security.login'))


class UserModelView(SecureModelView):

    #column_editable_list = ('active',)
    column_exclude_list = ['password', "date_modified"]
    column_list = ['email', 'date_created', 'is_active']


class SensorModelView(ModelView):

    column_exclude_list = ["date_modified"]
