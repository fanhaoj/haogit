from sele_wework.page.index import Index


class TestRegist:
    def setup(self):
        self.index=Index()

    def test_regist(self):
        self.index.goto_regist().regist_true()