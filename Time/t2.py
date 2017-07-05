# -*- coding: UTF-8 -*-

import calendar

cal = calendar.month(2016, 1)

print cal;

print calendar.calendar(2016,w=2,l=1,c=6)


print calendar.month(2017,8,w=2,l=1)


print calendar.monthcalendar(2017,5)


print calendar.monthrange(2017,8)


calendar.prcal(2017,w=2,l=1,c=6)
calendar.prmonth(2016,2,w=2,l=1)

print calendar.weekday(2017,8,9)