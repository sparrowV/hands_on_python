import requests

def get_branch_counts_by_companies(bikes_data):
    result = {}
    for elem in bikes_data:
        company_list = elem['company']
        print(elem)
        print(company_list)
        if(company_list != None):

            for company in company_list:

                if(company in result):
                    result[company]+=1
                else:
                    result[company] = 1

    return sorted(result.items(), key=lambda kv: kv[1],reverse=True)


def get_city_counts_by_companies(bikes_data):
    result = {}
    for elem in bikes_data:
        city_name = elem['location']['city']
        print(city_name)
        if(city_name in result):
            result[city_name]+=1
        else:
            result[city_name]=1
    return sorted(result.items(), key=lambda kv: kv[1], reverse=True)

response = requests.get("http://api.citybik.es/v2/networks",timeout=3)
if(response.ok):
    bikes_json_data = response.json()['networks'] #add networks after printing data
    # print(bikes_json_data)
    print(len(bikes_json_data))
    print(bikes_json_data[0])
    branch_counts = get_branch_counts_by_companies(bikes_json_data)
    print(branch_counts)
    city_counts = get_city_counts_by_companies(bikes_json_data)
    # pass value country
    # country_counts = get_city_counts_by_companies(bikes_json_data,'country')
    print(city_counts)
    # print(country_counts)
else:
    print("error with status code : ",response.status_code)
