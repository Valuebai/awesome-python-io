import unittest
import requests


class Test_Kuaidi(unittest.TestCase):
    def setUp(self):
        self.headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64; rv:44.0) Gecko/20100101 Firefox/44.0"}
        self.s = requests.session()

    def tearDown(self):
        pass

    def test_addNum(self):
        expect = 12
        result = 3 + 9
        self.assertEqual(expect, result)

    def test_yunda(self):
        danhao = "3945550719894"
        kd = "yunda"
        self.url = "http://www.kuaidi.com/index-ajaxselectcourierinfo-%s-%s.html" % (danhao, kd)
        print(self.url)
        # 1.发送get请求
        r = self.s.post(self.url, headers=self.headers, verify=False)
        result = r.json()
        # 2.获取结果
        print(result['company'])
        data = result["data"]
        print(data[0])
        get_result = data[0]['context']
        print(get_result)
        # 3.进行断言
        self.assertEqual("韵达快递", result['company'])
        self.assertIn("已签收", get_result)


if __name__ == "__main__":
    unittest.main()
