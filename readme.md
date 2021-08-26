# TelCo Churn Classification Project

## Telco Churn Data Dictionary

| Target                   | Encoded          | Description                                                                                                                        | Data Type |
|--------------------------|------------------|------------------------------------------------------------------------------------------------------------------------------------|-----------|
| NA                       | autopayment      | Split payment_type and includes: Bank Transfer (automatic) and  Credit Card (automatic) (Yes or No).                               | NA        |
| NA                       | not_autopayment  | Split payment_type and includes: Electronic Check and Mailed Check) (Yes or No).                                                   | NA        |
| payment_type_id          | DROPPED          | ID number assigned to payment type: 1. Electronic Check; 2. Mailed Check; 3. Bank Transfer (automatic); 4. Credit Card (automatic) | int64     |
| payment_type             | DROPPED          | Types of payments accepted: 1. Electronic Check; 2. Mailed Check; 3. Bank Transfer (automatic); 4. Credit Card (automatic)         | object    |
| internet_service_type_id | DROPPED          | ID number assigned to internet service type: 1. DSL; 2. Fiber Optic; 3. No interent service                                        | int64     |
| NA                       | dsl              | Customer enrolled in dsl internet service (yes or No).                                                                             | NA        |
| NA                       | fiber            | Customer enrolled in fiber internet service (Yes or No).                                                                           | NA        |
| NA                       | no_internet      | Customer is does not have internet service (Yes or No).                                                                            | NA        |
| internet_service_type    | DROPPED          | Type of internet service provided: 1. DSL; 2. Fiber Optic; 3. No interent service                                                  | object    |
| contract_type_id         | DROPPED          | ID number assigned to contract type: 1. month-to-month; 2. One Year contracts; 3. Two Year contracts.                              | int64     |
| NA                       | m2m              | month-to-month (Yes or No).                                                                                                        | NA        |
| contract_type            | DROPPED          | Type of contracts offered: 1. month-to-month; 2. One Year contracts; 3. Two Year contracts.                                        | object    |
| customer_id              | DROPPED          | ID number assigned to each customer.                                                                                               | object    |
| NA                       | is_male          | gender (Yes or No).                                                                                                                | NA        |
| gender                   | DROPPED          | Gender of customer (Male and Female).                                                                                              | object    |
| senior_citizen           | DROPPED          | Wheter or no customer is a senior citizen (Yes or No).                                                                             | int64     |
| partner                  | partner          | Whether or not customers have a partner (Yes or No).                                                                               | object    |
| dependents               | dependents       | Whether or not customers have dependents (Yes or No).                                                                              | object    |
| tenure                   | tenure           | Length of time customer has had service (Month count).                                                                             | int64     |
| phone_service            | phone_service    | Whether or not a customer has phone service (Yes or No).                                                                           | object    |
| multiple_lines           | DROPPED          | Whether or not a customer has multiple lines (Yes or No).                                                                          | object    |
| online_security          | DROPPED          | Whether or not a customer has online security service (Yes or No).                                                                 | object    |
| online_backup            | DROPPED          | Whether or not a customer has online backup service (Yes or No).                                                                   | object    |
| device_protection        | DROPPED          | Whether or not a customer has device protection service (Yes or No).                                                               | object    |
| tech_support             | tech_support     | Whether or not a customer has internet service tech support (Yes or No).                                                           | object    |
| streaming_tv             | streaming_tv     | Whether or not a customer has streaming TV (yes or No).                                                                            | object    |
| streaming_movies         | streaming_movies | Whether or not a customer has streaming movies (Yes or No).                                                                        | object    |
| paperless_billing        | DROPPED          | Whether or not a customer is enrolled in paperless billing (Yes or No).                                                            | object    |
| monthly_charges          | monthly_charges  | Monthly billing amount in dollars.                                                                                                 | float64   |
| total_charges            | DROPPED          | Total billing over tenure in dollars.                                                                                              | object    |
| churn                    | churned          | Whether or not a customer has churned (Yes or No).                                                                                 | object    |
