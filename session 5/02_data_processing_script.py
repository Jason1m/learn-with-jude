# Session 5: Data Processing Script - Automated Analysis

print("=" * 60)
print("BUILDING AN AUTOMATED DATA PROCESSING SCRIPT")
print("=" * 60)

print("Let's build a comprehensive data processing system!")
print("We'll automate analysis tasks that would take hours manually.")

# STEP 1: Basic Data Processing
print("\n" + "="*50)
print("STEP 1: BASIC DATA PROCESSING")
print("="*50)

def process_basic_list():
    """Process a simple list of numbers"""
    numbers = [23, 45, 67, 12, 89, 34, 56, 78, 91, 25]
    
    print(f"Original data: {numbers}")
    print(f"Total items: {len(numbers)}")
    
    # Calculate statistics
    total = 0
    for number in numbers:
        total += number
    
    average = total / len(numbers)
    
    print(f"Sum: {total}")
    print(f"Average: {average:.2f}")
    
    # Find min and max
    minimum = numbers[0]
    maximum = numbers[0]
    
    for number in numbers:
        if number < minimum:
            minimum = number
        if number > maximum:
            maximum = number
    
    print(f"Minimum: {minimum}")
    print(f"Maximum: {maximum}")
    
    return {"total": total, "average": average, "min": minimum, "max": maximum}

print("Testing basic data processing:")
process_basic_list()

# STEP 2: Student Grade Analysis System
print("\n" + "="*50)
print("STEP 2: STUDENT GRADE ANALYSIS SYSTEM")
print("="*50)

def analyze_student_grades():
    """Comprehensive grade analysis system"""
    
    # Sample student data
    students = [
        {"name": "Alice Johnson", "grades": [92, 88, 94, 87, 91]},
        {"name": "Bob Smith", "grades": [78, 82, 79, 85, 80]},
        {"name": "Charlie Brown", "grades": [95, 93, 97, 94, 96]},
        {"name": "Diana Prince", "grades": [65, 70, 68, 72, 69]},
        {"name": "Eve Wilson", "grades": [88, 90, 85, 92, 89]},
        {"name": "Frank Miller", "grades": [82, 84, 80, 86, 83]},
        {"name": "Grace Lee", "grades": [97, 95, 98, 96, 94]},
        {"name": "Henry Davis", "grades": [73, 75, 71, 77, 74]}
    ]
    
    print("🎓 STUDENT GRADE ANALYSIS REPORT")
    print("=" * 45)
    
    class_totals = []
    honor_roll = []
    at_risk = []
    
    # Process each student
    for student in students:
        name = student["name"]
        grades = student["grades"]
        
        # Calculate student statistics
        total_points = 0
        for grade in grades:
            total_points += grade
        
        average = total_points / len(grades)
        class_totals.append(average)
        
        # Determine letter grade
        if average >= 90:
            letter_grade = "A"
            honor_roll.append(name)
        elif average >= 80:
            letter_grade = "B"
        elif average >= 70:
            letter_grade = "C"
        elif average >= 60:
            letter_grade = "D"
        else:
            letter_grade = "F"
            at_risk.append(name)
        
        # Find highest and lowest grades
        highest = grades[0]
        lowest = grades[0]
        
        for grade in grades:
            if grade > highest:
                highest = grade
            if grade < lowest:
                lowest = grade
        
        # Print individual report
        print(f"{name:<15}: {average:5.1f}% ({letter_grade}) [H:{highest} L:{lowest}]")
    
    # Class statistics
    print("\n📊 CLASS STATISTICS")
    print("-" * 25)
    
    class_total = 0
    for avg in class_totals:
        class_total += avg
    
    class_average = class_total / len(class_totals)
    
    print(f"Class Average: {class_average:.1f}%")
    print(f"Total Students: {len(students)}")
    print(f"Honor Roll: {len(honor_roll)} students")
    print(f"At Risk: {len(at_risk)} students")
    
    if honor_roll:
        print(f"\n🌟 Honor Roll Students:")
        for student in honor_roll:
            print(f"  • {student}")
    
    if at_risk:
        print(f"\n⚠️  Students Needing Support:")
        for student in at_risk:
            print(f"  • {student}")

analyze_student_grades()

# STEP 3: Sales Data Processing
print("\n" + "="*50)
print("STEP 3: SALES DATA PROCESSING")
print("="*50)

