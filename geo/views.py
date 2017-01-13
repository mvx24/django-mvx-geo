from django.contrib.gis.geoip import GeoIP
from django.http import HttpResponse
from utils.decorators import require_referer

@require_referer()
def iplocation(request):
	"""Resolves the users's remote address into a location.

	Returns with a callback and argument similar to what is expected from navigator.geolocation.getCurrentPosition()
	"""
	loc = None
	if request.META.has_key('REMOTE_ADDR'):
		loc = GeoIP().lat_lon(request.META['REMOTE_ADDR'])
	if loc:
		return HttpResponse("iplocationLoaded({'coords':{'latitude': %f, 'longitude': %f}});" % loc, content_type='text/javascript')
	else:
		return HttpResponse("iplocationLoaded(null);", content_type='text/javascript')
