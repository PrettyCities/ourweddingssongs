#!/usr/bin/env bash
cd $HOME/ourweddingssongs
gunicorn -b 0.0.0.0:8000 service.app --reload --log-file=$HOME/log &
echo $! > ows.pid