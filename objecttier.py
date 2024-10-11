## CS 341, Fall 2024
## System: Arch GNU/Linux (Python 3.12) using nvim
## Author: Ethan Wong
#
# objecttier
#
# Builds Lobbyist-related objects from data retrieved through 
# the data tier.
#
# Original author: Ellen Kidane
#
import datatier


##################################################################
#
# Lobbyist:
#
# Constructor(...)
# Properties:
#   Lobbyist_ID: int
#   First_Name: string
#   Last_Name: string
#   Phone: string
#
class Lobbyist:
    def __init__(self, Lobbyist_ID: int, First_Name: str, Last_Name: str, Phone: str) -> None:
        self.__Lobbyist_ID = Lobbyist_ID
        self.__First_Name = First_Name
        self.__Last_Name = Last_Name
        self.__Phone = Phone

    @property
    def Lobbyist_ID(self) -> int:
        return self.__Lobbyist_ID

    @property
    def First_Name(self) -> str:
        return self.__First_Name

    @property
    def Last_Name(self) -> str:
        return self.__Last_Name

    @property
    def Phone(self) -> str:
        return self.__Phone

##################################################################
#
# LobbyistDetails:
#
# Constructor(...)
# Properties:
#   Lobbyist_ID: int
#   Salutation: string
#   First_Name: string
#   Middle_Initial: string
#   Last_Name: string
#   Suffix: string
#   Address_1: string
#   Address_2: string
#   City: string
#   State_Initial: string
#   Zip_Code: string
#   Country: string
#   Email: string
#   Phone: string
#   Fax: string
#   Years_Registered: list of years
#   Employers: list of employer names
#   Total_Compensation: float
#
class LobbyistDetails:
    def __init__(self, Lobbyist_ID: int, Salutation: str, First_Name: str, Middle_Initial: str, Last_Name: str, Suffix: str, Address_1: str, Address_2: str, City: str, State_Initial: str, Zip_Code: str, Country: str, Email: str, Phone: str, Fax: str, Years_Registered: list[str], Employers: list[str], Total_Compensation: float) -> None:
        self.__Lobbyist_ID = Lobbyist_ID
        self.__Salutation = Salutation
        self.__First_Name = First_Name
        self.__Middle_Initial = Middle_Initial
        self.__Last_Name = Last_Name
        self.__Suffix = Suffix
        self.__Address_1 = Address_1
        self.__Address_2 = Address_2
        self.__City = City
        self.__State_Initial = State_Initial
        self.__Zip_Code = Zip_Code
        self.__Country = Country
        self.__Email = Email
        self.__Phone = Phone
        self.__Fax = Fax
        self.__Years_Registered = Years_Registered
        self.__Employers = Employers
        self.__Total_Compensation = Total_Compensation

    @property
    def Lobbyist_ID(self) -> int:
        return self.__Lobbyist_ID

    @property
    def Salutation(self) -> str:
        return self.__Salutation

    @property
    def First_Name(self) -> str:
        return self.__First_Name

    @property
    def Middle_Initial(self) -> str:
        return self.__Middle_Initial

    @property
    def Last_Name(self) -> str:
        return self.__Last_Name

    @property
    def Address_1(self) -> str:
        return self.__Address_1

    @property
    def Address_2(self) -> str:
        return self.__Address_2

    @property
    def Suffix(self) -> str:
        return self.__Suffix

    @property
    def City(self) -> str:
        return self.__City

    @property
    def State_Initial(self) -> str:
        return self.__State_Initial

    @property
    def Zip_Code(self) -> str:
        return self.__Zip_Code

    @property
    def Country(self) -> str:
        return self.__Country

    @property
    def Email(self) -> str:
        return self.__Email

    @property
    def Phone(self) -> str:
        return self.__Phone

    @property
    def Fax(self) -> str:
        return self.__Fax

    @property
    def Years_Registered(self) -> list[str]:
        return self.__Years_Registered

    @property
    def Employers(self) -> list[str]:
        return self.__Employers

    @property
    def Total_Compensation(self) -> float:
        return self.__Total_Compensation

