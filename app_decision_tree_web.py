# importing the necessary dependencies
from flask import Flask, render_template, request, jsonify
from flask_cors import CORS, cross_origin

from wsgiref import simple_server
# from sklearn.tree import DecisionTreeClassifier
import pickle

app = Flask(__name__)  # initializing a flask app


@app.route('/', methods=['GET'])  # route to display the home page
@cross_origin()
def homePage():
    return render_template("index.html")


@app.route('/predict', methods=['POST', 'GET'])  # route to show the predictions in a web UI
@cross_origin()
def index():
    if request.method == 'POST':
        try:
            #  reading the inputs given by the user
            Pclass = float(request.form['Pclass'])
            Sex = float(request.form['Sex'])
            Age = float(request.form['Age'])
            SibSp = float(request.form['SibSp'])
            Parch = float(request.form['Parch'])
            Fare = float(request.form['Fare'])
            filename = 'modelFordec_tree_Prediction.sav'

            loaded_model = pickle.load(open(filename, 'rb'))  # loading the model file from the storage
            # predictions using the loaded model file

            prediction = loaded_model.predict([[Pclass, Sex, Age, SibSp, Parch, Fare]])
            print('prediction is', prediction)
            # showing the prediction results in a UI
            if prediction[0] == 0:
                result = 'The person did not survive'
            elif prediction[0] ==1:
                result = 'The person survived'
            return render_template('results.html', result=result)
        except Exception as e:
            print('The Exception message is: ', e)
            return 'something is wrong'
    # return render_template('results.html')
    else:
        return render_template('index.html')


if __name__ == "__main__":
    app.run(debug=True)
    # port = int(os.getenv("PORT"))
    # host = '0.0.0.0'
    # httpd = simple_server.make_server(host=host,port=5000, app=app)
    # print("localhost:5000")
    # httpd.serve_forever()
