from locust import HttpUser, task, SequentialTaskSet, between
import requests
            
class ExplorerUser(HttpUser):
    wait_time = between(0.5, 1)
                
    @task
    def first_request(self):
        self.client.cookies.clear()
        cookies = {}
        for i in range(1, 10):
            res = self.client.get("/counters", cookies=cookies, allow_redirects=False)        
            res.raise_for_status()        
            cookies = res.cookies.get_dict()                
            result = res.json()                
            if  len(result) != i * 10 :
                raise ValueError(cookies, result)
        
        self.client.close()