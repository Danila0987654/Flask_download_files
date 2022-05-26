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
    if request.method == 'POST':
        print(request.json['Test'])
        filename = excel()
        return filename
    else:
        way = request.args.get('way')
        print(way)
        return send_file(way, mimetype='text/xlsx', as_attachment=True)


# @bp.route('/download_file/')
# def download_file():
#     filename = request.args['filename']
#     # return filename
#     return send_file(filename, mimetype='text/xlsx', as_attachment=True)
