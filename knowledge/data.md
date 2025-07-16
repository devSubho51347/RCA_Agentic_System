# Data Schemas

## orders
| column | type | description |
|--------|------|-------------|
| order_id | int | unique order identifier |
| user_id | int | customer identifier |
| product_id | int | SKU identifier |
| department | string | product department |
| order_date | date | order timestamp |
| reorder_status | int | 1=reordered, 0=first time |

Primary key: `order_id`
Foreign keys: `user_id`, `product_id`

## products
| column | type | description |
|--------|------|-------------|
| product_id | int | SKU identifier |
| product_name | string | product title |
| category | string | category label |
| department | string | department label |
| price | float | retail price |

Primary key: `product_id`

## Join Keys
`orders.product_id` ↔ `products.product_id`
