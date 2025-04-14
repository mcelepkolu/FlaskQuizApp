# app.py
import os
from flask import Flask, render_template, request, redirect, url_for, session, flash
from flask_login import LoginManager, login_user, logout_user, login_required, current_user
from models import db, User, Quiz, Question, Option, Score
from config import Config

# Initialize Flask app
app = Flask(__name__)
app.config.from_object(Config)

# Initialize extensions
db.init_app(app)
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


# Create database tables within app context
with app.app_context():
    db.create_all()


# Home route - displays available quizzes
@app.route('/')
def index():
    quizzes = Quiz.query.all()

    # Get highest score data
    highest_score = Score.query.order_by(Score.score.desc()).first()

    # Get current user's highest score if logged in
    user_highest_score = None
    if current_user.is_authenticated:
        user_highest_score = Score.query.filter_by(user_id=current_user.id).order_by(Score.score.desc()).first()

    return render_template('index.html',
                           quizzes=quizzes,
                           highest_score=highest_score,
                           user_highest_score=user_highest_score)


# User registration
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')

        user = User.query.filter_by(email=email).first()
        if user:
            flash('Email already exists.')
            return redirect(url_for('register'))

        new_user = User(name=name, email=email)
        db.session.add(new_user)
        db.session.commit()

        login_user(new_user)
        return redirect(url_for('index'))

    return render_template('register.html')


# User login
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')

        user = User.query.filter_by(email=email).first()
        if not user:
            flash('No account found with that email.')
            return redirect(url_for('login'))

        login_user(user)
        return redirect(url_for('index'))

    return render_template('login.html')


# User logout
@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))


# Display quiz questions
@app.route('/quiz/<int:quiz_id>')
def quiz(quiz_id):
    quiz = Quiz.query.get_or_404(quiz_id)
    questions = Question.query.filter_by(quiz_id=quiz_id).all()

    # Get highest score data
    highest_score = Score.query.order_by(Score.score.desc()).first()

    # Get current user's highest score if logged in
    user_highest_score = None
    if current_user.is_authenticated:
        user_highest_score = Score.query.filter_by(user_id=current_user.id, quiz_id=quiz_id).order_by(
            Score.score.desc()).first()

    return render_template('quiz.html',
                           quiz=quiz,
                           questions=questions,
                           highest_score=highest_score,
                           user_highest_score=user_highest_score)


# Process quiz submission
@app.route('/submit/<int:quiz_id>', methods=['POST'])
def submit(quiz_id):
    quiz = Quiz.query.get_or_404(quiz_id)
    questions = Question.query.filter_by(quiz_id=quiz_id).all()

    score = 0
    total_questions = len(questions)

    # Process each question
    for question in questions:
        selected_option_id = request.form.get(f'question_{question.id}')
        if selected_option_id:
            selected_option = Option.query.get(int(selected_option_id))
            if selected_option and selected_option.is_correct:
                score += 1

    # Save score if user is logged in
    if current_user.is_authenticated:
        new_score = Score(
            user_id=current_user.id,
            quiz_id=quiz_id,
            score=score,
            total_questions=total_questions
        )
        db.session.add(new_score)
        db.session.commit()
    else:
        # For anonymous users, store score in session
        session['last_score'] = {
            'quiz_id': quiz_id,
            'score': score,
            'total_questions': total_questions
        }

    return redirect(url_for('results', quiz_id=quiz_id, score=score, total=total_questions))


# Display quiz results
@app.route('/results/<int:quiz_id>')
def results(quiz_id):
    quiz = Quiz.query.get_or_404(quiz_id)

    score = request.args.get('score', 0, type=int)
    total = request.args.get('total', 0, type=int)

    # Get highest score data
    highest_score = Score.query.order_by(Score.score.desc()).first()

    # Get current user's highest score and last score if logged in
    user_highest_score = None
    last_score = None
    if current_user.is_authenticated:
        user_highest_score = Score.query.filter_by(user_id=current_user.id, quiz_id=quiz_id).order_by(
            Score.score.desc()).first()
        last_score = Score.query.filter_by(user_id=current_user.id, quiz_id=quiz_id).order_by(
            Score.created_at.desc()).first()

    return render_template('results.html',
                           quiz=quiz,
                           score=score,
                           total=total,
                           highest_score=highest_score,
                           user_highest_score=user_highest_score,
                           last_score=last_score)


if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)