# Coffee-Time
a Project using Python/Django, Django Rest Framework and MongoDB to Build a RESTful API with endpoints that return products data in JSON format for building an e-commerce mobile application

Technology Used
Python 3.8.5
Django 3.0.5
MongoDB 4.4
Django Rest Framework 3.11.0
djongo 1.3.3
django-cors-headers 3.5.0
django-filter 2.3.0

API
paths:
  /api/coffee-machines/:
    get:
      operationId: listCoffeeMachines
      description: API endpoint  return the JSON data for all coffee machines products
        filterable by product type, water line.
      parameters:
      - name: product_type
        required: false
        in: query
        description: product_type
        schema:
          type: string
      - name: water_line_compatible
        required: false
        in: query
        description: water_line_compatible
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
          description: ''
  /api/coffee-pods/:
    get:
      operationId: listCoffeePods
      description: API endpoint  return the JSON data for all the coffee pods products
        filterable by product type, coffee flavor, and pack size.
      parameters:
      - name: product_type
        required: false
        in: query
        description: product_type
        schema:
          type: string
      - name: flavor
        required: false
        in: query
        description: flavor
        schema:
          type: string
      - name: pack_size
        required: false
        in: query
        description: pack_size
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
          description: ''