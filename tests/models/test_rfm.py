import pytest
from rfm_dashboard.models.rfm_data import get_rfm_data, percentage, reverse_percentage, bar_chart_score

def test_get_rfm_data():
    actual_result = get_rfm_data()
    expected_result = _expected_rfm_result()
    expected_keys = ['champion', 'royal', 'potential_royal', 'new', 'promising', 'need_attention', 'sleep', 'cant_lose', 'risk', 'hibernating']

    assert expected_result == actual_result
    assert type(expected_result) == type(actual_result)
    assert expected_keys == list(actual_result.keys())
    assert 10 == len(actual_result.keys())

def test_percentage_for_r_score():
    rfm_data = get_rfm_data()
    r_data = [data['recency'] for data in rfm_data.values()]

    actual_result = reverse_percentage(r_data, max(r_data), min(value for value in r_data if value != 0))
    expected_result = [0, 0, 72, 100, 72, 48, 52, 0, 0, 1]

    assert expected_result == actual_result

def test_percentage_for_f_score():
    rfm_data = get_rfm_data()
    f_data = [data['frequency'] for data in rfm_data.values()]

    actual_result = percentage(f_data, max(f_data))
    expected_result = [0, 0, 100, 22, 21, 17, 17, 0, 0, 18]

    assert expected_result == actual_result

def test_percentage_for_m_score():
    rfm_data = get_rfm_data()
    m_data = [data['monetary'] for data in rfm_data.values()]

    actual_result = percentage(m_data, max(m_data))
    expected_result = [0, 0, 16, 2, 3, 2, 100, 0, 0, 2]

    assert expected_result == actual_result

def test_get_bar_charts_score():
    actual_result = bar_chart_score()
    expected_result = _expected_bar_chart_result()

    assert expected_result == actual_result
    assert type(expected_result) == type(actual_result)
    # assert expected_result.keys() == actual_result.keys()

def _expected_rfm_result():
    return {
        "champion": {"customers": 0,"recency": 0,"frequency": 0,"monetary": 0},
        "royal": {"customers": 0,"recency": 0,"frequency": 0,"monetary": 0},
        "potential_royal": {"customers": 5,"recency": 35,"frequency": 6.0,"monetary": 161447},
        "new": {"customers": 28,"recency": 28,"frequency": 1.29,"monetary": 20064},
        "promising": {"customers": 40,"recency": 35,"frequency": 1.25,"monetary": 27397},
        "need_attention": {"customers": 34,"recency": 41,"frequency": 1.03,"monetary": 23527},
        "sleep": {"customers": 1,"recency": 40,"frequency": 1.0,"monetary": 1000000},
        "cant_lose": {"customers": 0,"recency": 0,"frequency": 0,"monetary": 0},
        "risk": {"customers": 0,"recency": 0,"frequency": 0,"monetary": 0},
        "hibernating": {"customers": 83,"recency": 53,"frequency": 1.08,"monetary": 22421}
    }

def _expected_bar_chart_result():
    '''
    # We do not expected this result, but we will leave it be.
    # Next times we will improve this result to be like
        {
            'champion': {'customers': 0, 'recency': 0, 'frequency': 0, 'monetary': 0, 'days': 0, 'orders': 0, 'baht': 0}, 
            'royal': {'customers': 0, 'recency': 0, 'frequency': 0, 'monetary': 0, 'days': 0, 'orders': 0, 'baht': 0}, 
            'potential_royal': {'customers': 5, 'recency': 35, 'frequency': 6.0, 'monetary': 161447, 'days': 72, 'orders': 100, 'baht': 16}, 
            'new': {'customers': 28, 'recency': 28, 'frequency': 1.29, 'monetary': 20064, 'days': 100, 'orders': 22, 'baht': 2}, 
            'promising': {'customers': 40, 'recency': 35, 'frequency': 1.25, 'monetary': 27397, 'days': 72, 'orders': 21, 'baht': 3}, 
            'need_attention': {'customers': 34, 'recency': 41, 'frequency': 1.03, 'monetary': 23527, 'days': 48, 'orders': 17, 'baht': 2}, 
            'sleep': {'customers': 1, 'recency': 40, 'frequency': 1.0, 'monetary': 1000000, 'days': 52, 'orders': 17, 'baht': 100}, 
            'cant_lose': {'customers': 0, 'recency': 0, 'frequency': 0, 'monetary': 0, 'days': 0, 'orders': 0, 'baht': 0}, 
            'risk': {'customers': 0, 'recency': 0, 'frequency': 0, 'monetary': 0, 'days': 0, 'orders': 0, 'baht': 0}, 
            'hibernating': {'customers': 83, 'recency': 53, 'frequency': 1.08, 'monetary': 22421, 'days': 0, 'orders': 18, 'baht': 2}
        }
    '''
    return (
        [(0, 0), (0, 0), (35, 72), (28, 100), (35, 72), (41, 48), (40, 52), (0, 0), (0, 0), (53, 1)], 
        [(0, 0), (0, 0), (6.0, 100), (1.29, 22), (1.25, 21), (1.03, 17), (1.0, 17), (0, 0), (0, 0), (1.08, 18)], 
        [(0, 0), (0, 0), (161447, 16), (20064, 2), (27397, 3), (23527, 2), (1000000, 100), (0, 0), (0, 0), (22421, 2)]
    )
