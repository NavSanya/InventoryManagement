# Inventory Management System

## Overview
This project aims to optimize inventory management by analyzing sales, purchases, and inventory data to identify overstocked and understocked items, calculate reorder points, and enhance supply chain efficiency. The project also integrates profit margin calculations and visualizations to identify the most and least profitable products. Additionally, demand forecasting is implemented using machine learning models to predict future demand based on historical sales data.

## Objectives
1. Inventory Optimization:
- Analyze inventory data to optimize stock levels and determine reorder points.
- Identify overstocked and understocked items.
- Calculate reorder points and enhance supply chain efficiency.

2. Profit Margin Analysis:
- Calculate and visualize profit margins to identify the most and least profitable products.

3. Database Integration:
- Integrate the system with a MySQL database to store and manage data efficiently.

4. Demand Forecasting:
- Implement machine learning models to predict future demand based on historical sales data.

## Data Preparation
#### Data Collection and Preparation
The following datasets are used:
- Sales Data (SalesFinal.csv)
- Purchase Data (PurchaseFinal.csv)
- Invoice Data (InvoicePurchases.csv)
- Ending Inventory (EndInvFinal.csv)
- Beginning Inventory (BegInvFinal.csv)
- Purchase Prices (2017PurchasePricesDec.csv)

Data is loaded, cleaned, and prepared for analysis. Missing values are filled, and columns are renamed for consistency. Dates are converted to datetime format.

## Inventory Analysis
- Merged beginning and ending inventory data.
- Calculated the change in inventory levels to identify overstocked and understocked items.
- Plotted the count of overstocked and understocked items.

#### Reorder Point Calculation
- Calculated the average sales quantity for each item.
- Merged sales data with inventory data.
- Calculated reorder points and identified items that need to be reordered.

#### Lead Time and Safety Stock Calculation
- Calculated average daily sales and lead times for each product.
- Calculated safety stock using maximum daily demand and standard deviation of daily demand.
- Calculated reorder points for each product.
#### Profit Margin Analysis
- Merged sales data with purchase prices.
- Calculated profit for each sale and grouped by product to get total sales and profit.
- Calculated profit margin for each product.
- Visualized the most and least profitable products.

## Database Integration
The project uses MySQL to store and manage data efficiently. The following steps were taken:

- Established a connection to the MySQL database.
- Created necessary tables to store data.
- Inserted data into the database.
Fetched and verified data from the database.

## Demand Forecasting
Implemented a machine learning model (Linear Regression) to predict future demand based on historical sales data. The following steps were taken:
- Aggregated sales quantity by date.
- Created features based on date information.
- Split data into training and testing sets.
- Trained the model and evaluated its performance.
- Predicted future sales and visualized the forecasted sales.

## Tables 

#### SalesFinal.csv
| Column Name        | Description                                                                                           |
|--------------------|-------------------------------------------------------------------------------------------------------|
| InventoryId        | A unique identifier for each inventory item.                                                          |
| Store              | The location or identifier of the store where the sale was made.                                      |
| Brand              | The brand name of the product sold.                                                                   |
| Description        | A detailed description of the product sold.                                                           |
| Size               | The size or quantity of the product (e.g., liters, grams, pieces).                                    |
| SalesQuantity      | The number of units sold.                                                                             |
| SalesDollars       | The total sales amount in dollars for the sold quantity.                                              |
| SalesPrice         | The price per unit of the product sold.                                                               |
| SalesDate          | The date on which the sale occurred.                                                                  |
| Volume             | The physical volume of the product, often used for liquid products (e.g., liters).                    |
| Classification     | The category or classification of the product, such as food, beverage, electronics, etc.              |
| ExciseTax          | The amount of excise tax applied to the product, if applicable.                                       |
| VendorNo           | A unique identifier for the vendor supplying the product.                                             |
| VendorName         | The name of the vendor supplying the product.                                                         |


