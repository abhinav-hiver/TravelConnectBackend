FROM mysql/mysql-server:8.0.23
RUN echo "export PS1='\[\e[38;5;202m\]\[\e[38;5;245m\]\u\[\e[00m\]@\[\e[38;5;172m\]mysql[C]\[\e[00m\]:\[\e[38;5;5m\]\W\[\e[00m\]\\$ '" >> ~/.bashrc

# Expose the ports to host
EXPOSE 3306