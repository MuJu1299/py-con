from city_functions import city_country_str

def test_city_country_str():
    '''测试city，country代码'''
    city_countrys=city_country_str('yi chun','jiang xi','1000000')
    assert city_countrys==f"\nYi Chun:Jiang Xi - 1000000."