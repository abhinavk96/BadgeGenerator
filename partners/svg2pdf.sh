#!/usr/bin/env bash
for i in {0..20}
do
   inkscape output$i.svg --export-text-to-path --export-pdf=output$i.pdf

done

