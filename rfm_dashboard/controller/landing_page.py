from flask import Blueprint, render_template
from rfm_dashboard.models.rfm_data import get_rfm_data, bar_chart_score

bp = Blueprint('landing_page', __name__)

@bp.route('/rfm', methods=['GET'])
def index():
    rfm_data = get_rfm_data()
    r_percent, f_percent, m_percent = bar_chart_score()

    return render_template('landing/barchart.html', rfm_data=rfm_data, r_percent=r_percent, f_percent=f_percent, m_percent=m_percent)