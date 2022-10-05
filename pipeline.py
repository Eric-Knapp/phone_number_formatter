import sys

for line in sys.stdin:
    raw_phone_num = line.strip()
    
    area_code = raw_phone_num[0:3]
    first_3 = raw_phone_num[3:6]
    last_4 = raw_phone_num[6:]
    
    print('(%s) %s-%s' % (area_code, first_3, last_4))
    
    
    # run txt file with phone numbers not formatted:
    # cat input.txt | python pipline.py > output.txt