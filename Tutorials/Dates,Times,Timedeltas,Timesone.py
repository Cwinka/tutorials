import pytz
import datetime
d = datetime.date(2019, 10, 7) #sets date
tday = datetime.date.today() #shows current date
# print(tdat.weekday()) # monday is 0 sunday is 6
# print(tdat.isoweekday()) #monday is 1 sunday is 7
tdelta = datetime.timedelta(days=7) #creates timedelta witch can be used for calculations with date
#also can contain year, month, hours, minutes, seconds
# print(tdat + tdelta) # shows what day will be through tdelta
bday = datetime.date(2020, 1, 21)
till_bday = bday - tday # equals to new timedelta till my byrthday
# print(till_bday.days) # showls just days
t = datetime.time(9, 30, 45, 100000) # creates  time
# print(t.hour)
t1 = datetime.datetime(2019, 10, 7, 10, 4, 40, 100000) # another date including time
print(t1)
# print(t1 + tdelta) # also supports timedelta
dt_today = datetime.datetime.today() # without timezone
dt_now = datetime.datetime.now() # allowds us add timezone
dt_utcnow = datetime.datetime.utcnow() # timezone aware timezone
# print(dt_today)
# print(dt_now)
# print(dt_utcnow)
dt = datetime.datetime(2019, 10, 7, 10, 14, 32, tzinfo= pytz.UTC) # add empty timezone
# print(dt)
dt_utc_now = datetime.datetime.now(tz=pytz.UTC) # add milliseconds
# print(dt_utc_now)
dt_mtn = dt_now.astimezone(pytz.timezone('Asia/Yekaterinburg')) #ad real timezone to dt
# print(dt_mtn)
dt_eastern = dt_now.astimezone(pytz.timezone('US/Eastern'))
# print(dt_eastern)
# for tz in pytz.all_timezones: #just shows all timezons witch allowded
#     print(tz)
dt_str = 'July 26, 2019'
dtstr = datetime. datetime.strptime(dt_str, '%B %d, %Y') # overdo dt_str from string into datetime
# print(dtstr)
