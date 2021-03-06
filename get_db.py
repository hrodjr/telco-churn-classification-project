import pandas as pd
import env

def get_connection(db, user=env.user, host=env.host, password=env.password):
    return f'mysql+pymysql://{user}:{password}@{host}/{db}'

def get_titanic_data():
    return pd.read_sql('SELECT * FROM passengers', get_connection('titanic_db'))

iris_sql="SELECT measurements.measurement_id, \
    measurements.sepal_length, measurements.sepal_width, measurements.petal_length, \
        measurements.petal_width, species.species_name, species.species_id \
            FROM measurements JOIN species ON(species.species_id=measurements.species_id)"

def get_iris_data():
    return pd.read_sql(iris_sql,get_connection('iris_db'))

telco_sql = "select *\
    FROM customers\
        RIGHT JOIN contract_types USING(contract_type_id)\
            RIGHT JOIN internet_service_types USING(internet_service_type_id)\
                RIGHT JOIN payment_types USING(payment_type_id);"

def get_telco_data():
    return pd.read_sql(telco_sql,get_connection('telco_churn'))