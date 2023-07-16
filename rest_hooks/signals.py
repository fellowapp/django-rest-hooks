from django.dispatch import Signal


# providing_args=['action', 'instance']
hook_event = Signal()
# providing_args=['event_name', 'payload', 'user']
raw_hook_event = Signal()
# providing_args=['payload', 'instance', 'hook']
hook_sent_event = Signal()
