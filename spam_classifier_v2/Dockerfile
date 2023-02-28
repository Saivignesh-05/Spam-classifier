FROM python:3.10-slim-buster

# WORKDIR ./app
COPY requirments.txt .  

EXPOSE 8501
# RUN apt-get update -y && apt-get install -y --no-install-recommends apt-utils
# -y puts yes when asked 

#using the buildkit to utilize cache
RUN --mount=type=cache,target=/root/.cache \
    pip install -r ./requirments.txt        

COPY . .

ENTRYPOINT [ "streamlit","run"]

CMD ["./App.py", "--server.address=0.0.0.0"]

# check 10.110.30.105
# --server.address=0.0.0.0 lets it access for others in web using your server!