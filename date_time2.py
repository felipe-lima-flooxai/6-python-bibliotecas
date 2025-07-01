from datetime import datetime, timedelta
from pytz import timezone
from dateutil.relativedelta import relativedelta

date_now = datetime.now(timezone("UTC"))
date_tokyo = datetime.now(timezone("Asia/Tokyo"))

delta_time = date_tokyo - date_now
delta_2h = timedelta(hours=2)
relative = relativedelta(date_tokyo, date_now)

print("UTC:", date_now)
print("Tóquio:", date_tokyo)
print("Delta horário:", delta_time)
print("Delta de 2 horas:", delta_2h)
print("Relativedelta:", relative)