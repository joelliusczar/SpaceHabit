import unittest

class SpaceUnitTest(unittest.TestCase):
    """description of class"""

    def assertTrue(self, expr, msg = None):
        self.assertEqual(expr,True,msg)

    def assertTrue_legacy(self, expr, msg = None):
        return super().assertTrue(expr, msg)

    def assertFalse(self, expr, msg = None):
        self.assertEqual(expr,False,msg)

    def assertFalse_legacy(self, expr, msg = None):
        return super().assertFalse(expr, msg)



