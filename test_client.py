from locust import HttpLocust, TaskSet, task
import sys
from random import choice

# 定义用户行为
class UserBehavior(TaskSet):

    @task
    def v2ex_index(self):
        #读取的CSV文件每一行以为逗号分开
        dataInfo = choice(self.locust.paramsdata)
        datainfo = dataInfo.split(",")
        url = "/api/nodes/show.json?name=" + datainfo[0]
        with  self.client.get(url,name='V2EX接口调用请求') as repones:
            print(repones.text)
            print(url)

class WebsiteUser(HttpLocust):
    task_set = UserBehavior
    min_wait = 3000
    max_wait = 6000
    host = 'https://www.v2ex.com'

    #参数化读取CSV文件内容
    paramsdata = []
    with open(sys.path[0]+'\data.csv') as file:
        for line in file.readlines():
            paramsdata.append(line.strip())