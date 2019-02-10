FROM ubuntu:16.04

ENV LANG=C.UTF-8

RUN apt-get update && apt-get install -y --no-install-recommends \
    autoconf festival festlex-cmu festlex-poslex libestools1.2 unzip bzip2 \
    festvox-kallpc16k festvox-kdlpc16k festvox-rablpc16k festvox-don \
    vim && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

## set default voice for the entire image
RUN echo "(set! voice_default 'voice_rab_diphone)" >> /etc/festival.scm

WORKDIR /

# show usage
RUN echo "echo Hello world | sudo docker run --rm -i festival /usr/bin/text2wave > hello.wav"

CMD ["/bin/bash"]
