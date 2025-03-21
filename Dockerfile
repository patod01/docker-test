### actual sh1t ###
FROM python:3.13.1-alpine3.21 AS pydep

ENV PATH="/server/.venv/bin:$PATH"
ENV VIRTUAL_ENV="/server/.venv"

WORKDIR /server
RUN python -m venv .venv
# RUN python -m pip install --upgrade pip
RUN pip install bottle


### actual sh2t ###
FROM python:3.13.1-alpine3.21

ENV MODE="dev"
ENV PORT="10001"
ENV TZ="America/Santiago"

WORKDIR /server/app
COPY --from=pydep /server/.venv ../.venv
COPY ./src .

CMD source ../.venv/bin/activate && python rock.py $MODE $PORT
