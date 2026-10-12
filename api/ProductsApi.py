from api.BaseApi import BaseApi


class ProductsApi(BaseApi):
    def get_all_products(self):
        return self.get("/productsList")

    def search_product(self, query: str):
        return self.post("/searchProduct", data={"search_product": query})