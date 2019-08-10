from flask import Flask, render_template, request, redirect, url_for
app = Flask('server')

#The Routes
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def processing_dojo_survey():
    studentNameFromForm = request.form['student_name']
    locationFromForm = request.form['dojo_location']
    commentFromForm = request.form['comment']
    decitionFromForm = request.form['the_decision']

    #Processing Checklist so the list can be printed as a single string.
    fave_language_from_form = request.form.getlist('fave_language')
    fave_language_from_form = [str(i) for i in fave_language_from_form]
    res = (", ".join(fave_language_from_form))

    return redirect(f'/result/{studentNameFromForm}/{locationFromForm}/{commentFromForm}/{decitionFromForm}/{res}')

@app.route('/result/<student_name>/<location>/<comment>/<decision>/<fave_languages>')
def show_results(student_name,location, comment, decision, fave_languages):

    return render_template("result.html", student_name_on_template=student_name, location_on_template=location, fave_language_on_template=fave_languages, comment_on_template=comment, decision_on_tamplate=decision)

if __name__ == "__main__":
    app.run(debug=True)
