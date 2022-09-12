create table countries(
	country varchar(50) primary key,
	region varchar(50)
);

create table export(
	id serial primary key,
	year smallint,
	month smallint,
	origincountry varchar(50),
	destinationcountry varchar(50),
	exports int,
	constraint fk_origin foreign key (origincountry) references countries(country),
	constraint fk_destination foreign key (destinationcountry) references countries(country)
);

create table budget(
    id serial primary key,
    month smallint,
    year smallint,
	origincountry varchar(50),
	destinationcountry varchar(50),
	budgetamount float,
	constraint fk_origin_bud foreign key (origincountry) references countries(country),
	constraint fk_destination_bud foreign key (destinationcountry) references countries(country)
);

alter table budget 
add column fiscalyearperiod varchar(50);

alter table budget 
USING fiscalyearperiod::date;

select * from budget;
