# coding: utf8

from python_inapp_purchase.response import Response

class InAppPurchase(object):

    def get_products_response(self, response, additional_data=None):
        return self.get_response(response=response, data=additional_data)

    def get_product_response(self, response, additional_data=None):
        return self.get_response(response=response, data=additional_data)

    def get_subscription_response(self, response, additional_data=None):
        return self.get_response(response=response, data=additional_data)

    def get_response(self, response, data=None):
        data = data if data is not None else response.json()
        return Response(
            status=response.status_code,
            raw=response.json(),
            data=data
        )
