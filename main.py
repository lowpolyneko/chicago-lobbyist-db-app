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
    """
    Given the user input of a name, find and output basic information for all
    lobbyists that match that name.

    @param db database
    """
    search = input('\nEnter lobbyist name (first or last, wildcards _ and % supported): ')
    lobbyists = objecttier.get_lobbyists(db, search)

    # check for too many items
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
    """
    Given a lobbyist ID, find and output detailed information about the
    lobbyist.

    @param db database
    """
    search = input('\nEnter Lobbyist ID: ')
    details = objecttier.get_lobbyist_details(db, search)

    # error check
    if not details:
        print('\nNo lobbyist with that ID was found.')
        return

    print(f'\n{details.Lobbyist_ID} :')
    print(f'  Full Name: {details.Salutation} {details.First_Name} {details.Middle_Initial} {details.Last_Name} {details.Suffix}')
    print(f'  Address: {details.Address_1} {details.Address_2} , {details.City} , {details.State_Initial} {details.Zip_Code} {details.Country}')
    print(f'  Email: {details.Email}')
    print(f'  Phone: {details.Phone}')
    print(f'  Fax: {details.Fax}')
    print('  Years Registered: ', end='')
    for y in details.Years_Registered:
        print(y, end=', ')
    print('\n  Employers: ', end='')
    for e in details.Employers:
        print(e, end=', ')
    print(f'\n  Total Compensation: ${details.Total_Compensation:,.02f}')


##################################################################  
#
# command 3
#
def command_3(db: sqlite3.Connection):
    """
    Given a year, output the top N lobbyists based on their total compensation
    for that year.

    @param db database
    """
    N = input('\nEnter the value of N: ')
    if int(N) < 1:
        print('Please enter a positive value for N...')
        return

    year = input('Enter the year: ')

    top_n_lobbyists = objecttier.get_top_N_lobbyists(db, N, year)

    # enumerate for index
    for i, l in enumerate(top_n_lobbyists):
        print(f'{i} . {l.First_Name} {l.Last_Name}')
        print(f'  Phone: {l.Phone}')
        print(f'  Total Compensation: ${l.Total_Compensation:,.02f}')
        print('  Clients: ', end='')
        for c in l.Clients:
            print(c, end=', ')


##################################################################  
#
# command 4
#
def command_4(db: sqlite3.Connection):
    """
    Register an existing lobbyist for a new year.

    @param db database
    """
    year = input('\nEnter year: ')
    search = input('Enter the lobbyist ID: ')

    # 1 for success, 0 for failure
    if objecttier.add_lobbyist_year(db, search, year):
        print('\nLobbyist successfully registered.')
    else:
        print('\nNo lobbyist with that ID was found.')


##################################################################  
#
# command 5
#
def command_5(db: sqlite3.Connection):
    """
    Set the salutation for a given lobbyist.

    @param db database
    """
    search = input('\nEnter the lobbyist ID: ')
    salutation = input('Enter the salutation: ')

    # 1 for success, 0 for failure
    if objecttier.set_salutation(db, search, salutation):
        print('\nSalutation successfully set.')
    else:
        print('\nNo lobbyist with that ID was found.')


##################################################################  
#
# print stats
#
def print_stats(db: sqlite3.Connection):
    """
    Print general statistics of the database.

    @param db database
    """
    print('\nGeneral Statistics:')
    print(f'  Number of Lobbyists: {objecttier.num_lobbyists(db):,}')
    print(f'  Number of Employers: {objecttier.num_employers(db):,}')
    print(f'  Number of Clients: {objecttier.num_clients(db):,}')


##################################################################  
#
# main
#
def main():
    dbConn = sqlite3.connect("Chicago_Lobbyists.db")

    print('** Welcome to the Chicago Lobbyist Database Application **')
    print_stats(dbConn)

    # main eval loop
    while True:
        i = input('\nPlease enter a command (1-5, x to exit): ')

        if i == '1':
            command_1(dbConn)
            continue
        elif i == '2':
            command_2(dbConn)
            continue
        elif i == '3':
            command_3(dbConn)
            continue
        elif i == '4':
            command_4(dbConn)
            continue
        elif i == '5':
            command_5(dbConn)
            continue
        elif i == 'x':
            break

        print('**Error, unknown command, try again...')


if __name__ == '__main__':
    main()

#
# done
#
