from mongoengine import Document, StringField, IntField, BooleanField, DateTimeField
import re


class audit_fields():
    created_on = DateTimeField()
    created_by = StringField()
    modified_by = StringField()
    modified_on = DateTimeField()


class restaurant(Document, audit_fields):
    Title = StringField(max_length=300)
    Tags = StringField(max_length=300)
    Area = StringField(max_length=500)
    Address = StringField(max_length=500)
    Category = StringField(max_length=500)
    Price = StringField(max_length=400)
    Timings = StringField(max_length=10)
    Phone = StringField(max_length=100)
    Cost_for_two = StringField(max_length=100)
    country_details = StringField(max_length=100)
    meta = {'indexes': [
        {'fields': ['$Title', "$Tags", "$Area", "$Address", "country_details"],
         'default_language': 'english',
         'weights': {'Title': 10, 'Tags': 10, 'Area': 10, 'Address': 10, 'country_details': 10}
         }
    ]}

    @classmethod
    def load_page(cls, page_no, no_of_records):
        if (page_no == 0):
            return restaurant.objects()
        offset = (page_no - 1) * no_of_records

        return restaurant.objects.skip(offset).limit(no_of_records)

    @classmethod
    def load_search_restaurant(cls, search_string, page_no):
        no_of_records = 500
        offset = (page_no - 1) * no_of_records
        return restaurant.objects.search_text(search_string)
