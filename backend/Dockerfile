FROM python

EXPOSE 8008

ARG USERNAME=sammiee5311
ARG USER_UID=1000
ARG USER_GID=$USER_UID

RUN groupadd --gid $USER_GID $USERNAME \
    && useradd --uid $USER_UID --gid $USER_GID -m $USERNAME

WORKDIR /app

USER $USERNAME 

COPY requirements_dev.txt ./

RUN python3 -m pip install flit

COPY . ./

RUN python3 -m flit install