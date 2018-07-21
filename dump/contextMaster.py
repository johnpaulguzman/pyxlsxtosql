from contextlib import contextmanager


@contextmanager
def connectionContext(config):
    print("my config open: " + str(config))
    yield
    print("close session")

with connectionContext("sup"):
    print("action1")
    print("action2")

#https://dev.mysql.com/doc/connector-python/en/connector-python-api-errors-error.html