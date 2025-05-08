from flask import render_template, redirect, request, url_for, flash
from flask_login import login_user, logout_user, login_required, current_user
from . import auth
from .. import db
from ..models import User, Profile
from .forms import LoginForm, RegistrationForm, ProfileForm

@auth.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('main.index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user is not None and user.verify_password(form.password.data):
            login_user(user, form.remember_me.data)
            next = request.args.get('next')
            if next is None or not next.startswith('/'):
                next = url_for('main.index')
            return redirect(next)
        flash('Invalid email or password.', 'error')
    return render_template('auth/login.html', form=form)

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    flash('You have been logged out.', 'success')
    return redirect(url_for('main.index'))

@auth.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('main.index'))
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(
            email=form.email.data,
            username=form.username.data,
            password=form.password.data
        )
        db.session.add(user)
        db.session.commit()
        
        # Create profile
        profile = Profile(
            user_id=user.id,
            full_name=form.full_name.data,
            phone=form.phone.data,
            lga=form.lga.data,
            batch=form.batch.data,
            ppa=form.ppa.data,
            profession=form.profession.data
        )
        db.session.add(profile)
        db.session.commit()
        
        flash('You can now login.', 'success')
        return redirect(url_for('auth.login'))
    return render_template('auth/register.html', form=form)

@auth.route('/profile', methods=['GET', 'POST'])
@login_required
def profile():
    form = ProfileForm()
    if form.validate_on_submit():
        current_user.profile.full_name = form.full_name.data
        current_user.profile.phone = form.phone.data
        current_user.profile.address = form.address.data
        current_user.profile.lga = form.lga.data
        current_user.profile.batch = form.batch.data
        current_user.profile.ppa = form.ppa.data
        current_user.profile.profession = form.profession.data
        current_user.profile.bio = form.bio.data
        
        if form.profile_picture.data:
            # Handle profile picture upload
            pass
            
        db.session.commit()
        flash('Your profile has been updated.', 'success')
        return redirect(url_for('auth.profile'))
        
    elif request.method == 'GET':
        form.full_name.data = current_user.profile.full_name
        form.phone.data = current_user.profile.phone
        form.address.data = current_user.profile.address
        form.lga.data = current_user.profile.lga
        form.batch.data = current_user.profile.batch
        form.ppa.data = current_user.profile.ppa
        form.profession.data = current_user.profile.profession
        form.bio.data = current_user.profile.bio
        
    return render_template('auth/profile.html', form=form) 