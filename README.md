# Shopping-cart-API
A simple shopping cart API using Python and MongoDB
The API can add a product, show all products, delete a product and update a product details.
It was tesed using Postman.

# To test the API:
- Download Postman from https://www.postman.com/downloads/
Run the src.py python script and note the local host URL on which it gets hosted. We will refer it as URL here (usually it is http://127.0.0.1:5000/)
Now, for testing the various CRUD operations.

### For adding a product
- Open Postman and open a new request
- Type the URL:/add and select POST from the dropdown button beside the "Enter request URL"
- Now, click on "Body" and select JSON from the right most tab below it.
- Type your product details in the format { "name" : <product_name>, "quantity" : <product_quantity> }
- E.g.: { "name" : "Carrot", "quantity" : 3 }
- Click on Send button.
- On successful addition, "Product added succesfully" will be printed.

### For viewing all products
- Follow the same procedure for adding, with the url as URL:/products
- Select GET from the dropdown button and click on Send button.
- All the products will be displayed in JSON format.

### For deleting a product
- Select the url as URL:/delete/<product name> 
- E.g.: URL:/delete/Carrot
- Select DELETE from the dropdown button and click on Send
- On successful deletion, "Product deleted successfully" will be displayed
  

