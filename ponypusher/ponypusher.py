"""Django integration for pusher app"""
import pusher
from settings import *

class PushMe():

    def __init__(self, channel):
        """Create pusher object for channel"""
        pusher.app_id = PUSHER_APP_ID
        pusher.key = PUSHER_KEY
        pusher.secret = PUSHER_SECRET
        self.pusher_object = pusher.Pusher()
        self.channel = channel
    
    def event (self, event_name, data_dict):
        """push and event to channel returns
        true on success"""
        return self.pusher_object[self.channel].\
        trigger(event_name, data_dict)

    def push_model(self, event_name, model, fields_tupple):
        """Push selected of model fields to channel"""
        data_dict = {}
        for field in model._meta.fields:
            if field.name in fields_tupple:
                data_dict[field.name] = field.value_to_string(model)
        return self.event (event_name, data_dict)

