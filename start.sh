#! /bin/sh   
export PATH=$PATH:/usr/local/bin  
  
#进入.py脚本所在目录  
cd /home/pi/PythonCode/houseprice  
  
#执行.py中定义的项目example其中nohup  
nohup scrapy crawl centanet >> centanet.log 2>&1 &
nohup scrapy crawl second >> second.log 2>&1 &
