# ops_tools
ops tools I used to manage server. Very simple to use

# netstatm

short cut for:

    netstat -n|grep ^tcp|awk '{print $NF}'|sort -nr|uniq -c

get the network connections of current server

SUCH AS:

    2 LAST_ACK
    66 ESTABLISHED
    27 CLOSE_WAIT

# killcmd

    usage: killcmd {cmd}

short cut for:

    ps aux | grep "{cmd}" | awk '{print $2}' | xargs kill -9

so, when you have losts of processes like:

    root     24517  0.5  0.3 1866992 52792 pts/9   Sl   19:31   0:17 python logic_server.py config/conf1.yaml easy
    root     24518  0.5  0.2 1867152 48780 pts/9   Sl   19:31   0:17 python logic_server.py config/conf2.yaml easy
    root     24519  0.5  0.3 1867148 52856 pts/9   Sl   19:31   0:17 python logic_server.py config/conf3.yaml easy
    root     24520  0.5  0.3 1866992 52796 pts/9   Sl   19:31   0:17 python logic_server.py config/conf4.yaml easy
    root     24521  0.5  0.2 1867152 48768 pts/9   Sl   19:31   0:17 python logic_server.py config/conf5.yaml easy
    root     24522  0.5  0.2 1866992 48704 pts/9   Sl   19:31   0:17 python logic_server.py config/conf6.yaml easy
    root     24523  0.5  0.2 1867152 48764 pts/9   Sl   19:31   0:17 python logic_server.py config/conf7.yaml easy
    root     24524  0.5  0.3 1867148 50828 pts/9   Sl   19:31   0:17 python logic_server.py config/conf8.yaml easy
    root     24525  0.5  0.3 1867148 50824 pts/9   Sl   19:31   0:17 python logic_server.py config/conf9.yaml easy

you can simply kill them all in once by

    killcmd "server.py config"

