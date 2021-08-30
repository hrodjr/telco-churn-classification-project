# TelCo Churn Classification Project

Creating a classification model, using the telco dataset, to predict customer churn.

Goal: 

    1. Identify driver(s) that cause the greatest churn.
    2. Construct a classification model.
    3. Document project process.

## Project details

    - Libraries
        - pandas
        - numpy
        - seaborn
        - matplotlib
        - scipy.stats
        - graphviz
        - sklearn
        
    - Individual modules
        - get_db.py (SQL data acquisition)
        - explore.py (data exploration)
        - prepare.py (data cleaning)
        
    - Statistical Tests
        - chi2
        - pearsonr
        - ttest
        
    - Exploration
        - Univariate
        - Bivariate
        - Multivariate

    - Modeling
        - Decision Tree
        - Random Forrest
        - KNN
        - Logistics Regression

## Pipeline
    
    My methodology follow is the data pipeline; plan, acquire, prepare, explore, model and deliver.
##### Planning    
    Taking you through the data pipeline I will begin with acquiring the telco data from the get_db.py module, prepare it using the prepare.py module, split the data and on through exploration. Using explore.py module I identified a set of features used to develop my initial hypothesis. Once cleaned I ran it through multivariate to compare features to help with testing the listed inital hypothesis. Each exploration will include takeaways that have led to preparing, cleaning and testing of the data resulting in either rejecting or failing to reject the final hypothesis.
        Features within my hypothesis have been split, tested and modeled in order to provide a recommendation on the final hypothesis in order to model and reduce churn rates based rejected or failed to reject of the hypothesis. 
##### Acquire
    Acquire data from get_db.py module.
##### Prepare
    Data was prepared using prepare.py module. Preparation was made visualizing and running the raw telco data through the univariate statisitics. After the initial prep I went I back and ran the encoded data through bavariate and made more changes as defined in the data dictionary below.
##### Explore
    I have also identified unknown variables that at a later time can be researched, developed and tested using this model to predict future churn.
    
    I will split my dataframe using train, validate and test.
    
    To explore the data using Univariate, Bivariate and Multivariate methods.
##### Modeling    
    In testing my hypothesis I'll be using chi2, pearsonr, and ttest methods.
    
    For modeling I'll be using DecisionTreeClassifier, RandomForrestClassifier, KNeighborsClassifier, and Logistics Regression.
##### Delivery

    A downloadable csv file has been created for future modeling.

## Hypothesis
    1. Churn is dependent of whether or not customers are on fiber. (chi2)
        * Null: Churn is independent of whether or not a customer are on fiber.
        * Alternate: churn is dependent of whether or not customers are on fiber.               
    
    2. Tenure and monthly charges are linearly correlated. (pearsonr)
        * Null: Tenure and monthly charges are not linearly correlated.
        * Alternate: Tenure and monthly charges are linearly correlated.
                
    3. Churn is dependent younger customers. (chi2)
        * Null: Churn is independent of younger customers.
        * Alternate: Churn is dependent of younger customers.
        
    4. Do you younger customers pay more then the older customers. (ttest 1samp)
        * Null: The average monthly charges for younger customers is no different than the population.
        * Alternate: The average monthly charges for younger customers are different than the population.
            
    5. Do younger customers churn more than older customers? (ttest 1samp)
        * Null: Younger customer churn is no different than the older population.
        * Alternate: Younger customer churn is different than the older population.
    
    6. Do single customers churn more than non single customers?  (ttest 1samp)
        * Null: Single customer churn is no different than the non single population.
        * Alternate: Single customer churn is different than the non single population.
    
    7. Is churn dependent on autopayment? (chi2)
        * Null: Churn is independent of whether or not customes are enrolled in the autopayment plan.
        * Alternate: Churn is dependent of whether or not customes are enrolled in the autopayment plan.
            
    8. Is churn dependent on phone_service? (chi2)
        * Null: Churn is independent on phone services.
        * Alternate: Churn is dependent on phone services.
            
    FINAL HYPOTHESIS:

    Customers who are young, single, on fiber, has phone service, on m2m, and not enrolled in a autopayment plan are more likely to churn than those customers that do not fall in this category. (ttest 1samp)
        * Null: Customers who are young, single, on fiber, has phone service, on m2m, and not enrolled on the autopayment plan are no different than the rest of the population.
        * Alternate: Customers who are young, single, on fiber, has phone service, on m2m, and not enrolled on the autopayment plan is different than the rest of the population.

## Key Findings, Takeaways & Recommendations
##### Key Findings
    Customers who are young, single, on fiber, has phone service, on m2m, and not enrolled on the autopayment plan is different than the rest of the population.
##### Takeaways
    Customer churn rates are dependent on high monthly payments and occur early on in customer tenure.