##################################################################
#
# LobbyistClients:
#
# Constructor(...)
# Properties:
#   Lobbyist_ID: int
#   First_Name: string
#   Last_Name: string
#   Phone: string
#   Total_Compensation: float
#   Clients: list of clients
#
class LobbyistClients:
    def __init__(self, Lobbyist_ID: int, First_Name: str, Last_Name: str, Phone: str, Total_Compensation: float, Clients: list[str]) -> None:
        self.__Lobbyist_ID = Lobbyist_ID
        self.__First_Name = First_Name
        self.__Last_Name = Last_Name
        self.__Phone = Phone
        self.__Total_Compensation = Total_Compensation
        self.__Clients = Clients

    @property
    def Lobbyist_ID(self) -> int:
        return self.__Lobbyist_ID

    @property
    def First_Name(self) -> str:
        return self.__First_Name

    @property
    def Last_Name(self) -> str:
        return self.__Last_Name

    @property
    def Phone(self) -> str:
        return self.__Phone

    @property
    def Total_Compensation(self) -> float:
        return self.__Total_Compensation

    @property
    def Clients(self) -> list[str]:
        return self.__Clients

##################################################################
# 
# num_lobbyists:
#
# Returns: number of lobbyists in the database
#           If an error occurs, the function returns -1
#
def num_lobbyists(dbConn):
   pass

##################################################################
# 
# num_employers:
#
# Returns: number of employers in the database
#           If an error occurs, the function returns -1
#
def num_employers(dbConn):
   pass

##################################################################
# 
# num_clients:
#
# Returns: number of clients in the database
#           If an error occurs, the function returns -1
#
def num_clients(dbConn):
   pass

##################################################################
#
# get_lobbyists:
#
# gets and returns all lobbyists whose first or last name are "like"
# the pattern. Patterns are based on SQL, which allow the _ and % 
# wildcards.
#
# Returns: list of lobbyists in ascending order by ID; 
#          an empty list means the query did not retrieve
#          any data (or an internal error occurred, in
#          which case an error msg is already output).
#
def get_lobbyists(dbConn, pattern):
   pass


##################################################################
#
# get_lobbyist_details:
#
# gets and returns details about the given lobbyist
# the lobbyist id is passed as a parameter
#
# Returns: if the search was successful, a LobbyistDetails object
#          is returned. If the search did not find a matching
#          lobbyist, None is returned; note that None is also 
#          returned if an internal error occurred (in which
#          case an error msg is already output).
#
def get_lobbyist_details(dbConn, lobbyist_id):
   pass
         

##################################################################
#
# get_top_N_lobbyists:
#
# gets and returns the top N lobbyists based on their total 
# compensation, given a particular year
#
# Returns: returns a list of 0 or more LobbyistClients objects;
#          the list could be empty if the year is invalid. 
#          An empty list is also returned if an internal error 
#          occurs (in which case an error msg is already output).
#
def get_top_N_lobbyists(dbConn, N, year):
   pass


##################################################################
#
# add_lobbyist_year:
#
# Inserts the given year into the database for the given lobbyist.
# It is considered an error if the lobbyist does not exist (see below), 
# and the year is not inserted.
#
# Returns: 1 if the year was successfully added,
#          0 if not (e.g. if the lobbyist does not exist, or if
#          an internal error occurred).
#
def add_lobbyist_year(dbConn, lobbyist_id, year):
   pass


##################################################################
#
# set_salutation:
#
# Sets the salutation for the given lobbyist.
# If the lobbyist already has a salutation, it will be replaced by
# this new value. Passing a salutation of "" effectively 
# deletes the existing salutation. It is considered an error
# if the lobbyist does not exist (see below), and the salutation
# is not set.
#
# Returns: 1 if the salutation was successfully set,
#          0 if not (e.g. if the lobbyist does not exist, or if
#          an internal error occurred).
#
def set_salutation(dbConn, lobbyist_id, salutation):
   pass
