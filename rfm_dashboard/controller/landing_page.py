from flask import Blueprint, render_template
from ..models.get_rfm_data import get_rfm_data

bp = Blueprint('landing_page', __name__)

@bp.route('/rfm',methods=['GET','POST'])
def index():
    rfm_data = get_rfm_data()
    return render_template('index.html', rfm_data=rfm_data)