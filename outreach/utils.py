import uuid, base64
from .models import *
from io import BytesIO
from matplotlib import pyplot
import pandas as pd
import plotly.express as px


def generate_code():
    return str(uuid.uuid4()).replace('-', '').upper()[:12]


from io import BytesIO
import base64
from matplotlib import pyplot

def get_key(res_by):
    if res_by == '#1':
        key = 'Clinic'
    elif res_by == '#2':
        key = 'Clinic'
    elif res_by == '#3':
        key = 'Clinic'
    else:
        key = None
    return key

def get_graph():
    buffer = BytesIO()
    pyplot.savefig(buffer, format='png')
    buffer.seek(0)
    image_png = buffer.getvalue()
    graph = base64.b64encode(image_png)
    graph = graph.decode('utf-8')
    buffer.close()
    return graph

def get_chart(chart_type, data, results_by, **kwargs):
    pyplot.switch_backend('AGG')
    fig = pyplot.figure(figsize=(12, 6))
    key = get_key(chart_type)
    if key == 'Clinic':
        d = data.groupby(key, as_index=False)['TCA Date'].count()
    else:
        d = data.groupby(key, as_index=False)['TCA Date'].sum()
    if len(d) == 0:
        return None
    if chart_type == '#1':
        print("Bar graph")
        pyplot.bar(d[key], d['TCA Date'])
    elif chart_type == '#2':
        print("Pie chart")
        labels = d[key].values
        size = d['TCA Date'].values
        pyplot.pie(x=size,labels=labels)
        pyplot.legend(title="Legend")
    elif chart_type == '#3':
        print("Line graph")
        pyplot.plot(d[key], d['TCA Date'], color='blue', marker='o', linestyle='dashed')
    else:
        print("Chart_type not identified")
    pyplot.title(chart_type)
    pyplot.xlabel(results_by)
    pyplot.ylabel("Count")
    pyplot.tight_layout()
    chart = get_graph()
    return chart



# def get_key(res_by):
#     if res_by == '#1':
#         key = 'Clinic'
#     elif res_by == '#2':
#         key ='Clinic'
#     elif res_by == '#3':
#         key = 'Clinic'
#     # elif res_by == '#4':
#     #     key = 'clinic'
#     return key
# def get_key(res_by):
#     if res_by == '#1':
#         key = 'Clinic'
#     elif res_by == '#2':
#         key = 'Clinic'
#     elif res_by == '#3':
#         key = 'Clinic'
#     else:
#         key = None
#     return key

    
# def get_graph():
#     buffer = BytesIO()
#     pyplot.savefig(buffer, format='png')
#     buffer.seek(0)
#     image_png = buffer.getvalue()
#     graph = base64.b64encode(image_png)
#     graph = graph.decode('utf-8')
#     buffer.close()
#     return graph

# def get_chart(chart_type, data, results_by, **kwargs):
#     pyplot.switch_backend('AGG')
#     fig = pyplot.figure(figsize=(12, 6))
#     key = get_key(chart_type)
    
#     if key == 'Clinic':
#         d = data.groupby(key, as_index=False)['TCA Date'].count()
#     else:
#         d = data.groupby(key, as_index=False)['TCA Date'].sum()
        
#     if len(d) == 0:
#         return None
    
#     if chart_type == '#1':
#         print("Bar graph")
#         pyplot.bar(d[key], d['TCA Date'])

#     elif chart_type == '#2':
#         print("Pie chart")
#         labels = d[key].values
#         sizes = d['TCA Date'].values
#         pyplot.pie(sizes=sizes, labels=labels)

    

#     elif chart_type == '#3':
#         print("Line graph")
#         pyplot.plot(d[key], d['TCA Date'], color='blue', marker='o', linestyle='dashed')

#     else:
#         print("Chart_type not identified")
    
#     pyplot.tight_layout()
#     chart = get_graph()
#     return chart

# def get_chart(chart_type, data, results_by, **kwargs):
#     pyplot.switch_backend('AGG')
#     fig = pyplot.figure(figsize=(12, 6))
#     key = get_key(results_by)
    
