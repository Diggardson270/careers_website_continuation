from sqlalchemy import create_engine, text

hostname = "127.0.0.1"
username = "root"
password = "12345"
port = 3307
database = "enochcareers"

engine = create_engine('mysql+pymysql://' +username+':'+password+'@'+hostname+':'+str(port)+'/'+database)

def load_jobs_from_db():
    with engine.connect() as conn:
        result = conn.execute(text("select * from jobs"))
        jobs = []
        for row in result.all():
            jobs.append((row._mapping))
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