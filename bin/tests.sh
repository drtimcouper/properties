#!/usr/bin/env bash

nosetests --with-coverage \
          --cover-erase --cover-html \
          --cover-package properties $1 $2
