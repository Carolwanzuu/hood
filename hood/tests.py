from _typeshed import Self
from django.test import TestCase
from .models import Profile, Business, NeighborHood
from django.contrib.auth.models import User

# Create your tests here.
class ProfileTest(TestCase):
    def setUp(self):
        self.wanzuu = User(username = 'wanzuu',email = 'wanzuu@gmail.com')
        self.wanzuu = Profile(user = Self.wanzuu,bio = 'tests',profile_picture = 'test.png')

    def test_instance(self):
        self.assertTrue(isinstance(self.wanzuu,Profile))


    def test_save_profile(self):
        Profile.save_profile(self)
        all_profiles = Profile.objects.all()
        self.assertTrue(len(all_profiles),0)

    def test_delete_profile(self):
        self.wanzuu.delete_profile()
        all_profiles = Profile.objects.all()
        self.assertEqual(len(all_profiles),0)



class BusinessTestCase(TestCase):
    def setUp(self):
        self.new_post = Business(name = 'testT',email = 'test@gmail.com',description = 'testD',user ='favian', neighborhood='embakasi')


    def test_create_business(self):
        self.new_post.save_project()
        name = Business.objects.all()
        self.assertEqual(len(name),1)

    def test_delete_project(self):
        self.new_post.delete_project()
        name = Business.objects.all()
        self.assertEqual(len(name),1)  

class NeighborhoodTestCase(TestCase):
    def setUp(self):
        self.new_post = Business(name = 'testT',hood_logo='test.jpg',location = 'testD',admin ='favian', health_contact='070000', police_number='07000')


    def test_create_neighborhood(self):
        self.new_post.save_project()
        location = NeighborHood.objects.all()
        self.assertEqual(len(location),1)

    def test_delete_neighborhood(self):
        self.new_post.delete_project()
        location = NeighborHood.objects.all()
        self.assertEqual(len(location),1)  