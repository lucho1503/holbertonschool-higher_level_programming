#!/usr/bin/pythpn3
def inherits_from(obj, a_class):
    if type(obj) == a_class:
        return False
    if isinstance(obj, a_class):
        return True
