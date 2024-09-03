from locust import HttpUser,Taskset,task,between
import random
class UserBehaviour(Taskset):
    @task
    def like_post(self):
        post_id=1
        self.client.get(f'posts/{post_id}/'),
        data={},
        headers={'Content-Type': 'application/json'}
class websiteUser(HttpUser):
    task=[UserBehaviour]
    wait_time=between(1,2)