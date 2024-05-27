from datetime import datetime, timedelta

subjects = {
    "Calculus": 8*3600 + 4*60 + 1,
    "Probability": 7*3600 + 49*60 + 45,
    "DSA": 23*3600 + 50*60 + 10,
    "DLD": 20*3600 + 49*60 + 23,
    "CO": 22*3600 + 26*60 + 6,
    "OS": 31*3600 + 6*60 + 39,
    "DBMS": 29*3600 + 4*60 + 35,
    "CN": 28*3600 + 21*60 + 43
}

totalstudyduration = sum(subjects.values())

startdate = datetime(2024, 5, 28)
completiondates = {}
remainingduration = totalstudyduration
totaldays = 0

print("\n")
print("Start Date (Including):", startdate.strftime('%B %d'))
print("Content Completed Per Day: 6 hours")
print("\n")

for subject, duration in subjects.items():
    daysneeded = duration / (6*3600)
    completiondate = startdate + timedelta(days=daysneeded)
    completiondates[subject] = completiondate
    startdate = completiondate
    remainingduration -= duration
    totaldays += daysneeded

for subject, completiondate in completiondates.items():
    days = subjects[subject] / (6*3600)
    print(f"{subject}: {completiondate.strftime('%B %d')} ({days:.2f} days)")

totalhours = totalstudyduration // 3600
totalminutes = (totalstudyduration % 3600) // 60
totalseconds = totalstudyduration % 60

print("\n")
print("Total Time: {} hours, {} minutes, and {} seconds.".format(totalhours, totalminutes, totalseconds))
print("Total Days: {:.2f} days".format(totaldays))
print("\n")
