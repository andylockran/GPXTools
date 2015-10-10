import sys
from BeautifulSoup import BeautifulSoup

if len(sys.argv) >1:

  gpxfile = sys.argv[1]

  soup = BeautifulSoup(open(gpxfile))

#Strip extensions

  for extension in soup.findAll('extensions'):
      extension.decompose()

#save new soup to file
  gpxfilenew = gpxfile + "new.gpx"

  f = open(gpxfilenew, 'w')
  f.write(soup.prettify())
  f.close()

else:
  print "Please add a gpx filename as the second parameter"
