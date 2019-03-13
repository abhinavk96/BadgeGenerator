#!/usr/bin/env bash
for i in {0..21}
do
   inkscape output$i.svg --export-text-to-path --export-pdf=output$i.pdf

done

