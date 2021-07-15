from flask import Flask, redirect, url_for, render_template,request
app=Flask(__name__)

@app.route('/')
def welcome():
    return render_template('index.html')


@app.route('/underweight/<float:score>')
def underweight(score):
    res=""
    if score<18.5:
        res="underweight"
        feed="please thoda khao yaar!!!!! your bmi is: "
    else:
        res="overweight"
    return render_template("bmi.html", result=res,comment=feed,score=score)
    
    
@app.route('/fit/<float:score>')
def fit(score):
    res=""
    if score>18.5 and score<24.5:
        res="fit"
        feed="lage raho bhai!!!!! your bmi is: "
    else:
        res="overweight"
    return render_template("bmi.html", result=res,comment=feed,score=score)



@app.route('/overweight/<float:score>')
def overweight(score):
    res=""
    if score>24.5:
        res="overweight"
        feed="thoda kam khao yaar bahut mote ho gaye ho!!!!! your bmi is: "
    else:
        res="fit"
    return render_template("bmi.html", result=res,comment=feed,score=score)




@app.route('/results/<float:marks>')
def results(marks):
    result=""
    if marks<18.5:
        result= "underweight"
    elif marks>18.5 and marks<24.5:
        result= "fit"
    else:
        result= "overweight"
    return redirect(url_for(result,score=marks))





@app.route('/submit',methods=['POST','GET'])
def submit():
    total_score=0
    if request.method=="POST":
        science=float(request.form["weight"])
        Maths=float(request.form["height"])
        m=Maths*0.3
        total_score=(science/(m**2))
        
    res=""
    if total_score<18.5:
        res="underweight"
    elif total_score>18.5 and total_score<24.5:
        res="fit"
    else:
        res="overweight" 
    return redirect(url_for(res,score=total_score))

    
if __name__=="__main__":
    app.run()