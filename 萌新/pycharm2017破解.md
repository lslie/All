.Ubuntu16.04及以上版本：
1，安装专业版：在终端中输入#sudo snap install pycharm-professional --classic
2，安装轻量级：sudo snap install pycharm-community --classic
其他版本的Linux：
官网下载PyCharm，官网提供付费版和免费版：https ://www.jetbrains.com/pycharm/
下载好的是tr.gz压缩包，自行解压到软件安装目录中（随便一个目录）
解压方法：
1，右键菜单解压压缩文件安装包
2，在压缩文件安装包文件夹下打开终端输入 sudo tar -zxvf压缩文件名.tar.gz /目标文件夹
进入解压后的文件夹/ bin在bin文件夹中打开终端输入 sh ./pycharm.sh （这种方式打开PyCharm时若关闭终端则会杀掉Pycharm进程）
此后若想运行PyCharm则执行上一步即可。若想一劳永逸请看下一步
制作PyCharm启动快捷方式
使用以下命令创建快捷方式
1、在终端输入 sudo gedit /usr/share/applications/Pycharm.desktop （若出现无法建立desktop的错误将gedit换为vim编辑器）
2、 然后在创建好的Pycharm.desktop中输入以下代码（注意代码中的Exec和Icon部分替换为正确的路径）：
[Desktop Entry]
Type=Application
Name=Pycharm
GenericName=Pycharm3
Comment=Pycharm3:The Python IDE
Exec="/home/snakeson/developer/pycharm-community-2017.2.3/bin/pycharm.sh" %f
Icon=/home/snakeson/developer/pycharm-community-2017.2.3/bin/pycharm.png
Terminal=pycharm
Categories=Pycharm; 
在启动器中搜索Pycharm，启动即可。若搜索不到在/ usr / share / applications文件夹中找到Pycharm.desktop复制到桌面
1、修改hosts文件：

添加下面一行到hosts文件，目的是屏蔽掉Pycharm对激活码的验证，将0.0.0.0 account.jetbrains.com复制到hosts文件的最下面，保存之后关闭hosts  

windows系统hosts文件路径为：C:\Windows\System32\drivers\etc

linux和mac的hosts文件路径为：/etc

 

2、选择Activation code，复制下方激活码到输入框

