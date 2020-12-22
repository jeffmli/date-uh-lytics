import pandas as pd
from datetime import date

def start_swiping(dating_app):

	swipe_string = """ Let's start swiping! 
	\n Swipe Left - (k)
	\n Swipe Rightor Like - (l)
	\n Send message - (m)
	"""

	exit_dating_app = False


	counter_dict = {
	'Dislike':0,
	'Like':0, 
	'Message':0,
	}

	mapping_dict = {
	'k':'Dislike',
	'l':'Like', 
	'm':'Message',
	}

	print(swipe_string)
	while exit_dating_app is False:
		user_input = input()
		
		if user_input in mapping_dict.keys():

			action = mapping_dict[user_input]
			counter_dict[action] += 1

			print("You added 1 to {0}".format(action))

		if user_input == 'exit':
			print("Exiting App session......")
			print("\n")
			break

		if user_input not in (mapping_dict.keys()):
			print("Please enter a correct input.")

	print(counter_dict)
	
	return counter_dict


def parse_dict(record_dict):

	today = date.today()

	
	all_rows = []
	for key in record_dict.keys():
		row = [today,key]
		like_dislike_records = record_dict[key]
		
		print(like_dislike_records)
		for key,value in like_dislike_records.items():
			row.append(value)
		all_rows.append(row)

	print(all_rows)
	return all_rows

def log_manual_data():

	today = date.today()

	print("How many dating apps did you use?")
	
	try:
		num_apps = int(input())
	except:
		print("Please enter a number as an input.")


	columns = ['App', 'Dislikes', 'Likes', 'Messages']
	records = []

	for i in range(0,num_apps):

		c = 0
		row = [today]
		while c < 4:
			print("Please enter the {0}".format(columns[c]))
			response = input()
			row.append(response)
			c += 1

		records.append(row)


	records = pd.DataFrame(records)
	records.columns = ['Date','App','Dislikes','Likes','Messages']
	return records

def main():

	welcome_string = """ 
	\n
	Hello! Welcome to the dating tracker.
	\n My job is to help you track the statistics of your dating app activity.
	\n Ultimately, I want to get you more dates. Using me, we can help provide you \n insights into how you can improve your funnel.
	\n Let's get started!"""

	print(welcome_string)
	
	input_string = """ Please enter the dating app you're using or select manual input:
	\n Hinge - (h)
	\n Tinder - (t)
	\n Coffee Meets Bagel - (c)
	\n Bumble - (b)
	\n Manual - (m)

	"""

	exit = False

	record_dict = dict()

	while exit is False:

		print(input_string)
		dating_input = input()

		if dating_input == 'm':
			records = log_manual_data()
			return records

		if dating_input == 'exit':
			print("Ending dating apps sessions......")
			print("\n")
			break

		dating_dict = {'h':'Hinge',
					   't':'Tinder',
					   'c':'Coffee Meets Bagel',
					   'b':'Bumble'}

		dating_app_used = dating_dict[dating_input]
		dating_app_count = start_swiping(dating_app_used)

		record_dict[dating_app_used] = dating_app_count

	parsed_record_dict = parse_dict(record_dict)
	record_df = pd.DataFrame(parsed_record_dict)
	record_df.columns = ['Date','App','Dislikes','Likes','Messages']
	return record_df

if __name__=='__main__':
	records = main()

	try:
		df = pd.read_csv("dating_app_records.csv")
		df = df[['Date','App','Dislikes','Likes','Messages']]
		df = df.append(records)
		df.to_csv("dating_app_records.csv")
		
		print(records)
		print(df)

	except IOError:
		print("No dating app records exists. Creating a new one now......")
		records.to_csv("dating_app_records.csv")



	## Enter the dating app I'm using 
	## Have a button for left or right swipe/like, messages 
	## Each day is stored as a single line, with the counts for each bucket. 
	## For that day, tally the number of respones. 
	## Append this to a csv file. 
