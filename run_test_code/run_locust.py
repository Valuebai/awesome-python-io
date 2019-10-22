from locust import HttpLocust, TaskSet, task


class UserBehavior(TaskSet):
    """
    创建UserBehavior()类继承TaskSet类，为用户行为。
    创建baidu() 方法表示一个行为，访问百度首页。用@task() 装饰该方法为一个任务。1表示一个Locust实例被挑选执行的权重，数值越大，执行频率越高。在当前UserBehavior()行为下只有一个baidu()任务，所以，这里的权重设置为几，并无影响。

    WebsiteUser()类用于设置性能测试。
    task_set ：指向一个定义了的用户行为类。
    min_wait ：用户执行任务之间等待时间的下界，单位：毫秒。
    max_wait ：用户执行任务之间等待时间的上界，单位：毫秒。

    运行性能测试,切换到性能测试脚本所在的目录，启动性能测试：
    …/> locust -f run_locust.py –-host=https://www.baidu.com
    run_locust.py 为测试脚本，https://www.baidu.com 为测试的网站。

    打开浏览器访问：http://127.0.0.1:8089或者http://localhost:8089/
    """

    @task(1)
    def baidu(self):
        self.client.get("/")


class WebsiteUser(HttpLocust):
    task_set = UserBehavior
    min_wait = 3000
    max_wait = 6000
