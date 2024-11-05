
#Open and read the file
data = open('book_data.txt', 'r')
book_data_list = [] #Empty list the data will be appended to.

for line in data:
    if not line.startswith('#'): #Ignores all comments.
        book_data = line.strip().split(';') #Seperates each bit of data
        # by a semi-colon.
        # Checks if each line contains all 7 columns of
        # complete book data, ensuring no data is missed.
        if len(book_data) >= 7:
            book_data_list.append(book_data)

data.close()

def task1():
    # Task 1 - Output a list of book titles and their respective details

    # Function to separate elements in the string 'book_data' using ;.
    def book_details(book_data):
        books_list = []
        details = book_data.split(';')

        # Check length of list and create a dictionary.
        if len(details) == 7:
            return {
                "Author": details[0],
                "Title": details[1],
                "Format": details[2],
                "Publisher": details[3],
                "Cost": float(details[4]),
                "Stock": int(details[5]),
                "Genre": details[6]
            }
        else:
            return None  # invalid details return None.

    # Try to open file 'book_data.txt' in read mode.
    try:
        with open('book_data.txt', 'r') as file:
            data = file.readlines()
            books = [book_details(line.strip()) for line in data if line.strip()]

            # Print title and book details.
        print("Book Titles and Their Respective Details")
        for book in books:
            if book:
                print("Title:", book["Title"])
                print("Author:", book["Author"])
                print("Format:", book["Format"])
                print("Publisher:", book["Publisher"])
                print("Cost:", book["Cost"])
                print("Stock:", book["Stock"])
                print("Genre:", book["Genre"])
                print()

                # Error message if file is not found.
    except FileNotFoundError:
        print("The file 'book_data.txt' does not exist.")

    return main()


# Task 2: Output a summary report displaying (a) total number of book titles,
# (b) total value of books in stock, (c) the average price of books in stock.
def bookreport():
    tot_titles = 0
    tot_val = 0

    # calculates the total number of book titles, value of available stock and
    # the overall average price of books for Bertha.
    for book in book_data_list:
        tot_titles += 1
        tot_val += (float(book[4]) * float(book[5]))
    # avg price of all books in stock.
    avg_price = tot_val / tot_titles


    #The report itself:
    print("Booksville Books Summary Report:")
    print("--------------------------------")
    print(f"Total number of book titles: {tot_titles}")
    print(f"Total value of books in stock: £{tot_val:.2f}")
    print(f"Average prices of books in stock: £{avg_price:.2f}")

    return main()

def task3():
    # Task 3 - Output a report detailing the number of titles existing in each genre type.

    # Generate report and create dictionary to store info on each genre.
    def generate_genre_report():
        genre_info = {}

        # Open 'book_data.txt' in read mode
        with open("book_data.txt", 'r') as file:
            # Skip the first two lines
            next(file)
            next(file)

            # For loop iterates through each line in the file.
            for line in file:
                # Split the line with delimiter ;.
                data = line.strip().split(';')

                # Extract genre information
                if len(data) >= 7:  # Ensure all necessary fields are present
                    genre = data[-1]
                    title = data[1]

                    # Update genre info
                    if genre in genre_info:
                        genre_info[genre]["count"] += 1
                        genre_info[genre]["titles"].append(title)
                    else:
                        genre_info[genre] = {"count": 1, "titles": [title]}

        return genre_info

        # Print genre report header.

    def print_genre_report(genre_info):
        print("Genre Report:")

        # For loop iterates through each genre in dictionary.
        for genre, info in genre_info.items():
            count = info["count"]
            titles = info["titles"]
            print()
            # Print genre name and list of titles.
            print(f"{genre.capitalize()}: {count} titles")
            for title in titles:
                print(f"  - {title}")

                # Generate and print genre report.

    def genre():
        genre_info = generate_genre_report()
        print_genre_report(genre_info)
        print()

    if __name__ == "__main__":
        genre()

    return main()

def task4():
    # Task 4 - Option to add a new book item and present a summary report
    # displaying the increase in total number of titles in stock

    # Read 'book_data' file and return a list of dictionaries.
    def read_book_data(book_data):
        books = []
        with open('book_data.txt', 'r') as file:
            for line in file:
                if line.strip() and not line.startswith('#'):
                    book_details = line.strip().split(';')
                    if len(book_details) >= 7:
                        try:
                            stock = int(book_details[5])
                        except ValueError:
                            continue

                        # Create dictionary for each book.
                        book = {
                            'Author': book_details[0],
                            'Title': book_details[1],
                            'Format': book_details[2],
                            'Publisher': book_details[3],
                            'Cost': float(book_details[4]),
                            'Stock': stock,
                            'Genre': book_details[6]
                        }
                        books.append(book)
        return books

        # Append data in 'book_data.txt' to add new book

    def add_book(books, new_book):
        with open('book_data.txt', 'a') as append_book:
            append_book.write(f"{new_book['Author']};{new_book['Title']};{new_book['Format']};"
                              f"{new_book['Publisher']};{new_book['Cost']};{new_book['Stock']};"
                              f"{new_book['Genre']}\n")
        books.append(new_book)

        # Calculate the stock increase.

    def calculate_stock_increase(books, original_stock):
        current_stock = sum(book['Stock'] for book in books)
        increase = current_stock - original_stock
        return increase

        # Generate summery report.

    def summary_report(original_stock, new_stock, increase):
        report = {
            "Original number of titles in stock": original_stock,
            "Updated number of titles in stock": new_stock,
            "Increase in stock count": increase
        }
        return report

        # Main function to run the inventory management system

    def IMS():
        file_name = 'book_data.txt'
        books = read_book_data(file_name)

        while True:
            original_stock = sum(book['Stock'] for book in books)

            # Input details of new book
            new_book = {
                'Title': input("Enter the title: "),
                'Author': input("Enter the author: "),
                'Format': input("Enter the format (hb/pb): "),
                'Publisher': input("Enter the publisher: "),
                'Cost': float(input("Enter the cost: ")),
                'Stock': int(input("Enter the stock count: ")),
                'Genre': input("Enter the genre: ")
            }
            print()

            add_book(books, new_book)
            new_stock = sum(book['Stock'] for book in books)
            increase = calculate_stock_increase(books, original_stock)

            # Generate and display summary report
            report = summary_report(original_stock, new_stock, increase)
            print("Summary Report:")
            print("Original number of titles in stock: " + str(report['Original number of titles in stock']))
            print("Updated number of titles in stock: " + str(report['Updated number of titles in stock']))
            print("Increase in stock count: " + str(report['Increase in stock count']))
            print()

            # Ask user if they want to add another book
            another_book = input("Do you want to add another book? (yes/no): ").strip().lower()
            if another_book != 'yes':
                break

    if __name__ == "__main__":
        IMS()

    return main()


