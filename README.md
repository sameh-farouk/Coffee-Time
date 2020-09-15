# Coffee-Time
a Project using Python/Django, Django Rest Framework and MongoDB to Build a **RESTful API** with endpoints that return products data in JSON format for Consuming by un e-commerce mobile application.

### live demo with browsable API:
Please check the link to instance of the web service deployed on **Heroku** and configured with a **MongoDB Atlas**, a Cloud-hosted MongoDB service.
***[https://coffeetime-api.herokuapp.com](https://coffeetime-api.herokuapp.com)***

Visiting the url will display human-friendly HTML output discribe each resource available with **browsable and clickable urls** for easy API browsing by humans.

The browsable API ensures that all the endpoints you create in your API are able to respond both with machine readable (in JSON) and human readable (in HTML) representations.

By default, the API will return the format specified by the headers, which in the case of the browser is HTML. The format can be specified using `?format=` in the request, so you can look at the raw JSON response in a browser by adding `?format=json` to the URL.


### Technology Used

- Python 3.8.5
- Django 3.0.5
- MongoDB 4.4
- Django Rest Framework 3.11.0
- djongo 1.3.3
- django-cors-headers 3.5.0
- django-filter 2.3.0
- Git 2.27

### API
#### paths:
#####  /api/coffee-machines/:
    get:
      operationId: listCoffeeMachines
      description: API endpoint  return the JSON data for all coffee machines products
        filterable by product type, water line.
      parameters:
      - name: product_type__name
        required: false
        in: query
        description: cofffee machine product type could be one of (COFFEE_MACHINE_LARGE, COFFEE_MACHINE_SMALL, ESPRESSO_MACHINE)
        schema:
          type: string
      - name: water_line_compatible
        required: false
        in: query
        description: whether the machine compatible with the water line or no (True, False)
        schema:
          type: string
      responses:
        '200':
          content:
            application/json:
              schema:
                type: array
                items:
                  properties:
                    sku:
                      type: string
                      maxLength: 50
                  required:
                  - sku
          description: 'the response contains array of product's sku'
#####  /api/coffee-pods/:
    get:
      operationId: listCoffeePods
      description: API endpoint  return the JSON data for all the coffee pods products
        filterable by product type, coffee flavor, and pack size.
      parameters:
      - name: product_type__name
        required: false
        in: query
        description: cofffee machine product type could be one of (COFFEE_POD_LARGE, COFFEE_POD_SMALL, ESPRESSO_POD)
        schema:
          type: string
      - name: flavor__name
        required: false
        in: query
        description: coffe pod flavor could be one of (COFFEE_FLAVOR_VANILLA, COFFEE_FLAVOR_CARAMEL, COFFEE_FLAVOR_PSL, COFFEE_FLAVOR_MOCHA, COFFEE_FLAVOR_HAZELNUT)
        schema:
          type: string
      - name: pack_size__dozen
        required: false
        in: query
        description: pack size by dozen could be one of (1, 3 , 5 , 7)
        schema:
          type: string
      responses:
        '200':
          content:
            application/json:
              schema:
                type: array
                items:
                  properties:
                    sku:
                      type: string
                      maxLength: 50
                  required:
                  - sku
          description: 'the response contains array of product's sku'
          
### Examples:

- All large machines:
  - [GET /api/coffee-machines/?product_type__name=COFFEE_MACHINE_LARGE](https://coffeetime-api.herokuapp.com/api/coffee-machines/?format=json&product_type__name=COFFEE_MACHINE_LARGE)
  
 - All large pods:
   - [GET /api/coffee-pods/?product_type__name=COFFEE_POD_LARGE](https://coffeetime-api.herokuapp.com/api/coffee-pods/?format=json&product_type__name=COFFEE_POD_LARGE)
   
 - All espresso vanilla pods:
   - [GET /api/coffee-pods/?product_type__name=ESPRESSO_POD&flavor__name=COFFEE_FLAVOR_VANILLA](https://coffeetime-api.herokuapp.com/api/coffee-pods/?flavor__name=COFFEE_FLAVOR_VANILLA&format=json&product_type__name=ESPRESSO_POD)
 
 - All espresso machines:
   - [GET /api/coffee-machines/?product_type__name=ESPRESSO_MACHINE](https://coffeetime-api.herokuapp.com/api/coffee-machines/?format=json&product_type__name=ESPRESSO_MACHINE)
 
 - All small pods:
   - [GET /api/coffee-pods/?product_type__name=COFFEE_POD_SMALL](https://coffeetime-api.herokuapp.com/api/coffee-pods/?format=json&product_type__name=COFFEE_POD_SMALL)
 
 - All pods sold in 7 dozen packs:
   - [GET /api/coffee-pods/?pack_size__dozen=7](https://coffeetime-api.herokuapp.com/api/coffee-pods/?format=json&pack_size__dozen=7)
