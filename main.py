#!/usr/bin/env python

## CS 341, Fall 2024
## System: Arch GNU/Linux (Python 3.12) using nvim
## Author: Ethan Wong
#
# Chicago Lobbyist Database App
#
# Text UI to query information about Chicago Lobbyists.
#
import sqlite3
import objecttier

##################################################################  
#
# command 1
#
def command_1(db: sqlite3.Connection):
    search = input('\nEnter lobbyist name (first or last, wildcards _ and % supported): ')
    lobbyists = objecttier.get_lobbyists(db, search)

    if len(lobbyists) > 100:
        print('\nThere are too many lobbyists to display, please narrow your search and try again...')
        return

    print(f'\nNumber of lobbyists found: {len(lobbyists)}\n')

    for l in lobbyists:
        print(f'{l.Lobbyist_ID} : {l.First_Name} {l.Last_Name} Phone: {l.Phone}')
        

##################################################################  
#
# command 2
#
def command_2(db: sqlite3.Connection):
    search = input('\nEnter Lobbyist ID: ')
    details = objecttier.get_lobbyist_details(db, search)

    if not details:
        print('\nNo lobbyist with that ID was found.')
        return

    print(f'\n{details.Lobbyist_ID} :')
    print(f'  Full Name: {details.Salutation} {details.First_Name} {details.Middle_Initial} {details.Last_Name} {details.Suffix}')
    print(f'  Address: {details.Address_1} {details.Address_2} , {details.City} , {details.State_Initial} , {details.Zip_Code} {details.Country}')
    print(f'  Email: {details.Email}')
    print(f'  Phone: {details.Phone}')
    print(f'  Fax: {details.Fax}')
    print('  Years Registered: ', end='')
    for y in details.Years_Registered:
        print(f'{y}', end=', ')
    print('\n  Employers: ', end='')
    for e in details.Employers:
        print(f'{e}', end=', ')
    print(f'\n  Total Compensation: ${details.Total_Compensation:.02f}')


##################################################################  
#
# main
#
def main():
    print('** Welcome to the Chicago Lobbyist Database Application **')

    db = sqlite3.connect('Chicago_Lobbyists.db')


    while True:
        i = input('\nPlease enter a command (1-5, x to exit): ')

        if i == '1':
            command_1(db)
            continue
        elif i == '2':
            command_2(db)
            continue
        elif i == '3':
            # command_3(db)
            continue
        elif i == '4':
            # command_4(db)
            continue
        elif i == '5':
            # command_5(db)
            continue
        elif i == 'x':
            break

    print('**Error, unknown command, try again...')


if __name__ == '__main__':
    main()

#
# done
#
