import time
from locust import HttpUser, task, between


class branchUser(HttpUser):
    wait_time = between(1, 5)

    @task
    def on_start(self):
        response = self.client.post("/api/auth/login",json={"login_id":"1001001","password":"1234"})
        global token 
        token = response["access_token"]
        self.client.headers = {"Autoraization": "key="+token}
        time.sleep(1)
        
    def createNonScheduledRoutePlan(self):
        self.client.post("/nonScheduled/routeplan:save",json=[{
        "driving_id": "",
        "route_naming": "",
        "ofc_org_cd": "TJNOCHT",
        "departure_tml_cd": "300",
        "departure_tml_nm": "대전A",
        "arrival_tml_cd": "112",
        "arrival_tml_nm": "동서울",
        "vehicle_model": "",
        "vehicle_req_in_tm": "1200",
        "request_reason": "배차",
        "approval_status": "ready",
        "driving_dt": "20220808",
        "request_emp_no": "",
        "confirmation_charge": "",
        "sales_office_burden_ratio": "30",
        "vehicle_vendor_nm": "제이비",
        "distance": "",
        "settlement_org_cd": "300",
        "vehicle_model_cd": "9",
        "route_plan_type": "E",
        "stopover": "",
        "loading_place_charger_nm": "임시-대전A",
        "loading_place_contact_place": "01088124535",
        "loading_place_address": "대전광역시 유성구 대정로 68(대정동)",
        "expectation_arrival_tm": "1600",
        "sales_office_cd": "3092",
        "sts": "i",
        "row_id": 0
    }
])
