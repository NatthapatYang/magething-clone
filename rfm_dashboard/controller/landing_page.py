from flask import Blueprint, render_template

bp = Blueprint('landing_page', __name__)

@bp.route('/rfm',methods=['GET','POST'])
def index():
    from ..models.get_rfm_data import get_rfm_data
    rfm_data = get_rfm_data()
    return render_template('index.html', rfm_data=rfm_data)