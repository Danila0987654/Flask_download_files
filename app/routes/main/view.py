from flask import render_template, request

from app.routes.main import bp
from app.services.create_excel import excel


@bp.route('/')
def main():
    account_id = request.args.get('account_id')
    return render_template('base.html')


@bp.route('/create_excel/', methods=['POST'])
def export_excel():
    test = excel()
    return test
