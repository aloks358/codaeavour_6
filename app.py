from flask import Flask, render_template, request, redirect, url_for, jsonify

app = Flask(__name__)

# Temporary storage for submitted data
teams = []

@app.route('/submit_team', methods=['GET', 'POST'])
def submit_team():
    if request.method == 'POST':
        # Collect form data
        team_name = request.form['team_name']
        category = request.form['category']
        track = request.form['track']
        username = request.form['username']
        student1 = request.form['student1']
        student2 = request.form['student2']
        student3 = request.form['student3']
        leader = request.form['leader']
        
        # Store team data
        team_data = {
            'team_name': team_name,
            'category': category,
            'track': track,
            'username': username,
            'students': [student1, student2, student3],
            'leader': leader
        }
        teams.append(team_data)
        return redirect(url_for('view_teams'))  # Redirect to a view page

    return render_template('submit_team.html')

@app.route('/view_teams', methods=['GET'])
def view_teams():
    return render_template('view_teams.html', teams=teams)

if __name__ == '__main__':
    app.run(debug=True)
