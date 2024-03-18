import requests
from django.conf import settings
from django.http import JsonResponse

from .serializers import TokenDataSerializer

def get_token(request):
  try:
    code = request.GET.get('code')
  except KeyError:
    return JsonResponse({'error': 'No strava code provided. Try logging again'}, status=400)

  token_url = 'https://www.strava.com/api/v3/oauth/token'

  data = {
      'grant_type': 'authorization_code',
      'code': code,
      'client_id': settings.OAUTH_CLIENT_ID,
      'client_secret': settings.OAUTH_CLIENT_SECRET,
  }
  try:
    response = requests.post(token_url, data=data)
    response.raise_for_status()  # Check for any HTTP errors
  except requests.exceptions.RequestException as e:
    return JsonResponse({'error': 'Strava server error' + str(e)}, status=500)
  except Exception as e:
    return JsonResponse({'error': 'An error occurred during the request to the Strava Server'}, status=500)

  return JsonResponse(response.json(), status=201)
  # Save the token to the user's profile in the database
  # serializer = TokenDataSerializer(data=response.json())

  # if serializer.is_valid():
  #   serializer.save()
  #   return JsonResponse(serializer.data, status=201)
  # else:
  #   return JsonResponse(serializer.errors, status=400)
