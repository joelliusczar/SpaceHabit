import Top

print("Importing replacer")

def fake_print_one():
    print("fake 1")

def replace():
    Top.print_one = fake_print_one

def call_print_one():
    Top.print_one()