from ast import Store
from black import re
from pytest_mock import session_mocker
from src.api.schema.request import TripPatchRequest, TripStatusRequest, UserPatchRequest, UserRequest
from src.models.trips import Trips
from src.models.users import Users
import logging
from sqlalchemy import func
from src.database.db import db_session

db_session = db_session()
logger = logging.getLogger("backend")


class DbRepositories:
    def __init__(self, user_id):
        self.user_id = user_id

    # def get_main_user(self):
    #     return Users.get({"id": self.user_id}).first()

    # def update_main_user_details(self, request):
    #     Users.update(
    #         {"id": self.user_id}, name=request.name, home_address=request.home_address
    #     )
    #     logger.info("Updated main user's details")

    # def create_new_customer(self, request):
    #     customer = Customers.get({"user_id": self.user_id}).first()
    #     if not customer:
    #         customer = Customers.create(
    #             user_id=self.user_id, home_address=request.home_address
    #         )
    #         logger.info(f"Created new customer {customer}")
    #     return customer

    # def create_new_store(self, request):
    #     store = Stores.get({"name": request.store_name}).first()
    #     if not store:
    #         business_cat_id = self.get_business_category(request.store_category_name)
    #         store = Stores(
    #             name=request.store_name,
    #             business_category_id=business_cat_id,
    #             address=request.store_address,
    #             description=request.store_description,
    #         )
    #         db_session.add(store)
    #         db_session.flush()
    #         logger.info(f"Created new Store {store}")
    #     return store

    # def get_business_category(self, category_name):
    #     item = BusinessCategories.get({"name": category_name}).first()
    #     if not item:
    #         raise Exception("Item with category name not found")
    #     return item.id

    # def create_new_owner(self, store_id):
    #     owner = Owners.get({"user_id": self.user_id}).first()
    #     if not owner:
    #         owner = Owners.create(user_id=self.user_id, store_id=store_id)
    #         logger.info(f"Created new customer {owner}")
    #     return owner

    # def create_new_product(self, request):
    #     product = (
    #         db_session.query(Products)
    #         .filter(
    #             func.lower(Products.name) == func.lower(request.product_name),
    #             Products.store_id == request.store_id,
    #         )
    #         .first()
    #     )
    #     if product:
    #         logger.info(f"The product already exists with name {request.product_name}")
    #         raise Exception("Product already exists")
    #     product = Products(
    #         name=request.product_name,
    #         brand=request.product_brand,
    #         description=request.product_description,
    #         store_id=request.store_id,
    #     )
    #     db_session.add(product)
    #     db_session.flush()
    #     return product

    # def add_product_details(self, request, product_id):
    #     for details in request.product_details:
    #         product_details = ProductDetails(
    #             product_id=product_id,
    #             unit=details.unit,
    #             actual_price=details.mrp_price,
    #             discounted_price=details.discounted_price,
    #             quantity=details.quantity,
    #         )
    #         db_session.add(product_details)
    #         db_session.flush()
    #     return True

    # def delete_customer(self):
    #     Customers.delete({"user_id": self.user_id})

    # def delete_store(self):
    #     owner = Owners.get({"user_id": self.user_id}).first()
    #     if owner:
    #         Stores.delete({"id": owner.store_id})

    # def delete_owner(self):
    #     Owners.delete({"user_id": self.user_id})

    # def delete_user(self):
    #     Users.delete({"id": self.user_id})

    # def get_store_products(self, store_id: int):
    #     products = Products.get({"store_id": store_id}).all()
    #     for product in products:
    #         a = self.get_product_details(product.id)
    #     return a
    
    # def get_product_details(self,product_id):
    #     product_details = ProductDetails.get({"product_id": product_id}).all()
    #     for pd in product_details:  
    #         a = ProductDetailsRequest.parse_obj({
                
    #         })
    #         break
    #     return a
        
    # def add_new_user(self, request):
    #     customer = Users.get({"user_id": self.user_id}).first()
    #     if not customer:
    #         customer = Users.create(
    #             user_id=self.user_id, home_address=request.home_address
    #         )
    #         logger.info(f"Created new customer {customer}")
    #     return customer

    def update__user_details(self, request: UserPatchRequest):
        if request.name != None:
            Users.update(
                {"id": self.user_id},
                name=request.name, 
            )
        
        if request.contact_no != None:
            Users.update(
                {"id": self.user_id},
                contact_no=request.contact_no,
            )
        
        if request.email_id != None:
            Users.update(
                {"id": self.user_id},
                email_id=request.email_id,
            )
        
        if request.age != None:
            Users.update(
                {"id": self.user_id},
                age=request.age,
            )
        
        if request.interests != None:
            Users.update(
                {"id": self.user_id},
                interests=request.interests,
            )
        
        if request.profile_photo != None:
            Users.update(
                {"id": self.user_id},
                profile_photo=request.profile_photo,
            )
        
        if request.places_visited != None:
            Users.update(
                {"id": self.user_id},
                places_visited=request.places_visited,
            )
        
        if request.other_info != None:
            Users.update(
                {"id": self.user_id},
                other_info=request.other_info,
            )

        logger.info("Updated main user's details")

    def update__trip_details(self, request: TripPatchRequest):
        if request.hosted_by != None:
            Trips.update(
                {"id": self.user_id},
                hosted_by=request.hosted_by, 
            )
        
        if request.destination != None:
            Trips.update(
                {"id": self.user_id},
                destination=request.destination,
            )
        
        if request.duration != None:
            Trips.update(
                {"id": self.user_id},
                duration=request.duration,
            )
        
        if request.events != None:
            Trips.update(
                {"id": self.user_id},
                events=request.events,
            )
        
        if request.status != None:
            Trips.update(
                {"id": self.user_id},
                status=request.status,
            )
        
        if request.additional_info != None:
            Trips.update(
                {"id": self.user_id},
                additional_info=request.additional_info,
            )
        
        if request.date_from != None:
            Trips.update(
                {"id": self.user_id},
                date_from=request.date_from,
            )
        
        if request.date_to != None:
            Trips.update(
                {"id": self.user_id},
                date_to=request.date_to,
            )

        logger.info("Updated Trip's details")

    def update__trip_status(self, request: TripStatusRequest):
        Trips.update(
            {"id": self.user_id},
            status=request.status, 
        )
        
        logger.info("Updated Trip's Status")