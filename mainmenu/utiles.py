'''
Created on 14/06/2011

@author: Francisco1
'''

import datetime
import time

from django.utils.tzinfo import LocalTimezone
from django.utils.translation import ungettext, ugettext

def tiempotranscurrido(d, now=None):
    """
    Takes two datetime objects and returns the time between d and now
    as a nicely formatted string, e.g. "10 minutes".  If d occurs after now,
    then "0 minutes" is returned.

    Units used are years, months, weeks, days, hours, and minutes.
    Seconds and microseconds are ignored.  Up to two adjacent units will be
    displayed.  For example, "2 weeks, 3 days" and "1 year, 3 months" are
    possible outputs, but "2 weeks, 3 hours" and "1 year, 5 days" are not.

    Adapted from http://blog.natbat.co.uk/archive/2003/Jun/14/time_since
    """

    # Convert datetime.date to datetime.datetime for comparison.
    if not isinstance(d, datetime.datetime):
        d = datetime.datetime(d.year, d.month, d.day)
    if now and not isinstance(now, datetime.datetime):
        now = datetime.datetime(now.year, now.month, now.day)

    if not now:
        if d.tzinfo:
            now = datetime.datetime.now(LocalTimezone(d))
        else:
            now = datetime.datetime.now()

    # ignore microsecond part of 'd' since we removed it from 'now'
    delta = now - (d - datetime.timedelta(0, 0, d.microsecond))
    since = delta.days * 24 * 60 * 60 + delta.seconds
    if since <= 0:
        # d is in the future compared to now, stop processing.
        return u'0 ' + ugettext('minutes')
    
    
    chunks = (
      (60 * 60 * 24 * 365, lambda n: 'hace ' + str(delta.days//365) + ' ' +ungettext('year', 'years', n)),
      (60 * 60 * 24 * 30, lambda n: 'hace ' + str(delta.days//30) + ' ' +ungettext('month', 'months', n)),
      (60 * 60 * 24 * 7, lambda n: 'hace ' + str(delta.days//7) + ' ' +ungettext('week', 'weeks', n)),
      (60 * 60 * 24 * 3, lambda n: 'hace ' + str(delta.days) + ' ' +ungettext('dias', 'dias', n)),
      (60 * 60 * 24 * 2, lambda n : 'ayer'),
      (60 * 60 * 24, lambda n : 'hoy'),
      (60 * 60, lambda n: 'hoy'),
      (60, lambda n: 'hoy')
    )

    for i, (seconds, name) in enumerate(chunks):
        count = since // seconds
        if count != 0:
            break
    s = name(count)
    '''
    if i + 1 < len(chunks):
        # Now get the second item
        seconds2, name2 = chunks[i + 1]
        count2 = (since - (seconds * count)) // seconds2
        if count2 != 0:
            s += ugettext(', %(number)d %(type)s') % {'number': count2, 'type': name2(count2)}
    '''
    return s