#5.	Query if a book title is available and present the option of
# (a) increasing stock level or (b) decreasing the stock level, due to a sale.
# If the stock level is decreased to zero indicate to the user that the
# book is now out of stock.
def availability():
    book_type = input("Which book title would you like to search for? ")
    stock = 0

    for book in book_data_list:  #For loop added, due to multiple copies of some books.
        if book[1] == book_type:
            # current stock value assigned to the variable 'Stock'.
            stock = int(book[5])
            if stock >= 1: #If the stock value is above zero, it's available.
                print("Yes! It's available.")
            else:
                print("Apologies! That book is out of stock.")
            #Option to increase or decrease the current stock level.
            stock_ans = input("Would you like to change the stock level? Type 'y' for yes,"
                              "or any other key to exit.")
            if stock_ans == 'y' or stock_ans == 'Y':
                stock_option = input("Type 1 to increase stock, type 2 to decrease it. ")
                if stock_option == '1':
                    stockincr_num = int(input("How much will you increase the stock by: "))
                    new_incr_stock = stock + stockincr_num
                elif stock_option == '2':
                    stockdecr_num = int(input("How much will you decrease the stock by: "))
                    new_decr_stock = stock - stockdecr_num
                else: #If input is invalid, Bertha must re-enter a valid input.
                    print("Invalid input. Please type a valid input")
                    availability()
            else:
                print("Ok! Have a nice day!")
            break

    print("Updated stock numbers: ") #Report displaying the new stock number
    print(f"Book title: {book_type}") # depending on Berta's selection.
    if stock_option == '1':   #If stock is increased, the increased stock is shown
        print(f"{book_type}'s new stock: {new_incr_stock}")
    elif stock_option == '2': #If stock is decreased, the decreased stock is shown.
        print(f"{book_type}'s new stock: {new_decr_stock}")
    # Brings Berta back to the main menu once she's finished
    # allowing her to make another menu selection if needed.
    main()

# Task 6: Output a list of book items ordered in alphabetical order by author.
def alph_sort():
    book_titles = []

    # Prints the title and author of each book, sorted by author.
    for book in book_data_list:
        book_content = book[0], book[1]
        book_titles.append(book_content)

    #sort the list by the author's name alphabettically.
    ordered_books = sorted(book_titles)
    print(f"Book items ordered in alphabetical order:")
    print(ordered_books)

    return main()

def task7():
    # Task 7 - Plot a labelled bar chart that presents the number of books existing in each genre type

    # Import library.
    from matplotlib import pyplot as plt

    genre = []
    count = []

    # Opens 'book_data.txt' in read mode.
    with open('book_data.txt', 'r') as f:
        next(f)
        next(f)

        # For loop iterates through each line in the file.
        for line in f:
            columns = line.strip().split(';')
            genre.append(columns[-1])
            count.append(1)

            # Keeping count of each genre occurrence.
    genre_counts = {}
    for g in genre:
        genre_counts[g] = genre_counts.get(g, 0) + 1

        # Extract genre types and counts.
    genre_types = list(genre_counts.keys())
    genre_seat_counts = list(genre_counts.values())

    # Position of bars on x-axis.
    left_edges = range(len(genre_types))

    # Create bar chart
    plt.bar(left_edges, genre_seat_counts, color='purple')
    plt.xticks(left_edges, genre_types)
    plt.title('The Number of Books Existing in Each Genre')
    plt.xlabel('Genre')
    plt.ylabel('Number of Books')
    plt.tight_layout()
    plt.show()

    return main()


# Booksville Book's main menu, which Berta can use
# to make a task selection.
def main():
    print("---------Welcome to Booksville Books---------")

    print("""1 - List of book titles and their details
         2 - Summary report displaying number, value and average of books in stock"]
         3 - Report for number of titles of different genres
         4 - Add a new book item and get updated stock
         5 - See if a book title is available, and edit stock levels
         6 - List book items ordered in alphabetical order
         7 - Show bar chart presenting number of books in each genre
         8 - Exit the program""")

    selection = input("Please enter the number of the task you wish to carry out:")
    # List of tasks Bertha is able to select from:
    while True:
        if selection == "1":
            task1()
        elif selection == "2":
            bookreport()
        elif selection == "3":
            task3()
        elif selection == "4":
            task4()
        elif selection == "5":
            availability()
        elif selection == "6":
            alph_sort()
        elif selection == "7":
            task7()
        elif selection == "8":
            print("Okay, goodbye!")
            break
        else:
            print("Selection not available. Please enter a valid selection!")
            # Returns Berta back to the beginning of the menu
            # to re-enter a correct selection
            main()
main()










