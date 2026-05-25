SERVICES = {}

def service(name):
    def decorator(func):
        SERVICES[name] = func
        return func
    return decorator
