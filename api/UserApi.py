from api.BaseApi import BaseApi


class UserApi(BaseApi):

    def verify_login(self, email: str, password: str):
        return self.post("/verifyLogin", data={"email": email, "password": password})

    def create_account(self, user_data: dict):
        return self.post("/createAccount", data=user_data)

    def delete_account(self, email: str, password: str):
        return self.delete("/deleteAccount", data={"email": email, "password": password})

    def get_user_detail(self, email: str):
        return self.get("/getUserDetailByEmail", params={"email": email})