from app import app
from unittest import TestCase

app.config['TESTING'] = True
app.config['DEBUG_TB_HOSTS'] = ['dont-show-debug-toolbar']


class UserModelTestCase(TestCase):


    def test_show_users(self):
        with app.test_client() as client:

            res = client.get('/user-list')
            html = res.get_data(as_text=True)

            self.assertEqual(res.status_code, 200)
            self.assertIn('<h1> User List </h1>', html)




    def test_show_form(self):
        with app.test_client() as client:

            res = client.get('/user-list')
            html = res.get_data(as_text=True)

            self.assertEqual(res.status_code, 200)
            self.assertIn('<label for="firstname"> First Name </label>', html)




    def test_edit_user_details(self):
        with app.test_client() as client: 

            res = client.get('/user/1')
            html = res.get_data(as_text=True)

            self.assertEqual(res.status_code, 200)
            self.assertIn('<h1> User Details </h1>', html)




    def test_delete_user(self):
        with app.test_client() as client: 

            res = client.get('/user/7/delete')
            html = res.get_data(as_text=True)

            self.assertEqual(res.status_code, 200)
            

