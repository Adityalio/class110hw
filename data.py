import csv
import random
from typing import Set
import pandas as pd
import plotly_express as px
import statistics
import plotly.graph_objects as go
import plotly.figure_factory as ff
df=pd.read_csv("newdata.csv")
data=df["average"].tolist()

def randommeans(counter_list):
    dataset=[]
    for i in range(0,counter_list):
        random.val=random.randint(0,len(data)-1)
        value=data[random.val]
        dataset.append(value)

    mean=statistics.mean(dataset)
    return mean
def main():
    mean_list=[]
    for i in range(0,1000):
        setmean=randommeans(100)
        mean_list.append(setmean)
        
    mean=statistics.mean(mean_list)
    print(mean)
    fig=ff.create_distplot([mean_list],["average"],show_hist=False)
    fig.add_trace(go.Scatter(x=[mean, mean], y=[0, 1], mode="lines", name="MEAN"))
    fig.show()

main()


