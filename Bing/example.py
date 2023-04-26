import Bing.BingPython as ai
import asyncio
import re


# Cookies
# You can get with Cookie Editor
# - Enter to https://www.bing.com/search?q=Bing+AI&showconv=1&FORM=hpcodx
# - Open cookie editor
# - Write your cookie
# OR
# - Export your cookies as Netscape
# - Write your cookies inside of cookies.txt
#     try:
#         import cookielib
#     except:
#         import http.cookiejar
#         cookielib = http.cookiejar
# cookies = cookielib.MozillaCookieJar('cookies.txt')
# cookies.load()
cookies = {
    'MUID': '3BA8B12BB7CC6D58391DA00FB6B06C29',
    'MUIDB': '3BA8B12BB7CC6D58391DA00FB6B06C29',
    'USRLOC': 'HS=1&ELOC=LAT=29.97455406188965|LON=31.260295867919922|N=Qesm%20El%20Basateen%2C%20Cairo|ELT=2|&CLOC=LAT=29.9745547908424|LON=31.260296034885485|A=733.4464586120832|TS=230426074216|SRC=W',
    'SRCHD': 'AF=hpcodx',
    'MMCASM': 'ID=33DF5FFA342842659368E1CEAE87E3D8',
    'ANON': 'A=BF86ACCF614097E03333ADB8FFFFFFFF&E=1c28&W=1',
    'ABDEF': 'V=13&ABDV=13&MRNB=1682459571185&MRB=0',
    'PPLState': '1',
    'KievRPSSecAuth': 'FACSBBRaTOJILtFsMkpLVWSG6AN6C/svRwNmAAAEgAAACNA4tSFNzEOdUASBrv42DrRkmYw/gkxtgGJjw66oWfEi+Qe4RKH4UyKcP9t7mRIkHVl8SUs0hZp+11qr19bej5Ipz5WHWhOu70thxD87v4d6EJvIepJbby/PMXnFBfpcY4S3KGz1TLqVm96UUV2yt+tA/jxYX5/mXW7FxUNjyd6T9pg72Vh+M5Pvi2V/R4Z6vmIKwzAIHxR/8XDOmwOjdbY1/qXmxcdYDN+iRBExfBIRAjnpsomircj9aLIRj0U3SZ35DpxhlIT+IPYNuemKR7UAl7A7jJLMAh4lpIAsiC38umbL0q6eun22WGj8FtqLnlpzwRiwFneWBipQa3uSQFbWIkeGVb1mlXMpK+Okwf9mv+n9+1rqrTo9ZDKm0yXw0A59Kee0sryNPiQXosvjN2qWxVMn2gulmzvPGGVZPR1ficQSRlQuiKgju63mZst4MJ1+JPBp710aMyP+OPk8sHWqNRAvo2bj6mDzQlMIdR5zWdgfYeB6/mM56VWGQVp0xGXWdKRcN+gS7BEJjS0Ki2+DVjdfVGvvreBbplojE+gwRmSIg9eU8sITvfAZleHshkKgcAxvhAf7zmrgkf5N+sAMReAlynA5P04xoAqIIuaeKecHh43Y2nqHqeMOD7Iwa0dIW/Rz0BcKaVA/mE09tZhTU2yalIv/8o4Lk0heXrRcfwMMco09HYd7bkS7t5QgEZzPx+NLkfYYQIoAwG4M/ivGqn9clFhM1AS41i9v8tvHu3ub73uQ78XxN/P9TeTTvXUjLUbABBvDJozOF51ZDex68L92kEqeLbrIMuXfcdPcNsNhlnwOQ8P1zNIfZOFTEyMCJaNXoN6RPqWsO9mWl+zgnRjmejE4HzTSmzcEovJnsNwD2QYbqdIg9y9Mxp3aaGAxvRsU0YGpHKbaao2dHZ68Ci/otFr5OmJQB2ZgHQh7wyTwuutUpH0qTImfVSNqcFlv2YbEv1114CyqzktoVUgNSKHXqqRRAq8owQSJVd782JjRBisKpgMR+8dCENaibwbd/zr3LA1VhfBZss/Aiux5w0dXdrwwF77kp5VC8X9gIQXjOERHfq3f2L7Hh4fgqvZvU1AXHI/aWRPCE7rJxRNAwlFMxhYTYtEVuwXtcr23LnERauqjR1aXVS4eRxxSY5ffmhJwT81FgBrtvhm/l3VjmtZYugbYMBYteQthvxueOtDmO3RLo5E67oLCgdAVsR4pHD/Y7rA+u7CJtKamHehPKHe16gZGV1KpWQBHHqupuqHsDBm1hUkapKAng6ZU70vYPR5yBr2jAigcRx8lXDbC4lmNXdxsS5Iy+QmD94dqzswg0S3URbl6eqC7I7o4UJktduYpnurYhYKCskDZCCVjNJvgr5x1sOiL8Y0PT5hKX7O5voj5UJ3VR8KItFZWKEf2W8bxlkyCCPD2AAJFLzoNvJnJxByqV9dgJVg7Q+uZrl/RvnhewOdL9v3ERRckeNiX7VCJDVjknNIUAJnI9lZXquwct+VHTXOK8GVO6iDb',
    '_U': '1LUmmuDx2Twpf_AV1JrVKfajnsVZmhZ86eaZ82N5aDv912WC-FxqNzKsE1RS9Hytv68H7fRXBhNrUA2T1diGTsvkQyDuImONpEX_Zk8-bkR3unrfFZiUt1viUjZB5cjOeSv-iZK2UVLiR3SbnOiWU_pn0WLcS6XHEGggVFsOthlDa-IWeNwqieIl4nTyQuvJZbZ0D2ekLeXN1ioBTOBTws0uyADBE0VVB8780dZTcGoc',
    'SUID': 'A',
    '_EDGE_S': 'SID=0ABCA05760CF63512F6BB2A861D1629C',
    'WLS': 'C=5084018b0ae91b63&N=raghad',
    '_SS': 'SID=0ABCA05760CF63512F6BB2A861D1629C&PC=EDBBAN&R=66&RB=66&GB=0&RG=0&RP=63',
    '_clck': '1s6jqay|1|fam|0',
    'SRCHUSR': 'DOB=20220107&T=1682495197000&POEX=W',
    '_RwBf': 'ilt=125&ihpd=0&ispd=1&rc=66&rb=66&gb=0&rg=0&pc=63&mtu=0&rbb=0.0&g=0&cid=&clo=0&v=4&l=2023-04-26T07:00:00.0000000Z&lft=0001-01-01T00:00:00.0000000&aof=0&o=0&p=BINGCOPILOTWAITLIST&c=MR000T&t=5936&s=2023-03-15T18:45:39.0717082+00:00&ts=2023-04-26T07:55:00.7937897+00:00&rwred=0&wls=2&lka=0&lkt=0&TH=&mta=0&e=8JJEDbAGkGe-6-Asr0LUMYtU1HzfvpUoDEa7VZIFOAjswv6LFg9kO7mpeNvj_zWS4juDl03X4IvQK-9LxFEzPA&A=&mte=0',
    'SRCHHPGUSR': 'SRCHLANG=en&BRW=XW&BRH=M&CW=1536&CH=754&SW=1536&SH=864&DPR=1.3&UTC=120&DM=0&EXLTT=31&WTS=63815762177&HV=1682495702&PV=10.0.0&PRVCW=770&PRVCH=754&SCW=1519&SCH=4015',
    'ipv6': 'hit=1682498804047&t=4',
    '_tarLang':'default=ar',
    '_EDGE_V':'1',
    '_TTSS_IN':'hist=WyJlbiIsImF1dG8tZGV0ZWN0Il0=',
    '_TTSS_OUT':'hist=WyJhciJd',
    'TTRSL':'en',
}

def get_revenue(ask):
    command = ai.BingPython.sendcom_sydney(ai.BingPython.CreateSession(cookies), ask)
    answer=asyncio.get_event_loop().run_until_complete(command)
    # check if the answer has I'm sorry in any form using regex
    print(answer)
    if re.search(r"i('m| am) sorry", answer, re.IGNORECASE):
        return None #print(None)
    # check if the answer has $numberM or $numberM-$numberM using regex
    else:
        result=re.search(r"(\$\d+(\.\d+)? ?(million|m)?(-\$\d+(\.\d+)? ?(million|m))?)", answer, re.IGNORECASE)
        if result:
            return result.group(0)
        else:
            return None  

