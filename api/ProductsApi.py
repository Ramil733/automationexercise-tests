from api.BaseApi import BaseApi


class ProductsApi(BaseApi):

    def get_all_products(self):
        return self.get("/productsList")

    def post_products(self):
        return self.post("/productsList")

    def search_product(self, query: str):
        return self.post("/searchProduct", data={"search_product": query})

    def search_product_without_param(self):
        return self.post("/searchProduct")