
--A
select year, origincountry, destinationcountry, sum(exports) as Exports_During_The_Year
from export
group by year, origincountry, destinationcountry
order by year desc, origincountry

--B
select year, origincountry, destinationcountry, sum(exports) as Exports_During_The_Quarter,
case when month <= 3 then '1Q' || year
	when month > 3 and month <= 6 then '2Q' || year
	when month > 6 and month <= 9 then '3Q' || year
	ELSE '4Q' || year
	END as Quarter
from export
group by year, origincountry, destinationcountry, month
order by year desc, origincountry, quarter;


--C
select ex.year, co.region, sum(ex.exports) as Region_yearly_report
from export ex join countries co on ex.origincountry = co.country
group by ex.year, co.region
order by ex.year desc;