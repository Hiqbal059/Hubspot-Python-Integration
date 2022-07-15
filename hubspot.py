from hubspot import HubSpot
from hubspot.crm.contacts import SimplePublicObjectInput
from hubspot.crm.contacts.exceptions import ApiException



API_Client = HubSpot()
API_Client.access_token = 'Replace your hubspot key'

def create_contact():
    """
    Create new contact on hubspot
    """
    try:
        simple_public_object_input = SimplePublicObjectInput(
            properties={"email": "your email", "name": "Enter Name", "phone": "Enter phone"} 
        )
        api_response = API_Client.crm.contacts.basic_api.create(
            simple_public_object_input=simple_public_object_input
        )
        return api_response
    except ApiException as e:
        print(e)

def get_all_contacts():
    """
    Return all contacts from hubspot
    """
    all_contacts = API_Client.crm.contacts.get_all()
    return all_contacts