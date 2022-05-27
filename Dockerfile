FROM public.ecr.aws/i7t6p8u9/ubuntu-20.04-python3.8:latest
RUN apt-get update

RUN pip install --upgrade pip \
  && pip install awscli
RUN echo "export PS1='\[\e[38;5;202m\]\[\e[38;5;245m\]\u\[\e[00m\]@\[\e[38;5;172m\]backend[C]\[\e[00m\]:\[\e[38;5;5m\]\W\[\e[00m\]\\$ '" >> ~/.bashrc
# RUN apt-get install vim curl -y
RUN pip install poetry

COPY ./ /usr/src/backend
WORKDIR /usr/src/backend

RUN poetry install
EXPOSE 80

# CMD [ ".venv/bin/hypercorn", "src.main:app", "--bind", "0.0.0.0:80" ]
RUN chmod +x /usr/src/backend/start.sh
ENTRYPOINT ["/usr/src/backend/start.sh"]
