import hashlib


class User():

    def __init__(self, name, password):
        self.name = name
        self._password = password

    @property
    def password(self):
        raise Exception("can't access")

    @password.setter
    def password(self, password):
        self._password = hashlib.new("md5", password.encode("utf-8")).hexdigest()

    def check_password(self, password):
        return hashlib.new("md5", password.encode("utf-8")).hexdigest() == self._password


if __name__ == '__main__':
    u = User("Vincent", "110")
    # print(u.password)

    u.password = "911"
    # print(u.password)

    print(u.check_password("900"))


