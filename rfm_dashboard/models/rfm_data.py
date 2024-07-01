import json

def get_rfm_data():
    with open('rfm_dashboard/db/rfm_data.json') as file:
        data = json.load(file)

    return data

def percent(data_value, max):
    percent_result = []
    for i in data_value:
        if i == 0:
            percent_result.append(0)
        else:
            percent_result.append(round((i / max) * 100))
    return percent_result

def reverse_percentage(data_value, max, min):
    percent_result = []
    for i in data_value:
        if i == 0:
            percent_result.append(0)
        else:
            percent_result.append(round(((max - i) / (max - min)) * 100))
    return percent_result

def bar_chart_score():  
    rfm_data = get_rfm_data()

    r_data = [v['recency'] for v in rfm_data.values()]
    f_data = [v['frequency'] for v in rfm_data.values()]
    m_data = [v['monetary'] for v in rfm_data.values()]

    get_r_percent = reverse_percentage(r_data, max(r_data), min(value for value in r_data if value > 0))
    get_f_percent = percent(f_data, max(f_data))
    get_m_percent = percent(m_data, max(m_data))

    r_percent = list(zip(rfm_data.keys(), get_r_percent))
    f_percent = list(zip(rfm_data.keys(), get_f_percent))
    m_percent = list(zip(rfm_data.keys(), get_m_percent))

    return r_percent, f_percent, m_percent  