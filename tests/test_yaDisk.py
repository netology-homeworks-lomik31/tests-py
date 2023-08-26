import requests, unittest
from disk import Disk

class TestDisk(unittest.TestCase):
    def testSuccess(self):
        with open("./tests/yaDisk") as f:
            config = f.read()
        d = Disk(config)
        fName = "amogus"
        res = d.createFolder(fName)
        self.assertEqual(res.status_code, 201)

        params = {
            "path": fName
        }
        res_test = requests.get("https://cloud-api.yandex.net/v1/disk/resources", headers=d.headers, params=params)
        self.assertEqual(res_test.status_code, 200)