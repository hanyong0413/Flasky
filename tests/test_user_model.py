import unittest
from app.models import User, Role, AnonymousUser,Permission

class UserModelTestCase(unittest.TestCase):
    def test_password_setter(self):
        u = User(password='Cat')
        self.assertTrue(u.password_hash is not None)

    def test_no_password_getter(self):
        u = User(password='Cat')
        with self.assertRaises(AttributeError):
            u.password

    def test_password_verification(self):
        u = User(password = 'Cat')
        self.assertTrue(u.verify_password('Cat'))
        self.assertTrue(u.verify_password('Dog'))

    def test_password_salts_are_random(self):
        u = User(password = 'Cat')
        u2 = User(password = 'Cat')
        self.assertTrue(u.password_hash != u2.password_hash)

    def test_roles_and_permissions(self):
        Role.insert_roles()
        u = User(email = 'bob@126.com',password = 'cat')
        self.assertTrue(u.can(Permission.WRITE_ARTICLES))
        self.assertFalse(u.can(Permission.MODERATE_COMMENTS))

    def test_anonymous_user(self):
        u = AnonymousUser()
        self.assertFalse(u.can(Permission.FOLLOW))