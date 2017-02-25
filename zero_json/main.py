import json
import time
import sys

if __name__ == '__main__':
    # if len(sys.argv) != 2:
    #    print "Usage python main.py data"
    #    sys.exit(-1)
    # f = open(sys.argv[1], 'r')

    reload(sys)
    sys.setdefaultencoding('utf-8')
    ISOTIMEFORMAT = '%Y-%m-%d %X'
    cnt = 0
    print "%s" % (time.strftime(ISOTIMEFORMAT, time.localtime()))

    f = open("zero.txt", 'r')
    zero_str = f.read()
    zero_json = json.loads(zero_str)
    zero_list = zero_json['t']['pageContent']
    testFile = open('zero_list.txt', 'w')
    for cust in zero_list:
        print cust['businessNo'], cust['custName'], cust['companyName'], cust['companyAddr'] \
            , cust['createTime'], cust['contactsName'], cust['contactsPhone'], cust['contactsRelation'] \
            , cust['custAddress'], cust['custAge'], cust['custEdu'], cust['custEmail'] \
            , cust['custGender'], cust['deductCardNum'], cust['monthIncome'], cust['custState'] \
            , cust['orderAmt'], cust['salerNo'], cust['yearOfCompany'], cust['stageNum'] \
            , cust['custId'], cust['custLoanNo'], cust['custMaritalStatus'], cust['custMobile'] \
            , cust['failReason']
        testFile.write(
            "%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s" % \
            (cust['businessNo'], cust['custName'], cust['companyName'], cust['companyAddr'] \
                 , cust['createTime'], cust['contactsName'], cust['contactsPhone'], cust['contactsRelation'] \
                 , cust['custAddress'], cust['custAge'], cust['custEdu'], cust['custEmail'] \
                 , cust['custGender'], cust['deductCardNum'], cust['monthIncome'], cust['custState'] \
                 , cust['orderAmt'], cust['salerNo'], cust['yearOfCompany'], cust['stageNum'] \
                 , cust['custId'], cust['custLoanNo'], cust['custMaritalStatus'], cust['custMobile'] \
                 , cust['failReason']))
        testFile.write("\n")
        cnt += 1

    print cnt
    print "%s" % (time.strftime(ISOTIMEFORMAT, time.localtime()))
    pass
