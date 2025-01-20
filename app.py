import requests
# import json
import pandas as pd
import numpy as np
from pandas import json_normalize

# def fetch_data(a):
#     try:
#         res=requests.get(a)
#         if(res.status_code==200): return res.json()
#         else: raise Exception ("Failed to fetch data.")
#     except Exception as e:
#         print(e)
#         return None
    
quiz_endpoint=requests.get('https://www.jsonkeeper.com/b/LLQT').json()
quiz_endpoint_df=pd.DataFrame(quiz_endpoint)

quiz_submission_data=requests.get('https://api.jsonserve.com/rJvd7g').json()
quiz_submission_df=json_normalize(quiz_submission_data)

historical_data=requests.get('https://api.jsonserve.com/XgAgFJ').json()
historical_df=json_normalize(historical_data)

historical_df['accuracy'] = historical_df['accuracy'].replace(' %','',regex=True).astype(float)
historical_df['accuracy']=pd.to_numeric(historical_df['accuracy'],errors='coerce')

topic_performance = historical_df.groupby('quiz.topic').agg(
    avg_score=('score','mean'),
    avg_accuracy = ('accuracy','mean')
).reset_index()

conditions=[
    (topic_performance['avg_accuracy']<=30),
    (topic_performance['avg_accuracy']>30)&(topic_performance['avg_accuracy']<=60),
    (topic_performance['avg_accuracy']>60)&(topic_performance['avg_accuracy']<=80),
    (topic_performance['avg_accuracy']>80)
]
labels=['Weak','Average','Good','Strong']

topic_performance['topic-strength']=np.select(conditions,labels,default='Unknown')
print("topicwise analysis\n",topic_performance)

strength_order=['Weak','Average','Good','Strong']
topic_performance['topic-strength']=pd.Categorical(topic_performance['topic-strength'],categories=strength_order,ordered=True)
curated_list=topic_performance.sort_values('topic-strength')

print("Curated list for improving:\n")
print(curated_list)

strengths=curated_list[curated_list['topic-strength'].isin(['Strong','Good'])]['quiz.topic'].tolist()
weaknesses=curated_list[curated_list['topic-strength'].isin(['Weak','Average'])]['quiz.topic'].tolist()

persona={
    "strengths":strengths,
    'weaknesses':weaknesses,
    'remark':f"Student has a good understanding of {', '.join(strengths)} \nShould focus on improving {', '.join(weaknesses)}. "
}

for key,val in persona.items():
    if isinstance(val,list):
        print(f"\n{key.capitalize()}: {', '.join(val)}")
    else:
        print(f"\n{key.capitalize()}: {val}")


#plot graph of student's performance

import matplotlib.pyplot as plt
#import seaborn as sns

color_map = {
    'Weak': 'red',
    'Average': 'orange',
    'Good': 'yellow',
    'Strong': 'green'
}
curated_list['color'] = curated_list['topic-strength'].map(color_map)

plt.figure(figsize=(10, 5))
bars = plt.bar(
    curated_list['quiz.topic'],  # x-axis= topics
    curated_list['avg_accuracy'],  # y= accuracy
    color=curated_list['color'] 
)

plt.title('Topic-Wise Performance', fontsize=14)
plt.xlabel('Topics', fontsize=10)
plt.ylabel('Average Accuracy (%)', fontsize=10)
plt.xticks(rotation=30, ha='right', fontsize=8)
plt.grid(axis='y', linestyle='--', alpha=0.7)

for bar, label in zip(bars, curated_list['topic-strength']):
    height = bar.get_height()
    plt.text(bar.get_x() + bar.get_width() / 2, height + 1, label, ha='center', va='bottom', fontsize=10)

# Display the bar graph
plt.tight_layout()
plt.show()

