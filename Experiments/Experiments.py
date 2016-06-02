import ConfigLayer
import ExperimentModule
import DatabaseLayer 
import ExperimentalModule2
import datetime
from bson.objectid import ObjectId
import Progression


class Experiment(object):
    """just a file to experiment with python"""
    def print_hello(self):
        print(ExperimentModule.return_something())
    def testing_testing(self):
        print("This is the non-test version")

def check_db_works():
        DatabaseLayer.open_conn()
        print(DatabaseLayer.get_open_connection().list_tables())

def python_dick():
    mydict = {'name':'joel',
              'color':'white'}

    print(mydict['name'])
    mydict['age'] = 27
    print(mydict['age'])

def add_item_to_db():
    item = {'name':"John",
            'lvl':31}
    heros = DatabaseLayer.get_table("heros")
    id = heros.insert_one(item).inserted_id
    print(id) 

def get_item_from_db():
    id = ObjectId("5733fa75eceb33173454efd0")
    hero = ModelLayer.get_hero_by_id(id)
    
    print(hero['name'])

def also_testing_testing():
    print("this is also not a test")

def update_db_item():
    hero = ModelLayer.get_hero_by_id(ObjectId("5733fa75eceb33173454efd0"))
    changes = {'lvl':145}
    ModelLayer.update_hero(hero,changes)

def get_non_existent_item_from_db():
    a = DatabaseLayer.get_stuff_by_id(ObjectId("5733fa75ec00000000000000"),"heros")
    if not a:
        print("not A")
    if a is None:
        print("A is none")

def print_objectId_with_something_else():
    a = "B - " + str(ObjectId("5733fa75eceb33173454efd0"))
    print(a)

def playing_with_dt():
    dt = datetime.datetime
    print("")

def print_converted_numbers():
    for i in range(0,53*53):
        n = Progression.convert_number_to_naming_number_base(i,53)
        if n % 53 == 0:
            print(str(i) + ": " + str(n) +"*")
        else:
            print(str(i) + ": " + str(n))

def print_all_name_combos():
    for i in range(0,2756):
        s = Progression.generate_zone_name_suffix(i)
        print(s)

def test_something_about_ifs():
    #if 1==2:
    #    somebool = True
    #if somebool is None:
    #    print("weird")
    if 1 == 1:
        someotherbool = True
    if someotherbool:
        print("makes sense")

testa = None

def g_testa():
    global testa
    if testa:
        print("A:"+ str(testa))
    else:
        print("anope") 
    testa = 5

def g_testab():
    try:
        if testa:
            print("B:"+ str(testa))
        else:
            print("bnope")
        testa =7
    except UnboundLocalError:
        print("error in g_testab")

def g_testc():
    global testa
    if testa:
        print("C:"+ str(testa))
    else:
        print("cnope")
    testa =11

testdict = {}

def g_testa_dict():
    global testdict
    testdict['testa'] = 5

def g_testab_dict():
    try:
        if 'testa' in testdict:
            print("B:"+ str(testa))
        else:
            print("bnope")
        testdict['testa'] =7
    except UnboundLocalError:
        print("error in g_testab")

def g_testc_dict():
    global testdict
    if 'testa' in testdict:
        print("C:"+ str(testdict['testa']))
    else:
        print("cnope")
    testdict['testa'] =11

def hopefully_not_a_ref():
    a = [4,6,2,3,5]
    b = a[0]
    a[0] = 7
    print(b)
    b = 19
    print(a[0])

genList = [4,6,2,8,1,4,3,63,0,7]

def trying_out_gens():
    yield genList.pop()

def gen2():
    print(1)
    yield 8
    print(2)
    yield
    print(3)
    yield

#for n in trying_out_gens():
#    print(n)

def reverse_dict():
    dict = {'4': 1,'a':9,'z':11}
    dict['7'] = 15
    dict['j'] = 2
    items = dict.items()
    print(type(items))

def is_a_list_in_a_tuple_still_a_ref():
    a = [1,2,4,6,7,43,3,5]
    b = [3,6,26,2,7,2,6,3,8,4]
    t = (a,b)
    t[0][1] = 999
    print(a[1])

def trying_something_with_the_db_layer_and_globals():
    a = DatabaseLayer.get_table("heros")
    b = DatabaseLayer.get_table("dailies")


trying_something_with_the_db_layer_and_globals()