from locust import HttpUser,TaskSet,task,between
import random
class UserBehaviour(TaskSet):
    @task
    def like_post(self):
        post_id=1
        self.client.get(f'posts/{post_id}/',
        data={},
        headers={'Content-Type': 'application/json'})
class websiteUser(HttpUser):
    tasks=[UserBehaviour]
    wait_time=between(1,2)