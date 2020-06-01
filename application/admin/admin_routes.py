from flask import Blueprint
from flask import render_template

admin_bp = Blueprint('admin_bp', __name__, template_folder='templates', static_folder='static')


@admin_bp.route('/admin')
def admin():
    """Procedura ce afiseaza panoul de control pentru administrarea bazei de date ce contine informatiile necesare
    simularii, luate din meciurile de Hattrick.

    Parametri:
    ----------
    Niciunul.

    Intoarce:
    ----------
    Nimic."""

    return render_template('admin.html', title='Admin Control Panel')
