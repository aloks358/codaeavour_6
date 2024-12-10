from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Temporary storage for team scores
team_scores = []

@app.route('/score_team', methods=['GET', 'POST'])
def score_team():
    if request.method == 'POST':
        # Collect scoring data from the form
        team_name = request.form['team_name']
        problem_definition = int(request.form['problem_definition'])
        root_cause = int(request.form['root_cause'])
        banner_visual = int(request.form['banner_visual'])
        clarity = int(request.form['clarity'])
        theme_relevance = int(request.form['theme_relevance'])
        project_alignment = int(request.form['project_alignment'])
        creativity = int(request.form['creativity'])
        functionality = int(request.form['functionality'])
        business_clarity = int(request.form['business_clarity'])
        target_market = int(request.form['target_market'])

        # Calculate total score
        total_score = sum([
            problem_definition, root_cause, banner_visual, clarity,
            theme_relevance, project_alignment, creativity,
            functionality, business_clarity, target_market
        ])

        # Save the score
        score_data = {
            'team_name': team_name,
            'scores': {
                'Problem Definition': problem_definition,
                'Root Cause Analysis': root_cause,
                'Banner Visual Appeal': banner_visual,
                'Clarity': clarity,
                'Theme Relevance': theme_relevance,
                'Project Alignment': project_alignment,
                'Creativity': creativity,
                'Functionality': functionality,
                'Business Clarity': business_clarity,
                'Target Market': target_market,
            },
            'total_score': total_score
        }
        team_scores.append(score_data)

        return redirect(url_for('view_scores'))  # Redirect to view scores page

    return render_template('score_team.html')


@app.route('/view_scores', methods=['GET'])
def view_scores():
    return render_template('view_scores.html', team_scores=team_scores)


if __name__ == '__main__':
    app.run(debug=True)
