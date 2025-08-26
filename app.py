from flask import Flask
from flask import request, render_template, redirect, url_for

item = dict(task="", completed=False)
tasks = list()
task_id_counter = 0

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    global task_id_counter
    if request.method == 'POST':
        form_data = request.form['task']
        tasks.append({'id': task_id_counter, 'task': form_data, 'completed': False})
        task_id_counter += 1
        return redirect(url_for('index'))
    return render_template('index.html', tasks=tasks)

@app.route('/complete/<int:task_id>')
def complete(task_id):
    for task in tasks:
        if task['id'] == task_id:
            task['completed'] = not task['completed']
            break
    return redirect(url_for('index'))

if __name__ == "__main__":
    app.run(debug=True)