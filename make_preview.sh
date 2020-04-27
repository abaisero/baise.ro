#!/bin/sh

# create png previews of all pdfs
echo "Creating PNG previews of all PDFs"

for pdf in app/static/docs/pubs/*/*.pdf
do
  echo - $pdf
  png="$(dirname $pdf)/thumbnail.png"
  # convert $f[0] -crop 100%x70%+0+0 $filename.png

  tmp=$(tempfile)

  pdftk "$pdf" cat 1 output $tmp
  convert $tmp -background white -alpha remove -crop 100%x70%+0+0 "$png"
done
