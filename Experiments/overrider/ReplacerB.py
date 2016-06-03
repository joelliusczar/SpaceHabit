import Top

print("Importing replacer B")

def counterfeit_print_one():
    print("counterfeit 1")

def replace():
    Top.print_one = counterfeit_print_one

def call_print_one():
    Top.print_one()