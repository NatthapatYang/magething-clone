import pytest
from rfm_dashboard.models.rfm_data import percentage, reverse_percentage, get_rfm_data, bar_chart_score

class TestRFMPercentages:
    def test_percent(self):
        assert percentage([1, 2, 3], 3) == [33, 67, 100]
        assert percentage([0, 0, 0], 3) == [0, 0, 0]
        assert not percentage([1, 2, 3], 3) == [100, 50, 0]
        assert not percentage([0, 0, 0], 3) == [33, 67, 100]
    
    def test_reverse_percentage(self):
        assert reverse_percentage([1, 2, 3], 3, 1) == [100, 50, 0]
        assert reverse_percentage([0, 0, 0], 3, 1) == [0, 0, 0]
        assert not reverse_percentage([1, 2, 3], 3, 1) == [33, 67, 100]
        assert not reverse_percentage([0, 0, 0], 3, 1) == [100, 50, 0]

class TestRFMData:
    def keys_rfm_data(self):
        test_keys_data = []

        for k in get_rfm_data().keys():
            test_keys_data.append(k)

        return test_keys_data

    def test_get_rfm_data_value(self):
        test_data_key = ['champion', 'royal', 'potential_royal', 'new', 'promising', 'need_attention', 'sleep', 'cant_lose', 'risk', 'hibernating']
        
        assert self.keys_rfm_data() == test_data_key

        for k in get_rfm_data().keys():
            assert 'recency' in get_rfm_data()[k]
            assert 'frequency' in get_rfm_data()[k]
            assert 'monetary' in get_rfm_data()[k]
            assert 'customers' in get_rfm_data()[k]
            assert not 'baht' in get_rfm_data()[k]
            assert not 'days' in get_rfm_data()[k]
            assert not 'amount' in get_rfm_data()[k]

            
class TestRFMBarChartScore:
    def test_bar_chart_score(self):
        r_percent, f_percent, m_percent = bar_chart_score()

        assert len(r_percent) == len(f_percent) == len(m_percent)
        assert len(r_percent) == len(get_rfm_data())
        assert len(f_percent) == len(get_rfm_data())
        assert len(m_percent) == len(get_rfm_data())
        assert len(r_percent) == len(f_percent) == len(m_percent) == 10
        assert not len(r_percent) == len(f_percent) == len(m_percent) == 0
        assert not len(r_percent) == len(f_percent) == len(m_percent) == 1
        assert not len(r_percent) == len(f_percent) == len(m_percent) == 9
        assert not r_percent[len(r_percent) - 1][0] == 100
        assert not f_percent[len(f_percent) - 1][0] == 100
        assert not m_percent[len(m_percent) - 1][0] == 100