from prettytable import PrettyTable

table = PrettyTable()

table.field_names = ['Pokemon Name', 'Type']
table.add_rows(
    [
        ['Pikachu', 'Electric'], 
        ['Squirtle', 'Water'], 
        ['Charmander', 'Fire']
    ]
)

print(table)

table.align = 'l'
print(f'change alignment to left\n {table}')

table.del_row(2)
print(f'delete row at index 2\n {table}')