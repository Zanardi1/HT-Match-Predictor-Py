from flask import Blueprint
from flask import render_template
from application.admin import delete_db

admin_bp = Blueprint('admin_bp', __name__, template_folder='templates', static_folder='static')


@admin_bp.route('/admin')
def admin():
    return render_template('admin.html', title='Admin Control Panel')


@admin_bp.route('/delete')
def delete():
    delete_db.delete_database()
