from flask import Blueprint
from flask import render_template

admin_bp = Blueprint('admin_bp', __name__, template_folder='templates', static_folder='static')


@admin_bp.route('/')
def admin():
    return render_template('admin.html', title='Admin Control Panel')
