# main.py

from flask import Blueprint, render_template, redirect, url_for, request, flash
from flask_login import login_required, current_user
import os
import random
from models import Computation, db
import time
from utils import RandomGaussElimination

main = Blueprint('main', __name__)
number = random.randint(1,100)


@main.route('/',  methods=['GET','POST'])
@login_required
def index():
    if request.method == 'POST':
        try:
            n = int(request.form['number_of_unknowns'])
            left, right = float(request.form['left']), float(request.form['right'])
            start = time.time()
            RandomGaussElimination(n=n, left=left, right=right)
            c = Computation(number_of_unknowns=n,
                            left_bound=left,
                            right_bound=right,
                            computation_time=time.time() - start,
                            user_id = current_user.id)
            db.session.add(c)
            db.session.commit()
        except:
            flash('Invalid input data')
            return redirect(url_for('main.index'))
    return render_template('index.html', number= number)



@main.route("/history", methods=['GET'] )
@login_required
def history():
    if current_user.is_authenticated:
        current_user
        history = Computation.query.filter_by(user_id=current_user.id).all()
        return render_template('history.html', user=current_user, history=history)
    return redirect(url_for('auth.login'))  


@main.route('/', defaults={'path': ''})
@main.route('/<path:path>')
def catch_all(path):
    return redirect(url_for('main.index'))