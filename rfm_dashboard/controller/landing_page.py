from flask import Blueprint, render_template
from rfm_dashboard.models.rfm_data import *

bp = Blueprint('landing_page', __name__)

@bp.route('/rfm', methods=['GET'])
def index():
    rfm_data = get_rfm_data()
    r_percent = get_r_percent()
    f_percent = get_f_percent()
    m_percent = get_m_percent()
    group_r_percent = [(keys, values) for i, (keys, values) in enumerate(zip(rfm_data.keys(), r_percent))]
    group_f_percent = [(keys, values) for i, (keys, values) in enumerate(zip(rfm_data.keys(), f_percent))]
    group_m_percent = [(keys, values) for i, (keys, values) in enumerate(zip(rfm_data.keys(), m_percent))]

    return render_template('landing/barchart.html', group_r_percent=group_r_percent, group_f_percent=group_f_percent, group_m_percent=group_m_percent)