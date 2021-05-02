class BookmyTicket:
    head = "\t\t\t\tBookmyTicket"

    def menu(self):  # Function for displaying menu to the user
        yes = True
        while yes:  # Loop will run until yes return True
            print("Please select the any of the given choices :")
            self.user_choice = int( input("1. Show the seats\n2. Buy a Ticket\n3. Statistics\n4. Show booked ticket's user info\n0. Exit\n"))
            if self.user_choice == 1:
                self.Show_the_seats()
            elif self.user_choice == 2:
                self.buy_a_ticket()
            elif self.user_choice == 3:
                self.statistics()
            elif self.user_choice == 4:
                self.user_info()
            elif self.user_choice == 0:
                yes = False
                self.ext()
            else:   #Loop will terminated if yes returns False
                print("\nPlease enter valid choice from given menu!!!")


    def __init__(self):
        self.row = int(input("Enter the number of rows\n"))
        self.col = int(input("Enter the number of seats in each row\n"))
        self.no_of_seats = self.row * self.col  # Calculating number of seats in the theater
        self.seats = []  # parent list for the seats
        self.seat_count = 0  # to count number of booked seats
        self.current_income = 0  # to calculate current income
        self.total_income = 0  # to calculate possible income
        self.user_details = {}  # to store details of users who booked the seat


        for i in range(self.row):  # Loop to append initial values to Matrix[]
            list1 = []           #sub_list that store the seats
            for j in range(self.col):
                list1.append("S")
            self.seats.append(list1)  #it appends 'S' in inner_list1
        print(end="  ")

    def Show_the_seats(self):  # Function used to show seats to the user (will be called by pressing 1)
        print("\nCinema :\n")
        count1 = 0  # to get no. of column in the first row .
        count2 = 0  #to get no. of row in each column.
        print(end="  ")
        for j in range(1, self.col + 1):  # Loop for printing updates matrix
            count1 = count1 + 1          #increamenting value by 1
            print(count1, end=" ")    #printing column numbers in first row
        print()
        for i in self.seats:                #printing the seating arrangements
            count2 = count2 + 1
            print(count2, end=" ")      #printing column numbers in before the column  
            print(" ".join(i), sep=",")   #it joins the element of seats list after row no.

    def buy_a_ticket(self):  # Function for Buying a Ticket(By pressing 2)
        a = int(input("Enter the row you wanted to book\n"))
        b = int(input("Enter the column you wanted to book\n"))
        if self.seats[a - 1][b - 1] == "B":  # we are checking here if it return 'B', then will show the message to the use already booked
            print("This seat is already booked")
            self.menu()
        elif self.no_of_seats < 60:  # if the no. of seats is less than 60 then it will cost 10 per seat
            self.price = 10
            print("Ticket per person is $10, do you want to proceed ahead? Press Y/N")
        elif a < self.row / 2:
            self.price = 10
            print("Ticket per person is $10, do you want to proceed ahead? Press Y/N")
        elif a > self.row / 2:
            self.price = 8
            print("Ticket per person is $8, do you want to proceed ahead? Press Y/N")
        self.user_input = input()

        if self.user_input == 'Y':  # If the user confirms the booking, take the user_details
            user_dict = {}
            user_name = input(" Enter your name\n")
            user_gen = input('Enter your gender in the format M/F\n')
            user_age = int(input("Enter your age\n"))
            user_contact = int(input("Please enter a phone number in the format XXX-XXX-XXXX:\n"))
            self.row1 = a - 1
            self.col1 = b - 1
            self.seats[self.row1][self.col1] = "B"  # Mark the seat as "B"
            self.seat_count = self.seat_count + 1  # Increase seat count by 1
            self.current_income = self.current_income + self.price  # Calculate current income till now
            # it stores the user_details in a dict with row, column as key and values as the details
            user_dict[(self.row1 + 1), (self.col1 + 1)] = list((user_name, user_gen, user_age, user_contact, self.price))
            self.user_details.update(user_dict)
            print("Booked successfully !!\n")  # print confirmation message
        elif self.user_input == 'N':
            self.user_choice = (input("Press any key for main menu\n"))
        else:
            print("Booking couldn't be processed!\n")  # it execute if the user will not select the given option i.e Y/N

    # function for returning total possible revenue that could be earned if all the seats are booked
    def total_revenue(self):
        if self.no_of_seats < 60:
            self.total_income = self.no_of_seats * 10
        elif self.no_of_seats >= 60:
            for i in range(0, int(self.row / 2)):
                x = int(self.row / 2) * self.col * 10
            for j in range(int(self.row / 2), self.row):
                y = int(self.row / 2) * self.col * 8
            self.total_income = x + y
        return self.total_income

    def statistics(self):  # Function for displaying statistics(By pressing 3)
        print("Number of purchased tickets : ", self.seat_count)
        self.percentage = (self.seat_count / self.no_of_seats) * 100
        print("Percentage of Tickets Booked : ", "{:.2f}".format(self.percentage), "%")
        print("Current Income : $", self.current_income)
        x = self.total_revenue()
        print("Total Income : $", x)

    def user_info(self):  # Function for printing the user details based on the row,col they booked(By pressing 4)
        self.check_x = int(input("Enter the row you booked\n"))
        self.check_y = int(input("Enter the column you booked\n"))
        if self.seats[self.check_a - 1][self.check_b - 1] == 'B':
            c = self.user_details[(self.check_x, self.check_y)]
            print('Name:', c[0])
            print('Gender:', c[1])
            print('Age:', c[2])
            print('Phone no.:', c[3])
        else:
            print("Hey this seat is vacant!! wanted to book one???")  # If the seat is not booked it will displaying "seat is vacant!! wanted to book one"
            self.user_choice = (input("Press any key for main menu\n"))

    def ext(self):  # To exit the function
        return None