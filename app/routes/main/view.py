from flask import render_template, request, redirect, send_file, url_for
import json

from app.routes.main import bp
from app.services.create_excel import excel


@bp.route('/')
def main():
    account_id = request.args.get('account_id')
    # return render_template('base.html')
    return render_template('base.html')


@bp.route('/create_excel/', methods=['POST', 'GET'])
def export_excel():
    filename = excel()
    return redirect(url_for('main.download_file', filename=filename))


@bp.route('/download_file/')
def download_file():
    filename = request.args['filename']
    # return filename
    return send_file(filename, mimetype='text/xlsx', as_attachment=True)