D87IQPUU3Q-eyJsaWNlbnNlSWQiOiJEODdJUVBVVTNRIiwibGljZW5zZWVOYW1lIjoiTnNzIEltIiwiYXNzaWduZWVOYW1lIjoiIiwiYXNzaWduZWVFbWFpbCI6IiIsImxpY2Vuc2VSZXN0cmljdGlvbiI6IkZvciBlZHVjYXRpb25hbCB1c2Ugb25seSIsImNoZWNrQ29uY3VycmVudFVzZSI6ZmFsc2UsInByb2R1Y3RzIjpbeyJjb2RlIjoiSUkiLCJwYWlkVXBUbyI6IjIwMTktMDItMDcifSx7ImNvZGUiOiJSUzAiLCJwYWlkVXBUbyI6IjIwMTktMDItMDcifSx7ImNvZGUiOiJXUyIsInBhaWRVcFRvIjoiMjAxOS0wMi0wNyJ9LHsiY29kZSI6IlJEIiwicGFpZFVwVG8iOiIyMDE5LTAyLTA3In0seyJjb2RlIjoiUkMiLCJwYWlkVXBUbyI6IjIwMTktMDItMDcifSx7ImNvZGUiOiJEQyIsInBhaWRVcFRvIjoiMjAxOS0wMi0wNyJ9LHsiY29kZSI6IkRCIiwicGFpZFVwVG8iOiIyMDE5LTAyLTA3In0seyJjb2RlIjoiUk0iLCJwYWlkVXBUbyI6IjIwMTktMDItMDcifSx7ImNvZGUiOiJETSIsInBhaWRVcFRvIjoiMjAxOS0wMi0wNyJ9LHsiY29kZSI6IkFDIiwicGFpZFVwVG8iOiIyMDE5LTAyLTA3In0seyJjb2RlIjoiRFBOIiwicGFpZFVwVG8iOiIyMDE5LTAyLTA3In0seyJjb2RlIjoiR08iLCJwYWlkVXBUbyI6IjIwMTktMDItMDcifSx7ImNvZGUiOiJQUyIsInBhaWRVcFRvIjoiMjAxOS0wMi0wNyJ9LHsiY29kZSI6IkNMIiwicGFpZFVwVG8iOiIyMDE5LTAyLTA3In0seyJjb2RlIjoiUEMiLCJwYWlkVXBUbyI6IjIwMTktMDItMDcifSx7ImNvZGUiOiJSU1UiLCJwYWlkVXBUbyI6IjIwMTktMDItMDcifV0sImhhc2giOiI4MDI4NjgyLzAiLCJncmFjZVBlcmlvZERheXMiOjAsImF1dG9Qcm9sb25nYXRlZCI6ZmFsc2UsImlzQXV0b1Byb2xvbmdhdGVkIjpmYWxzZX0=-iPLvfrIl0qTga/F9rnjf0Sz6yYvw+2FWgZpcLOFbvb3CllsE2ui4+bw8emxzcYr3GyxN4/4BhfcX6gmmI4EJaTSihP+m4Oa8jZApb5zGEHENJE+I8hewQWIyiekNE7+21meJ3swPCYiTWKkUXMIVUWNfieZhqHd96dHpD335dSRCmAImgQ31qpmzemMxztu1/FAIiaUrav1VU/M0waj9B9xuhDG77PU7deSxX363RQjbmRdWBorjH6gSyUpCXnyh6Crlhtj+lC+VndAdnT4HUXXsmpCw6uLotL5Gv/TM7/fAqIjSQghlnm4vpss4Pc7xI9n07KwQE9ok4fuF3HMRUA==-MIIEPjCCAiagAwIBAgIBBTANBgkqhkiG9w0BAQsFADAYMRYwFAYDVQQDDA1KZXRQcm9maWxlIENBMB4XDTE1MTEwMjA4MjE0OFoXDTE4MTEwMTA4MjE0OFowETEPMA0GA1UEAwwGcHJvZDN5MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAxcQkq+zdxlR2mmRYBPzGbUNdMN6OaXiXzxIWtMEkrJMO/5oUfQJbLLuMSMK0QHFmaI37WShyxZcfRCidwXjot4zmNBKnlyHodDij/78TmVqFl8nOeD5+07B8VEaIu7c3E1N+e1doC6wht4I4+IEmtsPAdoaj5WCQVQbrI8KeT8M9VcBIWX7fD0fhexfg3ZRt0xqwMcXGNp3DdJHiO0rCdU+Itv7EmtnSVq9jBG1usMSFvMowR25mju2JcPFp1+I4ZI+FqgR8gyG8oiNDyNEoAbsR3lOpI7grUYSvkB/xVy/VoklPCK2h0f0GJxFjnye8NT1PAywoyl7RmiAVRE/EKwIDAQABo4GZMIGWMAkGA1UdEwQCMAAwHQYDVR0OBBYEFGEpG9oZGcfLMGNBkY7SgHiMGgTcMEgGA1UdIwRBMD+AFKOetkhnQhI2Qb1t4Lm0oFKLl/GzoRykGjAYMRYwFAYDVQQDDA1KZXRQcm9maWxlIENBggkA0myxg7KDeeEwEwYDVR0lBAwwCgYIKwYBBQUHAwEwCwYDVR0PBAQDAgWgMA0GCSqGSIb3DQEBCwUAA4ICAQC9WZuYgQedSuOc5TOUSrRigMw4/+wuC5EtZBfvdl4HT/8vzMW/oUlIP4YCvA0XKyBaCJ2iX+ZCDKoPfiYXiaSiH+HxAPV6J79vvouxKrWg2XV6ShFtPLP+0gPdGq3x9R3+kJbmAm8w+FOdlWqAfJrLvpzMGNeDU14YGXiZ9bVzmIQbwrBA+c/F4tlK/DV07dsNExihqFoibnqDiVNTGombaU2dDup2gwKdL81ua8EIcGNExHe82kjF4zwfadHk3bQVvbfdAwxcDy4xBjs3L4raPLU3yenSzr/OEur1+jfOxnQSmEcMXKXgrAQ9U55gwjcOFKrgOxEdek/Sk1VfOjvS+nuM4eyEruFMfaZHzoQiuw4IqgGc45ohFH0UUyjYcuFxxDSU9lMCv8qdHKm+wnPRb0l9l5vXsCBDuhAGYD6ss+Ga+aDY6f/qXZuUCEUOH3QUNbbCUlviSz6+GiRnt1kA9N2Qachl+2yBfaqUqr8h7Z2gsx5LcIf5kYNsqJ0GavXTVyWh7PYiKX4bs354ZQLUwwa/cG++2+wNWP+HtBhVxMRNTdVhSm38AknZlD+PTAsWGu9GyLmhti2EnVwGybSD2Dxmhxk3IPCkhKAK+pl0eWYGZWG3tJ9mZ7SowcXLWDFAk0lRJnKGFMTggrWjV8GYpw5bq23VmIqqDLgkNzuoog==
