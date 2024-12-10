from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
import pandas as pd

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///teams.db'
db = SQLAlchemy(app)

# Database Models
class Team(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    category = db.Column(db.String(50), nullable=False)
    track = db.Column(db.String(10), nullable=False)
    scores = db.Column(db.String(200), default='{}')  # Store scores as JSON
    total_score = db.Column(db.Float, default=0)

# Initialize the database
with app.app_context():
    db.create_all()

# Home Page
@app.route('/')
def home():
    return render_template('home.html')

# Upload Teams Data
@app.route('/upload_teams', methods=['GET', 'POST'])
def upload_teams():
    if request.method == 'POST':
        file = request.files['file']
        if file:
            data = pd.read_excel(file)
            for _, row in data.iterrows():
                team = Team(name=row['Team Name'], category=row['Category'], track=row['Track'])
                db.session.add(team)
            db.session.commit()
            return redirect(url_for('upload_teams'))
    return render_template('upload_teams.html')

# Scoring Page
@app.route('/score_team', methods=['GET', 'POST'])
def score_team():
    teams = Team.query.all()
    if request.method == 'POST':
        team_id = int(request.form['team_id'])
        scores = {
            'Problem Definition': float(request.form['problem_definition']),
            'Root Cause Analysis': float(request.form['root_cause']),
            'Banner Visual Appeal': float(request.form['banner_visual']),
            'Clarity': float(request.form['clarity']),
            'Theme Relevance': float(request.form['theme_relevance']),
            'Project Alignment': float(request.form['project_alignment']),
            'Creativity': float(request.form['creativity']),
            'Functionality': float(request.form['functionality']),
            'Business Clarity': float(request.form['business_clarity']),
            'Target Market': float(request.form['target_market']),
        }
        total_score = sum(scores.values())
        team = Team.query.get(team_id)
        team.scores = str(scores)
        team.total_score = total_score
        db.session.commit()
        return redirect(url_for('score_team'))
    return render_template('score_team.html', teams=teams)

# Top Teams Page
@app.route('/top_teams', methods=['GET'])
def top_teams():
    teams = Team.query.order_by(Team.total_score.desc()).all()
    top_team = teams[0] if teams else None
    top_five = teams[:5] if teams else []
    return render_template('top_teams.html', top_team=top_team, top_five=top_five)

if __name__ == '__main__':
    app.run(debug=True)
