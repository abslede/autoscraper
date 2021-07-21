
import requests
from bs4 import BeautifulSoup

response = requests.get("https://www.motherjones.com/")
doc = BeautifulSoup(response.text, 'html.parser')

# Get everything with the class of hed
# and then loop through them each and print out the text
# each one of these is going to be a row

stories = doc.select('.layout-3')
# Starting off without ANY rows
rows = []

for story in stories:
    print("----")
    row = {}
    row['title'] = story.select_one('.hed').text.strip()
    row['byline'] = story.select_one('.byline').text.strip()
    try:
        row['url'] = story.find('a')['href']
    except:
        print("Couldn't find a link.")
    print(row)
    rows.append(row)

#make first dataframe
import pandas as pd

df = pd.DataFrame(rows)
df    

#find other top stories under separate web structure

stories2 = doc.select('.order-1')
# Starting off without ANY rows

rows2 = []
for story2 in stories2:
    print("----")
    row = {}
    
    #print(story2)
 
    try:
        row['title'] = story2.select_one('.hed').text.strip()
    except:
        print("Couldn't find a title.")
    try:
        row['byline']=story2.select_one('.byline').text.strip()
    except:
        print("Couldn't find a byline.")
    try:
        row['url'] = story2.find('a')['href']
    except:
        print("Couldn't find a link.")
    print(row)
    rows.append(row)

    #build second data frame of other top stories
df2 = pd.DataFrame(rows)
df2

#combine the two dataframes and check

frames = [df, df2]

#print(frames)
mojoresult = pd.concat(frames)
mojoresult

#download as csv
mojoresult.to_csv("mojo-headlines.csv", index=False)
