import peewee

db = SqliteDatabase('library.db')

class book(Model):
	title = CharField()
	author = CharField()
	publication = CharField()
	pub_year = IntegerField()
	isbn = CharField()
	num_of_books = IntegerField()

	class Meta:
		database = db


class member(Model):
	user_id = CharField()
	name = CharField()
	phone_no = CharField()

	class Meta:
		database = db

class issue_history(Model):
	user_id = ForeignKeyField(member, related_name='pets')
	isbn = ForeignKeyField(book, related_name='library')
	issue_id = CharField()
	issue_date = DateField()
	return_date = DateField()
	current_status = TextField()

	class Meta:
		database = db


def initialize_db():
    db.connect()
    try:
        db.create_tables([book, member, issue_history])
    except OperationalError:
        # Table already exists. Do nothing
        pass

def deinit():
    db.close()


def add_book():
	book_title = raw_input('Enter the book title: ')
	book_author = raw_input('Enter the book author: ')
	book_publication = raw_input('Enter the book publication: ')
	book_pub_year = raw_input('Enter the year of publication of book: ')
	book_isbn = raw_input('Enter the ISBN code of book: ')
	book_no = #number of books having same ISBN
	
def save_member(comment, TableName=member):
    member_data = book(user_id=user_id,
                        name=member_name,
                        phone_no=member_phone_no)
    book_data.save()
    
def save_issue(comment, TableName=issue):
    issue_data = book(user_id=alloc_member_id,
                        isbn=alloc_book_isbn,
                        issue_id=issue_id,
                        issue_date=issue_date,
                        return_date=return_date,
                        num_of_books=book_no)
    issue_data.save()

def save_book(comment, TableName=book):
    book_data = book(title=books_title,
                        author=book_author,
                        publication=book_publication,
                        pub_year=book_pub_year,
                        isbn=book_isbn,
                        current_status=current_status)
    book_data.save()

  

def remove_book():
	check_isbn = raw_input('Enter the ISBN code of the book you want to remove: ')
    
    for check_isbn in book_isbn(1,10):
    	#remove book action
	


def add_member():
	user_id = raw_input('Enter the user_id: ')
	member_name = raw_input('Enter the member name: ')
	member_phone_no = raw_input('Enter the phone number of the member: ')
		


def remove_member():
	rem_member_id = raw_input("Enter member's user_id : ")
    # remove member action
	


def allocate():
	alloc_book_isbn = raw_input('Enter book isbn to be allocated: ')
	#check alloc_book_id with actual book id in database
	if alloc_book_id in book_isbn:
		alloc_member_id = raw_input('Enter member id receving the book:')
		#checks if correct user_id is entered
		if alloc_member_id in user_id:
			issue_date = raw_input('Enter issueing date:')
			return_date = raw_input('Enter return date:')
			#checks if date is properly entered or not
			if start_date > return_date:
				print ('Issueing date cannot be after return date')
				#go to line 37
			
			else :
				issue_id = issue_date + user_id + return_date 
				issue_data.save()
				issue.append(sr_no)
				current_status = 'issued'
				print ('This is your issue id:' issue_id) /
				print ('Your return date is: 'return_date)

		else:
			print ('user_id entered does not exist')
			#go to line line 35
		
	else:
		print ('ISBN entered is not present in the database')
		#go to line 32
		
	


def de_allocate():
	de_alloc_issue_id = raw_input('Enter the issue id provided to you:')
	#check alloc_book_id with actual book id in database
	if de_alloc_issue_id in issue_data:
		if today_date == return_date in issue_data:
			print ('Book received')
			book_no += 1
			current_status = 'returned'

		elif:
			today_date < return_date:
			overdue_days = return_date - today_date
			fine = 5*overdue_days
			print "Your fine is Rs", fine
			current_status = 'returned'

		else:
			book_no+= 1
			print 'Thank you for choosing Python Library'


	
				