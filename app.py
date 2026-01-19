from flask import Flask, render_template, request, session
from quiz_data import QUIZ

app = Flask(__name__)
app.secret_key = "quiz_secret_key"

app.jinja_env.globals.update(enumerate=enumerate)

@app.route("/")
def index():
    return render_template("index.html", sections=QUIZ.keys())

@app.route("/quiz/<section>", methods=["GET", "POST"])
def quiz(section):
    questions = QUIZ[section]

    if request.method == "POST":
        score = 0
        review = []

        for i, q in enumerate(questions):
            user_ans = request.form.get(f"q{i}")
            correct_ans = q[2]

            is_correct = user_ans == correct_ans
            if is_correct:
                score += 1

            review.append({
                "question": q[0],
                "correct": correct_ans,
                "selected": user_ans,
                "is_correct": is_correct
            })

        total = len(questions)
        percentage = round((score / total) * 100, 2)

        # highest score (session-based)
        if "highest" not in session:
            session["highest"] = score
        else:
            session["highest"] = max(session["highest"], score)

        return render_template(
            "result.html",
            score=score,
            total=total,
            percentage=percentage,
            highest=session["highest"],
            review=review
        )

    return render_template("quiz.html", section=section, questions=questions)

if __name__ == "__main__":
    app.run(debug=True)
