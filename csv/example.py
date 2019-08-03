import csv

def get_people_counts_by_age(data):
    result = {}
    for elem in data[1:]:
        age = elem[3]
        if(age in result):
            result[age]+=1
        else:
            result[age] = 1

    return sorted(result.items(), key = lambda key_value : key_value[1],reverse=True)


def write_people_summary(data,f):
    writer = csv.writer(f,delimiter = ";")
    writer.writerow([data[0][0],data[0][1]])
    for elem in data[1:]:
        age = elem[3]
        if(int(age) > 30):
            people_summary = [elem[0],elem[1]]
            writer.writerow(people_summary)


#extension
# def get_counts_by_country():
#     pass



with open('people.csv') as f:
    data = csv.reader(f)
    people_by_age = get_people_counts_by_age(list(data))
    f.seek(0)
    print(people_by_age)
    with open("summary.csv","w",newline='') as summary:
        write_people_summary(list(data),summary)