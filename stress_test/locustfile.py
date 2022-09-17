from locust import HttpUser, TaskSet, task , between


class UserBehavior(TaskSet):

    # Put your stress tests here
    # TODO
    #raise NotImplementedError
    @task(1)
    def index(self):
        self.client.get("http://0.0.0.0/")

    @task(3)
    def predict(self):
        files= [
            ('file',('dog.jpeg',open('dog.jpeg','rb'),'image/jpeg'))
        ]
        headers={}
        payload={}

        self.client.post("http://0.0.0.0/predict",
                        headers=headers,
                        data=payload,
                        files=files
                        )    


class APIUser(HttpUser):
    tasks = [UserBehavior]
    wait_time = between(1, 5) #for a random time between a min and max value in seconds
    #min_wait=1000
    #max_wait=5000


#The result of the locust in: https://docs.google.com/document/d/1vRrfNXG6HJXJL9BO5a_xQHz9lKjyo15tBEyNEzx9-sw/edit?usp=sharing
