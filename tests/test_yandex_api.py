import unittest
from yandex import YaApi
from parameterized import parameterized


class TestCreateFolder(unittest.TestCase):
    def setUp(self) -> None:
        self.instance = YaApi()
        self.instance.get_create_folder('path')

    def tearDown(self) -> None:
        self.instance.get_del_folder('zzz')
        self.instance.get_del_folder('test')
        self.instance.get_del_folder('path')

    @parameterized.expand(
        [
            ('zzz', 201),
            ('test', 201)
        ]
    )
    def test_cls_create_folder(self, path, result):
        calc_result = self.instance.get_create_folder(path)
        self.assertEqual(calc_result, result)

    @parameterized.expand(
        [
            ('path', 200),
        ]
    )
    def test_cls_check_folder(self, path, result):
        calc_result = self.instance.check_folder(path)
        self.assertEqual(calc_result, result)

    @unittest.expectedFailure
    def test_fail_cls_check_folder(self):
        result = self.instance.check_folder('111')
        self.assertEqual(result, 200)

