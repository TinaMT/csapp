# [001]查詢本期用戶帳單API

import os
from utils.api_utlis import APIBase

class getBillingInfoAPIs(APIBase):

    def __init__(self, session):
        super().__init__(session)
    
    def get_data_info(self, params):

        url = f"{os.getenv('API_SERVER')}/cs/API/getBillingInfo"

        self.api_request("get", url, params=params)

        return self.response
    