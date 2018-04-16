## WEBServer.py
### 简述
这是一个用Python开发的简单的Web服务器，它仅能处理一个请求。

### 功能
+ 当一个客户联系时创建一个连接套接字
+ 从这个连接接收HTTP请求
+ 解释该请求以确定所请求的特定文件
+ 从服务器的文件系统获得请求的文件
+ 创建一个由请求的文件组成的HTTP响应报文，报文前面有首部行
+ 经TCP连接向请求的浏览器发送响应报文，
+ 如果浏览器请求一个在该服务器中不存在的文件，服务器返回一个“404 Not Found”差错报文

## WEBClient.py
### 简述
这是一个用python开发的Web客户端。

### 功能
+ 它能向web服务器请求一个文件
+ 并将接收到的报文和文件内容打印出来

## test.html
### 简述
这是一个测试文件，默认路径为/test.html。

## 使用说明
+ 先在一台主机上运行`WEBServer.py`，作为web服务器
+ 配置`WEBClient.py`中`"serverName"`为服务器主机的IP
+ 在另一台能和服务器主机通信的主机上运行客户端`WEBClient.py`
+ 输入`get /test.html`,即可获取到`test.html`的文件内容
# webserver-simple-python
# webserver-simple-python
