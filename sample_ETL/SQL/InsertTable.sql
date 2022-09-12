copy countries
from 'D:\training_assignment\Data\Table2.Countries and Regions.csv'
DELIMITER ','
CSV HEADER;

copy export(year, MONTH, origincountry, destinationcountry, exports)
FROM 'D:\training_assignment\Data\Table1.Exports Till May 2021.csv'
DELIMITER ','
CSV HEADER;

copy budget(year, month,  Origincountry, Destinationcountry, budgetamount, fiscalyearperiod)
FROM 'D:\training_assignment\Data\budget_transformed.csv'
DELIMITER ','
CSV HEADER;



SELECT * FROM budget;