##### Recommendations
    Increase retention by incentiving new customers within the features of the final hypothesis. Incentives can include:
    - Free limited time service.
    - Discounts for signing up for an autopayment plan.
    - Reduced service upgrades.
    - Package/bundle incentives.
    - Student, veteran, senior citizen, family, etc. discounts.
## Recreate
    Recreate following the listed instructions:
        - Clone the repository
        - Setup env.py
        - Open and run the classification_project.ipynb
## Telco Churn Data Dictionary

| Target                   | Encoded           | Description                                                                                                                                                         | Data Type |
|--------------------------|-------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------|
| NA                       | autopayment       | "Consolidated payment_type and includes: Bank Transfer (automatic),  Credit Card (automatic) as the autopayment and  Electronic Check and Mailed Check(Yes or No)." | int64     |
| payment_type_id          | DROPPED           | ID number assigned to payment type: 1. Electronic Check; 2. Mailed Check; 3. Bank Transfer (automatic); 4. Credit Card (automatic)                                  | int64     |
| payment_type             | DROPPED           | Types of payments accepted (Now autopayment): 1. Electronic Check; 2. Mailed Check; 3. Bank Transfer (automatic); 4. Credit Card (automatic)                        | object    |
| internet_service_type_id | DROPPED           | ID number assigned to internet service type: 1. DSL; 2. Fiber Optic; 3. No interent service                                                                         | int64     |
| NA                       | dsl               | DROPPED: Customer enrolled in dsl internet service.                                                                                                                 | NA        |
| NA                       | fiber             | Consolidated: Customer enrolled in fiber internet service. Assumption is if it is not fiber it is dsl (Yes or No).                                                  | int64     |
| NA                       | no_internet       | DROPPED: Customer is does not have internet service. Dropped completely as it only had 61 customer.                                                                 | NA        |
| internet_service_type    | DROPPED           | Type of internet service provided: 1. DSL; 2. Fiber Optic; 3. No interent service                                                                                   | object    |
| contract_type_id         | DROPPED           | ID number assigned to contract type: 1. month-to-month; 2. One Year contracts; 3. Two Year contracts.                                                               | int64     |
| NA                       | m2m               | month-to-month (Yes or No). Assumption is if it is not m2m it is a contract plan.                                                                                   | int64     |
| contract_type            | DROPPED           | Type of contracts offered: 1. month-to-month; 2. One Year contracts; 3. Two Year contracts.                                                                         | object    |
| customer_id              | DROPPED           | ID number assigned to each customer.                                                                                                                                | object    |
| NA                       | is_male           | gender (Yes or No).                                                                                                                                                 | int64     |
| gender                   | DROPPED           | Gender of customer (Male and Female).                                                                                                                               | object    |
| NA                       | is_senior         | Renamed for testing purposes from senior_citizen. (Yes or No)                                                                                                       | int64     |
| senior_citizen           | DROPPED           | Whether or no customer is a senior citizen (Yes or No).                                                                                                             | int64     |
| NA                       | not_single        | Consolidated: Whether a customer is single or not. Assumption is that if they are not single they have either a partner or dependents.                              | int64     |
| partner                  | DROPPED           | Whether or not customers have a partner (Yes or No).                                                                                                                | object    |
| dependents               | DROPPED           | Whether or not customers have dependents (Yes or No).                                                                                                               | object    |
| tenure                   | tenure            | Length of time customer has had service (Month count).                                                                                                              | int64     |
| phone_service            | phone_service     | Whether or not a customer has phone service (Yes or No).                                                                                                            | int64     |
| multiple_lines           | DROPPED           | Whether or not a customer has multiple lines (Yes or No).                                                                                                           | int64     |
| online_security          | online_security   | Whether or not a customer has online security service (Yes or No).                                                                                                  | int64     |
| online_backup            | online_backup     | Whether or not a customer has online backup service (Yes or No).                                                                                                    | int64     |
| device_protection        | device_protection | Whether or not a customer has device protection service (Yes or No).                                                                                                | int64     |
| tech_support             | tech_support      | Whether or not a customer has internet service tech support (Yes or No).                                                                                            | int64     |
| streaming_tv             | DROPPED           | Whether or not a customer has streaming TV (yes or No).                                                                                                             | object    |
| streaming_movies         | DROPPED           | Whether or not a customer has streaming movies (Yes or No).                                                                                                         | object    |
| paperless_billing        | DROPPED           | Whether or not a customer is enrolled in paperless billing (Yes or No).                                                                                             | object    |
| monthly_charges          | monthly_charges   | Monthly billing amount in dollars.                                                                                                                                  | float64   |
| total_charges            | DROPPED           | Total billing over tenure in dollars.                                                                                                                               | object    |
| churn                    | churned           | Whether or not a customer has churned (Yes or No).                                                                                                                  | int64     |
