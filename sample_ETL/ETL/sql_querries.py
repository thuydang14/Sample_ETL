#INSERT TO EXPORT
insert_export = (""" INSERT INTO export(year, month, origincountry, destinationcountry, exports)\
                 VALUES (%s,%s,%s,%s,%s)   
                """)