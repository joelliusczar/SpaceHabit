from TestDummyObjectMaker import DailySortingTestObject
from SpaceUnitTest import SpaceUnitTest
from collections import OrderedDict
from Heap import Heap
import random

class Test_Heap(SpaceUnitTest):
  
  def setUp(self):

    self.testList = []
    self.controlList = []
    for i in range(0,500):
      u = i // 100
      r = (500 -i) // 25
      f = i
      tObj = DailySortingTestObject(u,r,f)
      self.testList.append(tObj)
      self.controlList.append(tObj)
    random.shuffle(self.testList)
  
    print("done")
    return super().setUp()

  def tearDown(self):

    return super().tearDown()

  def test_heap_basic_functions(self):
    heap = Heap(lambda x,y: x > y)
    self.assertTrue(heap.is_empty())
    self.assertEqual(len(heap),0)
    heap.push(5)
    self.assertEqual(len(heap),1)
    heap.push_list([3,8,1,4])
    self.assertEqual(len(heap),5)
    
  def test_heapsort(self):
    heap1 = Heap(lambda x,y: x > y)
    presorted = []
    for i in range(0,1000):
      randNum = random.randint(0,1000)
      presorted.append(randNum)
      heap1.push(randNum)
    sorted = heap1.get_sorted_list()  
    prev = sorted[0]
    for s in sorted:
      self.assertTrue(s <= prev)
      prev = s

    presorted.sort()
    self.assertTrue(heap1.is_empty())
    for p in presorted:
      heap1.push(p)
    sorted1 = heap1.get_sorted_list()
    prev = sorted1[0]
    for s in sorted1:
      self.assertTrue(s <= prev)
      prev = s

    presorted.reverse()
    self.assertTrue(heap1.is_empty())
    for p in presorted:
      heap1.push(p)
    sorted2 = heap1.get_sorted_list()
    prev = sorted2[0]
    for s in sorted2:
      self.assertTrue(s <= prev)
      prev = s

    self.assertTrue(heap1.is_empty())
    for i in range(0,1000):
      heap1.push(random.randint(0,1000))
    prev = heap1.pop()
    for p in heap1.popper():
      self.assertTrue(s <= prev)
      prev = s

  def test_multifield_heapsort(self):
    heap = Heap(lambda a,b: a.daysUntilTrigger <= b.daysUntilTrigger 
          and a.urgency >= b.urgency and a.difficulty <= b.difficulty)
    heap.push_list(self.testList)
    for a,c in zip(heap.popper(),self.controlList):
      self.assertEqual(a.daysUntilTrigger,c.daysUntilTrigger)
      self.assertEqual(a.urgency,c.urgency)
      self.assertEqual(a.difficulty,c.difficulty)

if __name__ == '__main__':
  unittest.main()
