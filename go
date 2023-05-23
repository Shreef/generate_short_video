#!/bin/sh 


function _help()
{
    echo "";
    echo "./go [option]";
    echo " start: starts the env for this project";
    echo " install: install all needed brew and pip packages";
    echo " freeze: update requirements.txt";
    echo "";
}

function _install()
{
    _start 

    `brew install ffmpeg`;
    pip install -r requirements.txt
    # `pip install moviepy`;
    # `pip install openai-whisper`;
}

function _start()
{
    if [ -d "./env" ]
    then
        echo "Env exist"
    else
        `python3 -m venv env`
        echo "virtualenv created"
    fi 

    `source ./env/bin/activate`
}

function _freeze()
{
    `./env/bin/pip freeze > ./requirements.txt`
}



case $1 in 
"start")
    _start;;
"install")
    _install;;
"freeze")
    _freeze;;
*)
    _help;;
esac





 



