def phone_setup:

	phone = int(input("Please enter your 10-digit phone number (no spaces or punctuation): "))
	print("This device supports the following cellular carriers:\n1 - AT&T\n2 - Boost Mobile\n3 - Cricket\n4 - Google Fi\n5 - Metro PCS\n6 - Simple Mobile\n7 - Sprint\n8 - T-Mobile\n9 - Verizon\n10 - Virgin Mobile\n11 - Virgin Mobile Canada\n12 - Xfinity Mobile")
	carrier = int(input("Enter the number corresponding to your carrier: "))

	if phone not in [None, ''] and carrier not in [None, '']:
		network = ''
		if carrier == 1:
			network = '@txt.att.net'
		elif carrier == 2:
			network = '@myboostmobile.com'
		elif carrier == 3:
			network = '@mms.cricketwireless.net'
		elif carrier == 4:
			network = '@msg.fi.google.com'
		elif carrier == 5:
			network = '@mymetropcs.com'
		elif carrier == 6:
			network = '@mmst5.tracfone.com'
		elif carrier == 7:
			network = '@messaging.sprintpcs.com'
		elif carrier == 8:
			network = '@tmomail.net'
		elif carrier == 9:
			network = '@vtext.com'
		elif carrier == 10:
			network = '@vmobl.com'
		elif carrier == 11:
			network = '@vmobile.ca'
		elif carrier == 12:
			network = '@vtext.com'
		else:
			print('Error: Invalid carrier ID')
		if network is not '':
			with open('user.txt', 'w') as file:
				file.write(str(phone) + network)
	else:
		print("Error: Invalid data. Please try again.")

if __name__=='__main__':
    phone_setup()
