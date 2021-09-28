import re

url_substr = "http"
fields = ['Conv ID', 'Value of Characteristic']
rows = []
convID = ''
url_count = ''

def checkUrls(list):
    count = 0 #count how many urls were found

    for i in list:
        for j in i:
            if url_substr in j:
                entry = []
                print("Conv id: ", i[0])
                entry.append(int(i[0]))

                count2 = j.count(url_substr)  # counts repeats in same message
                count += count2
                print("URL count: ", count2)
                entry.append(count2)

                rows.append(entry)
    print("Total: ", count)
    print(rows)

def getChatID(list):
    return[item[0] for item in list]

    # for i in list[0:50]:
    #     if any(url_substr in string for string in i):
    #         #print(i)
    #         url_count = url_count+1
    #         print(url_count)
    # print("Total: ", url_count)