from datetime import date
from flask import Flask, redirect, session, render_template, request, url_for, abort, make_response, jsonify, make_response
import pymongo, time, os
import cryptocode
# from flask_bcrypt import Bcrypt

client = pymongo.MongoClient("mongodb+srv://root:root123@realmcluster.rbqar.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
db=client.website
collection=None
collection_pwd=db.user
app=Flask(__name__, static_folder="static", static_url_path="/")
app.config['SECRET_KEY']=os.urandom(120)
app.config["SESSION_COOKIE_NAME"]="dnjnf2y%24"
# sect=f"{os.urandom(513)}"
sect="hujhnjvsk76879679oyHUKJBDGUYVH786876%R^$#%$#$^&YTGHDt78%D^(&Tygvukj"
# app.permanent_session_lifetime=datetime.timedelta(seconds=1*60)
# session.permanent=True
def clearfnc():
    session.pop("account")
    res=redirect("/login")
    res.delete_cookie("user")
    return res

def state_check_bool():
    # if session["account"]==None:
    #     return False
    # else:
    #     return True
    if request.cookies.get("user")=="" or request.cookies.get("user")==None:
        return False
    else:
        return True

def state_output():
    datas={}
    if state_check_bool():
        datas["user"]=(session["account"])
        datas["click"]="logout()"
    else:
        datas["user"]="登入"
        datas["click"]="window.location.href='/login'"
    return datas    

def acce_required():
    datas={}
    # if session["account"]!=None:
    if request.cookies.get("user")=="" or request.cookies.get("user")==None:
        datas["user"]="登入"
        datas["click"]="window.location.href='/login'"
        datas["state"]="0"
    else:
        datas["user"]=cryptocode.decrypt(request.cookies.get("user"), sect) 
        datas["click"]="logout()"
        datas["state"]="1"
    return datas

@app.before_request
def login_required():
    # try:
    #     if session["account"]==None:
    #         return None
    # except:
    #     session["account"]=None
    #     return None
    try:
        if request.cookies.get("users")=="":
            return None
        else:
            return None
    except:
        res=redirect("/")
        res.set_cookie("user", "")
        return res

@app.errorhandler(404)
def err_handler(e):
    return """
    <h3>查無此頁面</h3>
    <a href="/">回首頁</a></br>
    <title>404查無頁面</title>
    """

@app.errorhandler(500)
def err_handler(e):
    return """
    <h3>有些地方出錯了</h3>
    <a href="/">回首頁</a></br>
    <title>500 error</title>
    """

@app.errorhandler(405)
def err_handler(e):
    return redirect("/")

@app.route("/term")
def term():
    return render_template("term.html") 

@app.route("/delet")
def deletf():
    if state_check_bool():
        return render_template("del.html", userdata=acce_required())
    else:
        return redirect("/login")

@app.route("/update_db")
def upd():
    pass

@app.route("/") # main
def indexdd():
    return render_template("index.html", userdata=acce_required())

@app.route("/assign")
def ass():
    # if state_check_bool:
    #     return redirect("/")
    # else:

    return render_template("signup.html",  userdata=acce_required())

@app.route("/login")
def login():
    return render_template("signin.html",  userdata=acce_required())

@app.route("/main")
def assas():
    if state_check_bool():
        return render_template("main.html", userdata=acce_required())
    else:
        return redirect("/login")

@app.route("/res", methods=["POST"])
def res():
    if state_check_bool():
        # collection=db[f"users_{session['account']}"]
        sp=cryptocode.decrypt(request.cookies.get("user"), sect) 
        collection=db[f"users_{sp}"]
        company=request.form["company"]
        years=request.form["year"]
        eps_1=request.form["EPS_1"]
        eps_2=request.form["EPS_2"]
        eps_3=request.form["EPS_3"]
        eps_4=request.form["EPS_4"]
        m_1=request.form["m_1"]
        m_2=request.form["m_2"]
        m_3=request.form["m_3"]
        m_4=request.form["m_4"]
        m_5=request.form["m_5"]
        m_6=request.form["m_6"]
        m_7=request.form["m_7"]
        m_8=request.form["m_8"]
        m_9=request.form["m_9"]
        m_10=request.form["m_10"]
        m_11=request.form["m_11"]
        m_12=request.form["m_12"]
        dividend_rate=request.form["dividend_rate"]
        last_update=request.form["date"]
        share=request.form["share"]
        share=round(float(share), 2)
        dividend_rate=round(float(dividend_rate), 2)
        if (m_1=="" and m_2==""):
            eps_1=float(eps_1)
            eps_2=float(eps_2)
            eps_3=float(eps_3)
            eps_4=float(eps_4)
            eps_year=eps_1+eps_2+eps_3+eps_4
        else:
            m_1=float(m_1)
            m_2=float(m_2)
            m_3=float(m_3)
            m_4=float(m_4)
            m_5=float(m_5)
            m_6=float(m_6)
            m_7=float(m_7)
            m_8=float(m_8)
            m_9=float(m_9)
            m_10=float(m_10)
            m_11=float(m_11)
            m_12=float(m_12)
            eps_year=m_1+m_2+m_3+m_4+m_5+m_6+m_7+m_8+m_9+m_10+m_11+m_12
        divend=(float(dividend_rate)*float(eps_year)*0.01)
        divend=round(divend, 2)
        yield_=((float(dividend_rate)*float(eps_year))/float(share))
        yield_=round(float(yield_), 2)
        try:
            datas_get=collection.find()
            data_get=[]
            company_list=[]
            for i in datas_get:
                data_get.append(i)
                company_list.append(i["company"])
            if data_get[0]==None: # none data in DB
                collection.insert_one({
                "company":company,
                "date":last_update,
                "share":share,
                years:{
                    "EPS_year":eps_year,
                    "EPS_Q1":eps_1,
                    "EPS_Q2":eps_2,
                    "EPS_Q3":eps_3,
                    "EPS_Q4":eps_4,
                    "EPS_m_1":m_1,
                    "EPS_m_2":m_2,
                    "EPS_m_3":m_3,
                    "EPS_m_4":m_4,
                    "EPS_m_5":m_5,
                    "EPS_m_6":m_6,
                    "EPS_m_7":m_7,
                    "EPS_m_8":m_8,
                    "EPS_m_9":m_9,
                    "EPS_m_10":m_10,
                    "EPS_m_11":m_11,
                    "EPS_m_12":m_12,
                    "dividend_rate":dividend_rate, 
                    "dividend":divend, 
                    "yield":yield_, 
                }
            })
            for i in data_get:
                if i['company']==company: 
                    collection.update_one({
                        "company":company
                    },{
                        "$set":{
                            "date":last_update,
                            "share":share,
                            years:{
                                "EPS_year":eps_year,
                                "EPS_Q1":eps_1,
                                "EPS_Q2":eps_2,
                                "EPS_Q3":eps_3,
                                "EPS_Q4":eps_4,
                                "EPS_m_1":m_1,
                                "EPS_m_2":m_2,
                                "EPS_m_3":m_3,
                                "EPS_m_4":m_4,
                                "EPS_m_5":m_5,
                                "EPS_m_6":m_6,
                                "EPS_m_7":m_7,
                                "EPS_m_8":m_8,
                                "EPS_m_9":m_9,
                                "EPS_m_10":m_10,
                                "EPS_m_11":m_11,
                                "EPS_m_12":m_12,
                                "dividend_rate":dividend_rate,
                                "dividend":divend,
                                "yield":yield_,
                            }
                        }
                    })
            else: # nothing exist
                non_exi=0
                for i in company_list:
                    if i != company:
                        non_exi+=1
                else:
                    if non_exi==len(company_list):
                        collection.insert_one({
                            "company":company,
                            "date":last_update,
                            "share":share,
                            (years):{
                                "EPS_year":eps_year,
                                "EPS_Q1":eps_1,
                                "EPS_Q2":eps_2,
                                "EPS_Q3":eps_3,
                                "EPS_Q4":eps_4,
                                "EPS_m_1":m_1,
                                "EPS_m_2":m_2,
                                "EPS_m_3":m_3,
                                "EPS_m_4":m_4,
                                "EPS_m_5":m_5,
                                "EPS_m_6":m_6,
                                "EPS_m_7":m_7,
                                "EPS_m_8":m_8,
                                "EPS_m_9":m_9,
                                "EPS_m_10":m_10,
                                "EPS_m_11":m_11,
                                "EPS_m_12":m_12,
                                "dividend_rate":dividend_rate, 
                                "dividend":divend,
                                "yield":yield_,
                                "guess":1
                            }
                        })

        except: # out of thinking
            collection.insert_one({
                "company":company,
                "date":last_update,
                "share":share,
                years:{
                    "EPS_year":eps_year,
                    "EPS_Q1":eps_1,
                    "EPS_Q2":eps_2,
                    "EPS_Q3":eps_3,
                    "EPS_Q4":eps_4,
                    "EPS_m_1":m_1,
                    "EPS_m_2":m_2,
                    "EPS_m_3":m_3,
                    "EPS_m_4":m_4,
                    "EPS_m_5":m_5,
                    "EPS_m_6":m_6,
                    "EPS_m_7":m_7,
                    "EPS_m_8":m_8,
                    "EPS_m_9":m_9,
                    "EPS_m_10":m_10,
                    "EPS_m_11":m_11,
                    "EPS_m_12":m_12,
                    "dividend_rate":dividend_rate,
                    "dividend":divend,
                    "yield":yield_,
                }
            })
        return redirect("/dis")
    else:
        return clearfnc()

@app.route("/dis")
def display(): # sorting data
    if state_check_bool():
        # collection=db[f"users_{session['account']}"]
        sp=cryptocode.decrypt(request.cookies.get("user"), sect) 
        collection=db[f"users_{sp}"]
        datas=collection.find()
        data_clus=[]
        year_clus={}
        year_doc=[]
        company_clus=[]
        output_doc={}
        output_clus=[]
        for i in datas:
            data_clus.append(i)
            for f in i:
                if f=="company":
                    company_clus.append(i["company"])
                if f!="_id" and f!="company" and f!="date" and f!="guess" and f!="share" and f!="yield_now" and f!="aim" and f!="l_aim" and f != "l_add" and f!="r_add":
                    year_doc.append(f)
            else:
                year_clus[i["company"]]=sorted(list(map(int, year_doc)))
                year_doc=[]
        fram=0
        for company_n in year_clus:
            output_doc["company"]=company_n
            output_doc["date"]=data_clus[fram]["date"]
            output_doc["share"]=data_clus[fram]["share"]
            try:
                output_doc["aim"]=data_clus[fram]["aim"]
            except:
                output_doc["aim"]=""
            try:
                output_doc["yield_now"]=(data_clus[fram][time.strftime('%Y',time.gmtime())]["yield"])
            except:
                pass
            try:
                if data_clus[fram]["aim"]!="":
                    eps_aim=round(100*(float(data_clus[fram][time.strftime('%Y',time.gmtime())]["dividend"]))/(float(data_clus[fram]["aim"])),2)
                    output_doc["l_aim"]=eps_aim
                    eps_add=eps_aim-float(data_clus[fram]["share"])
                    output_doc["l_add"]=round(eps_add,2)
                    output_doc["r_add"]=round(100*eps_add/float(data_clus[fram]["share"]),2)
            except:
                pass
            for year_ in year_clus[company_n]:
                output_doc[year_]=data_clus[fram][str(year_)]
            else:
                output_clus.append(output_doc)
                output_doc={}
            fram+=1
        
        return render_template("display.html", data=output_clus)
    else:
        return redirect("/login")

@app.route("/rev", methods=["POST"]) # 更新
def revise():
    # collection=db[f"users_{session['account']}"]
    sp=cryptocode.decrypt(request.cookies.get("user"), sect) 
    print(sp)
    collection=db[f"users_{sp}"]
    datas=collection.find()
    data_clus=[]
    year_clus={}
    year_doc=[]
    company_clus=[]
    date=request.form["up_dt"]
    for i in datas:
        data_clus.append(i)
        for f in i:
            if f=="company":
                company_clus.append(i["company"])
            if f!="_id" and f!="company" and f!="date" and f!="guess" and f!="share"  and f!="yield_now" and f!="aim"  and f!="l_aim"  and f != "l_add" and f != "r_add":
                year_doc.append(f)
        else:
            year_clus[i["company"]]=year_doc
            year_doc=[]  
    st=False
    for cp_n in company_clus:
        for years in year_clus[cp_n]:
            for da_c in data_clus:
                if da_c["company"]==cp_n:
                    if da_c[years]["EPS_Q1"]!="":
                        st=True
                    else:
                        st=False
            if st:
                eps_q_1=round((float(request.form[f"{cp_n}_{years}_Q_1"])), 3)
                eps_q_2=round((float(request.form[f"{cp_n}_{years}_Q_2"])), 3)
                eps_q_3=round((float(request.form[f"{cp_n}_{years}_Q_3"])), 3)
                eps_q_4=round((float(request.form[f"{cp_n}_{years}_Q_4"])), 3)
                eps_q_y=float(eps_q_1)+float(eps_q_2)+float(eps_q_3)+float(eps_q_4)
                eps_q_y=round(eps_q_y, 3)
                dividend=round((float(request.form[f"{cp_n}_{years}_dividend"])), 2)
                share=round((float(request.form[f"{cp_n}_share"])), 2)
                dividend_rate=round(100*(float(dividend/eps_q_y)), 2)
                yield_=round(100*(float(dividend/share)), 2)
                if request.form[f"{cp_n}_aim"]!="":
                    aim=round((float(request.form[f"{cp_n}_aim"])), 2)
                else:
                    aim=""
                collection.update_one({
                    "company":cp_n
                },{
                    "$set":{
                        "date":date,
                        "share":share,
                        "aim":aim,
                        years:{ 
                            "EPS_year":eps_q_y,
                            "EPS_m_1":"",
                            "EPS_m_2":"",
                            "EPS_m_3":"",
                            "EPS_Q1":eps_q_1,
                            "EPS_Q2":eps_q_2,
                            "EPS_Q3":eps_q_3,
                            "EPS_Q4":eps_q_4,
                            "dividend_rate":dividend_rate,
                            "dividend":dividend,
                            "yield":yield_,
                        }
                    }
                })
            else:
                eps_m_1=round((float(request.form[f"{cp_n}_{years}_m_1"])), 3)
                eps_m_2=round((float(request.form[f"{cp_n}_{years}_m_2"])), 3)
                eps_m_3=round((float(request.form[f"{cp_n}_{years}_m_3"])), 3)
                eps_m_4=round((float(request.form[f"{cp_n}_{years}_m_4"])), 3)
                eps_m_5=round((float(request.form[f"{cp_n}_{years}_m_5"])), 3)
                eps_m_6=round((float(request.form[f"{cp_n}_{years}_m_6"])), 3)
                eps_m_7=round((float(request.form[f"{cp_n}_{years}_m_7"])), 3)
                eps_m_8=round((float(request.form[f"{cp_n}_{years}_m_8"])), 3)
                eps_m_9=round((float(request.form[f"{cp_n}_{years}_m_9"])), 3)
                eps_m_10=round((float(request.form[f"{cp_n}_{years}_m_10"])), 3)
                eps_m_11=round((float(request.form[f"{cp_n}_{years}_m_11"])), 3)
                eps_m_12=round((float(request.form[f"{cp_n}_{years}_m_12"])), 3)
                eps_y=eps_m_1+eps_m_2+eps_m_3+eps_m_4+eps_m_5+eps_m_6+eps_m_7+eps_m_8+eps_m_9+eps_m_10+eps_m_11+eps_m_12
                dividend=round((float(request.form[f"{cp_n}_{years}_dividend"])), 2)
                share=round((float(request.form[f"{cp_n}_share"])), 2)
                dividend_rate=round(100*(float(dividend/eps_y)), 2)
                yield_=round(100*(float(dividend/share)), 2)
                if request.form[f"{cp_n}_aim"]!="":
                    aim=round((float(request.form[f"{cp_n}_aim"])), 2)
                else:
                    aim=""
                collection.update_one({
                    "company":cp_n
                },{
                    "$set":{
                        "share":share,
                        "date":date,
                        "aim":aim,
                        years:{
                            "EPS_year":eps_y,
                            "EPS_m_1":eps_m_1,
                            "EPS_m_2":eps_m_2,
                            "EPS_m_3":eps_m_3,
                            "EPS_m_4":eps_m_4,
                            "EPS_m_5":eps_m_5,
                            "EPS_m_6":eps_m_6,
                            "EPS_m_7":eps_m_7,
                            "EPS_m_8":eps_m_8,
                            "EPS_m_9":eps_m_9,
                            "EPS_m_10":eps_m_10,
                            "EPS_m_11":eps_m_11,
                            "EPS_m_12":eps_m_12,
                            "EPS_Q1":"",
                            "EPS_Q2":"",
                            "dividend_rate":dividend_rate,
                            "dividend":dividend,
                            "yield":yield_,
                        }
                    }
                })
    return render_template("redirecting.html")

@app.route("/simp") # 簡化
def simplify():
    # collection=db[f"users_{session['account']}"]
    sp=cryptocode.decrypt(request.cookies.get("user"), sect) 
    collection=db[f"users_{sp}"]
    datas=collection.find()
    year_now=int(time.strftime('%Y',time.gmtime()))
    data_clus=[]
    company_clus=[]
    for i in datas:
        data_clus.append(i)
        for f in i:
            if f=="company":
                company_clus.append(i["company"])
            if f!="_id" and f!="company" and f!="date" and f!="guess" and f!="share" and f!="yield_now" and f!="aim" and f!="l_aim" and f != "l_add" and f!="r_add":
                if int(f) < year_now-1:
                    collection.update_one({
                        "company":i["company"]
                    },{"$set":{
                        f:{
                            "EPS_year":i[f]["EPS_year"],
                            "dividend_rate":i[f]["dividend_rate"],
                            "dividend":i[f]["dividend"],
                            "yield":i[f]["yield"],
                            "simp":1
                        }
                    }})
    return redirect("/dis")

@app.route("/del", methods=["POST"])
def delete():
    # collection=db[f"users_{session['account']}"]
    sp=cryptocode.decrypt(request.cookies.get("user"), sect) 
    collection=db[f"users_{sp}"]

    try:
        company=request.form["company"]
        year=request.form["year"]
        company_del=request.form["company_del"]
    except:
        pass
    datas=collection.find()
    get_one=0
    year_che=0
    for i in datas:
        if i["company"]==company or i["company"]==company_del:
            get_one+=1
            for f in i:
                if f!="_id" and f!="company" and f!="date" and f!="guess" and f!="share" and f!="yield_now" and f!="aim" and f!="l_aim" and f != "l_add" and f!="r_add":
                    if f==year:
                        year_che+=1
    if get_one!=1 or year_che<1: #exi
        return jsonify({"sta":0})
    if company_del=="":
        try:
            collection.update_one({
                "company":company
            },{"$unset":{
                year:1,
            }})
        except:
            return jsonify({"sta":0})
    elif company_del!="":
        try:
            collection.delete_one({"company":company_del})
        except:
            return jsonify({"sta":0})
    
    ## 資料為空時刪除
    have=0
    for i in datas:
        print(i)
        for f in i:
            if f!="_id" and f!="company" and f!="date" and f!="guess" and f!="share" and f!="yield_now" and f!="aim" and f!="l_aim" and f != "l_add" and f!="r_add":
                have+=1
        if have ==0:
            collection.delete_one({"company":company_del}) 
    # return redirect("/dis")
    return jsonify({"sta":1}) #Ajax

@app.route("/signin", methods=["POST"])
def signin():
    account=request.form["account"]
    pwd=request.form["pwd"]
    data=collection_pwd.find()
    for i in data:
        if i["account"]==account:
            # if Bcrypt().check_password_hash(i["password"], pwd):
            if i["password"]==pwd:
                # session["account"]=account

                res=jsonify({"issue":0})
                res.set_cookie("user", cryptocode.encrypt(account, sect), max_age=8000, httponly=True)
                # res.set_cookie("user", account, max_age=9000)
                return res
            else:
                # session["account"]=None
                return jsonify({"issue":1}) # 密碼錯誤
    # session["account"]=None
    return jsonify({"issue":2}) # 無帳號

@app.route("/signup", methods=["POST"])
def signup():
    user_name=request.form["usn"]
    account=request.form["acc"]
    pwd=request.form["pwd"]
    # pwd=Bcrypt().generate_password_hash(pwd).decode("utf-8")
    data=collection_pwd.find()
    repeat=0
    for i in data:
        if i["account"]==account:
            repeat+=1
        else:
            repeat+=0
    if repeat==0:
        collection_pwd.insert_one({
            "name":user_name,
            "account":account,
            "password":pwd
        })
        return jsonify({"state":1})
    else:
        return jsonify({"state":0, "rep":account, "n":user_name})

@app.route("/signout")
def signout():
    res=redirect("/")
    res.set_cookie("user","")
    return res

@app.route("/dis_new")
def dis_new():
    if state_check_bool():
        sp=cryptocode.decrypt(request.cookies.get("user"), sect) 
        collection=db[f"users_{sp}"]
        amount=collection.find().count()
        return render_template("dis_aja.html", times=amount)
    else:
        return redirect("/login")

@app.route("/dis_ajx", methods=["POST"])
def display_ajx(): # sorting data
    if state_check_bool():
        times=int(request.form.get("tmc"))
        # collection=db[f"users_{session['account']}"]
        sp=cryptocode.decrypt(request.cookies.get("user"), sect) 
        collection=db[f"users_{sp}"]
        datas=collection.find()
        data_clus=[]
        year_clus={}
        year_doc=[]
        company_clus=[]
        output_doc={}
        output_clus=[]
        for i in datas:
            data_clus.append(i)
            for f in i:
                if f=="company":
                    company_clus.append(i["company"])
                if f!="_id" and f!="company" and f!="date" and f!="guess" and f!="share" and f!="yield_now" and f!="aim" and f!="l_aim" and f != "l_add" and f!="r_add":
                    year_doc.append(f)
            else:
                year_clus[i["company"]]=map(str,(sorted(list(map(int, year_doc)))))
                year_doc=[]
        fram=0
        for company_n in year_clus:
            output_doc["company"]=company_n
            output_doc["date"]=data_clus[fram]["date"]
            output_doc["share"]=data_clus[fram]["share"]
            try:
                output_doc["aim"]=data_clus[fram]["aim"]
            except:
                output_doc["aim"]=""
            try:
                output_doc["yield_now"]=(data_clus[fram][time.strftime('%Y',time.gmtime())]["yield"])
            except:
                pass
            try:
                if data_clus[fram]["aim"]!="":
                    eps_aim=round(100*(float(data_clus[fram][time.strftime('%Y',time.gmtime())]["dividend"]))/(float(data_clus[fram]["aim"])),2)
                    output_doc["l_aim"]=eps_aim
                    eps_add=eps_aim-float(data_clus[fram]["share"])
                    output_doc["l_add"]=round(eps_add,2)
                    output_doc["r_add"]=round(100*eps_add/float(data_clus[fram]["share"]),2)
            except:
                pass
            for year_ in year_clus[company_n]:
                output_doc[year_]=data_clus[fram][str(year_)]
            else:
                output_clus.append(output_doc)
                output_doc={}
            fram+=1
        
        return jsonify(output_clus[times])
    else:
        return "None session found"

@app.route("/little_game_1_had")
def game1():
    return render_template("ltg-01-cprt.html")

@app.route("/dis_new2faddfncoeew")
def nd2():
    return render_template("dis_new.html")

@app.route("/ajaxUpdate", methods=["POST"])
def procUni():
    if state_check_bool():
        # collection=db[f"users_{session['account']}"]
        sp=cryptocode.decrypt(request.cookies.get("user"), sect) 
        collection=db[f"users_{sp}"]
        state=int(request.form.get("state"))
        companySelector=request.form.get("company")
        shareNew=float(request.form.get("share"))
        aimNew=(request.form.get("aim"))
        dates=request.form.get("date")
        detail_list_string=request.form.get("detail")
        yearly_data=detail_list_string.split("/")
        yearly_data.remove("")
        for i in yearly_data:
            datas=list(map(float, i.split("_"))) # datas索引設計一覽 0: 年分 // 1-4or12: Q1-Q4orM1-M12 // 5or13: 配息
            if state==1:
                ey=datas[1]+datas[2]+datas[3]+datas[4]+datas[5]+datas[6]+datas[7]+datas[8]+datas[9]+datas[10]+datas[11]+datas[12]
                collection.update_one({
                    "company":companySelector
                },{
                    "$set":{
                        "share":shareNew,
                        "date":dates,
                        "aim":aimNew,
                        str(int(datas[0])):{
                            "EPS_year":round(ey, 2),
                            "EPS_m_1":round(datas[1], 2),
                            "EPS_m_2":round(datas[2], 2),
                            "EPS_m_3":round(datas[3], 2),
                            "EPS_m_4":round(datas[4], 2),
                            "EPS_m_5":round(datas[5], 2),
                            "EPS_m_6":round(datas[6], 2),
                            "EPS_m_7":round(datas[7], 2),
                            "EPS_m_8":round(datas[8], 2),
                            "EPS_m_9":round(datas[9], 2),
                            "EPS_m_10":round(datas[10], 2),
                            "EPS_m_11":round(datas[11], 2),
                            "EPS_m_12":round(datas[12], 2),
                            "EPS_Q1":"",
                            "dividend_rate":round((100*datas[13]/ey), 2),
                            "dividend":round(datas[13], 2),
                            "yield":round(100*datas[13]/shareNew, 2),
                        }
                    }
                })
            else:
                if state==0:
                    collection.update_one({
                        "company":companySelector
                    },{
                        "$set":{
                            "date":dates,
                            "share":round(shareNew,2),
                            "aim":(aimNew),
                            str(int(datas[0])):{ 
                                "EPS_year":round((datas[1]+datas[2]+datas[3]+datas[4]), 2),
                                "EPS_m_1":"",
                                "EPS_Q1":round(datas[1], 2),
                                "EPS_Q2":round(datas[2], 2),
                                "EPS_Q3":round(datas[3], 2),
                                "EPS_Q4":round(datas[4], 2),
                                "dividend_rate":round(100*datas[5]/(datas[1]+datas[2]+datas[3]+datas[4]), 2),
                                "dividend":round(datas[5], 2),
                                "yield":round(100*(datas[5]/shareNew), 2),
                            }
                        }
                    })
        return jsonify(dates)
    else:
        return ""


app.run()