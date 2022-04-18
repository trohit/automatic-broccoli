1. rmem_max : max OS recv buf size for all sort of connections.
also applies to max tcp recv window 
default: 128kb which is ok for low latency networks.
but if latency is larger then default size is small
Will increase mem usage.
2. wmem_max : max OS recv buf size for all sort of connections. 
3. tcp_wmem : Max TCP send window SO_SNDBUF
three diff vals
1st min send_buf
2nd default send buf
3rd max TCP send buf
4. tcp_rmem :  SO_RCVBUF
Both tcp_rmem and tcp_wmem governed by rmem_max and wmem_max
5. so_maxconn : max # of outstanding pending conns in the sockets listen queue. viz. listen(sockfd, int backlog)
if a aconn. request when the q is full, client may get 

