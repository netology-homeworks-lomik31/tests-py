import requests, unittest
from disk import Disk

class TestDisk(unittest.TestCase):
    with open("./tests/yaDisk") as f:
        config = f.read()
    d = Disk(config)

    def testSuccess(self):
        fName = "test1"
        res = self.d.createFolder(fName)
        self.assertEqual(res.status_code, 201)

        params = {
            "path": fName
        }
        res_test = requests.get("https://cloud-api.yandex.net/v1/disk/resources", headers=self.d.headers, params=params)
        self.assertEqual(res_test.status_code, 200)
    
    def testDuplicate(self):
        fName = "test2"
        
        for _ in range(2):
            res = self.d.createFolder(fName)
        
        self.assertEqual(res.status_code, 409)

        params = {
            "path": fName
        }
        res_test = requests.get("https://cloud-api.yandex.net/v1/disk/resources", headers=self.d.headers, params=params)
        self.assertEqual(res_test.status_code, 200)
