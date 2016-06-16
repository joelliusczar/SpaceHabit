import DatabaseLayer
import UserDBLayer
import MockDatabaseLayer

def set_up_mock_db_connections():
    DatabaseLayer.delete_thing_by_key = MockDatabaseLayer.delete_thing_by_key
    DatabaseLayer.get_sorted_stuff_by_search = MockDatabaseLayer.get_sorted_stuff_by_key
    DatabaseLayer.get_table = MockDatabaseLayer.get_table
    DatabaseLayer.get_thing_by_id = MockDatabaseLayer.get_thing_by_id
    DatabaseLayer.insert_thing = MockDatabaseLayer.insert_thing
    DatabaseLayer.update_thing_by_id = MockDatabaseLayer.update_thing_by_id
    DatabaseLayer.get_count_of_stuff_search = MockDatabaseLayer.get_count_of_stuff_search
    UserDBLayer.does_login_exist = MockDatabaseLayer.does_login_exist
    UserDBLayer.get_user = MockDatabaseLayer.get_user
    UserDBLayer.get_user_collection = MockDatabaseLayer.get_user_collection
    UserDBLayer.insert_user = MockDatabaseLayer.insert_user