#!/bin/sh

# create png previews of all pdfs
echo "Creating PNG previews of all PDFs"

FILES=app/static/docs/pubs/*.pdf
for pdf in $FILES
do
  echo - $pdf
  png="${pdf%.*}.png"
  # convert $f[0] -crop 100%x70%+0+0 $filename.png

  tmp=$(tempfile)

  pdftk "$pdf" cat 1 output $tmp
  convert $tmp -background white -alpha remove -crop 100%x70%+0+0 "$png"
done
