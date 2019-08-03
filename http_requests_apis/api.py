import requests

def get_branch_counts_by_companies(bikes_data):
    result = {}
    for elem in bikes_data:
        company_list = elem['company']
        if(company_list != None):
            for company in company_list:
                if(company in result):
                    result[company]+=1
                else:
                    result[company] = 1
    return sorted(result.items(), key = lambda key_value : key_value[1],reverse=True)


def get_city_counts(bikes_data):
    pass

def get_country_counts(bikes_data):
    pass

response = requests.get("http://api.citybik.es/v2/networks",timeout = 3)
if(response.ok):
    bikes_json_data = response.json()['networks']
    # print(len(bikes_json_data))
    # print(bikes_json_data)
    branch_counts = get_branch_counts_by_companies(bikes_json_data)
    print(branch_counts)
else:
    print("error with status code",response.status_code)
