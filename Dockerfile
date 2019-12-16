FROM mysql:5.7

ENV MYSQL_ALLOW_EMPTY_PASSWORD yes

# 复制文件到容器中，要复制的文件有：启动脚本和sql文件
COPY setup.sh /mysql/setup.sh
COPY data.sql /mysql/data.sql
#COPY privileges.sql /mysql/privileges.sql
# 容器启动命令启动脚本
CMD ["sh", "/mysql/setup.sh"]

CMD ["mysqld"]