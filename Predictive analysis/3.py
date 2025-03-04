year=[2007,2008,2009,2010,2011,2012,2013,2014,2015]
tickets=[272,283,293,300,310,320,330,350,384]
base_yr=int(input("Enter base year:"))
if base_yr in year:
    loc=year.index(base_yr)
base_yr_val=tickets[loc]
for i in range(len(tickets)):
    print(f"Simple price index for year {year[i]} is: {(tickets[i]/base_yr_val)*100}")