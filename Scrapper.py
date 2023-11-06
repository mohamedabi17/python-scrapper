from bs4 import BeautifulSoup
import requests
import csv

plone = 'https://plone.org/'
trainingPlone ='https://training.plone.org/'
ploneDocs = 'https://docs.plone.org/'

responsePlone = requests.get(plone)
responseTrainingPlone = requests.get(plone)
responsePloneDocs = requests.get(plone)

soup1 = BeautifulSoup(responsePlone.content, 'html.parser')

soup2 = BeautifulSoup(responseTrainingPlone.content, 'html.parser')

soup3 = BeautifulSoup(responsePloneDocs.content, 'html.parser')


# return the html content of each html page
 
# print(soup1.prettify())
# print(soup2.prettify())
# print(soup3.prettify())

# soup1 = soup1.string
# soup2 = soup2.prettify()
# soup3 = soup3.prettify()

# print(soup1.html.head.prettify())
# print(soup1.html.contents)
# print(len(soup1.html.body.contents))

print("####################")

PloneDocuments = [soup1.html,soup2.html,soup3.html]



def MakeCsvROws(data):
    with open('html_elements.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Number','Element Name',  'Parent Element','Attributes', 'Next Element','Presedent Element','Contant of Element'])
        writer.writerows(data)
    csvfile.close()




def AppendTag(index,data,Counter):
    Number=Counter
    name=index.name
    Parent=index.parent.name
    Attributes=index.attrs
    Next=index.next_element.name
    Pres=index.previous_element.name
    if not index.contents:
        Content=index.text
        print(Content)
    else:
        Content="TAG"
    # className=index['class']
    # Identity = index['id']

    # print(className)
    # print(Contant)

    # print(Contant)
    

    # print(name)
    # print(Parent)
    # print(Next)
    # print(Id)

    data.append([Number,name, Parent,Attributes , Next,Pres,Content])

def ReadCsvROws():
    with open('html_elements.csv','r') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            if line_count == 0:
                print(f'\t{", ".join(row)}\t')
                line_count += 1
            else:
                print(f'\t{row[0]} ,{row[1]} ,{row[2]},{row[3]},{row[4]},')
        print(f'Processed {line_count} lines.')


# Main function
data = []
Counter = 1
zTag = None
# for Tag in PloneContent:
#     AppendTag(Tag,data,Counter)
#     Counter+=1
#     # print(Tag)
#     while zTag in Tag.contents or zTag:
#             # print(zTag)
#             AppendTag(Tag,data,Counter)
#             Counter+=1
#             zTag=zTag.contents

#     else:
#         continue


# loop Through the 3 Html Files
for Doc in PloneDocuments:
    # for Tag in Doc: 
    #     AppendTag(Tag,data,Counter)
    #     Counter+=1
    #     if(Tag.contents):
    #         for zTag in Tag.contents:
    #                 print(zTag)
    #                 # print(zTag)
    #                 AppendTag(zTag,data,Counter)
    #                 Counter+=1
    #                 if (zTag.contents):
    #                     Tag=zTag.contents
    #                 else:
    #                     continue
    data2 =[]
    Counter = 0
def StockTags(tag,data,Counter):
        if (tag.contents==0 and tag.next_element==None):
            return data
        if(tag.contents>0):
           tag=tag.next_element
        else:
            AppendTag(Tag,data,Counter)
            print(tag.text)
        

data2=StockTags(Doc,data2,Counter)
    
MakeCsvROws(data)

ReadCsvROws()

print("####################")

