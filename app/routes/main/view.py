from flask import render_template
from app.routes.main import bp

@bp.route('/')
def main():
    return render_template('main/page.html')


