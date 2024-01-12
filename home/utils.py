import uuid, base64
from .models import *
from io import BytesIO
from matplotlib import pyplot

def generate_code():
    return str(uuid.uuid4()).replace('-', '').upper()[:12]
def get_key(res_by):
    if res_by == '#1':
        key = 'patient_category'
    elif res_by == '#2':
        key = 'patient_category'
    elif res_by == '#3':
        key = 'patient_category'
    elif res_by == '#4':
        key = 'patient_category'
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
    key = get_key(results_by)
    d = data.groupby(key, as_index=False)['age'].agg('sum')
    if chart_type == '#1':
        print("Bar graph")
        pyplot.bar(d[key], d['age'])
    elif chart_type == '#2':
        print("Pie chart")
        pyplot.pie(data=d,x='age', labels=d[key])
    elif chart_type == '#3':
        print("Line graph")
        pyplot.plot(d[key], d['age'], color='red', marker='o', linestyle='dashed')
    else:
        print("Chart_type not identified")
    pyplot.tight_layout()
    chart = get_graph()
    return chart