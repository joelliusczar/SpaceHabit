from SpaceUnitTest import SpaceUnitTest
import DatabaseLayer
import MockDatabaseLayer
from Hero import Hero
from Hero import create_new_hero

class Test_Hero(SpaceUnitTest):
    def setUp(self):
        DatabaseLayer.insert_thing = MockDatabaseLayer.insert_thing
        DatabaseLayer.get_thing_by_id = MockDatabaseLayer.get_thing_by_id
        DatabaseLayer.update_thing_by_id = MockDatabaseLayer.update_thing_by_id
        return super().setUp()

    def test_Hero_get_and_set(self):
        id = create_new_hero()
        self.assertEqual(id,"heros0")
        hero_stuff = DatabaseLayer.get_thing_by_id(id,"heros")
        id2 = create_new_hero()
        self.assertEqual(id2,"heros1")
        hero0 = Hero(dict=hero_stuff)
        hero1 = Hero(id=id2)
        hero1.lvl = 3
        hero2 = Hero(id=id2)
        self.assertEqual(hero2.lvl,1)
        hero1.save_changes()
        hero3 = Hero(id=id2)
        self.assertEqual(hero3.lvl,3)



        

if __name__ == '__main__':
    unittest.main()