user = input('Say hello: ')
if user == 'hello':
    office = input('Please tell your country: ')
    complain = input('complain: ')

if office.lower() == "kazakstan":
    with open("google_kazakstan.txt", "w") as somefile:
        somefile.write(complain)
if office.lower() == "france":
    with open("google_paris.txt", "w") as somefile:
        somefile.write(complain)
if office.lower() == "uar":
    with open("google_uar.txt", "w") as somefile:
        somefile.write(complain)
if office.lower() == "kyrgystan" or "kyrgyzstan":
    with open("google_kyrgystan.txt", "w") as somefile:
        somefile.write(complain)
if office.lower() == "germany":
    with open("google_germany.txt", "w") as somefile:
        somefile.write(complain)
if office.lower() == "russia":
    with open("google_moscow.txt", "w") as somefile:
        somefile.write(complain)
if office.lower() == "sweden":
    with open("google_sweden.txt", "w") as somefile:
        somefile.write(complain)
 
 