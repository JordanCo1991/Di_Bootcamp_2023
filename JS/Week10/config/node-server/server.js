const express = require("express");
const { products } = require("./config/data.js");
console.log(products);
const app = express();

app.listen(3001, () => {
  console.log(`server is listneing on port 3001`);
});

// CRUD - Create - Read - Update - Delete
// Create - POST
// Read - GET
// Update - PUT
// Delete - DELETE

// CREATE - POST - create a product {"name": "Ikey", "price": 900}
app.post('/api/products', (req, res) => {
    console.log(req.body);
    res.send('OK POST');
})

app.get("/api/products", (req, res) => {
  res.json(products);
});

// GET - get one product with id
app.get("/api/products/:product_id", (req, res) => {
  console.log(req.params);
  const productid = req.params.product_id;

  const product = products.find((item) => item.id == productid);
  if (!product) return res.status(404).json({ msg: "Product not found" });
  res.json(product);
});

// Read - GET searche a product with query ?name=ip
app.get("/api/search", (req, res) => {
  console.log(req.query);
  const name = req.query.name;
  const filtered = products.filter((item) => {
    return item.name.toLowerCase().includes(name.toLowerCase());
  });
  if(filtered.length === 0) {
    return res.status(404).json({msg:'No product matched your search!!!'})
  }
  res.json(filtered);
});