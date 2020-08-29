from flask import Flask, render_template, request
import pickle
import pandas as pd
global d1

app = Flask(__name__)
@app.route('/',methods=['POST','GET'])
def home():
    return render_template('index.html')
@app.route('/result',methods=['POST','GET'])
def result():
    if request.method=='POST':
        input = request.form
        a = float(input['a'])
        c = float(input['c'])
        d = input['d']
        e = float(input['e'])

        if d == 'Category: Art':
            d1 = [a,c,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,e]
        elif d == 'Category: Comics':
            d1 = [a,c,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,e]
        elif d == 'Category: Crafts':
            d1 = [a,c,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,e]
        elif d == 'Category: Dance':
            d1 = [a,c,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,e]
        elif d == 'Category: Design':
            d1 = [a,c,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,e]
        elif d == 'Category: Fashion':
            d1 = [a,c,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,e]
        elif d == 'Category: Film and Video':
            d1 = [a,c,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,e]
        elif d == 'Category: Food':
            d1 = [a,c,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,e]
        elif d == 'Category: Games':
            d1 = [a,c,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,e]
        elif d == 'Category: Journalism':
            d1 = [a,c,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,e]
        elif d == 'Category: Music':
            d1 = [a,c,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,e]
        elif d == 'Category: Photography':
            d1 = [a,c,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,e]
        elif d == 'Category: Publishing':
            d1 = [a,c,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,e]
        elif d == 'Category: Technology':
            d1 = [a,c,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,e]
        elif d == 'Category: Theater':
            d1 = [a,c,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,e]
        else:
            pass
        kolom = ['backers', 'usd_goal_real', 'time_avail',
       'main_category_Art', 'main_category_Comics', 'main_category_Crafts',
       'main_category_Dance', 'main_category_Design', 'main_category_Fashion',
       'main_category_Film & Video', 'main_category_Food',
       'main_category_Games', 'main_category_Journalism',
       'main_category_Music', 'main_category_Photography',
       'main_category_Publishing', 'main_category_Technology',
       'main_category_Theater']

        data = [d1]
        df = pd.DataFrame(data=data, columns=kolom)
        pred = Model.predict(df)[0]
        return render_template('result.html',data=input,prediksi=pred)

if __name__ == '__main__':
    with open('to_dashboard','rb') as model:
        Model = pickle.load(model)
    app.run(debug=True)