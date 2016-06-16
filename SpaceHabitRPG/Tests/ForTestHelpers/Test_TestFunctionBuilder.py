from SpaceUnitTest import SpaceUnitTest
import TestFunctionBuilder

class Test_TestFunctionBuilder(SpaceUnitTest):
    def test_build_sort_function_single_property(self):
        dictDict = {}
        dictDict[10] = {'a':0}
        dictDict[11] = {'a':1}
        dictDict[12] = {'a':2}
        compareFieldList = [('a',1)]
        comparer = TestFunctionBuilder.build_sort_by_function(compareFieldList,dictDict)
        t = comparer(dictDict[10],dictDict[11])
        self.assertTrue(t)
        t = comparer(dictDict[11],dictDict[10])
        self.assertFalse(t)
        t = comparer(dictDict[10],dictDict[10])
        self.assertTrue(t)

    def test_build_sort_function_double_property(self):
        dictDict = {}
        for i in range(0,15):
            dictDict[10 + i] = {'a':i % 5, 'b': 15-i}
        compareFieldList = [('a',1),('b',-1)]
        comparer = TestFunctionBuilder.build_sort_by_function(compareFieldList,dictDict)
        t = comparer(dictDict[10],dictDict[20])
        self.assertTrue(t)
        t = comparer(dictDict[10],dictDict[11])
        self.assertTrue(t)
        t = comparer(dictDict[10],dictDict[24])
        self.assertTrue(t)


if __name__ == '__main__':
    unittest.main()
