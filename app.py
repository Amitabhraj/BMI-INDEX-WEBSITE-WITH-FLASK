from flask import Flask, redirect, url_for, render_template,request
import math
app=Flask(__name__)


@app.route('/')
def welcome():
    return render_template('index.html')


@app.route('/underweight/<float:score>')
def underweight(score):
    res=""
    if score<18.5:
        res="underweight"
        feed="Please thoda khao yaar!! Your bmi is just: "
    return render_template("bmi.html", result=res,comment=feed,score=score)
    
    
@app.route('/fit/<float:score>')
def fit(score):
    res=""
    if score>18.5 and score<24.5:
        res="fit"
        feed="Lage raho bhai!! Your bmi is: "
    return render_template("bmi.html", result=res,comment=feed,score=score)



@app.route('/overweight/<float:score>')
def overweight(score):
    res=""
    if score>24.5:
        res="overweight"
        feed="Thoda kam khao yaar bahut mote ho gaye ho!! Your bmi is: "
        extra=",Which is too much"
    return render_template("bmi.html", result=res,comment=feed,score=score,ex=extra)





@app.route('/submit_feet',methods=['POST','GET'])
def submit_feet():
    if request.method=="POST":
        Weight=int(request.form["weight"])
        Heightf=int(request.form["heightf"])
        Heighti=int(request.form["heighti"])
        
            
        converted=(Heightf*12)+Heighti
        meter=converted/39.37
        BMI=(Weight/(meter**2))
        BMI_str=str(BMI)
        approx_num=BMI_str[0:4]

        
    if Heightf>0 and Weight>3 and Heighti<=11 and Heighti>=0 and BMI<=18.5 : 
        res="underweight"
        return redirect(url_for(res,score=approx_num))
    
    
    elif Heightf>0 and Weight>3 and Heighti<=11 and Heighti>=0 and BMI>18.5 and BMI<24.5:
        res="fit"
        return redirect(url_for(res,score=approx_num))
    
    
    elif Heightf >0 and Weight>3 and Heighti<=11 and Heighti>=0 and BMI>=24.5:
        res="overweight"
        return redirect(url_for(res,score=approx_num))
    
    
    elif Weight<=3 and (Heighti>=12 or Heighti<0) and Heightf<=0:
        F_w_i_f="please type 'weight' more than 3 and type 'inch' between 0 to 12 and type 'feet' more than 0"
        return render_template("wrong inch.html",wrong=F_w_i_f)
    
    
    elif Weight<=3 and (Heighti>=12 or Heighti<0):
        F_w_i="please type 'weight' more than 3 and type 'inch' between 0 to 12"
        return render_template("wrong inch.html",wrong=F_w_i)
    
    
    elif Weight<=3 and Heightf<=0:
        F_w_f="please type 'weight' more than 3 and type 'feet' more than 0"
        return render_template("wrong inch.html",wrong=F_w_f)
    
    
    elif (Heighti>=12 or Heighti<0) and Heightf<=0:
        F_i_f="please type 'inch' between 0 to 12 and type 'feet' more than 0"
        return render_template("wrong inch.html",wrong=F_i_f)


    elif (Heighti>=12 or Heighti<0):
        F_i="please type 'Inch' between 0 to 12"
        return render_template("wrong inch.html",wrong=F_i)
    
    
    elif Weight<=3:
        F_w="please type 'Weight' more than 3"
        return render_template("wrong inch.html",wrong=F_w)
    
    
    
    elif Heightf<=0:
        F_f="please Type 'feet' more than 0"
        return render_template("wrong inch.html",wrong=F_f)












@app.route('/submit_cm',methods=['POST','GET'])
def submit_cm():
    if request.method=="POST":
        Weight=int(request.form["weight"])
        Height=float(request.form["cm"])
        
            
        meter=Height/100
        BMI=(Weight/(meter**2))
        BMI_str=str(BMI)
        approx_num=BMI_str[0:4]

        
    if Height>30 and Weight>3 and BMI<=18.5 : 
        res="underweight"
        return redirect(url_for(res,score=approx_num))
    
    
    
    elif Height>30 and Weight>3 and BMI>18.5 and BMI<24.5:
        res="fit"
        return redirect(url_for(res,score=approx_num))
    
    
    
    elif Height>30 and Weight>3 and BMI>=24.5:
        res="overweight"
        return redirect(url_for(res,score=approx_num))
    
    
    
    elif Height<30 and Weight<=3:
        cm_h_w="please type 'cm' more than 30 and type 'weight' more than 3"
        return render_template("wrong inch.html", wrong=cm_h_w)
    
    
    elif Height<30:
        cm_h="please type 'cm' more than 30"
        return render_template("wrong inch.html", wrong=cm_h)
    
    
    elif Weight<=3:
        cm_w="please type Weight' more than 3"
        return render_template("wrong inch.html", wrong=cm_w)
    







@app.route('/submit_meter',methods=['POST','GET'])
def submit_meter():
    if request.method=="POST":
        Weight=int(request.form["weight"])
        meter=float(request.form["meter"])
        
        BMI=(Weight/(meter**2))
        BMI_str=str(BMI)
        approx_num=BMI_str[0:4]

        
    if Weight>3 and meter>0.3 and BMI<=18.5 : 
        res="underweight"
        return redirect(url_for(res,score=approx_num))
    
    
    
    elif Weight>3 and meter>0.3 and BMI>18.5 and BMI<24.5:
        res="fit"
        return redirect(url_for(res,score=approx_num))
    
    
    
    elif Weight>3 and meter>0.3 and BMI>=24.5:
        res="overweight"
        return redirect(url_for(res,score=approx_num))
    
    
    
    elif Weight<=3 and meter<=0.3:
        M_w_m="please Type 'Weight' more than 3 and type 'Meter' more than 0.3"
        return render_template("wrong inch.html",wrong=M_w_m)
    
    
    
    elif meter<=0.3 :
        M_m="please type 'Meter' more than 0.3"
        return render_template("wrong inch.html",wrong=M_m)
    
    
    
    elif Weight<=3 :
        M_w="please Type 'Weight' more than 3"
        return render_template("wrong inch.html",wrong=M_w)
    
    



@app.route('/sub',methods=['POST','GET'])
def feet_inch():
    if request.method=="POST":
        measure=request.form["measure"]
    if measure=="feet.inch":
        return render_template("feet.html")
    elif measure=="cm":
        return render_template("cm.html")
    elif measure=="meter":
        return render_template("meter.html")
    else:
        return "Error"







if __name__=="__main__":
    app.run()
