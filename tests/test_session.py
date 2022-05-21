import unittest
import requests


class SessionTest(unittest.TestCase):
    
    def test_one(self):        
        res =  requests.get('http://localhost:8082/counters')
        res.raise_for_status()
        cookies = res.cookies.get_dict()
        result = res.json()
        self.assertEquals([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], result)
        
        res =  requests.get('http://localhost:8082/counters', cookies=cookies)
        res.raise_for_status()
        result = res.json()
        self.assertEquals([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19], result)
        
        
        
        
        