#### PurchaseFinal.csv
| Column Name    | Description                                                                                          |
|----------------|------------------------------------------------------------------------------------------------------|
| InventoryId    | A unique identifier for each inventory item.                                                         |
| Store          | The location or identifier of the store receiving the purchase.                                      |
| Brand          | The brand name of the product purchased.                                                             |
| Description    | A detailed description of the product purchased.                                                     |
| Size           | The size or quantity of the product (e.g., liters, grams, pieces).                                   |
| VendorNumber   | A unique identifier for the vendor supplying the product.                                            |
| VendorName     | The name of the vendor supplying the product.                                                        |
| PONumber       | A unique identifier for the purchase order associated with the purchase.                             |
| PODate         | The date on which the purchase order was issued.                                                     |
| ReceivingDate  | The date on which the purchased goods were received.                                                 |
| InvoiceDate    | The date on which the invoice for the purchase was issued.                                           |
| PayDate        | The date on which the payment for the purchase was made.                                             |
| PurchasePrice  | The price per unit of the product purchased.                                                         |
| Quantity       | The number of units purchased.                                                                       |
| Dollars        | The total purchase amount in dollars for the purchased quantity.                                     |
| Classification | The category or classification of the product, such as food, beverage, electronics, etc.             |


#### InvoicePurchase.csv
| Column Name    | Description                                                                                          |
|----------------|------------------------------------------------------------------------------------------------------|
| VendorNumber   | A unique identifier for the vendor supplying the product.                                            |
| VendorName     | The name of the vendor supplying the product.                                                        |
| InvoiceDate    | The date on which the invoice for the purchase was issued.                                           |
| PONumber       | A unique identifier for the purchase order associated with the purchase.                             |
| PODate         | The date on which the purchase order was issued.                                                     |
| PayDate        | The date on which the payment for the purchase was made.                                             |
| Quantity       | The number of units purchased.                                                                       |
| Dollars        | The total purchase amount in dollars for the purchased quantity.                                     |
| Freight        | The cost of shipping or freight for the purchase.                                                    |
| Approval       | Indicates whether the purchase has been approved (e.g., Yes/No, Approved/Pending).                   |


#### EndInvFinal.csv
| Column Name  | Description                                                                                          |
|--------------|------------------------------------------------------------------------------------------------------|
| InventoryId  | A unique identifier for each inventory item.                                                         |
| Store        | The location or identifier of the store where the inventory is held.                                 |
| City         | The city where the store is located.                                                                 |
| Brand        | The brand name of the product in inventory.                                                          |
| Description  | A detailed description of the product in inventory.                                                  |
| Size         | The size or quantity of the product (e.g., liters, grams, pieces).                                   |
| onHand       | The quantity of the product currently in stock.                                                      |
| Price        | The current price per unit of the product.                                                           |
| endDate      | The date at which the inventory count was last updated.                                              |


#### BegInvFinal.csv
| Column Name  | Description                                                                                          |
|--------------|------------------------------------------------------------------------------------------------------|
| InventoryId  | A unique identifier for each inventory item.                                                         |
| Store        | The location or identifier of the store where the inventory is held.                                 |
| City         | The city where the store is located.                                                                 |
| Brand        | The brand name of the product in inventory.                                                          |
| Description  | A detailed description of the product in inventory.                                                  |
| Size         | The size or quantity of the product (e.g., liters, grams, pieces).                                   |
| onHand       | The quantity of the product currently in stock.                                                      |
| Price        | The current price per unit of the product.                                                           |
| startDate    | The date at which the inventory count was first recorded.                                            |


#### 2017PurchasePricesDec.csv
| Column Name     | Description                                                                                          |
|-----------------|------------------------------------------------------------------------------------------------------|
| Brand           | The brand name of the product.                                                                       |
| Description     | A detailed description of the product.                                                               |
| Price           | The current price per unit of the product.                                                           |
| Size            | The size or quantity of the product (e.g., liters, grams, pieces).                                   |
| Volume          | The physical volume of the product, often used for liquid products (e.g., liters).                   |
| Classification  | The category or classification of the product, such as food, beverage, electronics, etc.             |
| PurchasePrice   | The price per unit of the product at the time of purchase.                                           |
| VendorNumber    | A unique identifier for the vendor supplying the product.                                            |
| VendorName      | The name of the vendor supplying the product.                                                        |
