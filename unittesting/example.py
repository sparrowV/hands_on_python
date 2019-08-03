import unittest


class Client:
    def __init__(self,username):
        self.username = username
        self.balance = 0

    def get_username(self):
        return self.username

    def get_balance(self):
        return self.balance

    def add_funds(self,amount):
        self.balance+=amount

    def withdraw_funds(self,amount):
        if(amount > self.balance):
            raise Exception
        else:
            self.balance-=amount

    def transfer_to_another_account(self,amount,clientTo):
            if(self.balance < amount):
                raise Exception
            else:
                self.withdraw_funds(amount)
                clientTo.add_funds(amount)


class TestClient(unittest.TestCase):
    def setUp(self):
        mark = Client('Mark')
        tom = Client('Tom')
        self.mark = mark
        self.tom = tom
        #possible extension is to add another client, for example tim, and test transef_to_another_account method with triple transaction

    def test_get_balance(self):
        self.assertEqual(self.mark.get_balance(),0)
        self.assertTrue(self.tom.get_balance() == 0)

    def test_add_funds(self):
        self.mark.add_funds(500)
        self.assertNotEqual(self.mark.get_balance(),0)
        self.assertEqual(self.mark.get_balance(),500)

    def test_withdraw_funds(self):
        self.assertRaises(Exception,self.mark.withdraw_funds,20)
        self.mark.add_funds(400)
        self.mark.withdraw_funds(300)
        self.assertTrue(self.mark.get_balance() == 100)

    def test_transfer_to_another_account(self):
        self.mark.add_funds(1000)
        self.assertRaises(Exception,self.mark.transfer_to_another_account,2000,self.tom)
        self.mark.transfer_to_another_account(200,self.tom)
        self.assertEqual(self.mark.get_balance(), 800)
        self.assertTrue(self.tom.get_balance() == 200)

        #extension here for triple transaction
