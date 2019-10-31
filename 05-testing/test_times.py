import times
# define function with name of the file 

def test_given_input():
    large = times.time_range("2010-01-12 10:00:00", "2010-01-12 12:00:00")
    short = times.time_range("2010-01-12 10:30:00", "2010-01-12 10:45:00", 2, 60)
    # print(times.overlap_time(large, short))

    result = times.overlap_time(large, short) 
    print(result)
    expected = [('2010-01-12 10:30:00', '2010-01-12 10:37:00'), ('2010-01-12 10:38:00', '2010-01-12 10:45:00')]
    # not what it gives me when i run it on its own
    # copy the output of the program as the expected value
    assert result == expected

test_given_input()

def test_class_time():
    large = times.time_range("2019-10-31 10:00:00" , "2019-10-31 13:00:00")
    short = times.time_range("2019-10-31 10:05:00", "2019-10-31 12:55:00", 3, 600)
    # two breaks, therefore 3 blocks=
    result = times.overlap_time(large, short) 
    assert result == short
    # smaller time encompasses the bigger one (small time in a big time)
    # expected results is the shorter time range

test_class_time()
