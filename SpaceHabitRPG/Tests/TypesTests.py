import unittest
import DatabaseLayer
import MockDatabaseLayer
import TypeCreators
from Hero import Hero

class Test_TypesTests(unittest.TestCase):
    def setUp(self):
        DatabaseLayer.insert_thing = MockDatabaseLayer.insert_thing
        DatabaseLayer.get_thing_by_id = MockDatabaseLayer.get_thing_by_id
        DatabaseLayer.update_thing_by_id = MockDatabaseLayer.update_thing_by_id
        return super().setUp()

    def test_Hero_get_and_set(self):
        id = TypeCreators.create_new_hero("cpt. Hook","Jolly Roger")
        self.assertEqual(id,"heros0")
        hero_stuff = DatabaseLayer.get_thing_by_id(id,"heros")
        id2 = TypeCreators.create_new_hero("Pablo Escobar","USS Asskicked")
        self.assertEqual(id2,"heros1")
        hero0 = Hero(dict=hero_stuff)
        hero1 = Hero(id=id2)
        self.assertEqual(hero0.name,"cpt. Hook")
        self.assertEqual(hero1.name,"Pablo Escobar")
        hero1.lvl = 3
        hero2 = Hero(id=id2)
        self.assertEqual(hero2.lvl,1)
        hero1.save_changes()
        hero3 = Hero(id=id2)
        self.assertEqual(hero3.lvl,3)



        

if __name__ == '__main__':
    unittest.main()
