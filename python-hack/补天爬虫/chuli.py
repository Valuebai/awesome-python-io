#author:九世
#time:2019/1/12

import os

chuli_url=[]
def chuli():
    if os.path.exists('doc_host'):
        print('[a] Found doc_host')
        lk=os.listdir('doc_host')
        if len(lk)!=0:
            for z in lk:
                dk=open('doc_host/{}'.format(z),'r')
                for r in dk.readlines():
                    qc="".join(r.split('\n'))
                    dd=str(qc).replace('http://','').replace('www.','').replace('https://','')
                    chuli_url.append('www.{}'.format(dd))

                xj=open('doc_host/{}'.format(z),'w')
                xj.close()

                for i in chuli_url:
                    print('[a] {}'.format(i))
                    print(i,file=open('doc_host/{}'.format(z),'a'))
        else:
            print('[q] Found doc_host,but Not txt....')
    else:
        print('[q] Not Found doc_host')
if __name__ == '__main__':
    chuli()