from bs4 import BeautifulSoup
import os
import re


def get_test_case_name(file_name):
    with open(file_name,'r') as myfile:
        data=myfile.read().replace('<thead>','</table>\n<table>\n<thead>')
    soup = BeautifulSoup(data, 'html.parser')
    
    #html_doc=open(file_name)
    #soup = BeautifulSoup(html_doc, 'html.parser')
    table_body=soup.findAll('table')
    suite=str(soup.findAll('h1'))
    reg1=re.match(r'.*\<[a-z][0-9]\>(.*)\<\/[a-z][0-9]\>',suite)
    test_suite=reg1.group(1)
    test_case=soup.findAll('h2')
    image_list=[]
    images=[]
    data={}
    result={}

    test_case_names=[]
    test_cases = []
    
    for t in table_body:
        images_for_dic=[]
        test_case_for_dic=""
        test_case=str(t.findAll('h2'))
        
        if not test_case=="[]":
            
            reg1=re.match(r'.*\<[a-z][0-9]\>(.*)\<\/[a-z][0-9]\>',test_case)
            res1=reg1.group(1)
            test_case_for_dic=res1
            test_cases.append(res1)
        test_case_names.append(test_case)
        
        image=t.findAll('img')
        for i in image:
            image_list.append(str(i))
            if not i=="[]":
                reg=re.match(r'.*\\(.*\.[a-z]*)',str(i))
                if reg:
                    res=reg.group(1)
                    images.append(res)
                    images_for_dic.append(res)
        
        if not (test_case_for_dic=="" or images_for_dic==[]):
            data[test_case_for_dic]=images_for_dic
            
    #result[test_suite]=data
    
    
    return test_suite,data
