# 使用官方 Python 镜像
FROM python:3.9-slim

# 设置工作目录
WORKDIR /app

# 将当前目录的文件复制到容器中
COPY . .

# 安装依赖
RUN pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple
RUN pip install --no-cache-dir -r requirements.txt
RUN pip 

# 暴露端口（如果有 Web 服务）
EXPOSE 8000

# 运行主 Python 程序
CMD ["python", "main.py"]
