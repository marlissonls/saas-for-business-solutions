#!/bin/bash

if [ ! -d "venv" ]; then
    virtualenv venv
fi

source venv/Scripts/activate