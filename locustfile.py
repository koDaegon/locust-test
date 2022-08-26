import time
from locust import HttpUser, task, between

class DockerGettingStartedUser(HttpUser):
    wait_time = between(1, 5)

    @task
    def our_application(self):
        self.client.get("/tutorial/")
        time.sleep(3)
        self.client.get("/tutorial/our-application/")

    @task
    def updating_our_app(self):
        self.client.get("/tutorial/")
        time.sleep(3)
        self.client.get("/tutorial/updating-our-app/")

