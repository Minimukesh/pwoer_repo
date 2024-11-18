import pandas as pd
import numpy as np 
from flask import Flask , request ,  jsonify , render_template
from utility import EnergyConsum

app = Flask(__name__)

@app.route('/')
def energy_model():
    print('Wel-come to Power consumption model, lets predict todays power consumption')
    return render_template('index.html')

@app.route('/predict_energy' , methods= ['GET' , 'POST'])
def get_user_input():
    data = request.args
    p_name = data['Product_Name']
    b_size = data['Batch_Size']
    nop = data['Nature_of_Product']
    ath = eval(data['AHU_Time_Hr'])
    rth = eval(data['RMG_Time_Hr'])
    fth = eval(data['FBD_Time_Hr'])
    cth = eval(data['Comp_Time_Hr'])
    coth =eval( data['Coating_Time_Hr'])
    ith = eval(data['Inspection_Time_Hr'])

    e_obj = EnergyConsum(p_name , b_size , nop , ath , rth ,fth ,cth ,coth , ith)
    prediction = e_obj.get_energy_pred()
    return jsonify({'Power Consumption is' :f' {prediction} KWH'})

        



if __name__=='__main__':
    app.run(host='0.0.0.0' , port=5002 , debug=True)

