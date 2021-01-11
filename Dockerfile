FROM python:slim
RUN pip install flask -i https://pypi.douban.com/simple
ADD app.py ./ 
CMD ["python", "app.py"]
EXPOSE 5000
