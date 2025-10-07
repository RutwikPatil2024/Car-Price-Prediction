from flask import Flask,render_template,request
import numpy as np
import pandas as pd
import pickle as pkl

ds=pd.read_csv("clean_data.csv")
pipeMLR=pkl.load(open("MLR.pkl","rb"))

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home/home.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/car-project")
def car_project():
    companies=sorted(ds["company"].unique())
    names=sorted(ds["name"].unique())
    return render_template("car-project.html",companies=companies,names=names)

@app.route("/car-project-result")
def carprojectresult():
    company=request.args.get("company")
    name=request.args.get("name")
    year=request.args.get("year")
    kms_driven=request.args.get("kms_driven")
    fuel_type=request.args.get("fuel_type")


    data={
        "company":company,
        "name":name,
        "year":year,
        "kms_driven":kms_driven,
        "fuel_type":fuel_type
    }

    mydata=[name,company,year,kms_driven,fuel_type]
    columns=["name","company","year","kms_driven","fuel_type"]
    df=pd.DataFrame(columns=columns,data=np.array(mydata).reshape(1,5))
    result=round(pipeMLR.predict(df)[0,0])

    return render_template("car-project-result.html",data=data,result=result)

if __name__ == "__main__":
    app.run(debug=True)


# (old_env) D:\coding\Python Program\Machine Learning\Project>
# run project in this environment