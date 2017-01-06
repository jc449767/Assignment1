__author__ = 'jc449767'
#Syed Shareq Ahmed  Student id - 13428326  jc id - jc449767
# Initializing the respective constants
#https://github.com/jc449767/CP5632_assignment1.git

FILE = "books.csv"


def main():
    print("Reading List 1.0 - by Syed Shareq Ahmed")
    book_list = []
    load_books(book_list)
    print(book_list)
    display_menu()
    choice = input(">>>")
    while choice.lower() != 'q':
        if choice.lower() == 'r':
            required_a_book(book_list)
        elif choice.lower() == 'c':
            completed_books(book_list)
        elif choice.lower() == 'a':
            book_list = add_books()
        elif choice.lower() == 'm':
            complete_books(book_list)
        else:
            print("invalid menu choice")
        display_menu()
        choice = input(">>>")
    print("{} books have been saved to {}".format(len(book_list), FILE))
    print("Have a nice day :)")


def display_menu():
    """
	The following respective function is used to display the menu options
"""
    MENU = "Menu: \nR - List required books\nC - List completed books\nA - Add new book\nM - Mark a book as " \
           "completed\nQ - Quit"
    print(MENU)


# end of display_menu function

def load_books(book_list):
    """
    Following function is used to load the books from file to list
    book_file <- open books.csv in read mode
    loop line in book_file
        append line to book_list
    close book_file
"""
    book_file = open(FILE, 'r')
    for line in book_file:
        book_list.append(line.strip().split(','))
    book_file.close()


# end of load_books()

def complete_books(book_list):
    """
	Following function is used to mark a book as completed in the file
	call required_a_book function with aurgument book_list
	output "Enter the number of a book to mark as completed"
	try
	input num_of_book
	if third book in book list 'c':
	output "That book is already completed"
	else third book in book list is 'c'
	book file <- open file in write mode
	for book in book_list and
	write string of four books
	output display the book file
	book file >- close
	output "display the book with title and author of that book"
	except valueError
	output 'Invalid input; enter a valid number'


"""
    required_a_book(book_list)
    print("Enter the number of a book to mark as completed")
    try:
        num_of_book = int(input(">>>"))
        if book_list[num_of_book][3] == 'c':
            print("That book is already completed")
        else:
            book_list[num_of_book][3] = 'c'
            books_file = open(FILE, 'w')
            for book in book_list:
                line = book[0] + ',' + book[1] + ',' + book[2] + ',' + book[3]
                print(line,file=books_file)
            books_file.close()
            print("{} by {} is completed".format(book_list[num_of_book][0], book_list[num_of_book][1]))
    except ValueError:
        print('Invalid input; enter a valid number')
        #complete_a_book(book_list)


# end of complete_a_book()

def required_a_book(book_list):
    """
	The given respective function displays the list of books which is need to be read
	intializing total pages to 0
	output "Required Books:"
	intialize count to 0
	for i in book_list
	if 'r' in third book of the book list
	output "display the three books with their details with specific spacing as mentioned
    adding second book from book list to total pages
    incrementing count to +1
    if count is greater than 0:
    output "display the total pages for books"
    else
    output "No books"



"""

    total_pages = 0
    print("Required Books:")
    count = 0
    for i in book_list:
        if 'r' in book_list[count][3]:
            print("{}. {:<45s} by {:<15s} {:>10s} pages".format(count, book_list[count][0], book_list[count][1],
                                                                book_list[count][2]))
            total_pages = total_pages + int(book_list[count][2])
        count = count + 1
    if count > 0:
        print("Total pages for {} books: {}".format(count - 1, total_pages))
    else:
        print("No books")


# end of required_books function

def completed_books(book_list):
    """
	The following given function is used to print all completed books
	initializing total pages to 0
	output "Required Books:"
	initialize count to 0
	for book in book_list:
        if 'c' in third book of the book list
        get output "display the three books with their details with specific spacing
        incrementing count to 1
        adding  second book from book list to total pages

         get output  "displaying the total pages for the books"
"""
    total_pages = 0
    print("Required Books:")
    count = 0
    count2=0
    for i in book_list:
        if 'c' in i[3]:
            print("{}. {:<45s} by {:<15s} {:>10s} pages".format(count, book_list[count][0], book_list[count][1],
                                                                book_list[count][2]))
            total_pages = total_pages + int(book_list[count][2])
            count2 = count2 + 1
        count = count+1
    print("Total pages for {} books: {}".format(count2 , total_pages))


# end of completed_books function

def add_books():
    """
	The given respective function gives us the facility to add books to the file books.csv
	write
"""

    title = input("Title:")
    while title == "":
        print("Input can not be blank")
        title = input("Title:")
    author = input("Author:")
    while author == "":
        print("Input can not be blank")
        author = input("Author:")
    flag = 0
    pages = 0
    while flag == 0:
        try:
            pages = int(input("Pages: "))
            while pages <= 0:
                print("Number must be >= 0")
                pages = int(input("Pages: "))
            flag = 1
        except ValueError:
            print("Invalid input; enter a valid number")
    print("{} by {}, ({} pages) added to reading list".format(title, author, pages))
    book = [title, author, str(pages), 'r']
    book_list = []
    load_books(book_list)
    print(book_list)
    book_list.append(book)
    print(book_list)
    books_file = open(FILE, 'w')
    for book in book_list:
                line = book[0] + ',' + book[1] + ',' + book[2] + ',' + book[3]
                print(line,file=books_file)
    books_file.close()
    return book_list


# end of add_books function
main()
