import time

# Convert a time expressed in seconds since epoch to readable string
# epoch = when your computer thinks time began (reference point)
# print(time.ctime(0))

# Return current seconds since epoch
# print(time.time())

# Return the current date and time in a readable string format
# print(time.ctime(time.time()))

# Get local time and UTC time
# time_object = time.localtime()    # Local time
# time_object = time.gmtime()       # UTC time

# Format the time object into a readable string
# local_time = time.strftime('%B %d %Y %H:%M:%S', time_object)
# print(local_time)

# Parse a time string into a time object
# time_string = 'January 17, 2024'
# time_object = time.strptime(time_string, '%B %d, %Y')
# print(time_object)

# Convert a time tuple into a formatted time string
# (year, month, day, hours, minutes, secs, day of the week, day of the year, dst)
# time_tuple = (2024, 1, 17, 16, 25, 0, 3, 17, 0)
# time_string = time.asctime(time_tuple)
# print(time_string)

# Convert a time tuple into seconds since epoch
# (year, month, day, hours, minutes, secs, day of the week, day of the year, dst)
# time_tuple = (2024, 1, 17, 16, 25, 0, 3, 17, 0)
# time_seconds = time.mktime(time_tuple)
# print(time_seconds)
