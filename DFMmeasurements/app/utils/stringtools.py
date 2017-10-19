"""
module containg tools to create and transform strings.
"""
def str_to_bool(s):
    if s.lower() == 'true':
         return True
    elif s.lower() == 'false':
         return False
    else:
         raise  ValueError("Cannot covert {} to a bool".format(s))
