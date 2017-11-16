from flask import Flask, render_template, request

from src.predicio import predicio

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/predict', methods=['POST'])
def predict():
    user_data = {
        'age': int(request.form.get('age')),
        'workclass': str(request.form.get('workclass')),
        'education': str(request.form.get('education')),
        'education_number': int(request.form.get('education_number')),
        'marital_status': str(request.form.get('marital_status')),
        'occupation': str(request.form.get('occupation')),
        'relationship': str(request.form.get('relationship')),
        'race': str(request.form.get('race')),
        'sex': str(request.form.get('sex')),
        'capital_gain': float(request.form.get('capital_gain')),
        'capital_loss': float(request.form.get('capital_loss')),
        'hours_per_week': int(request.form.get('hours_per_week')),
        'native_country': str(request.form.get('native_country'))
    }

    return predicio(user_data)


if __name__ == '__main__':
    app.config['TEMPLATES_AUTO_RELOAD'] = True
    app.run()
