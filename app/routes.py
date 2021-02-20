"""Route declaration."""
from flask import current_app as app
from flask import render_template

from .forms import ContactForm


@app.route('/')
def home():
    """Landing Page"""
    nav = [
        {'name': 'Home', 'url': 'https://example.com/1'},
        {'name': 'About', 'url': 'https://example.com/2'},
        {'name': 'Pics', 'url': 'https://example.com/3'}
    ]
    return render_template(
        'home.html',
        nav_items=nav,
        title="Jinja Demo Site",
        description="Smarter page templates with Flask & Jinja."
    )


@app.route('/admin/')
def admin_panel():
    """Panel"""
    return "Admin Panel"


@app.route('/admin/<name>/')
def admin(name):
    """Admin Page"""
    return "Admin {}".format(name)


@app.route("/contact", methods=["GET", "POST"])
def contact():
    """Handle form data"""
    return "Contact page"
