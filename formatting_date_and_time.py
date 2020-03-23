from datetime import datetime
now = datetime.now()

print('%02d/%02d/%04d' % (now.month, now.day, now.year))
print('%02d:%02d:%02d' % (now.hour, now.minute, now.second))

#=> 03/23/2020
#=> 18:36:39