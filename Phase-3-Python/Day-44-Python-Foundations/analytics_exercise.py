# Day 44 - Analytics Thinking Exercise
# E-commerce Order Analysis

orders = [
    {"order_id": 1, "customer": "A", "amount": 1200, "status": "Delivered"},
    {"order_id": 2, "customer": "B", "amount": 800, "status": "Cancelled"},
    {"order_id": 3, "customer": "A", "amount": 1500, "status": "Delivered"},
    {"order_id": 4, "customer": "C", "amount": 2000, "status": "Delivered"},
    {"order_id": 5, "customer": "B", "amount": 600, "status": "Delivered"},
    {"order_id": 6, "customer": "A", "amount": 900, "status": "Cancelled"}
]

print("="*60)
print("E-COMMERCE ORDER ANALYSIS")
print("="*60)

# Question 1: Total delivered revenue
delivered_orders = [order for order in orders if order["status"] == "Delivered"]
total_delivered_revenue = sum(order["amount"] for order in delivered_orders)
print(f"\n1. Total Delivered Revenue: Rs.{total_delivered_revenue:,}")

# Question 2: Cancellation rate
total_orders = len(orders)
cancelled_orders = len([o for o in orders if o["status"] == "Cancelled"])
cancellation_rate = (cancelled_orders / total_orders) * 100
print(f"2. Cancellation Rate: {cancellation_rate:.1f}% ({cancelled_orders}/{total_orders} orders)")

# Question 3: Customer with highest spend (delivered only)
customer_spend = {}
for order in delivered_orders:
    customer = order["customer"]
    if customer in customer_spend:
        customer_spend[customer] += order["amount"]
    else:
        customer_spend[customer] = order["amount"]

top_customer = max(customer_spend.items(), key=lambda x: x[1])
print(f"3. Top Customer: {top_customer[0]} - Rs.{top_customer[1]:,}")

# Question 4: Average order value (delivered only)
avg_order_value = total_delivered_revenue / len(delivered_orders)
print(f"4. Average Order Value (Delivered): Rs.{avg_order_value:,.2f}")

# Question 5: Customer summary
customer_summary = {}
for order in orders:
    customer = order["customer"]
    if customer not in customer_summary:
        customer_summary[customer] = {
            "orders": 0,
            "revenue": 0,
            "delivered_orders": 0
        }
    
    customer_summary[customer]["orders"] += 1
    if order["status"] == "Delivered":
        customer_summary[customer]["revenue"] += order["amount"]
        customer_summary[customer]["delivered_orders"] += 1

# Calculate average order value per customer
for customer in customer_summary:
    delivered_count = customer_summary[customer]["delivered_orders"]
    if delivered_count > 0:
        customer_summary[customer]["avg_order"] = customer_summary[customer]["revenue"] / delivered_count
    else:
        customer_summary[customer]["avg_order"] = 0

print("\n5. Customer Summary:")
print("-" * 60)
for customer, stats in customer_summary.items():
    print(f"\nCustomer {customer}:")
    print(f"  Total Orders: {stats['orders']}")
    print(f"  Delivered Orders: {stats['delivered_orders']}")
    print(f"  Total Revenue: Rs.{stats['revenue']:,}")
    print(f"  Avg Order Value: Rs.{stats['avg_order']:,.2f}")

print("\n" + "="*60)
print("ANALYSIS COMPLETE ✅")
print("="*60)s