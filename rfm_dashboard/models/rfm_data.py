import json

file_path = 'rfm_dashboard/db/rfm_data.json'

class RFMDataProcessor:
    def __init__(self, file_path):
        self.file_path = file_path
        self.r_data, self.f_data, self.m_data = self.get_data_list()

    def get_rfm_data(self):
        with open(self.file_path) as file:
            data = json.load(file)
        return data

    def get_data_list(self):
        r_data, f_data, m_data = [], [], []
        for k, v in self.get_rfm_data().items():
            r_data.append(v['recency'])
            f_data.append(v['frequency'])
            m_data.append(v['monetary'])
        return r_data, f_data, m_data

    def get_r_percent(self):
        r_percent = []
        max_recency = int(max(self.r_data))
        min_recency = int(min(i for i in self.r_data if i > 0))

        for i in self.r_data:
            if i == 0:
                r_percent.append(0)
            else:
                r_percent.append(round(((max_recency - i) / (max_recency - min_recency)) * 100))

        return r_percent

    def get_f_percent(self):
        f_percent = []
        max_frequency = int(max(self.f_data))

        for i in self.f_data:
            if i == 0:
                f_percent.append(0)
            else:
                f_percent.append(round((i / max_frequency) * 100))
                
        return f_percent

    def get_m_percent(self):
        m_percent = []
        max_monetary = int(max(self.m_data))

        for i in self.m_data:
            if i == 0:
                m_percent.append(0)
            else:
                m_percent.append(round((i / max_monetary) * 100))

        return m_percent

    def group_rfm_percent(self):
        r_percent = self.get_r_percent()
        f_percent = self.get_f_percent()
        m_percent = self.get_m_percent()
        group_r_percent = [(keys, values) for keys, values in zip(self.get_rfm_data().keys(), r_percent)]
        group_f_percent = [(keys, values) for keys, values in zip(self.get_rfm_data().keys(), f_percent)]
        group_m_percent = [(keys, values) for keys, values in zip(self.get_rfm_data().keys(), m_percent)]

        return group_r_percent, group_f_percent, group_m_percent

processor = RFMDataProcessor(file_path)
group_r_percent, group_f_percent, group_m_percent = processor.group_rfm_percent()