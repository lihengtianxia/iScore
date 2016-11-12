#coding=GBK
'''
Created on Mar 25, 2015

@author: stanley
'''
import sys
import time

if __name__ == '__main__':
    if len(sys.argv)!=2:
        print "Usage python main.py data"
        sys.exit(-1)
    f = open(sys.argv[1],'r')
    #f = open("testFile.txt",'r')
    line=f.readline()
    ISOTIMEFORMAT='%Y-%m-%d %X'
    cnt=0
    print "%s"%(time.strftime(ISOTIMEFORMAT, time.localtime()))
    cust_dict={}    #客户字典(客户号，对手字典）
    #testFile = open('testFile.txt', 'w')
    while line!="":
        line=f.readline()
        #testFile.write("%s"%(line))
        cnt=cnt+1
        #if(cnt>10000):
        #    break
        infos=line.split(",")
        if(len(infos)!=18 or infos[4]=="" or infos[13]=="" or infos[15]=="" or infos[15].find('ATM')!= -1 or infos[15]== '30' or infos[15]== '50'):
            continue
        #print infos[4],infos[13],infos[15]     4-客户号，13-对手卡号，15-对手姓名
        if(cust_dict.has_key(infos[4])):
            opp_dict=cust_dict[infos[4]]
            if(opp_dict.has_key(infos[15])):
                opp_no_list=opp_dict[infos[15]]
                if(not(infos[13] in opp_no_list)):
                    opp_no_list.append(infos[13])
                opp_dict[infos[15]]=opp_no_list
            else:
                opp_no_list=[]
                opp_no_list.append(infos[13])
                opp_dict[infos[15]]=opp_no_list
            cust_dict[infos[4]]=opp_dict
        else:
            opp_dict={}     #对手字典(姓名，卡号列表）
            opp_no_list=[]       #卡号列表(卡号）
            opp_no_list.append(infos[13])
            opp_dict[infos[15]]=opp_no_list
            cust_dict[infos[4]]=opp_dict
    #testFile.close()
    #输出初步结果 客户号，姓名，[卡号列表]
    result1 = open('result1.txt', 'w')
    opp_list_2=[] #结果列表(姓名，[卡号列表])
    acct_dict={}
    line_no=0
    for k1,v1 in cust_dict.items():
        for k2,v2 in v1.items():
            if(len(v2)>1):
                result1.write("%s %s %s\n"%(k1,k2,v2))
                #print "%s %s %s\n"%(k1,k2,v2)
                for acct in v2:
                    if(acct_dict.has_key(acct)):
                        cust_list=acct_dict[acct]
                        if(not(line_no in cust_list)):
                            cust_list.append(line_no)
                        acct_dict[acct]=cust_list
                    else:
                        cust_list=[]
                        cust_list.append(line_no)
                        acct_dict[acct]=cust_list
                v2.insert(0,k2)
                v2.insert(0,k1)
                opp_list_2.append(v2)
                line_no=line_no+1
                '''
                isOK=False
                for opp in opp_list_2:
                    if(isOK):
                        break
                    elif(k2==opp[0]):
                        for acct in v2:
                            if(acct in opp):
                                opp.extend(v2)
                                isOK=True
                                break
                if(isOK==False):
                    v2.insert(0,k2)
                    opp_list_2.append(v2)
                '''
    result1.close()
    #输出最终结果：姓名，[卡号列表]
    result2 = open('result2.txt', 'w')
    result3 = open('result3.txt', 'w')
    line_dict={}    #(行号，唯一码）
    line_dict2={}    #(唯一码，行号列表)
    idx=0
    for k3,v3 in acct_dict.items():
        if(len(v3)>1):
            result3.write("%s"%(k3))
            hit=False
            hitIdx=0
            for cust in v3:
                if(line_dict.has_key(cust)):
                    hit=True
                    hitIdx=line_dict[cust]
                    break
            if(hit):
                for cust in v3:
                    result3.write(",%s"%(opp_list_2[cust][0]))
                    line_dict[cust]=hitIdx
                    if(line_dict2.has_key(hitIdx) and (cust not in line_dict2[hitIdx])):
                        line_dict2[hitIdx].append(cust)
            else:
                idx=idx+1
                for cust in v3:
                    result3.write(",%s"%(opp_list_2[cust][0]))
                    line_dict[cust]=idx
                    if(line_dict2.has_key(idx) and (cust not in line_dict2[idx])):
                        line_dict2[idx].append(cust)
                    elif(not line_dict2.has_key(idx)):
                        line_list2=[]
                        line_list2.append(cust)
                        line_dict2[idx]=line_list2
            result3.write("\n")
    opp_list_3=[]
    for k4,v4 in line_dict2.items():
        if(len(v4)>1):
            opp3=[]
            opp3.append(opp_list_2[v4[0]][1])
            for cust in v4:
                opp_list_2[cust][0]="deleted"
                opp4=[]
                opp4.extend(opp_list_2[cust])
                opp4.remove(opp4[0])
                opp4.remove(opp4[0])
                opp3.extend(opp4)
            opp_list_3.append(opp3)
    for opp in opp_list_3:
        name=opp[0]
        opp.remove(name)
        acct_set=set(opp)
        result2.write("%s,%s\n"%(name,acct_set))
    for opp in opp_list_2:
        if(opp[0]!="deleted"):
            name=opp[1]
            opp.remove(name)
            opp.remove(opp[0])
            acct_set=set(opp)
            result2.write("%s,%s\n"%(name,acct_set))
        '''
        name=opp[0]
        opp.remove(name)
        acct_set=set(opp)
        result2.write("%s,%s\n"%(name,acct_set))
        '''
    result2.close()
    result3.close()
    print cnt
    print "%s"%(time.strftime(ISOTIMEFORMAT, time.localtime()))
    pass
