from flask_admin import Admin
from apps.admin.views import admin_views

admin = Admin(name="RestPi-Controller",
              template_mode='bootstrap4')

admin.add_views(*admin_views)
