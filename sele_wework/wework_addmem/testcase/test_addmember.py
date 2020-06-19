from sele_wework.wework_addmem.page.main import Main


class TestAddMember():

    def setup(self):
        self.main=Main()

    def test_addmember(self):
        self.main.address_list().add_mem().save_mem()
