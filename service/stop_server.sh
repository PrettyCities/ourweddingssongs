#!/usr/bin/env bash
pid=`cat $HOME/ourweddingssongs/ows.pid`
kill $pid
rm $HOME/ourweddingssongs/ows.pid