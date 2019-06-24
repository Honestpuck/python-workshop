#!/bin/bash

pandoc -t revealjs slides.md -f markdown+pipe_tables --slide-level=3 -s -o index.html \
    -V theme=white \
    -V parallaxBackgroundImage="XW19-empty.png" \
    -V parallaxBackgroundSize="1920px 1080px" \
    -V parrallaxBackgroundHorizontal="0" \
    -V parrallaxBackgroundVertical="0"

