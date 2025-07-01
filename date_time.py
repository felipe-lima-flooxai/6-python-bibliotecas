from datetime import datetime
from pytz import timezone

#ano, mes, dia
date = datetime(2022, 4, 20)
print(date)

date_str = "2022-04-20 07:49:24"
date_fmt = "%Y-%m-%d %H:%M:%S"
date2 = datetime.strptime(date_str, date_fmt)
print(date2)


date_now = datetime.now()
print(date_now)

date_timezone = datetime.now(timezone("Asia/Tokyo"))
print(date_timezone)