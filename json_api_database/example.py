import json
import requests
import sqlite3 as db

params = {
    'description':'python',
}
response  = requests.get("https://jobs.github.com/positions.json?",params = params,timeout = 3)

def insert(cursor,job):
    insert_query = 'insert into jobs(title,type,company) values(:title,:type,:company)'
    cursor.execute(insert_query,{'title':job['title'],'type':job['type'],'company':job['company']})


def get_job_counts_by_companies(cursor):
    pass

if(response.ok):
    jobs_json = response.json()
    print(jobs_json)
    json_string = json.dumps(jobs_json,indent=4)
    print(json_string)
    connection = db.connect("jobs_database.db")
    cursor = connection.cursor()
    jobs_table_query = '''
        CREATE TABLE jobs(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title text,
            type text,
            company text
        )
    '''
    cursor.execute(jobs_table_query)
    for job in jobs_json:
        insert(cursor,job)
    connection.commit()

    cursor.close()
    connection.close()

else:
    print("some error happend with status code ",response.status_code)