#     if key == 'Clinic':
#         d = data.groupby(key, as_index=False)['TCA Date'].count()
#     else:
#         d = data.groupby(key, as_index=False)['TCA Date'].sum()
        
#     if len(d) == 0:
#         return None
    
#     if chart_type == '#1':
#         print("Bar graph")
#         pyplot.bar(d[key], d['TCA Date'])

#     elif chart_type == '#2':
#         print("Pie chart")
#         labels = d[key].values
#         sizes = d['TCA Date'].values
#         pyplot.pie(sizes, labels=labels, autopct='%1.1f%%')

#     elif chart_type == '#3':
#         print("Line graph")
#         pyplot.plot(d[key], d['TCA Date'], color='blue', marker='o', linestyle='dashed')

#     else:
#         print("Chart_type not identified")
    
#     pyplot.tight_layout()
#     chart = get_graph()
#     return chart

# def get_chart(chart_type, data, results_by, **kwargs):
#     pyplot.switch_backend('AGG')
#     fig = pyplot.figure(figsize=(12, 6))
#     key = get_key(chart_type)
    
#     if key == 'Clinic':
#         d = data.groupby(key, as_index=False)['TCA Date'].count()
#     else:
#         d = data.groupby(key, as_index=False)['TCA Date'].sum()
        
#     if len(d) == 0:
#         return None
    
#     if chart_type == '#1':
#         print("Bar graph")
#         pyplot.bar(d[key], d['TCA Date'])

#     elif chart_type == '#2':
#         print("Pie chart")
#         pyplot.pie(d, x='TCA Date', labels=d[key])

#     elif chart_type == '#3':
#         print("Line graph")
#         pyplot.plot(d[key], d['TCA Date'], color='blue', marker='o', linestyle='dashed')

#     else:
#         print("Chart_type not identified")
    
#     pyplot.tight_layout()
#     chart = get_graph()
#     return chart

# def get_chart(chart_type, data, results_by, **kwargs):
#     pyplot.switch_backend('AGG')
#     fig = pyplot.figure(figsize=(12, 6))
#     key = get_key(chart_type)
#     d = data.groupby(key, as_index=False)['TCA Date'].agg('sum')
#     d['add'] = pd.Series([10 for x in range(len(d.index))])
#     aa = d['Clinic'].value_counts()
#     ##fig = px.bar(df, x="x", y=["SF", "Montreal"], barmode="group")
#     #d = d.stack().groupby(level=1).mean()

#     if chart_type == '#1':
#         print("Bar graph")
#         pyplot.bar(d[key], d['TCA Date'])

#     elif chart_type == '#2':
#         print("Pie chart")
#         pyplot.pie(data=d,x='add', labels=d[key])
#     elif chart_type == '#3':
#         print("Line graph")
#         pyplot.plot(d[key], d['TCA Date'], color='blue', marker='o', linestyle='dashed')
#     else:
#         print("Chart_type not identified")
#     pyplot.tight_layout()
#     chart = get_graph()
#     return chart


# def get_chart(chart_type, data, results_by, **kwargs):
#     pyplot.switch_backend('AGG')
#     fig = pyplot.figure(figsize=(12, 6))
#     key = get_key(results_by)
#     d = data.groupby(key, as_index=False)['TCA Date'].agg('sum')

#     if chart_type == '#1':
#         print("Bar graph")
#         pyplot.bar(d[key], d['TCA Date'])

#     elif chart_type == '#2':
#         print("Pie chart")
#         grouped = data.groupby('Clinic')

#         pyplot.pie(data=key, x="Clinic", labels='Clinic')

#     elif chart_type == '#3':
#         print("Line graph")
#         pyplot.plot(d[key], d['TCA Date'], color='red', marker='o', linestyle='dashed')
   
#     else:
#         print("Chart_type not identified")
#     pyplot.tight_layout()
#     chart = get_graph()
#     return chart

