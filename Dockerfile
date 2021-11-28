FROM amazon/aws-lambda-python:3.9

# install redis-cli
RUN yum -y install wget \
	&& wget http://download.redis.io/redis-stable.tar.gz \
	&& yum -y install gzip \
	&& yum -y install tar \
	&& tar xvzf redis-stable.tar.gz \
	&& yum -y groupinstall 'Development Tools' \
	&& make -C redis-stable \
	&& cp redis-stable/src/redis-cli /usr/local/bin \
	&& rm -rf redis-stable \
	&& rm -rf redis-stable.tar.gz

COPY requirements.txt .
RUN pip3 install -r requirements.txt --target "${LAMBDA_TASK_ROOT}"

COPY lambda_function.py ${LAMBDA_TASK_ROOT}
CMD ["lambda_function.lambda_handler"]