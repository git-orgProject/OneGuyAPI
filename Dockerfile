FROM kuralabs/python3-dev:latest
MAINTAINER wdpedwin wdpedwin@163.com
WORKDIR /usr/src
RUN apt update
RUN apt install cron
RUN git clone https://github.com/git-orgProject/OneGuyAPI.git
WORKDIR /usr/src/OneGuyAPI
RUN pip3 install -r requirements.txt -i https://mirrors.aliyun.com/pypi/simple
RUN chmod +x auto_down.sh
RUN crontab auto_down.cron
CMD python3 manage.py runserver 0:8080