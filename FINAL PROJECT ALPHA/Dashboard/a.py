import pickle
import pandas as pd

# model = pickle.load('to_dashboard')

with open('to_dashboard','rb') as model:
    Model = pickle.load(model)

kolom = ['backers', 'usd_pledged_real', 'usd_goal_real', 'time_avail',
       'main_category_Art', 'main_category_Comics', 'main_category_Crafts',
       'main_category_Dance', 'main_category_Design', 'main_category_Fashion',
       'main_category_Film & Video', 'main_category_Food',
       'main_category_Games', 'main_category_Journalism',
       'main_category_Music', 'main_category_Photography',
       'main_category_Publishing', 'main_category_Technology',
       'main_category_Theater']
data = [[14,645.0,600,29,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0]]
df = pd.DataFrame(data=data, columns=kolom)

pred = Model.predict(df)[0]
print(pred)