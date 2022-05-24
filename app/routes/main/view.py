from flask import render_template, request, redirect, send_file, url_for

from app.routes.main import bp
from app.services.create_excel import excel


@bp.route('/')
def main():
    account_id = request.args.get('account_id')
    # return render_template('base.html')
    return render_template('base.html')


@bp.route('/create_excel/', methods=['POST'])
def export_excel():
    filename = excel()
    return redirect(url_for('main.download_file'))


@bp.route('/download_file/')
def download_file():
    return 'filename'
