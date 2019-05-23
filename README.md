## 大麦dota2
明天要抢门票了，简单做了个抢购脚本。

逻辑很简单，鼠标狂点开始购买，进去之后自动选择购买人，自动点击购买。

时间不够了，就不模拟http请求了，抢不到就抢不到吧。。。

## 安装

#### python +selenium

 不说了
 
#### chromedriver

下载与自己chrome对应的chromedreiver，下载之后 移动到/usr/local/bin底下

```
mv chromedriver /usr.local.bin
```

```
chromedriver -v
```
有版本信息安装成功

## 流程

进去之后扫码登陆，选到dota2页面，填好邀请码，狂点按钮就行，进去之后软件会自动下单。
