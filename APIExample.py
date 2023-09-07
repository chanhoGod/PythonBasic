# API
# Application Programming Interface
# API is the acronym for Application Programming Interface, which is a software intermediary that allows two applications to talk to each other. Each time you use an app like Facebook, send an instant message, or check the weather on your phone, you’re using an API.

# example today
# http://open-notify.org/Open-Notify-API/ISS-Location-Now/

import requests  ##API를 호출하여 JSON으로 데이터를 받아올때 사용하는 라이브러리

response = requests.get(url="http://api.open-notify.org/iss-now.json")
print(response)

if response.status_code != 200:
    raise Exception("Error from server")

response.raise_for_status()

payload = response.json()

print(payload)
print(payload["iss_position"]["longitude"])

# What is response status code?
# 1XX : Informational responses
# 2XX : Successful responses
# 3XX: Redirection messages
# 4XX : Client error responses
# 5xx : Server error responses

# 200 OK
# The request succeeded. The result meaning of "success" depends on the HTTP method:

# 403 Forbidden
# The client does not have access rights to the content; that is, it is unauthorized, so the server is refusing to give the requested resource. Unlike 401 Unauthorized, the client's identity is known to the server.

# 404 Not Found
# The server can not find the requested resource. In the browser, this means the URL is not recognized. In an API, this can also mean that the endpoint is valid but the resource itself does not exist. Servers may also send this response instead of 403 Forbidden to hide the existence of a resource from an unauthorized client. This response code is probably the most well known due to its frequent occurrence on the web.

# 503 Service Unavailable
# The server is not ready to handle the request. Common causes are a server that is down for maintenance or that is overloaded. Note that together with this response, a user-friendly page explaining the problem should be sent. This response should be used for temporary conditions and the Retry-After HTTP header should, if possible, contain the estimated time before the recovery of the service. The webmaster must also take care about the caching-related headers that are sent along with this response, as these temporary condition responses should usually not be cached.

# 504 Gateway Timeout
# This error response is given when the server is acting as a gateway and cannot get a response in time.