import urllib.request
import urllib.parse
import urllib.response

# if __name__ == '__main__':
#
#     request = urllib.request.Request('http://127.0.0.1:3000/')
#     with urllib.request.urlopen(request) as response:
#         html = response.read()
#         realurl = response.geturl()
#         rtuinfo = response.info()
#         print(realurl, '----\n', rtuinfo)
#
#         for key, val in enumerate(rtuinfo):
#             print(key, '--', val, '--', rtuinfo[val])
#
#         for k, v in rtuinfo.items():
#             print(k, '--', v)
#
#     # if __name__ == '__main__':
#     #     url = 'https://www.google.com/search'
#     #     user_agent = 'Mozilla/5.0 (Windows NT 6.1; Win64; x64)'
#     #     headers = {'User-Agent': user_agent}
#     #     queryval = {'q': 'hello'}
#     #     querystr = urllib.parse.urlencode(queryval)
#     #     url = url + '?' + querystr
#     #     req = urllib.request.Request(url, None, headers)
#     #     # with urllib.request.urlopen(req) as response:
#     #     #     rtnpage = response.read().decode('utf-8')
#     #     #     print(rtnpage)
#     #     try:
#     #         urllib.request.urlopen(req)
#     #     except urllib.error.HTTPError as e:
#     #         print(e.code)
#     #         print(e.read())
if __name__ == '__main__':
    with urllib.request.urlopen('http://python.org') as response:
        print('real url---', response.geturl())
        for k, v in response.info().items():
            print(k, '==', v)
        html = response.read()
        import subprocess
        import os.path

        if os.path.exists('tmp.html') is True and os.path.isfile('tmp.html') is True:
            print('remove tmp.html')
            os.remove('tmp.html')
        rtnv = subprocess.check_output(['touch', 'tmp.html'])
        with open('./tmp.html', 'r+') as filehandle:
            for line in html.splitlines():
                filehandle.write(line.decode('utf-8'))
                filehandle.write('\n')
                filehandle.seek(1)
