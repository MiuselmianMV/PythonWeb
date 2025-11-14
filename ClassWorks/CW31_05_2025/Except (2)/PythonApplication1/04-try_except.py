class MyException(Exception):
    pass

try:
    raise Exception

except MyException:
    try:
        print("asdfasdfasdfa")
    except TypeError:
        print("some typeerror")
except Exception:
    print('some exception')
