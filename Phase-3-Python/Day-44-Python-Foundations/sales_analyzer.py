# Day 44 - OOP for Data Analysis
# SalesAnalyzer Class

class SalesAnalyzer:
    """
    A class to analyze sales data
    Demonstrates OOP concepts for data analytics
    """
    
    def __init__(self, sales_data):
        """
        Initialize with sales data
        sales_data: list of dicts with keys: 'date', 'product', 'quantity', 'revenue'
        """
        self.data = sales_data
    
    def total_revenue(self):
        """Calculate total revenue across all transactions"""
        return sum(item['revenue'] for item in self.data)
    
    def top_product(self):
        """Find product with highest total revenue"""
        product_revenue = {}
        for item in self.data:
            product = item['product']
            if product in product_revenue:
                product_revenue[product] += item['revenue']
            else:
                product_revenue[product] = item['revenue']
        
        top = max(product_revenue.items(), key=lambda x: x[1])
        return {"product": top[0], "revenue": top[1]}
    
    def average_order_value(self):
        """Calculate average order value"""
        total_rev = self.total_revenue()
        return total_rev / len(self.data)
    
    def filter_by_product(self, product_name):
        """Return all transactions for a specific product"""
        return [item for item in self.data if item['product'] == product_name]
    
    def summary_report(self):
        """Generate complete summary report"""
        return {
            "total_revenue": self.total_revenue(),
            "total_transactions": len(self.data),
            "average_order_value": self.average_order_value(),
            "top_product": self.top_product()
        }


# Test the class
if __name__ == "__main__":
    # Sample data
    sales = [
        {"date": "2025-01-01", "product": "Laptop", "quantity": 2, "revenue": 80000},
        {"date": "2025-01-02", "product": "Mouse", "quantity": 15, "revenue": 7500},
        {"date": "2025-01-03", "product": "Laptop", "quantity": 1, "revenue": 40000},
        {"date": "2025-01-04", "product": "Keyboard", "quantity": 8, "revenue": 12000}
    ]
    
    # Create analyzer
    analyzer = SalesAnalyzer(sales)
    
    # Test all methods
    print("="*60)
    print("SALES ANALYZER - TEST RESULTS")
    print("="*60)
    
    print(f"\nTotal Revenue: Rs.{analyzer.total_revenue():,}")
    print(f"Average Order Value: Rs.{analyzer.average_order_value():,.2f}")
    print(f"\nTop Product: {analyzer.top_product()}")
    
    print(f"\nLaptop Transactions:")
    laptop_sales = analyzer.filter_by_product("Laptop")
    for sale in laptop_sales:
        print(f"  {sale['date']}: {sale['quantity']} units - Rs.{sale['revenue']:,}")
    
    print(f"\n{'='*60}")
    print("SUMMARY REPORT")
    print("="*60)
    summary = analyzer.summary_report()
    for key, value in summary.items():
        print(f"{key}: {value}")