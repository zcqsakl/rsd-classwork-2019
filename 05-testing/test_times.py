import times
# define function with name of the file 

import datetime
# to use corresponding functions (strp)

# def test_given_input():
#    large = times.time_range("2010-01-12 10:00:00", "2010-01-12 12:00:00")
#    short = times.time_range("2010-01-12 10:30:00", "2010-01-12 10:45:00", 2, 60)
    # print(times.overlap_time(large, short))

#    result = times.overlap_time(large, short) 
    # print(result)
#    expected = [('2010-01-12 10:30:00', '2010-01-12 10:37:00'), ('2010-01-12 10:38:00', '2010-01-12 10:45:00')]
    # not what it gives me when i run it on its own
    # copy the output of the program as the expected value
#    assert result == expected

# test_given_input()

def test_class_time():
    large = times.time_range("2019-10-31 10:00:00" , "2019-10-31 13:00:00")
    short = times.time_range("2019-10-31 10:05:00", "2019-10-31 12:55:00", 3, 600)
    # two breaks, therefore 3 blocks
    result = times.overlap_time(large, short) 
    assert result == short
    # smaller time encompasses the bigger one (small time in a big time)
    # expected results is the shorter time range

# test_class_time()

# new test: multiple ranges on both inputs
# testing05

def new_20_min():
    large = times.time_range("2019-01-01 00:00:00" , "2019-01-01 23:50:00", 24, 10*60)
    # full day with intervals of 50 min and 10 min gaps. (00:00 - 00:50; 01:00 - 01:50; ..
    short = times.time_range("2019-01-01 00:30:00", "2019-01-01 23:55:00", 24, 35*60)
    # full day too but starts at 00:30 with intervals of 25 min and gaps of 35 min. (00:30 - 00:55; 01:30 - 01:55; ... )
    result = times.overlap_time(large,short)
    # test that all the overlaping intervals are 20 min long
    assert all ([(datetime.datetime.strptime(t1, "%Y-%m-%d %H:%M:%S") - datetime.datetime.strptime(t0, "%Y-%m-%d %H:%M:%S")).total_seconds() == 20 * 60 for t0, t1 in result])
    # BOOLEAN FOR LOOP IN CONCATENATED WAY (bcs ==), if total seconds == 20*60, then true, otherwise false

    # t1, t0
    # unpacking because we have like a,b = [(1,2]), (2,3)]
    # a is (1,2)
    # b is (2,3)
    # we are doing iterate for a,b in a results (the entire thing) element by element

new_20_min()