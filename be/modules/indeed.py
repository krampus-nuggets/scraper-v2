import ast
import sys

# Create empty lists [Global]
jobs = []
names = []
dates = []
summaries = []
locations = []

# Function - Ingest parsed HTML data | Filter out required values
def getJobs(parsedHTML):

    # Loop - Get job title
    for div in parsedHTML.find_all(name='h2', attrs={'class':'title'}):
        for a in div.find_all(name='a', attrs={'data-tn-element':'jobTitle'}):
            dictItem = {"job-title": f"{a.getText().strip()}"}
            jobs.append(dictItem)
            

    # Loop - Get job poster's name
    for div in parsedHTML.find_all(name='div', attrs={'class':'sjcl'}):
        for span in div.find_all(name='span', attrs={'class':'company'}):
            dictItem = {"company-name": f"{span.getText().strip()}"}
            names.append(dictItem)

    # Loop - Get the date the job post was created
    for div in parsedHTML.find_all(name='div', attrs={'class':'result-link-bar'}):
        for span in div.find_all(name='span', attrs={'class':'date date-a11y'}):
            dictItem = {"date-created": f"{span.getText().strip()}"}
            dates.append(dictItem)

    # Loop - Get short job description
    for divParent in parsedHTML.find_all(name='div', attrs={'class':'result'}):
        for divChild in divParent.find_all(name='div', attrs={'class':'summary'}):
            dictItem = {"short-description": f"{divChild.getText().strip()}"}
            summaries.append(dictItem)

    # Loop - Get job location
    for div in parsedHTML.find_all(name='div', attrs={'class':'sjcl'}):
        for divChild in div.find_all(name='div', attrs={'class':'recJobLoc'}):
            dictItem = {"location": f"{divChild['data-rc-loc']}"}
            locations.append(dictItem)

    
# Function - Generate test data
def testData(parsedHTML, typeProc):

    # typeProc == True | Export data to text files
    if typeProc:
        #getJobs(parsedHTML)

        with open("jobs.txt", "w") as file:
            for line in jobs:
                file.write(str(line))
                file.write("\n")
            file.close()
        
        with open("names.txt", "w") as file:
            for line in names:
                file.write(str(line))
                file.write("\n")
            file.close()
        
        with open("dates.txt", "w") as file:
            for line in dates:
                file.write(str(line))
                file.write("\n")
            file.close()
        
        with open("summaries.txt", "w") as file:
            for line in summaries:
                file.write(str(line))
                file.write("\n")
            file.close()
        
        with open("locations.txt", "w") as file:
            for line in locations:
                file.write(str(line))
                file.write("\n")
            file.close()
    
    # typeProc == False | Import data from txt files, convert to dictionary and append to list
    elif typeProc == False:
        with open("jobs.txt", "r") as file:
            content = file.readlines()
            for i in range(len(content)):
                content[i] = content[i].replace("\n", "")
                content[i] = ast.literal_eval(content[i])
                jobs.append(content[i])
            file.close()

        with open("names.txt", "r") as file:
            content = file.readlines()
            for i in range(len(content)):
                content[i] = content[i].replace("\n", "")
                content[i] = ast.literal_eval(content[i])
                names.append(content[i])
            file.close()

        with open("dates.txt", "r") as file:
            content = file.readlines()
            for i in range(len(content)):
                content[i] = content[i].replace("\n", "")
                content[i] = ast.literal_eval(content[i])
                dates.append(content[i])
            file.close()

        with open("summaries.txt", "r") as file:
            content = file.readlines()
            for i in range(len(content)):
                content[i] = content[i].replace("\n", "")
                content[i] = ast.literal_eval(content[i])
                summaries.append(content[i])
            file.close()

        with open("locations.txt", "r") as file:
            content = file.readlines()
            for i in range(len(content)):
                content[i] = content[i].replace("\n", "")
                content[i] = ast.literal_eval(content[i])
                locations.append(content[i])
            file.close()

    # Else | If this else is hit, something is greatly fvcked
    else:
        print("Function: testData | Error: if statement else output")
        sys.exit(1)

# Function - Remove items from all lists
def wipeLists():
    jobs.clear()
    names.clear()
    dates.clear()
    summaries.clear()
    locations.clear()

# Function - JSON Blob Generator
def genJSON(parsedHTML):
    # Testing with cached local IRL data
    #testData(parsedHTML, False)

    wipeLists()
    getJobs(parsedHTML)
    jsonBlob = []
    
    # Merge dictionaries | Combining dictionaries into single object + Append to jsonBlob list
    for i in range(len(jobs)):
        print(f"""
jobs: {len(jobs)}
names: {len(names)}
dates: {len(dates)}
summaries: {len(summaries)}
locations: {len(locations)}
        """)
        sumObj = {**jobs[i], **names[i], **dates[i], **summaries[i], **locations[i]}
        #sumObj = {**jobs[i], **names[i], **dates[i], **summaries[i]}
        jsonBlob.append(sumObj)

    return jsonBlob
