from flask_admin.contrib.sqla import ModelView
from flask_security import current_user
from flask import redirect, url_for


class SecureModelView(ModelView):

    """Base Class for protected views.

    Classes that derive from this class will only be accessible by authenticted users

    """
    # attributes added to secure /admin url paths

    def is_accessible(self):
        return (current_user.is_active and current_user.is_authenticated)

    def _handle_view(self, name, **kwargs):
        if not self.is_accessible():
            return redirect(url_for('security.login'))


class UserModelView(SecureModelView):

    column_editable_list = ('active',)
    column_exclude_list = ['password', "date_modified"]


class SensorModelView(ModelView):

    column_choices = {
        'sensor_category': [('Temperature', 'Humidity'), ]
    }

    column_exclude_list = ['password', "date_created"]
