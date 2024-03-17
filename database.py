from sqlalchemy import create_engine, text
import json
from flask import Flask
import os

with open('config.json', 'r') as f:
    config = json.load(f)


config['dab_connection_string'] = f"mysql+pymysql://{config['username']}:{config['password']}@{config['hostname']}:{config['port']}/{config['database']}"

engine = create_engine(config['dab_connection_string'])

def load_jobs_from_db():
    with engine.connect() as conn:
        result = conn.execute(text("select * from jobs"))
        jobs = []
        for row in result.all():
            row = row._mapping
            row = dict(row)
            jobs.append((row))
            json_data = json.dumps(row)
        return jobs
    
    
    # print("type(result):", type(result))
    # result_all = result.all()
    # print("type(result.all()):", type(result_all))
    # first_result = result_all[0]
    # print("type(first_result):", type(first_result))
    # first_result_map = result_all[0]._mapping
    # print("type(first_result_map):", type(first_result_map))
    # first_result_dict = dict(first_result_map)
    # print("type(first_result_dict):", type(first_result_dict))
    # print(first_result_dict)