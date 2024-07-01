from flask import Blueprint, render_template
from rfm_dashboard.models.rfm_data import *

bp = Blueprint('landing_page', __name__)

@bp.route('/rfm', methods=['GET'])
def index():
    rfm_data = processor.get_rfm_data()
    group_r_percent, group_f_percent, group_m_percent = processor.group_rfm_percent()

    return render_template('landing/barchart.html', rfm_data=rfm_data, group_r_percent=group_r_percent, group_f_percent=group_f_percent, group_m_percent=group_m_percent)