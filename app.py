from flask import Flask, render_template, request
import pickle

app = Flask(__name__)


@app.route('/')
def index():
   return render_template('home.html')


@app.route('/predict',methods=['POST'])

def predict():


    if request.method == 'POST':
        message = request.form['message']
        data = [message.lower()]
        
        model = pickle.load(open('classifier.pkl','rb')) 
        my_prediction =model.predict(data)[0]

        
        d = {'0':'hate speech','1':'offensive language','2':'neither hate nor offensive'}
    
    return render_template('result.html',prediction = d[str(my_prediction)])
   

if __name__ == '__main__':
	app.run(debug=True, host='0.0.0.0', port=12345)

#0.0.0.0 rester dans docker

