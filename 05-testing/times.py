import datetime

def time_range(t0, t1, n=1, g=0):
    # n is number of steps, number of time blocks
    # the lenght of gap in between the blocks
    # expect two elements of times
    t0_s = datetime.datetime.strptime(t0, "%Y-%m-%d %H:%M:%S")
    t1_s = datetime.datetime.strptime(t1, "%Y-%m-%d %H:%M:%S")
    d = (t1_s - t0_s).total_seconds() / n + g * (1/n - 1)
    # print(d)
    sec_range = [(t0_s + datetime.timedelta(seconds=i * d + i * g),
                  t0_s + datetime.timedelta(seconds=(i + 1) * d + i * g)) for i in range(n)]
    return [(ta.strftime("%Y-%m-%d %H:%M:%S"), tb.strftime("%Y-%m-%d %H:%M:%S")) for ta, tb in sec_range]


def overlap_time(obs1, obs2):
    # looking for overlap of observations
    ot = []
    for tr0, tr1 in obs1:
        for tra, trb in obs2:
            if tr0 <= tra <= tr1 or tr0 <= trb <= tr1:
                low = max(tr0,tra)
                high = min(tr1,trb)
                ot.append((low,high))
    return ot
    # gives list of time observations with a time where it started and finished 


if __name__ == "__main__":
     large = time_range("2019-01-01 00:00:00" , "2019-01-01 23:50:00", 24, 10*60)
    # full day with intervals of 50 min and 10 min gaps. (00:00 - 00:50; 01:00 - 01:50; ..
     short = time_range("2019-01-01 00:30:00", "2019-01-01 23:55:00", 24, 35*60)
     #large = time_range("2010-01-12 10:00:00", "2010-01-12 12:00:00")
     #short = time_range("2010-01-12 10:30:00", "2010-01-12 10:45:00", 2, 60)
     print(overlap_time(large, short))
     print(len(overlap_time(large,short)))
