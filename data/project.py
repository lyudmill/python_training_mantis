from model.project import Project
import random
import string


def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + string.punctuation + " "*10
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])

_testdata = [Project(name=random_string("name", 15), status=None, description =random_string("dsc ", 30))] + [
    Project(name=random_string("name", 15), status="development", description=random_string("dsc ", 30))
    for i in range(3)
]

testdata = [Project(name=random_string("name", 15), status="development", description =random_string("dsc ", 30))]
