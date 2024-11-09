from locust import HttpUser, task, between

class FlaskAppUser(HttpUser):
    wait_time = between(1, 3)  # Simulate wait time between user actions
    
    @task
    def load_home_page(self):
        self.client.get("/")  # Access the home page

    @task
    def load_products(self):
        self.client.get("/products")  # Access the products page
