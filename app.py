from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

initial_state = ["OFF"] * 16
schedule = {}

def switch_on(index):
    initial_state[index] = "ON"
    print("Switch", (index + 1), "is turned ON")

def switch_off(index):
    initial_state[index] = "OFF"
    print("Switch", (index + 1), "is turned OFF")

def schedule_switch(index, action, hour):
    schedule[index] = (hour, action)

def sense_state(z):
    if z == 'ALL':
        return [(i + 1, state) for i, state in enumerate(initial_state)]
    else:
        return [(int(z), initial_state[int(z) - 1])]

@app.route('/')
def index():
    return render_template('index.html', switches=sense_state('ALL'))

@app.route('/switch', methods=['POST'])
def switch():
    index = int(request.form['index'])
    action = request.form['action']

    if action == 'ON':
        switch_on(index - 1)
    elif action == 'OFF':
        switch_off(index - 1)

    return redirect(url_for('switch_success', action=action))

@app.route('/schedule', methods=['POST'])
def schedule_switch_action():
    index = int(request.form['index'])
    action = request.form['action']
    hour = int(request.form['hour'])

    schedule_switch(index - 1, action, hour)

    return redirect(url_for('schedule_success', action=action, hour=hour))

@app.route('/switch_success')
def switch_success():
    action = request.args.get('action')
    return render_template('success.html', message=f"Switch action '{action}' was added successfully.")

@app.route('/schedule_success')
def schedule_success():
    action = request.args.get('action')
    hour = request.args.get('hour')
    return render_template('success.html', message=f"Switch action '{action}' was scheduled successfully for hour {hour}.")

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