def process_sales_data():
    """Process and analyze sales data"""
    
    sales_data = [
        {"product": "Laptop", "price": 999.99, "quantity": 5, "category": "Electronics"},
        {"product": "Mouse", "price": 29.99, "quantity": 25, "category": "Electronics"},
        {"product": "Desk Chair", "price": 199.99, "quantity": 8, "category": "Furniture"},
        {"product": "Monitor", "price": 299.99, "quantity": 12, "category": "Electronics"},
        {"product": "Keyboard", "price": 79.99, "quantity": 18, "category": "Electronics"},
        {"product": "Desk Lamp", "price": 49.99, "quantity": 15, "category": "Furniture"},
        {"product": "Notebook", "price": 12.99, "quantity": 50, "category": "Office Supplies"},
        {"product": "Pen Set", "price": 24.99, "quantity": 30, "category": "Office Supplies"},
        {"product": "Coffee Mug", "price": 15.99, "quantity": 40, "category": "Office Supplies"},
        {"product": "Bookshelf", "price": 149.99, "quantity": 6, "category": "Furniture"}
    ]
    
    print("💰 SALES DATA ANALYSIS")
    print("=" * 30)
    
    # Initialize tracking variables
    total_revenue = 0
    category_sales = {}
    high_value_items = []
    low_stock_items = []
    
    # Process each sale
    for item in sales_data:
        product = item["product"]
        price = item["price"]
        quantity = item["quantity"]
        category = item["category"]
        
        # Calculate revenue for this item
        item_revenue = price * quantity
        total_revenue += item_revenue
        
        # Track sales by category
        if category in category_sales:
            category_sales[category] += item_revenue
        else:
            category_sales[category] = item_revenue
        
        # Identify high-value items (>$200 each)
        if price > 200:
            high_value_items.append(product)
        
        # Identify low stock items (<10 units)
        if quantity < 10:
            low_stock_items.append(product)
        
        # Print item details
        print(f"{product:<12}: ${price:>7.2f} × {quantity:>2} = ${item_revenue:>8.2f}")
    
    print("-" * 30)
    print(f"Total Revenue: ${total_revenue:,.2f}")
    
    # Category breakdown
    print(f"\n📈 SALES BY CATEGORY")
    print("-" * 25)
    for category, revenue in category_sales.items():
        percentage = (revenue / total_revenue) * 100
        print(f"{category:<15}: ${revenue:>8,.2f} ({percentage:4.1f}%)")
    
    # Alerts and recommendations
    print(f"\n🔍 INSIGHTS & ALERTS")
    print("-" * 25)
    
    if high_value_items:
        print(f"💎 Premium Items: {', '.join(high_value_items)}")
    
    if low_stock_items:
        print(f"⚠️  Low Stock Alert: {', '.join(low_stock_items)}")
    
    # Find best selling category
    best_category = ""
    highest_sales = 0
    for category, sales in category_sales.items():
        if sales > highest_sales:
            highest_sales = sales
            best_category = category
    
    print(f"🎯 Top Category: {best_category} (${highest_sales:,.2f})")

process_sales_data()

# STEP 4: Text Analysis Engine
print("\n" + "="*50)
print("STEP 4: TEXT ANALYSIS ENGINE")
print("="*50)

def analyze_text_data():
    """Analyze text data for insights"""
    
    customer_reviews = [
        "This product is absolutely amazing! Great quality and fast shipping.",
        "Not satisfied with the purchase. Poor quality materials.",
        "Excellent customer service. Very happy with my order.",
        "The item arrived damaged. Disappointed with the packaging.",
        "Outstanding value for money. Highly recommend this product.",
        "Slow delivery but good product quality overall.",
        "Perfect! Exactly what I was looking for. Great job!",
        "Could be better. Average quality for the price.",
        "Fantastic experience! Will definitely buy again.",
        "Not worth the money. Found better alternatives elsewhere."
    ]
    
    print("📝 CUSTOMER REVIEW ANALYSIS")
    print("=" * 35)
    
    # Analysis tracking
    positive_words = ["amazing", "great", "excellent", "outstanding", "perfect", "fantastic", "happy", "recommend"]
    negative_words = ["poor", "disappointed", "damaged", "slow", "average", "not satisfied", "not worth"]
    
    positive_reviews = 0
    negative_reviews = 0
    neutral_reviews = 0
    
    word_frequency = {}
    total_words = 0
    
    # Process each review
    for i, review in enumerate(customer_reviews, 1):
        print(f"\nReview {i}: {review}")
        
        # Convert to lowercase for analysis
        review_lower = review.lower()
        
        # Check sentiment
        positive_score = 0
        negative_score = 0
        
        for word in positive_words:
            if word in review_lower:
                positive_score += 1
        
        for word in negative_words:
            if word in review_lower:
                negative_score += 1
        
        # Determine sentiment
        if positive_score > negative_score:
            sentiment = "😊 Positive"
            positive_reviews += 1
        elif negative_score > positive_score:
            sentiment = "😞 Negative"
            negative_reviews += 1
        else:
            sentiment = "😐 Neutral"
            neutral_reviews += 1
        
        print(f"Sentiment: {sentiment} (P:{positive_score} N:{negative_score})")
        
        # Word frequency analysis
        words = review_lower.split()
        for word in words:
            # Clean word (remove punctuation)
            clean_word = ""
            for char in word:
                if char.isalpha():
                    clean_word += char
            
            if len(clean_word) > 3:  # Only count words longer than 3 chars
                total_words += 1
                if clean_word in word_frequency:
                    word_frequency[clean_word] += 1
                else:
                    word_frequency[clean_word] = 1
    
    # Summary report
    print(f"\n📊 ANALYSIS SUMMARY")
    print("-" * 25)
    print(f"Total Reviews: {len(customer_reviews)}")
    print(f"Positive: {positive_reviews} ({positive_reviews/len(customer_reviews)*100:.1f}%)")
    print(f"Negative: {negative_reviews} ({negative_reviews/len(customer_reviews)*100:.1f}%)")
    print(f"Neutral: {neutral_reviews} ({neutral_reviews/len(customer_reviews)*100:.1f}%)")
    
    # Most common words
    print(f"\n🔤 MOST COMMON WORDS")
    print("-" * 25)
    
    # Find top 5 words manually
    top_words = []
    for word, count in word_frequency.items():
        if count >= 2:  # Only words that appear at least twice
            top_words.append((word, count))
    
    # Simple sorting (bubble sort for educational purposes)
    for i in range(len(top_words)):
        for j in range(len(top_words) - 1):
            if top_words[j][1] < top_words[j + 1][1]:
                top_words[j], top_words[j + 1] = top_words[j + 1], top_words[j]
    
    # Display top words
    for word, count in top_words[:5]:
        print(f"{word}: {count} times")

