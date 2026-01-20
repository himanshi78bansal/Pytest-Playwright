from playwright.sync_api import Playwright


class ApiUtils:
    def getToken(self, playwright: Playwright):
        loginPayload = {"userEmail": "Shubhamlambha.1996@gmail.com", "userPassword": "Shubh123"}
        apiRequestContext = playwright.request.new_context(base_url="https://rahulshettyacademy.com")
        response = apiRequestContext.post("/api/ecom/auth/login",
                                          data=loginPayload,
                                          headers = {
                                              "content-type": "application/json"
                                          })
        responseJson = response.json()
        print(responseJson)
        return responseJson["token"]

    def createOrder(self, playwright: Playwright):
        token = self.getToken(playwright)
        print(token)
        orderPayload = {"orders": [{"country": "India", "productOrderedId": "68a961459320a140fe1ca57a"}]}

        apiRequestContext = playwright.request.new_context(base_url="https://rahulshettyacademy.com")
        response = apiRequestContext.post("/api/ecom/order/create-order",
                                          data = orderPayload,
                                          headers = {
                                              "authorization": token,
                                              "content-type": "application/json"
                                          })

        # assert response.ok()
        responseJson = response.json()
        print(responseJson)
        return responseJson["orders"][0]