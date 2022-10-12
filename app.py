#  Importing essential libraries
from flask import Flask,render_template,request
import pickle

# Load the Random Forest CLassifier model using pickle
model = pickle.load(open('model.pkl','rb'))



app = Flask(__name__)

@app.route('/')
def index():
          return render_template('index.html')


@app.route('/predict', methods=['GET', 'POST'])
def predict():
    if request.method == 'POST':

        symptom_1 = request.form.get('')
        symptom_2 = request.form.get('')
        symptom_3 = request.form.get('')
        symptom_4 = request.form.get('')
        symptom_5 = request.form.get('')
        symptom_6 = request.form.get('')


        data = np.array([[symptom_1,symptom_2,symptom_3,symptom_4,symptom_5,symptom_6]])
        my_prediction = model.predict(data)

        return render_template('result.html', prediction=my_prediction)

if __name__ == '__main__':
    app.run(debug=True)