analyze_text_data()

# STEP 5: Complete Automation Framework
print("\n" + "="*50)
print("STEP 5: COMPLETE AUTOMATION FRAMEWORK")
print("="*50)

def automated_report_generator():
    """Complete automated reporting system"""
    
    print("🤖 AUTOMATED REPORT GENERATOR")
    print("=" * 40)
    print("Processing multiple data sources...")
    
    # Simulate processing multiple datasets
    datasets = [
        {"name": "Q1 Sales", "data": [1000, 1200, 1100, 1300, 1250]},
        {"name": "Q2 Sales", "data": [1400, 1350, 1500, 1450, 1600]},
        {"name": "Q3 Sales", "data": [1550, 1700, 1650, 1800, 1750]},
        {"name": "Q4 Sales", "data": [1900, 1850, 2000, 1950, 2100]}
    ]
    
    yearly_total = 0
    quarterly_averages = []
    best_quarter = ""
    best_performance = 0
    
    # Process each quarter
    for quarter in datasets:
        quarter_name = quarter["name"]
        sales_data = quarter["data"]
        
        # Calculate quarter statistics
        quarter_total = 0
        for sale in sales_data:
            quarter_total += sale
        
        quarter_average = quarter_total / len(sales_data)
        quarterly_averages.append(quarter_average)
        yearly_total += quarter_total
        
        # Track best quarter
        if quarter_total > best_performance:
            best_performance = quarter_total
            best_quarter = quarter_name
        
        print(f"{quarter_name}: Total=${quarter_total:,}, Avg=${quarter_average:,.0f}")
    
    # Generate executive summary
    print(f"\n📈 EXECUTIVE SUMMARY")
    print("-" * 25)
    print(f"Yearly Revenue: ${yearly_total:,}")
    print(f"Best Quarter: {best_quarter} (${best_performance:,})")
    
    # Calculate year-over-year growth simulation
    previous_year_total = yearly_total * 0.85  # Simulate 15% growth
    growth_rate = ((yearly_total - previous_year_total) / previous_year_total) * 100
    print(f"YoY Growth: {growth_rate:.1f}%")
    
    # Performance trends
    print(f"\n📊 QUARTERLY TRENDS")
    print("-" * 25)
    for i, avg in enumerate(quarterly_averages):
        quarter_num = i + 1
        if i == 0:
            trend = "Baseline"
        else:
            prev_avg = quarterly_averages[i-1]
            if avg > prev_avg:
                trend = "📈 Growing"
            elif avg < prev_avg:
                trend = "📉 Declining"
            else:
                trend = "➡️  Stable"
        
        print(f"Q{quarter_num}: ${avg:,.0f} {trend}")
    
    print(f"\n✅ Report generated automatically!")
    print(f"⏱️  Processing time: Seconds (vs hours manually)")

automated_report_generator()

print("\n" + "="*60)
print("🎯 DATA PROCESSING AUTOMATION COMPLETE!")
print("You've learned how to:")
print("• Process large datasets automatically")
print("• Generate comprehensive reports")
print("• Analyze trends and patterns")
print("• Create reusable automation scripts")
print("• Save hours of manual work!")
print("="*60)