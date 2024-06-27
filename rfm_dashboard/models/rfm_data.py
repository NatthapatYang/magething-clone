import json

def get_rfm_data():
    with open('rfm_dashboard/db/rfm_data.json') as file:
        data = json.load(file)

    return data

def get_data_list():
    r_data, f_data, m_data = [], [], []

    for k, v in get_rfm_data().items():
        r_data.append(v['recency'])
        f_data.append(v['frequency'])
        m_data.append(v['monetary'])

    return r_data, f_data, m_data

r_data, f_data, m_data = get_data_list()

def get_r_percent():
    r_percent = []
    max_recency = int(max(r_data))
    min_recency = int(min(i for i in r_data if i > 0))

    for i in r_data:
        if i == 0:
            r_percent.append(0)
        else:
            r_percent.append(round(((max_recency - i) / (max_recency - min_recency)) * 100))

    return r_percent

def get_f_percent():
    f_percent = []
    max_frequency = int(max(f_data))

    for i in f_data:
        if i == 0:
            f_percent.append(0)
        else:
            f_percent.append(round((i / max_frequency) * 100))
            
    return f_percent

def get_m_percent():
    m_percent = []
    max_monetary = int(max(m_data))

    for i in m_data:
        if i == 0:
            m_percent.append(0)
        else:
            m_percent.append(round((i / max_monetary) * 100))

    return m_percent