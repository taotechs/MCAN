from flask import render_template, request, flash, redirect, url_for
from datetime import datetime
from ..models import Event, News, Project
from app import db
from . import main

@main.route('/')
def index():
    # Get featured events, news, and projects
    events = Event.query.filter(Event.date >= datetime.utcnow()).order_by(Event.date).limit(3).all()
    news_items = News.query.order_by(News.date.desc()).limit(3).all()
    projects = Project.query.order_by(Project.created_at.desc()).limit(3).all()
    return render_template('main/index.html', events=events, news_items=news_items, projects=projects)

@main.route('/about')
def about():
    return render_template('main/about.html')

@main.route('/events')
def events():
    events = Event.query.filter(Event.date >= datetime.utcnow()).order_by(Event.date).all()
    return render_template('main/events.html', events=events)

@main.route('/executives')
def executives():
    return render_template('main/executives.html')

@main.route('/teams')
def teams():
    return render_template('main/teams.html')

@main.route('/projects')
def projects():
    projects = Project.query.order_by(Project.created_at.desc()).all()
    return render_template('main/projects.html', projects=projects)

@main.route('/camp')
def camp():
    return render_template('main/camp.html')

@main.route('/lodges')
def lodges():
    return render_template('main/lodges.html')

@main.route('/education')
def education():
    return render_template('main/education.html')

@main.route('/gallery')
def gallery():
    return render_template('main/gallery.html')

@main.route('/news')
def news():
    news_items = News.query.order_by(News.date.desc()).all()
    return render_template('main/news.html', news_items=news_items)

@main.route('/contact')
def contact():
    return render_template('main/contact.html')

@main.route('/donate', methods=['GET', 'POST'])
def donate():
    if request.method == 'POST':
        amount = request.form.get('amount')
        name = request.form.get('name')
        email = request.form.get('email')
        message = request.form.get('message')
        
        # Here you would typically integrate with a payment gateway
        # For now, we'll just flash a success message
        flash('Thank you for your donation! We will contact you shortly.', 'success')
        return redirect(url_for('main.donate'))
    
    return render_template('main/donate.html')

@main.context_processor
def inject_now():
    return {'now': datetime.utcnow()} 