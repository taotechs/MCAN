from flask import render_template, flash, redirect, url_for, request, jsonify
from flask_login import login_required, current_user
from . import members
from .. import db
from ..models import User, Profile

@members.route('/profile')
@login_required
def profile():
    return render_template('members/profile.html', user=current_user)

@members.route('/directory')
@login_required
def directory():
    members = User.query.join(Profile).all()
    return render_template('members/directory.html', members=members)

@members.route('/api/profile', methods=['PUT'])
@login_required
def update_profile():
    data = request.get_json()
    if not data:
        return jsonify({'error': 'No data provided'}), 400
    
    try:
        profile = current_user.profile
        for key, value in data.items():
            if hasattr(profile, key):
                setattr(profile, key, value)
        
        db.session.commit()
        return jsonify({'message': 'Profile updated successfully'})
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500 