#  Dark Net Monitor

企业威胁情报平台建设之暗网监控

## 代理服务器搭建

由于国内网络环境的原因，为了顺利访问暗网，我们需要一台海外服务器，系统版本是ubuntu 18.04(当然其他系统也可以，只是本文会把这个版本的系统作为例子)，同时需要在这台服务器上安装Tor与Privoxy用作访问代理服务器。 

![image](https://user-images.githubusercontent.com/75350727/147442743-7703bbb0-76e4-42fc-ba25-5ee00ee0f0d1.png)


本文的系统版本：
```
root@vultr:~# cat /etc/issue.net
Ubuntu 18.04.6 LTS
```

## 安装和配置Tor

可能很多人一开始会直接执行这条命令：sudo apt-get install tor，从这个命令安装的Tor是v2版本的，不支持较新的加密算法，所以导致访问不到某些使用最新加密算法的暗网网址。 

Tor v2到Tor v3的转变主要表现为如下几点： 

    1.签名算法从SHA1/DH/RSA1024升级到SHA3/ed25519/curve25519；
    2.改进的Tor directory protocol，安全性更高；
    3.更好的洋葱地址，换成sha3，可以提高枚举生成一样地址的难度；
    4.可拓展的交换协议。

参考官网的安装方法，安装最新版（v3版本）的Tor步骤如下：

```
sudo apt install apt-transport-https curl

sudo -i

echo "deb https://deb.torproject.org/torproject.org/ $(lsb_release -cs) main" > /etc/apt/sources.list.d/tor.list

curl https://deb.torproject.org/torproject.org/A3C4F0F979CAA22CDBA8F512EE8CBC9E886DDD89.asc | gpg --import

gpg --export A3C4F0F979CAA22CDBA8F512EE8CBC9E886DDD89 | apt-key add -

apt update

exit

sudo apt install tor tor-geoipdb torsocks deb.torproject.org-keyring
```

验证
```
root@vultr:~# tor -v
Dec 27 06:11:29.039 [notice] Tor 0.4.6.9 running on Linux with Libevent 2.1.8-stable, OpenSSL 1.1.1, Zlib 1.2.11, Liblzma 5.2.2, Libzstd 1.3.3 and Glibc 2.27 as libc.
```

## 安装与配置Privoxy

这里暂时没有什么版本要求，所以可以直接执行apt-get install privoxy。 

安装好后，为了让Privoxy把http协议转发到Tor，需要编辑/etc/privoxy/config加上：
```
forward-socks5t / 127.0.0.1:9050
```
修改后，重启服务service privoxy restart。

## 本地使用

官网下载地址

https://www.torproject.org/download/

选择对应版本下载安装

使用时 修改Tor浏览器的网络设置（假设我们的代理服务器ip为：11.11.11.11）

![image](https://user-images.githubusercontent.com/75350727/147444420-8d93a98d-a464-4148-b9e9-622ab9200d67.png)

## 暗网监控

| 网站名 | 网址 | 监控结果 |
|  ----  | ----  | ----  | 
|FreeCity | http://xbtppbb7oz5j2stohmxzvkprpqw5dwmhhhdo2ygv6c7cs4u46ysufjyd.onion| |
| 楼兰城 | http://c2p3hg35jalss7b2a6hkmhzflgevkonqt7g6jze62ro2g4h4wmzwobid.onion/ | |
