from api.BaseApi import BaseApi


class BrandsApi(BaseApi):

    def get_all_brands(self):
        return self.get("/brandsList")