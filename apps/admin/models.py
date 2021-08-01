from typing import MutableMapping
from flask.helpers import url_for
from flask_admin.contrib.sqla import ModelView
from flask_security import current_user
from wtforms.fields.core import SelectField

from apps.extensions import security
from werkzeug.utils import redirect


class UserModelView(ModelView):

    column_editable_list = ('active',)
    column_exclude_list = ['password', ]

    # def is_accessible(self):
    #     return (current_user.is_active and current_user.is_authenticated)
    # def _handle_view(self, name, **kwargs):
    #     if not self.is_accessible():
    #         return redirect(url_for('security.login'))
