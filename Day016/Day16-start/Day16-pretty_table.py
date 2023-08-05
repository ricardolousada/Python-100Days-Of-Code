from prettytable import PrettyTable

my_table = PrettyTable()
my_table.add_column("Pokemon Name",["Pikachu","Squirle","Charmander"])
my_table.add_column("Type",["Electric","Water","Fire"])
my_table.align = "l"
print(my_table)

