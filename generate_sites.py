"""
SA-Flow Website Generator
Generates all brochure pages and example websites (Basic, Medium, Advanced)
for 38 shop types across 8 categories.
"""
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# ============================================================
# SHOP DATA — 38 shop types with category, colors, images, etc.
# ============================================================
SHOPS = [
    # --- Category 1: Daily Essentials & Groceries ---
    {
        "name": "Kirana / Grocery Store",
        "slug": "kirana-grocery",
        "category": "Daily Essentials & Groceries",
        "cat_index": 0,
        "emoji": "🛒",
        "tagline": "Your Neighborhood Store, Now Online",
        "desc": "Bring your kirana store to the digital world. Showcase daily essentials, attract more customers, and let them find you on Google.",
        "colors": {"bg": "#EFEDE6", "accent": "#CD0000", "accent_light": "#fde8e8", "text": "#1a1a1a"},
        "hero_img": "https://images.unsplash.com/photo-1604719312566-8912e9227c6a?w=1200&q=80",
        "gallery": [
            "https://images.unsplash.com/photo-1542838132-92c53300491e?w=600&q=80",
            "https://images.unsplash.com/photo-1578916171728-46686eac8d58?w=600&q=80",
            "https://images.unsplash.com/photo-1556767576-5ec41e3239ea?w=600&q=80",
            "https://images.unsplash.com/photo-1601599561213-832382fd07ba?w=600&q=80",
            "https://images.unsplash.com/photo-1553546895-531931aa1aa8?w=600&q=80",
            "https://images.unsplash.com/photo-1583258292688-d0213dc5a3a8?w=600&q=80"
        ],
        "products": ["Rice & Grains", "Cooking Oil & Ghee", "Spices & Masala", "Snacks & Beverages", "Cleaning Supplies", "Personal Care"],
        "about": "Serving the neighborhood for over 15 years with quality groceries, daily essentials, and household items at the best prices. We stock everything your family needs — from fresh spices to premium brands."
    },
    {
        "name": "Green Grocer",
        "slug": "green-grocers",
        "category": "Daily Essentials & Groceries",
        "cat_index": 0,
        "emoji": "🥬",
        "tagline": "Farm-Fresh Vegetables & Fruits, Daily",
        "desc": "Showcase your fresh produce online. Let customers see your daily stock of vegetables and fruits before they visit.",
        "colors": {"bg": "#EFEDE6", "accent": "#CD0000", "accent_light": "#fde8e8", "text": "#1a1a1a"},
        "hero_img": "https://images.unsplash.com/photo-1488459716781-31db52582fe9?w=1200&q=80",
        "gallery": [
            "https://images.unsplash.com/photo-1518843875459-f738682238a6?w=600&q=80",
            "https://images.unsplash.com/photo-1573246123716-6b1782bfc499?w=600&q=80",
            "https://images.unsplash.com/photo-1610348725531-acac70e7c4d3?w=600&q=80",
            "https://images.unsplash.com/photo-1540420773420-3366772f4999?w=600&q=80",
            "https://images.unsplash.com/photo-1557844352-761f2565b576?w=600&q=80",
            "https://images.unsplash.com/photo-1516594798947-e65505dbb29d?w=600&q=80"
        ],
        "products": ["Seasonal Vegetables", "Exotic Vegetables", "Fresh Fruits", "Leafy Greens", "Organic Produce", "Herbs & Sprouts"],
        "about": "We bring you the freshest vegetables and fruits sourced directly from local farms every morning. Quality you can taste, prices you'll love."
    },
    {
        "name": "Dairy Booth",
        "slug": "dairy-booths",
        "category": "Daily Essentials & Groceries",
        "cat_index": 0,
        "emoji": "🥛",
        "tagline": "Fresh Dairy Products, Every Day",
        "desc": "Showcase your dairy products — from farm-fresh milk to artisan cheese — and grow your customer base.",
        "colors": {"bg": "#EFEDE6", "accent": "#CD0000", "accent_light": "#fde8e8", "text": "#1a1a1a"},
        "hero_img": "https://images.unsplash.com/photo-1550583724-b2692b85b150?w=1200&q=80",
        "gallery": [
            "https://images.unsplash.com/photo-1563636619-e9143da7973b?w=600&q=80",
            "https://images.unsplash.com/photo-1628088062854-d1870b4553da?w=600&q=80",
            "https://images.unsplash.com/photo-1486297678162-eb2a19b0a32d?w=600&q=80",
            "https://images.unsplash.com/photo-1559598467-f8b76c8155d0?w=600&q=80",
            "https://images.unsplash.com/photo-1587167056547-0fd2f69e993a?w=600&q=80",
            "https://images.unsplash.com/photo-1589985270826-4b7bb135bc9d?w=600&q=80"
        ],
        "products": ["Fresh Milk", "Paneer & Cheese", "Yogurt & Curd", "Butter & Ghee", "Cream & Khoya", "Eggs"],
        "about": "Your trusted source for pure, unadulterated dairy products. From farm-fresh milk delivered every morning to handmade paneer and curd."
    },
    {
        "name": "Butchery & Fishmonger",
        "slug": "butcheries-fishmongers",
        "category": "Daily Essentials & Groceries",
        "cat_index": 0,
        "emoji": "🥩",
        "tagline": "Premium Meats & Fresh Seafood",
        "desc": "A professional online presence for your meat and seafood business with product showcases and ordering.",
        "colors": {"bg": "#EFEDE6", "accent": "#CD0000", "accent_light": "#fde8e8", "text": "#1a1a1a"},
        "hero_img": "https://images.unsplash.com/photo-1607623814075-e51df1bdc82f?w=1200&q=80",
        "gallery": [
            "https://images.unsplash.com/photo-1558030006-450675393462?w=600&q=80",
            "https://images.unsplash.com/photo-1529692236671-f1f6cf9683ba?w=600&q=80",
            "https://images.unsplash.com/photo-1544551763-46a013bb70d5?w=600&q=80",
            "https://images.unsplash.com/photo-1615141982883-c7ad0e69fd62?w=600&q=80",
            "https://images.unsplash.com/photo-1600891964092-4316c288032e?w=600&q=80",
            "https://images.unsplash.com/photo-1551028150-64b9f398f678?w=600&q=80"
        ],
        "products": ["Fresh Chicken", "Mutton & Lamb", "Fish & Prawns", "Marinated Meats", "Eggs", "Ready-to-Cook Packs"],
        "about": "Quality meats and fresh seafood sourced daily from trusted suppliers. Hygiene and freshness guaranteed with every order."
    },
    {
        "name": "Supermarket",
        "slug": "supermarkets",
        "category": "Daily Essentials & Groceries",
        "cat_index": 0,
        "emoji": "🏬",
        "tagline": "Everything Under One Roof",
        "desc": "A comprehensive website for your supermarket — showcase departments, weekly offers, and bring customers through the door.",
        "colors": {"bg": "#EFEDE6", "accent": "#CD0000", "accent_light": "#fde8e8", "text": "#1a1a1a"},
        "hero_img": "https://images.unsplash.com/photo-1604742762228-5b58f03d7748?w=1200&q=80",
        "gallery": [
            "https://images.unsplash.com/photo-1534723452862-4c874018d66d?w=600&q=80",
            "https://images.unsplash.com/photo-1601599561213-832382fd07ba?w=600&q=80",
            "https://images.unsplash.com/photo-1578916171728-46686eac8d58?w=600&q=80",
            "https://images.unsplash.com/photo-1556767576-5ec41e3239ea?w=600&q=80",
            "https://images.unsplash.com/photo-1542838132-92c53300491e?w=600&q=80",
            "https://images.unsplash.com/photo-1583258292688-d0213dc5a3a8?w=600&q=80"
        ],
        "products": ["Groceries", "Fresh Produce", "Dairy & Frozen", "Household Items", "Personal Care", "Bakery & Snacks"],
        "about": "Your one-stop supermarket for everything — from fresh produce to electronics. Great variety, competitive prices, and a shopping experience you'll love."
    },
    {
        "name": "Convenience Store",
        "slug": "convenience-stores",
        "category": "Daily Essentials & Groceries",
        "cat_index": 0,
        "emoji": "🏪",
        "tagline": "Quick Stops, Everyday Needs",
        "desc": "A simple, effective website for your convenience store — show your hours, location, and key products.",
        "colors": {"bg": "#EFEDE6", "accent": "#CD0000", "accent_light": "#fde8e8", "text": "#1a1a1a"},
        "hero_img": "https://images.unsplash.com/photo-1604719312566-8912e9227c6a?w=1200&q=80",
        "gallery": [
            "https://images.unsplash.com/photo-1556767576-5ec41e3239ea?w=600&q=80",
            "https://images.unsplash.com/photo-1604742762228-5b58f03d7748?w=600&q=80",
            "https://images.unsplash.com/photo-1601599561213-832382fd07ba?w=600&q=80",
            "https://images.unsplash.com/photo-1534723452862-4c874018d66d?w=600&q=80",
            "https://images.unsplash.com/photo-1583258292688-d0213dc5a3a8?w=600&q=80",
            "https://images.unsplash.com/photo-1578916171728-46686eac8d58?w=600&q=80"
        ],
        "products": ["Beverages & Juices", "Snacks & Chips", "Cigarettes & Tobacco", "Quick Meals", "Toiletries", "Stationery"],
        "about": "Open early, close late — your go-to convenience store for everything you need in a hurry. Quick service, friendly staff, and essentials always in stock."
    },

    # --- Category 2: Food & Beverage ---
    {
        "name": "Bakery",
        "slug": "bakeries",
        "category": "Food & Beverage",
        "cat_index": 1,
        "emoji": "🍰",
        "tagline": "Freshly Baked, Made with Love",
        "desc": "A delicious website for your bakery — showcase cakes, breads, and pastries with mouth-watering photography.",
        "colors": {"bg": "#FFF8F0", "accent": "#780116", "accent_light": "#fde8e8", "text": "#1a1a1a"},
        "hero_img": "https://images.unsplash.com/photo-1509440159596-0249088772ff?w=1200&q=80",
        "gallery": [
            "https://images.unsplash.com/photo-1558961363-fa8fdf82db35?w=600&q=80",
            "https://images.unsplash.com/photo-1486427944544-d2c246c4d957?w=600&q=80",
            "https://images.unsplash.com/photo-1555507036-ab1f4038024a?w=600&q=80",
            "https://images.unsplash.com/photo-1517433670267-08bbd4be890f?w=600&q=80",
            "https://images.unsplash.com/photo-1464349095431-e9a21285b5f3?w=600&q=80",
            "https://images.unsplash.com/photo-1495147466023-ac5c588e2e94?w=600&q=80"
        ],
        "products": ["Artisan Breads", "Custom Cakes", "Pastries & Croissants", "Cookies & Biscuits", "Cupcakes & Muffins", "Wedding Cakes"],
        "about": "Crafting the finest breads, cakes, and pastries since day one. Every item is baked fresh with premium ingredients and a whole lot of love."
    },
    {
        "name": "Cafe & Eatery",
        "slug": "cafes-eateries",
        "category": "Food & Beverage",
        "cat_index": 1,
        "emoji": "☕",
        "tagline": "Your Perfect Cup, Your Perfect Spot",
        "desc": "An inviting website for your cafe — show your menu, ambiance, and location to attract more visitors.",
        "colors": {"bg": "#FFF8F0", "accent": "#780116", "accent_light": "#fde8e8", "text": "#1a1a1a"},
        "hero_img": "https://images.unsplash.com/photo-1501339847302-ac426a4a7cbb?w=1200&q=80",
        "gallery": [
            "https://images.unsplash.com/photo-1554118811-1e0d58224f24?w=600&q=80",
            "https://images.unsplash.com/photo-1453614512568-c4024d13c247?w=600&q=80",
            "https://images.unsplash.com/photo-1495474472287-4d71bcdd2085?w=600&q=80",
            "https://images.unsplash.com/photo-1442512595331-e89e73853f31?w=600&q=80",
            "https://images.unsplash.com/photo-1517248135467-4c7edcad34c4?w=600&q=80",
            "https://images.unsplash.com/photo-1559305616-3f99cd43e353?w=600&q=80"
        ],
        "products": ["Specialty Coffee", "Fresh Teas", "Sandwiches & Wraps", "Breakfast Platters", "Smoothies & Shakes", "Desserts"],
        "about": "A cozy café where every cup is brewed to perfection. Whether you're catching up with friends or working remotely, we've got the vibe and the menu for you."
    },
    {
        "name": "Confectionery & Chocolatier",
        "slug": "confectioneries",
        "category": "Food & Beverage",
        "cat_index": 1,
        "emoji": "🍫",
        "tagline": "Handcrafted Sweets & Chocolates",
        "desc": "A sweet website for your confectionery — display your chocolate collections, gift boxes, and seasonal specials.",
        "colors": {"bg": "#FFF8F0", "accent": "#780116", "accent_light": "#fde8e8", "text": "#1a1a1a"},
        "hero_img": "https://images.unsplash.com/photo-1549007994-cb92caebd54b?w=1200&q=80",
        "gallery": [
            "https://images.unsplash.com/photo-1481391319762-47dff72954d9?w=600&q=80",
            "https://images.unsplash.com/photo-1511381939415-e44015466834?w=600&q=80",
            "https://images.unsplash.com/photo-1548907040-4baa42d10919?w=600&q=80",
            "https://images.unsplash.com/photo-1571115177098-24ec42ed204d?w=600&q=80",
            "https://images.unsplash.com/photo-1526081347589-7fa3cb41b4b2?w=600&q=80",
            "https://images.unsplash.com/photo-1582176604856-e824b4736522?w=600&q=80"
        ],
        "products": ["Handmade Chocolates", "Gift Boxes", "Indian Sweets", "Seasonal Specials", "Sugar-Free Range", "Corporate Gifting"],
        "about": "Crafting premium chocolates and sweets with the finest ingredients. Perfect for gifting, celebrations, or just treating yourself."
    },
    {
        "name": "Delicatessen",
        "slug": "delicatessens",
        "category": "Food & Beverage",
        "cat_index": 1,
        "emoji": "🧀",
        "tagline": "Premium Gourmet Selections",
        "desc": "An elegant website for your deli — showcase premium cheeses, cold cuts, and prepared specialty foods.",
        "colors": {"bg": "#FFF8F0", "accent": "#780116", "accent_light": "#fde8e8", "text": "#1a1a1a"},
        "hero_img": "https://images.unsplash.com/photo-1550507992-eb63ffee0847?w=1200&q=80",
        "gallery": [
            "https://images.unsplash.com/photo-1486297678162-eb2a19b0a32d?w=600&q=80",
            "https://images.unsplash.com/photo-1559598467-f8b76c8155d0?w=600&q=80",
            "https://images.unsplash.com/photo-1534308983496-4fabb1a015ee?w=600&q=80",
            "https://images.unsplash.com/photo-1528750717929-32abb73d3bd9?w=600&q=80",
            "https://images.unsplash.com/photo-1592415486689-125cbbfcbee2?w=600&q=80",
            "https://images.unsplash.com/photo-1521305916504-4a1121188589?w=600&q=80"
        ],
        "products": ["Artisan Cheeses", "Cold Cuts & Salami", "Gourmet Sandwiches", "Olive & Pickle Bar", "Imported Wines", "Prepared Foods"],
        "about": "A curated selection of the finest gourmet foods — from artisan cheeses to imported delicacies. For those who appreciate quality in every bite."
    },
    {
        "name": "Wine & Spirit Shop",
        "slug": "wine-spirit-shops",
        "category": "Food & Beverage",
        "cat_index": 1,
        "emoji": "🍷",
        "tagline": "Fine Wines & Premium Spirits",
        "desc": "A sophisticated website for your liquor store — display your collection with elegance and attract discerning customers.",
        "colors": {"bg": "#FFF8F0", "accent": "#780116", "accent_light": "#fde8e8", "text": "#1a1a1a"},
        "hero_img": "https://images.unsplash.com/photo-1553361371-9b22f78e8b1d?w=1200&q=80",
        "gallery": [
            "https://images.unsplash.com/photo-1474722883778-792e7990302f?w=600&q=80",
            "https://images.unsplash.com/photo-1569529465841-dfecdab7503b?w=600&q=80",
            "https://images.unsplash.com/photo-1582819509237-d5b75f20ff7a?w=600&q=80",
            "https://images.unsplash.com/photo-1569924498404-b5a7f0e9d76f?w=600&q=80",
            "https://images.unsplash.com/photo-1558642452-9d2a7deb7f62?w=600&q=80",
            "https://images.unsplash.com/photo-1547595628-c61a29f496f0?w=600&q=80"
        ],
        "products": ["Red Wines", "White Wines", "Whiskey & Bourbon", "Vodka & Gin", "Beer & Craft Ales", "Premium Spirits"],
        "about": "A carefully curated collection of wines, spirits, and craft beverages from around the world. Expert recommendations and the best prices in town."
    },

    # --- Category 3: Health, Wellness & Personal Care ---
    {
        "name": "Pharmacy / Chemist",
        "slug": "pharmacies",
        "category": "Health, Wellness & Personal Care",
        "cat_index": 2,
        "emoji": "💊",
        "tagline": "Your Health, Our Priority",
        "desc": "A trustworthy website for your pharmacy — display services, medicines, and health products professionally.",
        "colors": {"bg": "#F4FFF4", "accent": "#222022", "accent_light": "#e8ffe8", "text": "#1a1a1a"},
        "hero_img": "https://images.unsplash.com/photo-1585435557343-3b92740e3e7b?w=1200&q=80",
        "gallery": [
            "https://images.unsplash.com/photo-1576091160399-112ba8d25d1d?w=600&q=80",
            "https://images.unsplash.com/photo-1631549916768-4119b2e5f926?w=600&q=80",
            "https://images.unsplash.com/photo-1587854692152-cbe660dbde88?w=600&q=80",
            "https://images.unsplash.com/photo-1583912267550-d974311a9a6e?w=600&q=80",
            "https://images.unsplash.com/photo-1471864190281-a93a3070b6de?w=600&q=80",
            "https://images.unsplash.com/photo-1556741533-6e6a62bd8b49?w=600&q=80"
        ],
        "products": ["Prescription Medicines", "OTC Drugs", "Health Supplements", "Personal Hygiene", "Medical Devices", "Baby Care"],
        "about": "A trusted pharmacy serving the community with quality medicines, health supplements, and expert pharmaceutical advice. Your health is our mission."
    },
    {
        "name": "Salon & Barber Shop",
        "slug": "salons-barber",
        "category": "Health, Wellness & Personal Care",
        "cat_index": 2,
        "emoji": "💇",
        "tagline": "Look Good, Feel Amazing",
        "desc": "A stylish website for your salon — showcase your services, portfolio, and make it easy to book appointments.",
        "colors": {"bg": "#F7F5F0", "accent": "#222022", "accent_light": "#e8e6e0", "text": "#1a1a1a"},
        "hero_img": "https://images.unsplash.com/photo-1560066984-138dadb4c035?w=1200&q=80",
        "gallery": [
            "https://images.unsplash.com/photo-1521590832167-7bcbfaa6381f?w=600&q=80",
            "https://images.unsplash.com/photo-1562322140-8baeececf3df?w=600&q=80",
            "https://images.unsplash.com/photo-1559599101-f09722fb4948?w=600&q=80",
            "https://images.unsplash.com/photo-1600948836101-f9ffda59d250?w=600&q=80",
            "https://images.unsplash.com/photo-1633681122956-4a30c80a1dba?w=600&q=80",
            "https://images.unsplash.com/photo-1522337360788-8b13dee7a37e?w=600&q=80"
        ],
        "products": ["Haircuts & Styling", "Hair Coloring", "Shaving & Grooming", "Facials & Skin Care", "Bridal Packages", "Spa Treatments"],
        "about": "A premium salon experience with skilled stylists, top-brand products, and a relaxing ambiance. Walk in looking good, walk out feeling amazing."
    },
    {
        "name": "Gym & Yoga Studio",
        "slug": "gyms-yoga",
        "category": "Health, Wellness & Personal Care",
        "cat_index": 2,
        "emoji": "💪",
        "tagline": "Transform Your Body & Mind",
        "desc": "A powerful website for your fitness center — highlight classes, trainers, and membership plans.",
        "colors": {"bg": "#F0F4F0", "accent": "#222022", "accent_light": "#e0e8e0", "text": "#1a1a1a"},
        "hero_img": "https://images.unsplash.com/photo-1534438327276-14e5300c3a48?w=1200&q=80",
        "gallery": [
            "https://images.unsplash.com/photo-1571019613454-1cb2f99b2d8b?w=600&q=80",
            "https://images.unsplash.com/photo-1518611012118-696072aa579a?w=600&q=80",
            "https://images.unsplash.com/photo-1544367567-0f2fcb009e0b?w=600&q=80",
            "https://images.unsplash.com/photo-1540497077202-7c8a3999166f?w=600&q=80",
            "https://images.unsplash.com/photo-1518310383802-640c2de311b2?w=600&q=80",
            "https://images.unsplash.com/photo-1574680096145-d05b474e2155?w=600&q=80"
        ],
        "products": ["Weight Training", "Cardio & HIIT", "Yoga Classes", "Personal Training", "Group Fitness", "Nutrition Counseling"],
        "about": "State-of-the-art equipment, certified trainers, and a motivating atmosphere. Whether you're into weights, yoga, or cardio — we've got you covered."
    },

    # --- Category 4: Apparel, Fashion & Accessories ---
    {
        "name": "Boutique",
        "slug": "boutiques",
        "category": "Apparel, Fashion & Accessories",
        "cat_index": 3,
        "emoji": "👗",
        "tagline": "Curated Fashion, Unique Style",
        "desc": "An elegant website for your boutique — showcase designer collections with stunning visuals.",
        "colors": {"bg": "#FFFDF5", "accent": "#02462E", "accent_light": "#e0f5eb", "text": "#1a1a1a"},
        "hero_img": "https://images.unsplash.com/photo-1441984904996-e0b6ba687e04?w=1200&q=80",
        "gallery": [
            "https://images.unsplash.com/photo-1558618666-fcd25c85f82e?w=600&q=80",
            "https://images.unsplash.com/photo-1567401893414-76b7b1e5a7a5?w=600&q=80",
            "https://images.unsplash.com/photo-1558171813-01ed3d751d6a?w=600&q=80",
            "https://images.unsplash.com/photo-1490481651871-ab68de25d43d?w=600&q=80",
            "https://images.unsplash.com/photo-1445205170230-053b83016050?w=600&q=80",
            "https://images.unsplash.com/photo-1469334031218-e382a71b716b?w=600&q=80"
        ],
        "products": ["Designer Sarees", "Ethnic Wear", "Western Wear", "Party Dresses", "Bridal Collection", "Accessories"],
        "about": "A curated collection of designer clothing and accessories for the modern fashionista. Unique styles, premium fabrics, and designs that make you stand out."
    },
    {
        "name": "Footwear Store",
        "slug": "footwear-stores",
        "category": "Apparel, Fashion & Accessories",
        "cat_index": 3,
        "emoji": "👟",
        "tagline": "Step Into Style & Comfort",
        "desc": "A sharp website for your shoe store — showcase collections for every occasion with size guides.",
        "colors": {"bg": "#FFFDF5", "accent": "#02462E", "accent_light": "#e0f5eb", "text": "#1a1a1a"},
        "hero_img": "https://images.unsplash.com/photo-1460353581641-37baddab0fa2?w=1200&q=80",
        "gallery": [
            "https://images.unsplash.com/photo-1542291026-7eec264c27ff?w=600&q=80",
            "https://images.unsplash.com/photo-1549298916-b41d501d3772?w=600&q=80",
            "https://images.unsplash.com/photo-1595950653106-6c9ebd614d3a?w=600&q=80",
            "https://images.unsplash.com/photo-1543163521-1bf539c55dd2?w=600&q=80",
            "https://images.unsplash.com/photo-1608256246200-53e635b5b65f?w=600&q=80",
            "https://images.unsplash.com/photo-1560343090-f0409e92791a?w=600&q=80"
        ],
        "products": ["Sports Shoes", "Formal Shoes", "Casual Sneakers", "Sandals & Slippers", "Boots", "Kids' Footwear"],
        "about": "From athletic performance to formal elegance — we have the perfect pair for every step of your life. Top brands, great prices."
    },
    {
        "name": "Jewelry Store",
        "slug": "jewelry-stores",
        "category": "Apparel, Fashion & Accessories",
        "cat_index": 3,
        "emoji": "💎",
        "tagline": "Timeless Elegance, Crafted in Gold",
        "desc": "A luxurious website for your jewelry store — display collections with the sparkle they deserve.",
        "colors": {"bg": "#FFFDF5", "accent": "#02462E", "accent_light": "#e0f5eb", "text": "#1a1a1a"},
        "hero_img": "https://images.unsplash.com/photo-1515562141589-67f0d569b2c6?w=1200&q=80",
        "gallery": [
            "https://images.unsplash.com/photo-1601121141461-9d6647bca1ed?w=600&q=80",
            "https://images.unsplash.com/photo-1605100804763-247f67b3557e?w=600&q=80",
            "https://images.unsplash.com/photo-1603561596112-0a132b757442?w=600&q=80",
            "https://images.unsplash.com/photo-1588444837495-c6cfeb53f32d?w=600&q=80",
            "https://images.unsplash.com/photo-1599643478518-a784e5dc4c8f?w=600&q=80",
            "https://images.unsplash.com/photo-1573408301185-9146fe634ad0?w=600&q=80"
        ],
        "products": ["Gold Necklaces", "Diamond Rings", "Silver Jewelry", "Bridal Sets", "Watches", "Custom Designs"],
        "about": "Exquisite jewelry crafted with passion and precision. From traditional gold to modern diamond collections — every piece tells a story."
    },
    {
        "name": "Tailor Shop",
        "slug": "tailor-shops",
        "category": "Apparel, Fashion & Accessories",
        "cat_index": 3,
        "emoji": "🧵",
        "tagline": "Custom Tailored to Perfection",
        "desc": "A professional website for your tailor shop — showcase your craftsmanship and custom designs.",
        "colors": {"bg": "#FFFDF5", "accent": "#02462E", "accent_light": "#e0f5eb", "text": "#1a1a1a"},
        "hero_img": "https://images.unsplash.com/photo-1558618666-fcd25c85f82e?w=1200&q=80",
        "gallery": [
            "https://images.unsplash.com/photo-1507679799987-c73779587ccf?w=600&q=80",
            "https://images.unsplash.com/photo-1594938298603-c8148c4dae35?w=600&q=80",
            "https://images.unsplash.com/photo-1558171813-01ed3d751d6a?w=600&q=80",
            "https://images.unsplash.com/photo-1490481651871-ab68de25d43d?w=600&q=80",
            "https://images.unsplash.com/photo-1445205170230-053b83016050?w=600&q=80",
            "https://images.unsplash.com/photo-1617137968427-85924c800a22?w=600&q=80"
        ],
        "products": ["Men's Suits", "Women's Ethnic Wear", "Alterations", "Blouse Stitching", "Curtains & Upholstery", "School Uniforms"],
        "about": "Expert tailoring with decades of experience. From bespoke suits to everyday alterations — we make sure every stitch is perfect."
    },
    {
        "name": "Haberdashery",
        "slug": "haberdasheries",
        "category": "Apparel, Fashion & Accessories",
        "cat_index": 3,
        "emoji": "🪡",
        "tagline": "Everything for Sewing & Crafting",
        "desc": "A niche website for your haberdashery — display your sewing supplies, fabrics, and accessories.",
        "colors": {"bg": "#FFFDF5", "accent": "#02462E", "accent_light": "#e0f5eb", "text": "#1a1a1a"},
        "hero_img": "https://images.unsplash.com/photo-1558618666-fcd25c85f82e?w=1200&q=80",
        "gallery": [
            "https://images.unsplash.com/photo-1558171813-01ed3d751d6a?w=600&q=80",
            "https://images.unsplash.com/photo-1589578228447-e1a4e481c6c8?w=600&q=80",
            "https://images.unsplash.com/photo-1452587925148-ce544e77e70d?w=600&q=80",
            "https://images.unsplash.com/photo-1606722590583-6951b5ea92ad?w=600&q=80",
            "https://images.unsplash.com/photo-1530259152377-3a014354da04?w=600&q=80",
            "https://images.unsplash.com/photo-1494783367193-149034c05e8f?w=600&q=80"
        ],
        "products": ["Buttons & Zippers", "Threads & Needles", "Fabrics & Laces", "Ribbons & Trims", "Sewing Machines", "Craft Supplies"],
        "about": "Your one-stop shop for all sewing needs — from buttons and zippers to premium fabrics and laces. Serving tailors and crafters for years."
    },

    # --- Category 5: Home, Hardware & Infrastructure ---
    {
        "name": "Hardware Store",
        "slug": "hardware-stores",
        "category": "Home, Hardware & Infrastructure",
        "cat_index": 4,
        "emoji": "🔨",
        "tagline": "Build It Right, Build It Strong",
        "desc": "A solid website for your hardware store — showcase tools, materials, and make it easy to find your shop.",
        "colors": {"bg": "#EFEDE6", "accent": "#CD0000", "accent_light": "#fde8e8", "text": "#1a1a1a"},
        "hero_img": "https://images.unsplash.com/photo-1504148455328-c376907d081c?w=1200&q=80",
        "gallery": [
            "https://images.unsplash.com/photo-1581783898377-1c85bf937427?w=600&q=80",
            "https://images.unsplash.com/photo-1530124566582-a45a7e3f3867?w=600&q=80",
            "https://images.unsplash.com/photo-1572981779307-38b8cabb2407?w=600&q=80",
            "https://images.unsplash.com/photo-1590402494682-cd3fb53b1f70?w=600&q=80",
            "https://images.unsplash.com/photo-1504148455328-c376907d081c?w=600&q=80",
            "https://images.unsplash.com/photo-1522199755839-a2bacb67c546?w=600&q=80"
        ],
        "products": ["Power Tools", "Hand Tools", "Plumbing Supplies", "Paints & Primers", "Electrical Items", "Building Materials"],
        "about": "Everything you need to build, fix, and improve. Quality tools, competitive prices, and expert advice from our experienced staff."
    },
    {
        "name": "Furniture Store & Warehouse",
        "slug": "furniture-stores",
        "category": "Home, Hardware & Infrastructure",
        "cat_index": 4,
        "emoji": "🛋️",
        "tagline": "Furnish Your Dream Home",
        "desc": "A beautiful website for your furniture store — showcase your collections with room-setting photography.",
        "colors": {"bg": "#EFEDE6", "accent": "#CD0000", "accent_light": "#fde8e8", "text": "#1a1a1a"},
        "hero_img": "https://images.unsplash.com/photo-1555041469-a586c61ea9bc?w=1200&q=80",
        "gallery": [
            "https://images.unsplash.com/photo-1524758631624-e2822e304c36?w=600&q=80",
            "https://images.unsplash.com/photo-1540518614846-7eded433c457?w=600&q=80",
            "https://images.unsplash.com/photo-1491926626834-766ae2858c3c?w=600&q=80",
            "https://images.unsplash.com/photo-1555041469-a586c61ea9bc?w=600&q=80",
            "https://images.unsplash.com/photo-1506439773649-6e0eb8cfb237?w=600&q=80",
            "https://images.unsplash.com/photo-1600210492493-0946911123ea?w=600&q=80"
        ],
        "products": ["Living Room Sets", "Bedroom Furniture", "Dining Tables", "Office Desks", "Storage Solutions", "Outdoor Furniture"],
        "about": "Transform your home with our stunning furniture collection. From modern minimalist to traditional Indian — designs for every taste and budget."
    },
    {
        "name": "Home Goods Showroom",
        "slug": "home-goods",
        "category": "Home, Hardware & Infrastructure",
        "cat_index": 4,
        "emoji": "🏡",
        "tagline": "Design Your Perfect Space",
        "desc": "An impressive website for your home goods showroom — display tiles, kitchen fittings, and interior products.",
        "colors": {"bg": "#EFEDE6", "accent": "#CD0000", "accent_light": "#fde8e8", "text": "#1a1a1a"},
        "hero_img": "https://images.unsplash.com/photo-1556909114-f6e7ad7d3136?w=1200&q=80",
        "gallery": [
            "https://images.unsplash.com/photo-1556909114-f6e7ad7d3136?w=600&q=80",
            "https://images.unsplash.com/photo-1523413184730-e85dbbd04aba?w=600&q=80",
            "https://images.unsplash.com/photo-1600607687939-ce8a6c25118c?w=600&q=80",
            "https://images.unsplash.com/photo-1600566753086-00f18fb6b3ea?w=600&q=80",
            "https://images.unsplash.com/photo-1617325247661-675ab4b64ae2?w=600&q=80",
            "https://images.unsplash.com/photo-1600585154340-be6161a56a0c?w=600&q=80"
        ],
        "products": ["Wall & Floor Tiles", "Kitchen Fittings", "Bathroom Fixtures", "Lighting Solutions", "Interior Decor", "Modular Kitchens"],
        "about": "Your one-stop destination for home interiors. Browse our extensive collection of tiles, sanitaryware, kitchen solutions, and decor items."
    },
    {
        "name": "Nursery / Garden Center",
        "slug": "nurseries-garden",
        "category": "Home, Hardware & Infrastructure",
        "cat_index": 4,
        "emoji": "🌿",
        "tagline": "Grow Your Green Paradise",
        "desc": "A fresh website for your nursery — showcase plants, gardening supplies, and landscaping services.",
        "colors": {"bg": "#F0F7F0", "accent": "#2D6A4F", "accent_light": "#D8F3DC", "text": "#1a1a1a"},
        "hero_img": "https://images.unsplash.com/photo-1416879595882-3373a0480b5b?w=1200&q=80",
        "gallery": [
            "https://images.unsplash.com/photo-1459411552884-841db9b3cc2a?w=600&q=80",
            "https://images.unsplash.com/photo-1491147334573-44cbb4602074?w=600&q=80",
            "https://images.unsplash.com/photo-1463936575829-25148e1db1b8?w=600&q=80",
            "https://images.unsplash.com/photo-1437252611977-07f74518abd7?w=600&q=80",
            "https://images.unsplash.com/photo-1416879595882-3373a0480b5b?w=600&q=80",
            "https://images.unsplash.com/photo-1585320806297-9794b3e4eeae?w=600&q=80"
        ],
        "products": ["Indoor Plants", "Outdoor Plants", "Seeds & Saplings", "Pots & Planters", "Gardening Tools", "Soil & Fertilizers"],
        "about": "Nurturing green dreams since day one. We offer the widest variety of plants, gardening supplies, and expert advice to help your garden thrive."
    },

    # --- Category 6: Technology, Hobbies & Entertainment ---
    {
        "name": "Electronics Showroom",
        "slug": "electronics-showrooms",
        "category": "Technology, Hobbies & Entertainment",
        "cat_index": 5,
        "emoji": "📱",
        "tagline": "Latest Tech, Best Prices",
        "desc": "A modern website for your electronics store — showcase gadgets, appliances, and offer deals.",
        "colors": {"bg": "#EDF1F5", "accent": "#0145F2", "accent_light": "#e8efff", "text": "#0f172a"},
        "hero_img": "https://images.unsplash.com/photo-1468495244123-6c6c332eeece?w=1200&q=80",
        "gallery": [
            "https://images.unsplash.com/photo-1498049794561-7780e7231661?w=600&q=80",
            "https://images.unsplash.com/photo-1519389950473-47ba0277781c?w=600&q=80",
            "https://images.unsplash.com/photo-1588508065123-287b28e013da?w=600&q=80",
            "https://images.unsplash.com/photo-1593642632559-0c6d3fc62b89?w=600&q=80",
            "https://images.unsplash.com/photo-1550009158-9ebf69173e03?w=600&q=80",
            "https://images.unsplash.com/photo-1555664424-778a1e5e1b48?w=600&q=80"
        ],
        "products": ["Smartphones", "Laptops & PCs", "TVs & Displays", "Home Appliances", "Audio & Speakers", "Accessories"],
        "about": "The latest gadgets and home appliances at unbeatable prices. Expert demo, after-sales service, and EMI options available."
    },
    {
        "name": "Bookstore",
        "slug": "bookstores",
        "category": "Technology, Hobbies & Entertainment",
        "cat_index": 5,
        "emoji": "📚",
        "tagline": "A World of Stories Awaits",
        "desc": "A literary website for your bookstore — showcase collections, new arrivals, and reading events.",
        "colors": {"bg": "#EDF1F5", "accent": "#0145F2", "accent_light": "#e8efff", "text": "#0f172a"},
        "hero_img": "https://images.unsplash.com/photo-1507842217343-583bb7270b66?w=1200&q=80",
        "gallery": [
            "https://images.unsplash.com/photo-1521587760476-6c12a4b040da?w=600&q=80",
            "https://images.unsplash.com/photo-1495446815901-a7297e633e8d?w=600&q=80",
            "https://images.unsplash.com/photo-1544947950-fa07a98d237f?w=600&q=80",
            "https://images.unsplash.com/photo-1497633762265-9d179a990aa6?w=600&q=80",
            "https://images.unsplash.com/photo-1524578271613-d550eacf6090?w=600&q=80",
            "https://images.unsplash.com/photo-1526243741027-444d633d7365?w=600&q=80"
        ],
        "products": ["Fiction & Novels", "Non-Fiction", "Academic & Textbooks", "Children's Books", "Competitive Exams", "Stationery"],
        "about": "A curated haven for book lovers. From bestselling fiction to academic resources — we have something for every reader."
    },
    {
        "name": "Stationery Shop",
        "slug": "stationery-shops",
        "category": "Technology, Hobbies & Entertainment",
        "cat_index": 5,
        "emoji": "✏️",
        "tagline": "Write, Create, Organize",
        "desc": "A clean website for your stationery store — display office supplies, art materials, and school needs.",
        "colors": {"bg": "#EDF1F5", "accent": "#0145F2", "accent_light": "#e8efff", "text": "#0f172a"},
        "hero_img": "https://images.unsplash.com/photo-1513542789411-b6a5d4f31634?w=1200&q=80",
        "gallery": [
            "https://images.unsplash.com/photo-1456735190827-d1262f71b8a3?w=600&q=80",
            "https://images.unsplash.com/photo-1513364776144-60967b0f800f?w=600&q=80",
            "https://images.unsplash.com/photo-1434030216411-0b793f4b4173?w=600&q=80",
            "https://images.unsplash.com/photo-1544947950-fa07a98d237f?w=600&q=80",
            "https://images.unsplash.com/photo-1586075010923-2dd4570fb338?w=600&q=80",
            "https://images.unsplash.com/photo-1603796846097-bee99e4a601f?w=600&q=80"
        ],
        "products": ["Pens & Markers", "Notebooks & Diaries", "Art Supplies", "Office Essentials", "Printers & Ink", "Gift Wrapping"],
        "about": "From school essentials to premium office supplies — everything you need to write, create, and stay organized."
    },
    {
        "name": "Hobby & Craft Shop",
        "slug": "hobby-craft",
        "category": "Technology, Hobbies & Entertainment",
        "cat_index": 5,
        "emoji": "🎨",
        "tagline": "Unleash Your Creativity",
        "desc": "A creative website for your hobby shop — showcase craft supplies, workshops, and project ideas.",
        "colors": {"bg": "#EDF1F5", "accent": "#0145F2", "accent_light": "#e8efff", "text": "#0f172a"},
        "hero_img": "https://images.unsplash.com/photo-1513364776144-60967b0f800f?w=1200&q=80",
        "gallery": [
            "https://images.unsplash.com/photo-1452587925148-ce544e77e70d?w=600&q=80",
            "https://images.unsplash.com/photo-1460661419201-fd4cecdf8a8b?w=600&q=80",
            "https://images.unsplash.com/photo-1556909114-44e3e70034e2?w=600&q=80",
            "https://images.unsplash.com/photo-1513364776144-60967b0f800f?w=600&q=80",
            "https://images.unsplash.com/photo-1517697471339-4aa32003c11a?w=600&q=80",
            "https://images.unsplash.com/photo-1596464716127-f2a82984de30?w=600&q=80"
        ],
        "products": ["Art Supplies", "Model Kits", "Board Games", "Craft Materials", "DIY Kits", "Workshop Sessions"],
        "about": "A paradise for hobbyists and crafters. Find everything from paints and canvases to model kits and board games."
    },
    {
        "name": "Musical Instrument Store",
        "slug": "musical-instruments",
        "category": "Technology, Hobbies & Entertainment",
        "cat_index": 5,
        "emoji": "🎸",
        "tagline": "Play Your Heart Out",
        "desc": "A dynamic website for your music store — showcase instruments, audio gear, and offer lessons.",
        "colors": {"bg": "#EDF1F5", "accent": "#0145F2", "accent_light": "#e8efff", "text": "#0f172a"},
        "hero_img": "https://images.unsplash.com/photo-1493225457124-a3eb161ffa5f?w=1200&q=80",
        "gallery": [
            "https://images.unsplash.com/photo-1510915361894-db8b60106cb1?w=600&q=80",
            "https://images.unsplash.com/photo-1558098329-a11cff621064?w=600&q=80",
            "https://images.unsplash.com/photo-1525201548942-d8732f6617a0?w=600&q=80",
            "https://images.unsplash.com/photo-1520523839897-bd0b52f945a0?w=600&q=80",
            "https://images.unsplash.com/photo-1598488035139-bdbb2231ce04?w=600&q=80",
            "https://images.unsplash.com/photo-1507838153414-b4b713384a76?w=600&q=80"
        ],
        "products": ["Guitars", "Keyboards & Pianos", "Drums & Percussion", "Audio Equipment", "DJ Gear", "Music Accessories"],
        "about": "From beginner guitars to professional studio equipment — we're your one-stop music shop. Expert advice and lessons available."
    },
    {
        "name": "Pet Boutique",
        "slug": "pet-boutiques",
        "category": "Technology, Hobbies & Entertainment",
        "cat_index": 5,
        "emoji": "🐾",
        "tagline": "Everything Your Pet Loves",
        "desc": "An adorable website for your pet store — showcase products, grooming services, and pet care tips.",
        "colors": {"bg": "#EDF1F5", "accent": "#0145F2", "accent_light": "#e8efff", "text": "#0f172a"},
        "hero_img": "https://images.unsplash.com/photo-1601758228041-f3b2795255f1?w=1200&q=80",
        "gallery": [
            "https://images.unsplash.com/photo-1583511655857-d19b40a7a54e?w=600&q=80",
            "https://images.unsplash.com/photo-1602526430780-2017ecae1262?w=600&q=80",
            "https://images.unsplash.com/photo-1596854407944-bf87f6fdd49e?w=600&q=80",
            "https://images.unsplash.com/photo-1583337130417-13104dec14a2?w=600&q=80",
            "https://images.unsplash.com/photo-1623387641168-d9803ddd3f35?w=600&q=80",
            "https://images.unsplash.com/photo-1612196808214-b8e1d6145a8c?w=600&q=80"
        ],
        "products": ["Pet Food", "Toys & Accessories", "Grooming Services", "Health Supplements", "Pet Beds & Crates", "Clothing & Costumes"],
        "about": "Because your fur babies deserve the best. Premium pet food, toys, grooming, and healthcare products for dogs, cats, and more."
    },
    {
        "name": "Antique Shop & Art Gallery",
        "slug": "antique-art",
        "category": "Technology, Hobbies & Entertainment",
        "cat_index": 5,
        "emoji": "🏛️",
        "tagline": "Curated Art & Rare Collectibles",
        "desc": "A sophisticated website for your gallery — showcase artworks, antiques, and auction items.",
        "colors": {"bg": "#EDF1F5", "accent": "#0145F2", "accent_light": "#e8efff", "text": "#0f172a"},
        "hero_img": "https://images.unsplash.com/photo-1531913764164-f85c3e01e2da?w=1200&q=80",
        "gallery": [
            "https://images.unsplash.com/photo-1544967082-d9d25d867d66?w=600&q=80",
            "https://images.unsplash.com/photo-1579783902614-a3fb3927b6a5?w=600&q=80",
            "https://images.unsplash.com/photo-1518998053901-5348d3961a04?w=600&q=80",
            "https://images.unsplash.com/photo-1577720643272-265f09367456?w=600&q=80",
            "https://images.unsplash.com/photo-1531913764164-f85c3e01e2da?w=600&q=80",
            "https://images.unsplash.com/photo-1547826039-bfc35e0f1ea8?w=600&q=80"
        ],
        "products": ["Paintings & Prints", "Sculptures", "Vintage Furniture", "Rare Collectibles", "Handcrafted Art", "Exhibition Events"],
        "about": "A curated space for art lovers and collectors. Discover unique paintings, vintage finds, and handcrafted pieces with stories to tell."
    },

    # --- Category 7: Maintenance & Support Services ---
    {
        "name": "Laundry & Dry Cleaner",
        "slug": "laundry-dryclean",
        "category": "Maintenance & Support Services",
        "cat_index": 6,
        "emoji": "👔",
        "tagline": "Fresh, Clean, Perfectly Pressed",
        "desc": "A clean website for your laundry service — show services, pricing, and pickup/delivery options.",
        "colors": {"bg": "#F5F7F0", "accent": "#222022", "accent_light": "#e8eae0", "text": "#1a1a1a"},
        "hero_img": "https://images.unsplash.com/photo-1545173168-9f1947eebb7f?w=1200&q=80",
        "gallery": [
            "https://images.unsplash.com/photo-1582735689369-4fe89db7114c?w=600&q=80",
            "https://images.unsplash.com/photo-1517677208171-0bc6725a3e60?w=600&q=80",
            "https://images.unsplash.com/photo-1545173168-9f1947eebb7f?w=600&q=80",
            "https://images.unsplash.com/photo-1585659722983-3a675dabf23d?w=600&q=80",
            "https://images.unsplash.com/photo-1604335398980-ededccdcc37d?w=600&q=80",
            "https://images.unsplash.com/photo-1489274495757-95c7c837b101?w=600&q=80"
        ],
        "products": ["Wash & Fold", "Dry Cleaning", "Ironing & Pressing", "Stain Removal", "Curtain Cleaning", "Pickup & Delivery"],
        "about": "Professional laundry and dry cleaning services with free pickup and delivery. We handle your clothes with the same care as our own."
    },
    {
        "name": "Repair Shop",
        "slug": "repair-shops",
        "category": "Maintenance & Support Services",
        "cat_index": 6,
        "emoji": "🔧",
        "tagline": "We Fix Everything",
        "desc": "A practical website for your repair service — list your capabilities, pricing, and turnaround time.",
        "colors": {"bg": "#F5F7F0", "accent": "#222022", "accent_light": "#e8eae0", "text": "#1a1a1a"},
        "hero_img": "https://images.unsplash.com/photo-1581091226825-a6a2a5aee158?w=1200&q=80",
        "gallery": [
            "https://images.unsplash.com/photo-1597872200969-2b65d56bd16b?w=600&q=80",
            "https://images.unsplash.com/photo-1581092160562-40aa08e78837?w=600&q=80",
            "https://images.unsplash.com/photo-1621905250437-ce86e5c89b6d?w=600&q=80",
            "https://images.unsplash.com/photo-1588508065123-287b28e013da?w=600&q=80",
            "https://images.unsplash.com/photo-1597872200969-2b65d56bd16b?w=600&q=80",
            "https://images.unsplash.com/photo-1563770660941-20978e870e26?w=600&q=80"
        ],
        "products": ["Mobile Repair", "Laptop Service", "TV & AC Repair", "Appliance Fix", "Screen Replacement", "Data Recovery"],
        "about": "Expert repair services for all electronics and appliances. Quick turnaround, genuine parts, and warranty on all repairs."
    },
    {
        "name": "Print & Xerox Shop",
        "slug": "print-xerox",
        "category": "Maintenance & Support Services",
        "cat_index": 6,
        "emoji": "🖨️",
        "tagline": "Print, Copy, Create",
        "desc": "A functional website for your print shop — show services, pricing, and bulk order capabilities.",
        "colors": {"bg": "#F5F7F0", "accent": "#222022", "accent_light": "#e8eae0", "text": "#1a1a1a"},
        "hero_img": "https://images.unsplash.com/photo-1562654501-a0ccc0fc3fb1?w=1200&q=80",
        "gallery": [
            "https://images.unsplash.com/photo-1562654501-a0ccc0fc3fb1?w=600&q=80",
            "https://images.unsplash.com/photo-1585282263861-f55e341878f8?w=600&q=80",
            "https://images.unsplash.com/photo-1529612700005-e35391c2e2fa?w=600&q=80",
            "https://images.unsplash.com/photo-1611532736597-de2d4265fba3?w=600&q=80",
            "https://images.unsplash.com/photo-1517524008697-e204a0ab6556?w=600&q=80",
            "https://images.unsplash.com/photo-1614624532983-4ce03382d63d?w=600&q=80"
        ],
        "products": ["Color & B/W Printing", "Photocopying", "Lamination", "Binding & Spiral", "Business Cards", "Flex & Banner Printing"],
        "about": "High-quality printing and copying services at affordable rates. From single-page prints to bulk corporate orders — we deliver precision."
    },

    # --- Category 8: Retail Formats & Digital Commerce ---
    {
        "name": "Department Store",
        "slug": "department-stores",
        "category": "Retail Formats & Digital Commerce",
        "cat_index": 7,
        "emoji": "🏢",
        "tagline": "Fashion, Home & More — All In One",
        "desc": "A comprehensive website for your department store — highlight departments, brands, and weekly offers.",
        "colors": {"bg": "#EDF1F5", "accent": "#0145F2", "accent_light": "#e8efff", "text": "#0f172a"},
        "hero_img": "https://images.unsplash.com/photo-1472851294608-062f824d29cc?w=1200&q=80",
        "gallery": [
            "https://images.unsplash.com/photo-1441986300917-64674bd600d8?w=600&q=80",
            "https://images.unsplash.com/photo-1472851294608-062f824d29cc?w=600&q=80",
            "https://images.unsplash.com/photo-1567958451986-2de427a4a0be?w=600&q=80",
            "https://images.unsplash.com/photo-1556742049-0cfed4f6a45d?w=600&q=80",
            "https://images.unsplash.com/photo-1560472354-b33ff0c44a43?w=600&q=80",
            "https://images.unsplash.com/photo-1555529771-835f59fc5efa?w=600&q=80"
        ],
        "products": ["Men's Fashion", "Women's Wear", "Kids & Baby", "Home & Living", "Beauty & Grooming", "Electronics"],
        "about": "Your ultimate shopping destination. Multiple departments, top brands, and the latest collections — all under one roof with unbeatable deals."
    },
    {
        "name": "Discount Store",
        "slug": "discount-stores",
        "category": "Retail Formats & Digital Commerce",
        "cat_index": 7,
        "emoji": "💰",
        "tagline": "Maximum Value, Minimum Price",
        "desc": "An impactful website for your discount store — highlight deals, clearance sales, and value packs.",
        "colors": {"bg": "#EDF1F5", "accent": "#0145F2", "accent_light": "#e8efff", "text": "#0f172a"},
        "hero_img": "https://images.unsplash.com/photo-1607082348824-0a96f2a4b9da?w=1200&q=80",
        "gallery": [
            "https://images.unsplash.com/photo-1556742049-0cfed4f6a45d?w=600&q=80",
            "https://images.unsplash.com/photo-1441986300917-64674bd600d8?w=600&q=80",
            "https://images.unsplash.com/photo-1472851294608-062f824d29cc?w=600&q=80",
            "https://images.unsplash.com/photo-1567958451986-2de427a4a0be?w=600&q=80",
            "https://images.unsplash.com/photo-1560472354-b33ff0c44a43?w=600&q=80",
            "https://images.unsplash.com/photo-1607082348824-0a96f2a4b9da?w=600&q=80"
        ],
        "products": ["Clearance Deals", "Bulk Packs", "Dollar Items", "Seasonal Sales", "Overstock Finds", "Value Bundles"],
        "about": "The smartest way to shop — quality products at rock-bottom prices. New deals every week, savings on every visit."
    },
    {
        "name": "Pop-up Shop",
        "slug": "popup-shops",
        "category": "Retail Formats & Digital Commerce",
        "cat_index": 7,
        "emoji": "🎪",
        "tagline": "Limited Time, Unlimited Style",
        "desc": "A trendy website for your pop-up events — create buzz with countdown timers and exclusive launches.",
        "colors": {"bg": "#EDF1F5", "accent": "#0145F2", "accent_light": "#e8efff", "text": "#0f172a"},
        "hero_img": "https://images.unsplash.com/photo-1441986300917-64674bd600d8?w=1200&q=80",
        "gallery": [
            "https://images.unsplash.com/photo-1567958451986-2de427a4a0be?w=600&q=80",
            "https://images.unsplash.com/photo-1441986300917-64674bd600d8?w=600&q=80",
            "https://images.unsplash.com/photo-1472851294608-062f824d29cc?w=600&q=80",
            "https://images.unsplash.com/photo-1556742049-0cfed4f6a45d?w=600&q=80",
            "https://images.unsplash.com/photo-1560472354-b33ff0c44a43?w=600&q=80",
            "https://images.unsplash.com/photo-1607082348824-0a96f2a4b9da?w=600&q=80"
        ],
        "products": ["Exclusive Launches", "Limited Editions", "Flash Sales", "Brand Collaborations", "Seasonal Collections", "Art Exhibitions"],
        "about": "Catch the buzz before it's gone! Rotating brands, exclusive drops, and one-of-a-kind shopping experiences."
    },
    {
        "name": "Dark Store",
        "slug": "dark-stores",
        "category": "Retail Formats & Digital Commerce",
        "cat_index": 7,
        "emoji": "📦",
        "tagline": "Hyperlocal Delivery, Lightning Fast",
        "desc": "A sleek website for your dark store operations — showcase delivery zones, speed, and product range.",
        "colors": {"bg": "#EDF1F5", "accent": "#0145F2", "accent_light": "#e8efff", "text": "#0f172a"},
        "hero_img": "https://images.unsplash.com/photo-1553413077-190dd305871c?w=1200&q=80",
        "gallery": [
            "https://images.unsplash.com/photo-1553413077-190dd305871c?w=600&q=80",
            "https://images.unsplash.com/photo-1578575437130-527eed3abbec?w=600&q=80",
            "https://images.unsplash.com/photo-1565793298595-6a879b1d9492?w=600&q=80",
            "https://images.unsplash.com/photo-1618005198919-d3d4b5a92ead?w=600&q=80",
            "https://images.unsplash.com/photo-1586528116311-ad8dd3c8310d?w=600&q=80",
            "https://images.unsplash.com/photo-1531297484001-80022131f5a1?w=600&q=80"
        ],
        "products": ["10-Min Groceries", "Fresh Produce", "Snacks & Beverages", "Personal Care", "Pet Supplies", "Medicine Delivery"],
        "about": "A micro-fulfillment center designed for lightning-fast hyperlocal delivery. Order online, get it at your doorstep in minutes."
    },
    {
        "name": "E-commerce Marketplace",
        "slug": "ecommerce-marketplaces",
        "category": "Retail Formats & Digital Commerce",
        "cat_index": 7,
        "emoji": "🛍️",
        "tagline": "Shop Anything, Anytime, Anywhere",
        "desc": "A powerful website for your e-commerce platform — multi-vendor marketplace with modern UI.",
        "colors": {"bg": "#EDF1F5", "accent": "#0145F2", "accent_light": "#e8efff", "text": "#0f172a"},
        "hero_img": "https://images.unsplash.com/photo-1556742049-0cfed4f6a45d?w=1200&q=80",
        "gallery": [
            "https://images.unsplash.com/photo-1556742049-0cfed4f6a45d?w=600&q=80",
            "https://images.unsplash.com/photo-1441986300917-64674bd600d8?w=600&q=80",
            "https://images.unsplash.com/photo-1472851294608-062f824d29cc?w=600&q=80",
            "https://images.unsplash.com/photo-1607082348824-0a96f2a4b9da?w=600&q=80",
            "https://images.unsplash.com/photo-1460925895917-afdab827c52f?w=600&q=80",
            "https://images.unsplash.com/photo-1555529771-835f59fc5efa?w=600&q=80"
        ],
        "products": ["Electronics", "Fashion & Apparel", "Home & Kitchen", "Beauty & Health", "Sports & Outdoors", "Books & Media"],
        "about": "A complete digital marketplace connecting sellers with buyers across India. Millions of products, trusted sellers, and seamless delivery."
    },
]


# ============================================================
# HTML TEMPLATES
# ============================================================

def truncate_desc(text, max_len=155):
    """Truncate text at word boundary, adding ellipsis if needed."""
    if len(text) <= max_len:
        return text
    truncated = text[:max_len].rsplit(' ', 1)[0]
    return truncated.rstrip('.,;:!') + '...'


def get_related_shops(shop, max_count=4):
    """Return up to max_count other shops from the same category."""
    return [s for s in SHOPS if s["category"] == shop["category"] and s["slug"] != shop["slug"]][:max_count]

ICON_BY_SLUG = {
    "kirana-grocery": "shopping-cart",
    "green-grocers": "leaf",
    "dairy-booths": "milk",
    "butcheries-fishmongers": "drumstick",
    "supermarkets": "warehouse",
    "convenience-stores": "store",
    "bakeries": "cake-slice",
    "cafes-eateries": "coffee",
    "confectioneries": "candy",
    "delicatessens": "sandwich",
    "wine-spirit-shops": "wine",
    "pharmacies": "pill",
    "salons-barber": "scissors",
    "gyms-yoga": "dumbbell",
    "boutiques": "shirt",
    "footwear-stores": "footprints",
    "jewelry-stores": "gem",
    "tailor-shops": "ruler",
    "haberdasheries": "scissors-line-dashed",
    "hardware-stores": "hammer",
    "furniture-stores": "armchair",
    "home-goods": "house",
    "nurseries-garden": "sprout",
    "electronics-showrooms": "smartphone",
    "bookstores": "book-open",
    "stationery-shops": "pencil-ruler",
    "hobby-craft": "palette",
    "musical-instruments": "music",
    "pet-boutiques": "paw-print",
    "antique-art": "landmark",
    "laundry-dryclean": "shirt",
    "repair-shops": "wrench",
    "print-xerox": "printer",
    "department-stores": "building-2",
    "discount-stores": "badge-indian-rupee",
    "popup-shops": "tent",
    "dark-stores": "package",
    "ecommerce-marketplaces": "shopping-bag",
}


def icon_name(shop):
    """Return a Lucide icon name for a shop type."""
    return ICON_BY_SLUG.get(shop["slug"], "store")


def icon_markup(shop, class_name="brand-icon", label=None):
    """Generate Lucide icon markup for shop-specific visual marks."""
    aria = f' aria-label="{label}"' if label else ' aria-hidden="true"'
    return f'<span class="{class_name}"{aria}><i data-lucide="{icon_name(shop)}"></i></span>'


def lucide_init_script(path_prefix=""):
    """Load and initialize Lucide icons."""
    return '''<script src="https://unpkg.com/lucide@latest/dist/umd/lucide.min.js" defer></script>
    <script>
        window.addEventListener('DOMContentLoaded', function () {
            if (window.lucide) {
                window.lucide.createIcons();
            }
        });
    </script>'''


def lucide_fallback_css():
    """CSS fallback so icon containers remain visible if the icon script is blocked."""
    return '''i[data-lucide]{display:inline-block;width:1.15em;height:1.15em;position:relative;flex-shrink:0;}
        i[data-lucide]::before,i[data-lucide]::after{content:"";position:absolute;inset:18%;border:2px solid currentColor;border-radius:42% 58% 55% 45%;}
        i[data-lucide]::after{inset:42% 16% auto 16%;height:2px;border:0;background:currentColor;border-radius:99px;transform:rotate(-25deg);}
        svg.lucide{display:block;}'''


def related_links_html(shop):
    """Generate HTML for related solutions cross-links."""
    related = get_related_shops(shop)
    if not related:
        return ""
    cards = ""
    for r in related:
        cards += f'''
            <a href="{r["slug"]}.html" class="related-card" style="border-left:3px solid {r["colors"]["accent"]}; padding:12px 16px; text-decoration:none; color:inherit; border-radius:8px; background:#f9f9f9; display:flex; align-items:center; gap:10px;">
                {icon_markup(r, "related-icon")}
                <span style="font-weight:600; color:{r["colors"]["accent"]};">{r["name"]}</span>
            </a>'''
    return f'''
    <section style="padding:48px 0; background:#fff;">
        <div class="container">
            <h3 style="text-align:center; margin-bottom:24px; font-size:1.3rem; color:#333;">Related Solutions in {shop["category"]}</h3>
            <div style="display:grid; grid-template-columns:repeat(auto-fit, minmax(220px, 1fr)); gap:12px; max-width:800px; margin:0 auto;">
                {cards}
            </div>
            <p style="text-align:center; margin-top:20px;"><a href="../index.html#solutions" style="color:#555; font-size:0.95rem;">View all 38 business types &rarr;</a></p>
        </div>
    </section>'''


def brochure_template(shop):
    """Generate a brochure page for a shop type — shows 3 tier previews."""
    c = shop["colors"]
    desc = truncate_desc(shop["desc"])
    schema_json = '{"@context":"https://schema.org","@type":"Service","name":"' + shop["name"] + ' Website Design","description":"' + shop["desc"].replace('"', '\\"') + '","provider":{"@type":"Organization","name":"SA-Flow","url":"https://saflow.app"},"areaServed":"India","hasOfferCatalog":{"@type":"OfferCatalog","name":"Website Packages","itemListElement":[{"@type":"Offer","name":"Basic","price":"1500","priceCurrency":"INR"},{"@type":"Offer","name":"Medium","price":"2500","priceCurrency":"INR"},{"@type":"Offer","name":"Advanced","price":"5000","priceCurrency":"INR"}]}}'
    return f'''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <script async src="https://www.googletagmanager.com/gtag/js?id=G-G7QH2GJMM0"></script>
    <script>window.dataLayer=window.dataLayer||[];function gtag(){{dataLayer.push(arguments);}}gtag('js',new Date());gtag('config','G-G7QH2GJMM0');</script>
    <title>{shop["name"]} Website Design Starting ₹1,500 | SA-Flow India</title>
    <meta name="description" content="{shop["desc"]}">
    <meta name="robots" content="index, follow">
    <link rel="canonical" href="https://saflow.app/brochures/{shop['slug']}.html">
    <meta property="og:title" content="{shop['name']} Website Design Starting ₹1,500 | SA-Flow">
    <meta property="og:description" content="{shop['desc']}">
    <meta property="og:type" content="website">
    <meta property="og:url" content="https://saflow.app/brochures/{shop['slug']}.html">
    <meta property="og:image" content="https://saflow.app/og-image.png">
    <meta name="twitter:card" content="summary">
    <meta name="twitter:title" content="{shop['name']} Website Design Starting ₹1,500 | SA-Flow">
    <meta name="twitter:description" content="{shop['desc']}">
    <meta name="twitter:image" content="https://saflow.app/og-image.png">
    <link rel="icon" type="image/svg+xml" href="../favicon.svg">
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800;900&display=swap" rel="stylesheet">
    <style>
        *, *::before, *::after {{ margin:0; padding:0; box-sizing:border-box; }}
        :root {{ --bg: {c["bg"]}; --accent: {c["accent"]}; --accent-light: {c["accent_light"]}; --text: {c["text"]}; }}
        html {{ scroll-behavior: smooth; }}
        body {{ font-family: 'Inter', -apple-system, sans-serif; color: var(--text); background: #fff; line-height: 1.6; -webkit-font-smoothing: antialiased; }}
        a {{ color: inherit; text-decoration: none; }}
        .container {{ max-width: 1100px; margin: 0 auto; padding: 0 24px; }}
        {lucide_fallback_css()}

        /* Nav */
        .b-nav {{ position: sticky; top:0; z-index:100; background: rgba(255,255,255,0.9); backdrop-filter: blur(20px); border-bottom: 1px solid #f0f0f0; padding: 14px 0; }}
        .b-nav .container {{ display: flex; align-items: center; justify-content: space-between; }}
        .b-nav .logo {{ font-size: 20px; font-weight: 800; letter-spacing: -0.02em; display: flex; align-items: center; gap: 8px; }}
        .sa-icon, .brand-icon, .related-icon {{ display:inline-flex; align-items:center; justify-content:center; color:var(--accent); flex-shrink:0; }}
        .sa-icon svg {{ width:22px; height:22px; stroke-width:2.4; }}
        .brand-icon {{ width:64px; height:64px; border-radius:20px; background:rgba(255,255,255,0.14); border:1px solid rgba(255,255,255,0.22); backdrop-filter:blur(10px); margin-bottom:16px; }}
        .brand-icon svg {{ width:34px; height:34px; stroke-width:1.8; }}
        .related-icon {{ width:32px; height:32px; border-radius:10px; background:rgba(1,69,242,0.08); }}
        .related-icon svg {{ width:18px; height:18px; }}
        .b-nav .back {{ font-size: 14px; font-weight: 500; color: var(--accent); display: flex; align-items: center; gap: 4px; }}
        .b-nav .back:hover {{ text-decoration: underline; }}

        /* Hero */
        .b-hero {{ position: relative; height: 60vh; min-height: 400px; display: flex; align-items: flex-end; overflow: hidden; }}
        .b-hero img {{ position: absolute; inset:0; width:100%; height:100%; object-fit:cover; }}
        .b-hero-overlay {{ position: absolute; inset:0; background: linear-gradient(to top, rgba(0,0,0,0.75) 0%, rgba(0,0,0,0.1) 60%, transparent 100%); }}
        .b-hero-content {{ position:relative; z-index:1; padding: 48px 0; color: #fff; }}
        .b-hero-content h1 {{ font-size: clamp(32px, 5vw, 48px); font-weight: 900; letter-spacing: -0.03em; line-height: 1.1; margin-bottom: 8px; }}
        .b-hero-content p {{ font-size: 18px; opacity: 0.85; max-width: 500px; }}

        /* Section */
        .b-section {{ padding: 80px 0; }}
        .b-section:nth-child(even) {{ background: var(--bg); }}
        .b-section-title {{ font-size: clamp(24px, 4vw, 36px); font-weight: 800; letter-spacing: -0.02em; text-align: center; margin-bottom: 12px; }}
        .b-section-desc {{ text-align: center; color: #64748b; font-size: 16px; max-width: 500px; margin: 0 auto 48px; }}

        /* Tier Cards */
        .tiers {{ display: grid; grid-template-columns: repeat(3, 1fr); gap: 24px; }}
        .tier-card {{ background: #fff; border: 1px solid #e8e8e8; border-radius: 20px; overflow: hidden; transition: all 0.3s ease; }}
        .tier-card:hover {{ transform: translateY(-6px); box-shadow: 0 20px 40px rgba(0,0,0,0.1); }}
        .tier-card.featured {{ border-color: var(--accent); box-shadow: 0 0 0 2px var(--accent), 0 10px 30px rgba(0,0,0,0.08); }}
        .tier-preview {{ position: relative; height: 220px; overflow: hidden; background: var(--bg); }}
        .tier-preview img {{ width:100%; height:100%; object-fit:cover; transition: transform 0.5s ease; }}
        .tier-card:hover .tier-preview img {{ transform: scale(1.05); }}
        .tier-badge {{ position: absolute; top: 12px; left: 12px; background: var(--accent); color: #fff; font-size: 11px; font-weight: 700; padding: 4px 12px; border-radius: 100px; text-transform: uppercase; letter-spacing: 0.5px; }}
        .tier-body {{ padding: 24px; }}
        .tier-name {{ font-size: 13px; font-weight: 700; text-transform: uppercase; letter-spacing: 1px; color: var(--accent); margin-bottom: 4px; }}
        .tier-price {{ font-size: 36px; font-weight: 900; letter-spacing: -0.03em; margin-bottom: 8px; }}
        .tier-desc {{ font-size: 14px; color: #64748b; margin-bottom: 16px; }}
        .tier-features {{ list-style: none; margin-bottom: 20px; }}
        .tier-features li {{ display: flex; align-items: center; gap: 8px; font-size: 13px; padding: 6px 0; border-bottom: 1px solid #f5f5f5; }}
        .tier-features li::before {{ content: ""; width:7px; height:7px; border-radius:50%; background: var(--accent); flex-shrink:0; }}
        .tier-btn {{ display: block; text-align: center; padding: 14px; background: var(--accent); color: #fff; border-radius: 12px; font-size: 15px; font-weight: 600; transition: all 0.2s; }}
        .tier-btn:hover {{ filter: brightness(0.9); transform: translateY(-1px); }}
        .tier-btn.outline {{ background: transparent; color: var(--accent); border: 2px solid var(--accent); }}
        .tier-btn.outline:hover {{ background: var(--accent); color: #fff; }}

        /* Products Showcase */
        .products-grid {{ display: grid; grid-template-columns: repeat(3, 1fr); gap: 16px; }}
        .product-card {{ background: #fff; border-radius: 16px; overflow: hidden; border: 1px solid #f0f0f0; transition: all 0.3s; }}
        .product-card:hover {{ transform: translateY(-3px); box-shadow: 0 8px 24px rgba(0,0,0,0.08); }}
        .product-card img {{ width:100%; height: 180px; object-fit:cover; }}
        .product-card h4 {{ padding: 14px 16px; font-size: 15px; font-weight: 600; }}

        /* About */
        .about-grid {{ display: grid; grid-template-columns: 1fr 1fr; gap: 48px; align-items: center; }}
        .about-text h3 {{ font-size: 28px; font-weight: 800; letter-spacing: -0.02em; margin-bottom: 16px; }}
        .about-text p {{ color: #64748b; font-size: 16px; line-height: 1.7; }}
        .about-img {{ border-radius: 20px; overflow: hidden; }}
        .about-img img {{ width: 100%; height: 360px; object-fit: cover; }}

        /* CTA */
        .cta-section {{ text-align: center; padding: 80px 0; background: var(--accent); color: #fff; }}
        .cta-section h2 {{ font-size: clamp(28px, 4vw, 40px); font-weight: 900; letter-spacing: -0.03em; margin-bottom: 12px; }}
        .cta-section p {{ font-size: 17px; opacity: 0.8; margin-bottom: 32px; }}
        .cta-btn {{ display: inline-flex; padding: 16px 40px; background: #fff; color: var(--accent); font-size: 16px; font-weight: 700; border-radius: 100px; transition: all 0.2s; }}
        .cta-btn:hover {{ transform: translateY(-2px); box-shadow: 0 8px 20px rgba(0,0,0,0.2); }}

        /* Footer */
        .b-footer {{ background: #0f172a; color: #fff; padding: 32px 0; text-align: center; }}
        .b-footer p {{ font-size: 13px; opacity: 0.4; }}

        @media(max-width: 768px) {{
            .tiers {{ grid-template-columns: 1fr; max-width: 400px; margin: 0 auto; }}
            .products-grid {{ grid-template-columns: 1fr 1fr; }}
            .about-grid {{ grid-template-columns: 1fr; }}
            .b-hero {{ height: 50vh; }}
        }}
    </style>
</head>
<body>
    <nav class="b-nav">
        <div class="container">
            <a href="../index.html" class="logo"><span class="sa-icon" aria-hidden="true"><i data-lucide="zap"></i></span> SA-Flow</a>
            <a href="../index.html#solutions" class="back">← All Solutions</a>
        </div>
    </nav>

    <section class="b-hero">
        <img src="{shop["hero_img"]}" alt="{shop["name"]}" loading="eager">
        <div class="b-hero-overlay"></div>
        <div class="container b-hero-content">
            {icon_markup(shop, "brand-icon", shop["name"])}
            <h1>{shop["name"]} Website</h1>
            <p>{shop["tagline"]}</p>
        </div>
    </section>

    <section class="b-section">
        <div class="container">
            <h2 class="b-section-title">Choose Your Plan</h2>
            <p class="b-section-desc">{shop["desc"]}</p>
            <div class="tiers">
                <div class="tier-card">
                    <div class="tier-preview">
                        <img src="{shop["gallery"][0]}" alt="Basic Preview" loading="lazy">
                        <span class="tier-badge">Basic</span>
                    </div>
                    <div class="tier-body">
                        <div class="tier-name">Basic</div>
                        <div class="tier-price">₹1,500</div>
                        <p class="tier-desc">A single-page website to establish your online presence.</p>
                        <ul class="tier-features">
                            <li>Single landing page</li>
                            <li>Mobile responsive</li>
                            <li>6 product showcase</li>
                            <li>Google Maps embed</li>
                            <li>Contact form</li>
                            <li>Basic SEO</li>
                            <li>Delivery: 2–3 days</li>
                        </ul>
                        <a href="../examples/{shop["slug"]}/basic/index.html" class="tier-btn outline">View Demo →</a>
                    </div>
                </div>
                <div class="tier-card featured">
                    <div class="tier-preview">
                        <img src="{shop["gallery"][1]}" alt="Medium Preview" loading="lazy">
                        <span class="tier-badge">Popular</span>
                    </div>
                    <div class="tier-body">
                        <div class="tier-name">Medium</div>
                        <div class="tier-price">₹2,500</div>
                        <p class="tier-desc">A multi-page website with gallery, reviews, and more.</p>
                        <ul class="tier-features">
                            <li>3–5 custom pages</li>
                            <li>Image gallery + lightbox</li>
                            <li>Email contact form</li>
                            <li>Customer reviews</li>
                            <li>Social media integration</li>
                            <li>On-page SEO</li>
                            <li>Delivery: 5–7 days</li>
                        </ul>
                        <a href="../examples/{shop["slug"]}/medium/index.html" class="tier-btn">View Demo →</a>
                    </div>
                </div>
                <div class="tier-card">
                    <div class="tier-preview">
                        <img src="{shop["gallery"][2]}" alt="Advanced Preview" loading="lazy">
                        <span class="tier-badge">Premium</span>
                    </div>
                    <div class="tier-body">
                        <div class="tier-name">Advanced</div>
                        <div class="tier-price">₹5,000</div>
                        <p class="tier-desc">A fully-featured website with booking, blog, and advanced SEO.</p>
                        <ul class="tier-features">
                            <li>7–10+ custom pages</li>
                            <li>Online booking system</li>
                            <li>Blog &amp; FAQ</li>
                            <li>Testimonials carousel</li>
                            <li>Full SEO + Schema</li>
                            <li>Performance optimized</li>
                            <li>Delivery: 10–15 days</li>
                        </ul>
                        <a href="../examples/{shop["slug"]}/advanced/index.html" class="tier-btn outline">View Demo →</a>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <section class="b-section">
        <div class="container">
            <h2 class="b-section-title">What We Showcase</h2>
            <p class="b-section-desc">Products &amp; services sections tailored for your {shop["name"].lower()}.</p>
            <div class="products-grid">
                {"".join(f'<div class="product-card"><img src="{shop["gallery"][i]}" alt="{p}" loading="lazy"><h4>{p}</h4></div>' for i, p in enumerate(shop["products"][:6]))}
            </div>
        </div>
    </section>

    <section class="b-section">
        <div class="container">
            <div class="about-grid">
                <div class="about-text">
                    <h3>Built for {shop["name"]}s</h3>
                    <p>{shop["about"]}</p>
                    <p style="margin-top:16px; color: var(--accent); font-weight: 600;">Every website is customized with your real business details, photos, and branding.</p>
                </div>
                <div class="about-img">
                    <img src="{shop["hero_img"]}" alt="{shop["name"]}" loading="lazy">
                </div>
            </div>
        </div>
    </section>

    <section class="cta-section">
        <h2>Ready to get your {shop["name"]} online?</h2>
        <p>Contact us today and get started in under 48 hours.</p>
        <a href="../index.html#contact" class="cta-btn">Get Started — From ₹1,500</a>
    </section>

    {related_links_html(shop)}

    <footer class="b-footer">
        <div class="container">
            <p>&copy; 2026 SA-Flow. All rights reserved. | support@saflow.app | info@saflow.app | <a href="https://saflow.app" style="color:rgba(255,255,255,0.5)">saflow.app</a></p>
        </div>
    </footer>
    {lucide_init_script("../")}
</body>
</html>'''


def basic_template(shop):
    """Generate a basic single-page example website."""
    c = shop["colors"]
    meta_desc = truncate_desc(shop["about"])
    return f'''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <script async src="https://www.googletagmanager.com/gtag/js?id=G-G7QH2GJMM0"></script>
    <script>window.dataLayer=window.dataLayer||[];function gtag(){{dataLayer.push(arguments);}}gtag('js',new Date());gtag('config','G-G7QH2GJMM0');</script>
    <title>{shop["name"]} — {shop["tagline"]}</title>
    <meta name="description" content="{meta_desc}">
    <meta name="robots" content="index, follow">
    <link rel="canonical" href="https://saflow.app/examples/{shop['slug']}/basic/">
    <meta property="og:title" content="{shop['name']} — {shop['tagline']}">
    <meta property="og:description" content="{meta_desc}">
    <meta property="og:type" content="website">
    <meta property="og:url" content="https://saflow.app/examples/{shop['slug']}/basic/">
    <meta property="og:image" content="https://saflow.app/og-image.png">
    <meta name="twitter:card" content="summary">
    <meta name="twitter:title" content="{shop['name']} — Basic Website Demo">
    <meta name="twitter:description" content="{meta_desc}">
    <meta name="twitter:image" content="https://saflow.app/og-image.png">
    <link rel="icon" type="image/svg+xml" href="../../../favicon.svg">
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&display=swap" rel="stylesheet">
    <style>
        *,*::before,*::after{{ margin:0;padding:0;box-sizing:border-box; }}
        :root{{ --bg:{c["bg"]};--accent:{c["accent"]};--accent-light:{c["accent_light"]};--text:{c["text"]}; }}
        html{{ scroll-behavior:smooth; }}
        body{{ font-family:'Inter',-apple-system,sans-serif;color:var(--text);background:var(--bg);line-height:1.6;-webkit-font-smoothing:antialiased; }}
        a{{ color:inherit;text-decoration:none; }}
        .container{{ max-width:1000px;margin:0 auto;padding:0 20px; }}
        {lucide_fallback_css()}

        /* Demo Banner */
        .demo-banner{{ background:var(--accent);color:#fff;text-align:center;padding:8px;font-size:12px;font-weight:600; }}
        .demo-banner a{{ color:#fff;text-decoration:underline; }}
        .inline-icon,.shop-icon,.contact-icon{{ display:inline-flex;align-items:center;justify-content:center;flex-shrink:0; }}
        .inline-icon{{ width:16px;height:16px;margin-right:6px;vertical-align:-3px; }}
        .inline-icon svg{{ width:16px;height:16px; }}
        .shop-icon{{ width:34px;height:34px;border-radius:10px;background:var(--accent-light);color:var(--accent); }}
        .shop-icon svg{{ width:19px;height:19px;stroke-width:2; }}
        .contact-icon{{ width:18px;height:18px;margin-right:6px;vertical-align:-4px; }}
        .contact-icon svg{{ width:18px;height:18px; }}

        /* Nav */
        nav{{ background:#fff;padding:16px 0;border-bottom:1px solid rgba(0,0,0,0.06);position:sticky;top:0;z-index:50; }}
        nav .container{{ display:flex;align-items:center;justify-content:space-between; }}
        .shop-name{{ font-size:22px;font-weight:800;letter-spacing:-0.02em;display:flex;align-items:center;gap:8px; }}
        .nav-email{{ font-size:14px;font-weight:600;color:var(--accent); }}

        /* Hero */
        .hero{{ position:relative;height:70vh;min-height:400px;display:flex;align-items:center;justify-content:center;overflow:hidden;text-align:center;color:#fff; }}
        .hero img{{ position:absolute;inset:0;width:100%;height:100%;object-fit:cover; }}
        .hero-overlay{{ position:absolute;inset:0;background:linear-gradient(135deg,rgba(0,0,0,0.6),rgba(0,0,0,0.4)); }}
        .hero-text{{ position:relative;z-index:1;max-width:600px;padding:20px; }}
        .hero-text h1{{ font-size:clamp(28px,6vw,48px);font-weight:900;letter-spacing:-0.03em;line-height:1.1;margin-bottom:8px; }}
        .hero-text p{{ font-size:18px;opacity:0.9;margin-bottom:24px; }}
        .hero-btn{{ display:inline-flex;padding:14px 32px;background:var(--accent);color:#fff;border-radius:100px;font-weight:700;font-size:15px;transition:all 0.2s; }}
        .hero-btn:hover{{ filter:brightness(1.1);transform:translateY(-2px); }}

        /* Products */
        .section{{ padding:60px 0; }}
        .section:nth-child(even){{ background:#fff; }}
        .section-title{{ text-align:center;font-size:clamp(22px,4vw,32px);font-weight:800;letter-spacing:-0.02em;margin-bottom:32px; }}
        .products{{ display:grid;grid-template-columns:repeat(3,1fr);gap:16px; }}
        .product{{ background:#fff;border-radius:14px;overflow:hidden;border:1px solid rgba(0,0,0,0.06);transition:all 0.2s; }}
        .product:hover{{ transform:translateY(-3px);box-shadow:0 8px 20px rgba(0,0,0,0.08); }}
        .product img{{ width:100%;height:160px;object-fit:cover; }}
        .product h3{{ padding:14px 16px;font-size:15px;font-weight:600; }}

        /* Map */
        .map-frame{{ width:100%;height:300px;border:0;border-radius:14px; }}

        /* Contact */
        .contact-bar{{ background:var(--accent);color:#fff;padding:32px 0;text-align:center; }}
        .contact-bar h3{{ font-size:22px;font-weight:700;margin-bottom:8px; }}
        .contact-bar p{{ font-size:16px;opacity:0.85; }}

        /* Footer */
        footer{{ background:#111;color:#fff;padding:20px 0;text-align:center;font-size:12px;opacity:0.5; }}

        @media(max-width:640px){{ .products{{ grid-template-columns:1fr 1fr; }} .hero{{ height:50vh; }} }}
    </style>
</head>
<body>
    <div class="demo-banner">
        {icon_markup(shop, "inline-icon")} This is a BASIC tier demo — <a href="../../../brochures/{shop["slug"]}.html">View all plans</a> | Designed by <a href="../../../index.html">SA-Flow</a>
    </div>
    <nav>
        <div class="container">
            <div class="shop-name">{icon_markup(shop, "shop-icon")} {shop["name"]}</div>
            <div class="nav-email"><span class="contact-icon" aria-hidden="true"><i data-lucide="mail"></i></span> info@example.com</div>
        </div>
    </nav>
    <section class="hero">
        <img src="{shop["hero_img"]}" alt="{shop["name"]}">
        <div class="hero-overlay"></div>
        <div class="hero-text">
            <h1>{shop["tagline"]}</h1>
            <p>{shop["desc"][:100]}...</p>
            <a href="#contact" class="hero-btn">Contact Us</a>
        </div>
    </section>
    <section class="section">
        <div class="container">
            <h2 class="section-title">Our Products &amp; Services</h2>
            <div class="products">
                {"".join(f'<div class="product"><img src="{shop["gallery"][i]}" alt="{p}" loading="lazy"><h3>{p}</h3></div>' for i, p in enumerate(shop["products"][:6]))}
            </div>
        </div>
    </section>
    <section class="section" id="location">
        <div class="container">
            <h2 class="section-title">Find Us</h2>
            <iframe class="map-frame" src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d117235.18759521538!2d85.2493468!3d23.3440997!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x39f4e104aa5db7dd%3A0xdc09d49d6fee60df!2sRanchi%2C%20Jharkhand!5e0!3m2!1sen!2sin!4v1" allowfullscreen loading="lazy"></iframe>
        </div>
    </section>
    <section class="contact-bar" id="contact">
        <h3>Visit us today!</h3>
        <p>Main Road, Ranchi, Jharkhand — Email: info@example.com</p>
    </section>
    <footer><p>&copy; 2026 {shop["name"]}. Website by SA-Flow.</p></footer>
    {lucide_init_script("../../../")}
</body>
</html>'''


def medium_template(shop):
    """Generate a medium multi-section example website."""
    c = shop["colors"]
    meta_desc = truncate_desc(shop["about"])
    return f'''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <script async src="https://www.googletagmanager.com/gtag/js?id=G-G7QH2GJMM0"></script>
    <script>window.dataLayer=window.dataLayer||[];function gtag(){{dataLayer.push(arguments);}}gtag('js',new Date());gtag('config','G-G7QH2GJMM0');</script>
    <title>{shop["name"]} — {shop["tagline"]}</title>
    <meta name="description" content="{meta_desc}">
    <meta name="robots" content="index, follow">
    <link rel="canonical" href="https://saflow.app/examples/{shop['slug']}/medium/">
    <meta property="og:title" content="{shop['name']} — {shop['tagline']}">
    <meta property="og:description" content="{meta_desc}">
    <meta property="og:type" content="website">
    <meta property="og:url" content="https://saflow.app/examples/{shop['slug']}/medium/">
    <meta property="og:image" content="https://saflow.app/og-image.png">
    <meta name="twitter:card" content="summary">
    <meta name="twitter:title" content="{shop['name']} — Medium Website Demo">
    <meta name="twitter:description" content="{meta_desc}">
    <meta name="twitter:image" content="https://saflow.app/og-image.png">
    <link rel="icon" type="image/svg+xml" href="../../../favicon.svg">
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800;900&display=swap" rel="stylesheet">
    <style>
        *,*::before,*::after{{ margin:0;padding:0;box-sizing:border-box; }}
        :root{{ --bg:{c["bg"]};--accent:{c["accent"]};--accent-light:{c["accent_light"]};--text:{c["text"]}; }}
        html{{ scroll-behavior:smooth; }}
        body{{ font-family:'Inter',-apple-system,sans-serif;color:var(--text);background:#fff;line-height:1.6;-webkit-font-smoothing:antialiased; }}
        a{{ color:inherit;text-decoration:none; }}
        .container{{ max-width:1100px;margin:0 auto;padding:0 24px; }}
        {lucide_fallback_css()}

        /* Demo Banner */
        .demo-banner{{ background:var(--accent);color:#fff;text-align:center;padding:8px;font-size:12px;font-weight:600; }}
        .demo-banner a{{ color:#fff;text-decoration:underline; }}

        /* Nav */
        .m-nav{{ background:#fff;padding:14px 0;border-bottom:1px solid #f0f0f0;position:sticky;top:0;z-index:99;backdrop-filter:blur(10px); }}
        .m-nav .container{{ display:flex;align-items:center;justify-content:space-between; }}
        .m-logo{{ font-size:22px;font-weight:800;letter-spacing:-0.02em;display:flex;align-items:center;gap:8px; }}
        .m-links{{ display:flex;gap:28px; }}
        .m-links a{{ font-size:14px;font-weight:500;color:#64748b;transition:color 0.2s; }}
        .m-links a:hover{{ color:var(--accent); }}
        .m-cta{{ display:inline-flex;padding:8px 20px;background:var(--accent);color:#fff;border-radius:100px;font-size:13px;font-weight:600; }}

        /* Hero */
        .m-hero{{ position:relative;height:80vh;min-height:500px;display:flex;align-items:center;overflow:hidden; }}
        .m-hero img{{ position:absolute;inset:0;width:100%;height:100%;object-fit:cover; }}
        .m-hero-overlay{{ position:absolute;inset:0;background:linear-gradient(to right,rgba(0,0,0,0.7) 0%,rgba(0,0,0,0.3) 60%,rgba(0,0,0,0.15) 100%); }}
        .m-hero-content{{ position:relative;z-index:1;color:#fff;max-width:550px; }}
        .m-hero-content h1{{ font-size:clamp(32px,5vw,52px);font-weight:900;letter-spacing:-0.03em;line-height:1.08;margin-bottom:16px; }}
        .m-hero-content p{{ font-size:17px;opacity:0.85;margin-bottom:28px;line-height:1.7; }}
        .m-hero-actions{{ display:flex;gap:12px; }}
        .btn-hero{{ padding:14px 32px;border-radius:100px;font-weight:700;font-size:15px;transition:all 0.2s; }}
        .btn-hero.primary{{ background:#fff;color:var(--accent); }}
        .btn-hero.ghost{{ background:rgba(255,255,255,0.15);color:#fff;border:1px solid rgba(255,255,255,0.3); }}

        /* Sections */
        .m-section{{ padding:80px 0; }}
        .m-section:nth-child(even){{ background:var(--bg); }}
        .m-section-header{{ text-align:center;margin-bottom:48px; }}
        .m-section-header h2{{ font-size:clamp(26px,4vw,38px);font-weight:800;letter-spacing:-0.02em;margin-bottom:8px; }}
        .m-section-header p{{ color:#64748b;font-size:16px; }}

        /* Products Grid */
        .m-products{{ display:grid;grid-template-columns:repeat(3,1fr);gap:20px; }}
        .m-product{{ background:#fff;border-radius:16px;overflow:hidden;border:1px solid #eee;transition:all 0.3s; }}
        .m-product:hover{{ transform:translateY(-4px);box-shadow:0 12px 30px rgba(0,0,0,0.08); }}
        .m-product img{{ width:100%;height:200px;object-fit:cover; }}
        .m-product-body{{ padding:18px; }}
        .m-product-body h3{{ font-size:17px;font-weight:700;margin-bottom:4px; }}
        .m-product-body p{{ font-size:13px;color:#64748b; }}

        /* Gallery */
        .m-gallery{{ display:grid;grid-template-columns:repeat(3,1fr);gap:8px; }}
        .m-gallery img{{ width:100%;height:250px;object-fit:cover;border-radius:12px;cursor:pointer;transition:all 0.3s; }}
        .m-gallery img:hover{{ transform:scale(1.02);box-shadow:0 8px 24px rgba(0,0,0,0.12); }}

        /* Reviews */
        .m-reviews{{ display:grid;grid-template-columns:repeat(3,1fr);gap:20px; }}
        .m-review{{ background:#fff;border:1px solid #eee;border-radius:16px;padding:24px;transition:all 0.3s; }}
        .m-review:hover{{ box-shadow:0 8px 20px rgba(0,0,0,0.06); }}
        .m-review .stars{{ display:flex;gap:2px;color:#f59e0b;margin-bottom:10px; }}
        .m-review .stars i{{ width:16px;height:16px;fill:currentColor; }}
        .m-review p{{ font-size:14px;color:#475569;margin-bottom:12px;line-height:1.6; }}
        .m-review .author{{ font-size:13px;font-weight:600; }}

        /* About */
        .m-about{{ display:grid;grid-template-columns:1fr 1fr;gap:48px;align-items:center; }}
        .m-about img{{ width:100%;height:380px;object-fit:cover;border-radius:20px; }}
        .m-about-text h3{{ font-size:28px;font-weight:800;letter-spacing:-0.02em;margin-bottom:16px; }}
        .m-about-text p{{ color:#475569;font-size:15px;line-height:1.7;margin-bottom:12px; }}

        /* Contact */
        .m-contact{{ display:grid;grid-template-columns:1fr 1fr;gap:48px; }}
        .m-contact-info h3{{ font-size:24px;font-weight:800;margin-bottom:16px; }}
        .m-contact-info p{{ color:#475569;font-size:15px;margin-bottom:20px; }}
        .m-contact-detail{{ display:flex;align-items:center;gap:10px;font-size:15px;padding:8px 0; }}
        .m-form{{ background:var(--bg);border-radius:20px;padding:32px; }}
        .m-form input,.m-form textarea,.m-form select{{ width:100%;padding:12px 16px;border:1.5px solid #ddd;border-radius:10px;font-family:inherit;font-size:14px;margin-bottom:14px;background:#fff;outline:none;transition:border 0.2s; }}
        .m-form input:focus,.m-form textarea:focus{{ border-color:var(--accent); }}
        .m-form button{{ width:100%;padding:14px;background:var(--accent);color:#fff;border:none;border-radius:10px;font-family:inherit;font-size:15px;font-weight:700;cursor:pointer;transition:all 0.2s; }}
        .m-form button:hover{{ filter:brightness(0.9); }}

        /* Map */
        .m-map{{ width:100%;height:300px;border:0;border-radius:16px;margin-top:32px; }}

        /* Footer */
        .m-footer{{ background:#0f172a;color:#fff;padding:40px 0;text-align:center; }}
        .m-footer .social{{ display:flex;justify-content:center;gap:16px;margin-bottom:16px; }}
        .m-footer .social a{{ width:36px;height:36px;border-radius:50%;background:rgba(255,255,255,0.1);display:flex;align-items:center;justify-content:center;font-size:16px;transition:all 0.2s; }}
        .m-footer .social a:hover{{ background:var(--accent); }}
        .m-footer p{{ font-size:13px;opacity:0.4; }}

        @media(max-width:768px){{
            .m-links{{ display:none; }}
            .m-products,.m-reviews,.m-gallery{{ grid-template-columns:1fr; }}
            .m-about,.m-contact{{ grid-template-columns:1fr; }}
            .m-hero{{ height:60vh; }}
            .m-hero-actions{{ flex-direction:column; }}
        }}
    </style>
</head>
<body>
    <div class="demo-banner">
        {icon_markup(shop, "inline-icon")} This is a MEDIUM tier demo — <a href="../../../brochures/{shop["slug"]}.html">View all plans</a> | Designed by <a href="../../../index.html">SA-Flow</a>
    </div>

    <nav class="m-nav">
        <div class="container">
            <div class="m-logo">{icon_markup(shop, "shop-icon")} {shop["name"]}</div>
            <div class="m-links">
                <a href="#products">Products</a>
                <a href="#gallery">Gallery</a>
                <a href="#about">About</a>
                <a href="#reviews">Reviews</a>
                <a href="#contact">Contact</a>
            </div>
            <a href="#contact" class="m-cta">Get in Touch</a>
        </div>
    </nav>

    <section class="m-hero">
        <img src="{shop["hero_img"]}" alt="{shop["name"]}">
        <div class="m-hero-overlay"></div>
        <div class="container m-hero-content">
            <h1>{shop["tagline"]}</h1>
            <p>{shop["about"][:180]}...</p>
            <div class="m-hero-actions">
                <a href="#products" class="btn-hero primary">View Products</a>
                <a href="#contact" class="btn-hero ghost">Contact Us</a>
            </div>
        </div>
    </section>

    <section class="m-section" id="products">
        <div class="container">
            <div class="m-section-header">
                <h2>Our Products &amp; Services</h2>
                <p>Quality you can trust, variety you'll love</p>
            </div>
            <div class="m-products">
                {"".join(f'''<div class="m-product">
                    <img src="{shop["gallery"][i]}" alt="{p}" loading="lazy">
                    <div class="m-product-body">
                        <h3>{p}</h3>
                        <p>Premium quality products for your needs</p>
                    </div>
                </div>''' for i, p in enumerate(shop["products"][:6]))}
            </div>
        </div>
    </section>

    <section class="m-section" id="gallery">
        <div class="container">
            <div class="m-section-header">
                <h2>Gallery</h2>
                <p>Take a look inside our store</p>
            </div>
            <div class="m-gallery">
                {"".join(f'<img src="{img}" alt="Gallery" loading="lazy">' for img in shop["gallery"][:6])}
            </div>
        </div>
    </section>

    <section class="m-section" id="about">
        <div class="container">
            <div class="m-about">
                <img src="{shop["hero_img"]}" alt="{shop["name"]}" loading="lazy">
                <div class="m-about-text">
                    <h3>About Us</h3>
                    <p>{shop["about"]}</p>
                    <p>Visit us and experience the difference. We're located in the heart of Ranchi, serving customers with dedication and quality.</p>
                </div>
            </div>
        </div>
    </section>

    <section class="m-section" id="reviews">
        <div class="container">
            <div class="m-section-header">
                <h2>What Our Customers Say</h2>
                <p>Real reviews from real people</p>
            </div>
            <div class="m-reviews">
                <div class="m-review">
                    <div class="stars"><i data-lucide="star"></i><i data-lucide="star"></i><i data-lucide="star"></i><i data-lucide="star"></i><i data-lucide="star"></i></div>
                    <p>"Excellent quality and great service! Have been a regular customer for over 2 years now. Highly recommended!"</p>
                    <div class="author">— Rahul S.</div>
                </div>
                <div class="m-review">
                    <div class="stars"><i data-lucide="star"></i><i data-lucide="star"></i><i data-lucide="star"></i><i data-lucide="star"></i><i data-lucide="star"></i></div>
                    <p>"Best {shop["name"].lower()} in Ranchi! The staff is friendly and prices are very reasonable. Will definitely come back."</p>
                    <div class="author">— Priya M.</div>
                </div>
                <div class="m-review">
                    <div class="stars"><i data-lucide="star"></i><i data-lucide="star"></i><i data-lucide="star"></i><i data-lucide="star"></i><i data-lucide="star-half"></i></div>
                    <p>"Great variety and quality products. The store is well-organized and clean. Very satisfied with my experience."</p>
                    <div class="author">— Amit K.</div>
                </div>
            </div>
        </div>
    </section>

    <section class="m-section" id="contact">
        <div class="container">
            <div class="m-section-header">
                <h2>Contact Us</h2>
                <p>We'd love to hear from you</p>
            </div>
            <div class="m-contact">
                <div class="m-contact-info">
                    <h3>{shop["name"]}</h3>
                    <p>Visit us at our store or reach out through any of the channels below.</p>
                    <div class="m-contact-detail"><span class="contact-icon" aria-hidden="true"><i data-lucide="map-pin"></i></span> Main Road, Ranchi, Jharkhand - 834001</div>
                    <div class="m-contact-detail"><span class="contact-icon" aria-hidden="true"><i data-lucide="mail"></i></span> info@example.com</div>
                    <div class="m-contact-detail"><span class="contact-icon" aria-hidden="true"><i data-lucide="clock"></i></span> Mon-Sat: 9:00 AM - 9:00 PM</div>
                    <iframe class="m-map" src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d117235.18759521538!2d85.2493468!3d23.3440997!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x39f4e104aa5db7dd%3A0xdc09d49d6fee60df!2sRanchi%2C%20Jharkhand!5e0!3m2!1sen!2sin!4v1" allowfullscreen loading="lazy"></iframe>
                </div>
                <div class="m-form">
                    <h3 style="font-size:20px;font-weight:700;margin-bottom:20px;">Send us a message</h3>
                    <input type="text" placeholder="Your Name" required>
                    <input type="email" placeholder="Email Address" required>
                    <textarea rows="4" placeholder="Your Message"></textarea>
                    <button type="button" onclick="alert('Thank you! We will get back to you soon.')">Send Message</button>
                </div>
            </div>
        </div>
    </section>

    <footer class="m-footer">
        <div class="container">
            <div class="social">
                <a href="#" aria-label="Social feed"><span class="social-icon"><i data-lucide="share-2"></i></span></a>
                <a href="#" aria-label="Photo gallery"><span class="social-icon"><i data-lucide="camera"></i></span></a>
                <a href="#" aria-label="Messages"><span class="social-icon"><i data-lucide="message-circle"></i></span></a>
            </div>
            <p>&copy; 2026 {shop["name"]}. Website designed by <a href="../../../index.html" style="color:rgba(255,255,255,0.5)">SA-Flow</a> | <a href="https://saflow.app" style="color:rgba(255,255,255,0.4)">saflow.app</a></p>
        </div>
    </footer>
    {lucide_init_script("../../../")}
</body>
</html>'''


def advanced_template(shop):
    """Generate an advanced full-featured example website."""
    c = shop["colors"]
    meta_desc = truncate_desc(shop["about"])
    return f'''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <script async src="https://www.googletagmanager.com/gtag/js?id=G-G7QH2GJMM0"></script>
    <script>window.dataLayer=window.dataLayer||[];function gtag(){{dataLayer.push(arguments);}}gtag('js',new Date());gtag('config','G-G7QH2GJMM0');</script>
    <title>{shop["name"]} — {shop["tagline"]}</title>
    <meta name="description" content="{meta_desc}">
    <meta name="robots" content="index, follow">
    <link rel="canonical" href="https://saflow.app/examples/{shop['slug']}/advanced/">
    <meta property="og:title" content="{shop['name']} — {shop['tagline']}">
    <meta property="og:description" content="{meta_desc}">
    <meta property="og:type" content="website">
    <meta property="og:url" content="https://saflow.app/examples/{shop['slug']}/advanced/">
    <meta property="og:image" content="https://saflow.app/og-image.png">
    <meta name="twitter:card" content="summary">
    <meta name="twitter:title" content="{shop['name']} — Advanced Website Demo">
    <meta name="twitter:description" content="{meta_desc}">
    <meta name="twitter:image" content="https://saflow.app/og-image.png">
    <link rel="icon" type="image/svg+xml" href="../../../favicon.svg">
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800;900&display=swap" rel="stylesheet">
    <style>
        *,*::before,*::after{{ margin:0;padding:0;box-sizing:border-box; }}
        :root{{ --bg:{c["bg"]};--accent:{c["accent"]};--accent-light:{c["accent_light"]};--text:{c["text"]}; }}
        html{{ scroll-behavior:smooth; }}
        body{{ font-family:'Inter',-apple-system,sans-serif;color:var(--text);background:#fff;line-height:1.6;-webkit-font-smoothing:antialiased; }}
        a{{ color:inherit;text-decoration:none; }}
        .container{{ max-width:1200px;margin:0 auto;padding:0 24px; }}
        {lucide_fallback_css()}

        /* Demo Banner */
        .demo-banner{{ background:var(--accent);color:#fff;text-align:center;padding:10px;font-size:12px;font-weight:600; }}
        .demo-banner a{{ color:#fff;text-decoration:underline; }}
        .inline-icon,.shop-icon,.feature-icon,.info-lucide{{ display:inline-flex;align-items:center;justify-content:center;flex-shrink:0; }}
        .inline-icon{{ width:16px;height:16px;margin-right:6px;vertical-align:-3px; }}
        .inline-icon svg{{ width:16px;height:16px; }}
        .shop-icon{{ width:34px;height:34px;border-radius:10px;background:var(--accent-light);color:var(--accent); }}
        .shop-icon svg{{ width:19px;height:19px;stroke-width:2; }}
        .feature-icon svg{{ width:24px;height:24px;stroke-width:1.9; }}
        .info-lucide svg{{ width:20px;height:20px;stroke-width:2; }}

        /* Nav */
        .a-nav{{ background:rgba(255,255,255,0.92);backdrop-filter:blur(20px);padding:12px 0;border-bottom:1px solid rgba(0,0,0,0.04);position:sticky;top:0;z-index:100; }}
        .a-nav .container{{ display:flex;align-items:center;justify-content:space-between; }}
        .a-logo{{ font-size:24px;font-weight:900;letter-spacing:-0.03em;display:flex;align-items:center;gap:10px; }}
        .a-links{{ display:flex;gap:28px; }}
        .a-links a{{ font-size:14px;font-weight:500;color:#475569;transition:color 0.2s; }}
        .a-links a:hover{{ color:var(--accent); }}
        .a-nav-actions{{ display:flex;align-items:center;gap:12px; }}
        .a-cta{{ padding:10px 24px;background:var(--accent);color:#fff;border-radius:100px;font-size:14px;font-weight:600;transition:all 0.2s; }}
        .a-cta:hover{{ filter:brightness(0.9);transform:translateY(-1px); }}

        /* Hero — Advanced */
        .a-hero{{ position:relative;min-height:90vh;display:flex;align-items:center;overflow:hidden; }}
        .a-hero-bg{{ position:absolute;inset:0; }}
        .a-hero-bg img{{ width:100%;height:100%;object-fit:cover; }}
        .a-hero-bg::after{{ content:'';position:absolute;inset:0;background:linear-gradient(135deg,rgba(0,0,0,0.7) 0%,rgba(0,0,0,0.3) 50%,rgba(0,0,0,0.15) 100%); }}
        .a-hero-content{{ position:relative;z-index:1;color:#fff;max-width:650px; }}
        .a-hero-badge{{ display:inline-flex;align-items:center;gap:6px;padding:6px 14px;background:rgba(255,255,255,0.15);border:1px solid rgba(255,255,255,0.2);border-radius:100px;font-size:12px;font-weight:600;backdrop-filter:blur(10px);margin-bottom:24px; }}
        .a-hero-badge .dot{{ width:6px;height:6px;border-radius:50%;background:#22c55e; }}
        .a-hero-content h1{{ font-size:clamp(36px,6vw,64px);font-weight:900;letter-spacing:-0.04em;line-height:1.05;margin-bottom:20px; }}
        .a-hero-content p{{ font-size:18px;opacity:0.85;line-height:1.7;margin-bottom:32px;max-width:500px; }}
        .a-hero-btns{{ display:flex;gap:14px;flex-wrap:wrap; }}
        .btn-a{{ padding:16px 36px;border-radius:100px;font-weight:700;font-size:15px;transition:all 0.2s;cursor:pointer;border:none; }}
        .btn-a.primary{{ background:#fff;color:var(--accent); }}
        .btn-a.primary:hover{{ box-shadow:0 8px 20px rgba(0,0,0,0.2);transform:translateY(-2px); }}
        .btn-a.secondary{{ background:rgba(255,255,255,0.1);color:#fff;border:1.5px solid rgba(255,255,255,0.3);backdrop-filter:blur(5px); }}

        /* Sections */
        .a-section{{ padding:100px 0; }}
        .a-section.alt{{ background:var(--bg); }}
        .a-header{{ text-align:center;margin-bottom:56px; }}
        .a-tag{{ display:inline-block;font-size:12px;font-weight:700;text-transform:uppercase;letter-spacing:1.5px;color:var(--accent);margin-bottom:12px; }}
        .a-header h2{{ font-size:clamp(28px,4.5vw,44px);font-weight:800;letter-spacing:-0.03em;margin-bottom:10px; }}
        .a-header p{{ color:#64748b;font-size:17px;max-width:500px;margin:0 auto; }}

        /* Features Grid */
        .a-features{{ display:grid;grid-template-columns:repeat(3,1fr);gap:24px; }}
        .a-feature{{ background:#fff;border:1px solid #f0f0f0;border-radius:20px;padding:32px;transition:all 0.3s; }}
        .a-feature:hover{{ transform:translateY(-4px);box-shadow:0 12px 30px rgba(0,0,0,0.06);border-color:#ddd; }}
        .a-feature .icon{{ width:48px;height:48px;border-radius:14px;background:var(--accent-light);display:flex;align-items:center;justify-content:center;margin-bottom:16px;color:var(--accent); }}
        .a-feature h3{{ font-size:18px;font-weight:700;margin-bottom:6px; }}
        .a-feature p{{ font-size:14px;color:#64748b;line-height:1.6; }}

        /* Products — Advanced Layout */
        .a-products{{ display:grid;grid-template-columns:repeat(3,1fr);gap:24px; }}
        .a-prod{{ background:#fff;border-radius:20px;overflow:hidden;border:1px solid #f0f0f0;transition:all 0.3s;position:relative; }}
        .a-prod:hover{{ transform:translateY(-6px);box-shadow:0 16px 40px rgba(0,0,0,0.08); }}
        .a-prod img{{ width:100%;height:240px;object-fit:cover;transition:transform 0.5s; }}
        .a-prod:hover img{{ transform:scale(1.05); }}
        .a-prod-body{{ padding:20px; }}
        .a-prod-body h3{{ font-size:18px;font-weight:700;margin-bottom:4px; }}
        .a-prod-body p{{ font-size:13px;color:#64748b; }}

        /* Testimonials Carousel */
        .a-testimonials{{ display:grid;grid-template-columns:repeat(3,1fr);gap:24px; }}
        .a-testi{{ background:#fff;border:1px solid #eee;border-radius:20px;padding:32px;position:relative; }}
        .a-testi .quote{{ font-size:48px;color:var(--accent);opacity:0.15;line-height:1;position:absolute;top:16px;right:24px; }}
        .a-testi .stars{{ display:flex;gap:2px;color:#f59e0b;margin-bottom:12px; }}
        .a-testi .stars i{{ width:15px;height:15px;fill:currentColor; }}
        .a-testi p{{ font-size:15px;color:#475569;line-height:1.7;margin-bottom:16px; }}
        .a-testi .author{{ display:flex;align-items:center;gap:10px; }}
        .a-testi .avatar{{ width:38px;height:38px;border-radius:50%;background:var(--accent-light);display:flex;align-items:center;justify-content:center;font-size:16px;font-weight:700;color:var(--accent); }}
        .a-testi .author-info{{ font-size:14px; }}
        .a-testi .author-info strong{{ display:block;font-weight:600; }}
        .a-testi .author-info span{{ color:#94a3b8;font-size:12px; }}

        /* FAQ */
        .a-faq{{ max-width:700px;margin:0 auto; }}
        .faq-item{{ border-bottom:1px solid #eee;padding:20px 0; }}
        .faq-q{{ display:flex;justify-content:space-between;align-items:center;font-size:16px;font-weight:600;cursor:pointer;padding:4px 0; }}
        .faq-q span{{ transition:transform 0.2s; }}
        .faq-a{{ max-height:0;overflow:hidden;transition:max-height 0.3s ease;font-size:15px;color:#64748b;line-height:1.7; }}
        .faq-item.open .faq-a{{ max-height:200px;padding-top:12px; }}
        .faq-item.open .faq-q span{{ transform:rotate(45deg); }}

        /* Blog */
        .a-blog{{ display:grid;grid-template-columns:repeat(3,1fr);gap:24px; }}
        .blog-card{{ background:#fff;border-radius:20px;overflow:hidden;border:1px solid #f0f0f0;transition:all 0.3s; }}
        .blog-card:hover{{ transform:translateY(-4px);box-shadow:0 12px 30px rgba(0,0,0,0.06); }}
        .blog-card img{{ width:100%;height:200px;object-fit:cover; }}
        .blog-body{{ padding:20px; }}
        .blog-body .date{{ font-size:12px;color:#94a3b8;font-weight:600;text-transform:uppercase;letter-spacing:0.5px; }}
        .blog-body h3{{ font-size:17px;font-weight:700;margin:6px 0;line-height:1.3; }}
        .blog-body p{{ font-size:13px;color:#64748b; }}

        /* CTA */
        .a-cta-section{{ background:var(--accent);padding:80px 0;text-align:center;color:#fff; }}
        .a-cta-section h2{{ font-size:clamp(28px,4vw,42px);font-weight:900;letter-spacing:-0.03em;margin-bottom:12px; }}
        .a-cta-section p{{ font-size:17px;opacity:0.8;margin-bottom:32px;max-width:500px;margin-left:auto;margin-right:auto; }}
        .a-cta-btn{{ display:inline-flex;padding:16px 40px;background:#fff;color:var(--accent);font-weight:700;font-size:16px;border-radius:100px;transition:all 0.2s; }}
        .a-cta-btn:hover{{ box-shadow:0 8px 24px rgba(0,0,0,0.2);transform:translateY(-2px); }}

        /* Contact Advanced */
        .a-contact{{ display:grid;grid-template-columns:1fr 1fr;gap:60px; }}
        .a-contact-form{{ background:var(--bg);border-radius:24px;padding:40px; }}
        .a-contact-form h3{{ font-size:22px;font-weight:800;margin-bottom:24px; }}
        .a-input-row{{ display:grid;grid-template-columns:1fr 1fr;gap:14px; }}
        .a-input{{ width:100%;padding:14px 18px;border:1.5px solid #ddd;border-radius:12px;font-family:inherit;font-size:14px;background:#fff;outline:none;transition:border 0.2s;margin-bottom:14px; }}
        .a-input:focus{{ border-color:var(--accent); }}
        textarea.a-input{{ resize:vertical;min-height:100px; }}
        .a-submit{{ width:100%;padding:16px;background:var(--accent);color:#fff;border:none;border-radius:12px;font-family:inherit;font-size:16px;font-weight:700;cursor:pointer;transition:all 0.2s; }}
        .a-submit:hover{{ filter:brightness(0.9); }}
        .a-contact-info h3{{ font-size:24px;font-weight:800;margin-bottom:16px; }}
        .a-contact-info > p{{ color:#475569;font-size:15px;margin-bottom:24px;line-height:1.7; }}
        .a-info-item{{ display:flex;align-items:center;gap:12px;padding:10px 0;font-size:15px; }}
        .a-info-icon{{ width:40px;height:40px;border-radius:12px;background:var(--accent-light);display:flex;align-items:center;justify-content:center;color:var(--accent);flex-shrink:0; }}
        .a-map{{ width:100%;height:240px;border:0;border-radius:16px;margin-top:24px; }}

        /* Newsletter */
        .newsletter{{ background:var(--bg);border-radius:24px;padding:48px;text-align:center;margin-top:48px; }}
        .newsletter h3{{ font-size:22px;font-weight:800;margin-bottom:8px; }}
        .newsletter p{{ color:#64748b;font-size:15px;margin-bottom:24px; }}
        .nl-form{{ display:flex;gap:10px;max-width:450px;margin:0 auto; }}
        .nl-form input{{ flex:1;padding:14px 18px;border:1.5px solid #ddd;border-radius:12px;font-family:inherit;font-size:14px;outline:none; }}
        .nl-form button{{ padding:14px 28px;background:var(--accent);color:#fff;border:none;border-radius:12px;font-weight:700;cursor:pointer; }}

        /* Footer Advanced */
        .a-footer{{ background:#0f172a;color:#fff;padding:60px 0 24px; }}
        .a-footer-grid{{ display:grid;grid-template-columns:2fr 1fr 1fr 1fr;gap:40px;margin-bottom:40px; }}
        .a-footer-brand .logo{{ font-size:22px;font-weight:800;margin-bottom:12px;display:flex;align-items:center;gap:8px; }}
        .a-footer-brand p{{ font-size:14px;color:rgba(255,255,255,0.5);line-height:1.6; }}
        .a-footer-col h4{{ font-size:13px;font-weight:700;text-transform:uppercase;letter-spacing:1px;margin-bottom:16px;color:rgba(255,255,255,0.4); }}
        .a-footer-col a{{ display:block;font-size:14px;color:rgba(255,255,255,0.6);padding:4px 0;transition:color 0.2s; }}
        .a-footer-col a:hover{{ color:#fff; }}
        .a-footer-bottom{{ border-top:1px solid rgba(255,255,255,0.08);padding-top:24px;text-align:center;font-size:13px;color:rgba(255,255,255,0.3); }}

        @media(max-width:768px){{
            .a-links,.a-nav-actions{{ display:none; }}
            .a-features,.a-products,.a-testimonials,.a-blog{{ grid-template-columns:1fr; }}
            .a-contact,.a-footer-grid{{ grid-template-columns:1fr; }}
            .a-about{{ grid-template-columns:1fr; }}
            .a-hero{{ min-height:70vh; }}
            .a-input-row{{ grid-template-columns:1fr; }}
            .nl-form{{ flex-direction:column; }}
        }}

        /* FAQ Toggle Script Style */
        .faq-item {{ cursor:pointer; }}
    </style>
</head>
<body>
    <div class="demo-banner">
        {icon_markup(shop, "inline-icon")} This is an ADVANCED tier demo — <a href="../../../brochures/{shop["slug"]}.html">View all plans</a> | Designed by <a href="../../../index.html">SA-Flow</a>
    </div>

    <nav class="a-nav">
        <div class="container">
            <div class="a-logo">{icon_markup(shop, "shop-icon")} {shop["name"]}</div>
            <div class="a-links">
                <a href="#features">Features</a>
                <a href="#products">Products</a>
                <a href="#testimonials">Reviews</a>
                <a href="#blog">Blog</a>
                <a href="#faq">FAQ</a>
                <a href="#contact">Contact</a>
            </div>
            <div class="a-nav-actions">
                <a href="#contact" class="a-cta">Book Now</a>
            </div>
        </div>
    </nav>

    <section class="a-hero">
        <div class="a-hero-bg">
            <img src="{shop["hero_img"]}" alt="{shop["name"]}">
        </div>
        <div class="container a-hero-content">
            <div class="a-hero-badge"><span class="dot"></span> Now Open — Visit Today!</div>
            <h1>{shop["tagline"]}</h1>
            <p>{shop["about"][:200]}...</p>
            <div class="a-hero-btns">
                <a href="#products" class="btn-a primary">Explore Products</a>
                <a href="#contact" class="btn-a secondary">Book Appointment</a>
            </div>
        </div>
    </section>

    <section class="a-section" id="features">
        <div class="container">
            <div class="a-header">
                <div class="a-tag">Why Choose Us</div>
                <h2>What Makes Us Special</h2>
                <p>Reasons customers love shopping with us</p>
            </div>
            <div class="a-features">
                <div class="a-feature">
                    <div class="icon"><span class="feature-icon"><i data-lucide="badge-check"></i></span></div>
                    <h3>Premium Quality</h3>
                    <p>We source only the finest products to ensure you get the best quality every single time.</p>
                </div>
                <div class="a-feature">
                    <div class="icon"><span class="feature-icon"><i data-lucide="rocket"></i></span></div>
                    <h3>Fast Service</h3>
                    <p>Quick and efficient — we value your time and ensure a smooth, speedy experience.</p>
                </div>
                <div class="a-feature">
                    <div class="icon"><span class="feature-icon"><i data-lucide="badge-indian-rupee"></i></span></div>
                    <h3>Best Prices</h3>
                    <p>Competitive pricing without compromising quality. Get the best value for your money.</p>
                </div>
                <div class="a-feature">
                    <div class="icon"><span class="feature-icon"><i data-lucide="handshake"></i></span></div>
                    <h3>Expert Advice</h3>
                    <p>Our knowledgeable staff is always ready to help you make the right choice.</p>
                </div>
                <div class="a-feature">
                    <div class="icon"><span class="feature-icon"><i data-lucide="shield-check"></i></span></div>
                    <h3>Trusted &amp; Reliable</h3>
                    <p>Years of serving the community with honesty and integrity. Your trust is our foundation.</p>
                </div>
                <div class="a-feature">
                    <div class="icon"><span class="feature-icon"><i data-lucide="package"></i></span></div>
                    <h3>Home Delivery</h3>
                    <p>Can't visit? No worries! We deliver right to your doorstep within Ranchi city limits.</p>
                </div>
            </div>
        </div>
    </section>

    <section class="a-section alt" id="products">
        <div class="container">
            <div class="a-header">
                <div class="a-tag">Our Collection</div>
                <h2>Products &amp; Services</h2>
                <p>Explore our wide range of offerings</p>
            </div>
            <div class="a-products">
                {"".join(f'''<div class="a-prod">
                    <img src="{shop["gallery"][i]}" alt="{p}" loading="lazy">
                    <div class="a-prod-body">
                        <h3>{p}</h3>
                        <p>Top quality {p.lower()} for all your needs</p>
                    </div>
                </div>''' for i, p in enumerate(shop["products"][:6]))}
            </div>
        </div>
    </section>

    <section class="a-section" id="testimonials">
        <div class="container">
            <div class="a-header">
                <div class="a-tag">Testimonials</div>
                <h2>Loved by Customers</h2>
                <p>What people are saying about us</p>
            </div>
            <div class="a-testimonials">
                <div class="a-testi">
                    <div class="quote">"</div>
                    <div class="stars"><i data-lucide="star"></i><i data-lucide="star"></i><i data-lucide="star"></i><i data-lucide="star"></i><i data-lucide="star"></i></div>
                    <p>Absolutely the best {shop["name"].lower()} in Ranchi! The quality is unmatched and the staff goes above and beyond to help.</p>
                    <div class="author">
                        <div class="avatar">R</div>
                        <div class="author-info"><strong>Rahul S.</strong><span>Regular Customer</span></div>
                    </div>
                </div>
                <div class="a-testi">
                    <div class="quote">"</div>
                    <div class="stars"><i data-lucide="star"></i><i data-lucide="star"></i><i data-lucide="star"></i><i data-lucide="star"></i><i data-lucide="star"></i></div>
                    <p>Been coming here for years. Consistent quality, fair prices, and excellent customer service. Highly recommended!</p>
                    <div class="author">
                        <div class="avatar">P</div>
                        <div class="author-info"><strong>Priya M.</strong><span>Loyal Customer</span></div>
                    </div>
                </div>
                <div class="a-testi">
                    <div class="quote">"</div>
                    <div class="stars"><i data-lucide="star"></i><i data-lucide="star"></i><i data-lucide="star"></i><i data-lucide="star"></i><i data-lucide="star-half"></i></div>
                    <p>Great selection and the store is always well-organized. The home delivery option is a game-changer!</p>
                    <div class="author">
                        <div class="avatar">A</div>
                        <div class="author-info"><strong>Amit K.</strong><span>Verified Buyer</span></div>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <section class="a-section alt" id="blog">
        <div class="container">
            <div class="a-header">
                <div class="a-tag">Blog</div>
                <h2>Latest Updates</h2>
                <p>Tips, news, and insights from our team</p>
            </div>
            <div class="a-blog">
                <div class="blog-card">
                    <img src="{shop["gallery"][0]}" alt="Blog" loading="lazy">
                    <div class="blog-body">
                        <div class="date">March 15, 2026</div>
                        <h3>How to Choose the Best {shop["products"][0]} for Your Needs</h3>
                        <p>A comprehensive guide to making smart choices and getting the best value...</p>
                    </div>
                </div>
                <div class="blog-card">
                    <img src="{shop["gallery"][1]}" alt="Blog" loading="lazy">
                    <div class="blog-body">
                        <div class="date">March 8, 2026</div>
                        <h3>Top 5 Trends in {shop["category"]} for 2026</h3>
                        <p>Stay ahead of the curve with these emerging trends in the industry...</p>
                    </div>
                </div>
                <div class="blog-card">
                    <img src="{shop["gallery"][2]}" alt="Blog" loading="lazy">
                    <div class="blog-body">
                        <div class="date">February 28, 2026</div>
                        <h3>Customer Spotlight: Why Local Businesses Matter</h3>
                        <p>Hear from our customers about what makes shopping local so special...</p>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <section class="a-section" id="faq">
        <div class="container">
            <div class="a-header">
                <div class="a-tag">FAQ</div>
                <h2>Frequently Asked Questions</h2>
                <p>Quick answers to common questions</p>
            </div>
            <div class="a-faq">
                <div class="faq-item" onclick="this.classList.toggle('open')">
                    <div class="faq-q">What are your operating hours? <span>+</span></div>
                    <div class="faq-a">We're open Monday to Saturday, 9:00 AM to 9:00 PM. Sundays by appointment only.</div>
                </div>
                <div class="faq-item" onclick="this.classList.toggle('open')">
                    <div class="faq-q">Do you offer home delivery? <span>+</span></div>
                    <div class="faq-a">Yes! We offer free delivery within 5km of our store for orders above ₹500. Additional charges apply for farther distances.</div>
                </div>
                <div class="faq-item" onclick="this.classList.toggle('open')">
                    <div class="faq-q">Can I return or exchange products? <span>+</span></div>
                    <div class="faq-a">We accept returns and exchanges within 7 days of purchase with the original receipt. Products must be in their original condition.</div>
                </div>
                <div class="faq-item" onclick="this.classList.toggle('open')">
                    <div class="faq-q">Do you accept online payments? <span>+</span></div>
                    <div class="faq-a">Yes, we accept UPI (GPay, PhonePe, Paytm), credit/debit cards, and of course, cash.</div>
                </div>
                <div class="faq-item" onclick="this.classList.toggle('open')">
                    <div class="faq-q">How can I contact you for bulk orders? <span>+</span></div>
                    <div class="faq-a">For bulk orders, please send us an email at info@example.com. We offer special rates for wholesale buyers.</div>
                </div>
            </div>
        </div>
    </section>

    <section class="a-cta-section">
        <h2>Ready to Experience the Best?</h2>
        <p>Visit us today or book an appointment — we'd love to serve you!</p>
        <a href="#contact" class="a-cta-btn">Contact Us Now</a>
    </section>

    <section class="a-section" id="contact">
        <div class="container">
            <div class="a-header">
                <div class="a-tag">Get in Touch</div>
                <h2>Contact Us</h2>
                <p>We're here to help — reach out anytime</p>
            </div>
            <div class="a-contact">
                <div class="a-contact-form">
                    <h3>Send a Message</h3>
                    <div class="a-input-row">
                        <input class="a-input" type="text" placeholder="Full Name" required>
                        <input class="a-input" type="email" placeholder="Email Address" required>
                    </div>
                    <select class="a-input">
                        <option>Select Service</option>
                        {"".join(f"<option>{p}</option>" for p in shop["products"][:6])}
                    </select>
                    <textarea class="a-input" placeholder="Your Message" rows="4"></textarea>
                    <button class="a-submit" type="button" onclick="alert('Thank you! We will contact you shortly!')">Send Message</button>
                </div>
                <div class="a-contact-info">
                    <h3>{shop["name"]}</h3>
                    <p>{shop["about"][:120]}...</p>
                    <div class="a-info-item">
                        <div class="a-info-icon"><span class="info-lucide"><i data-lucide="map-pin"></i></span></div>
                        <div>Main Road, Ranchi<br>Jharkhand - 834001</div>
                    </div>
                    <div class="a-info-item">
                        <div class="a-info-icon"><span class="info-lucide"><i data-lucide="mail"></i></span></div>
                        <div>info@example.com</div>
                    </div>
                    <div class="a-info-item">
                        <div class="a-info-icon"><span class="info-lucide"><i data-lucide="clock"></i></span></div>
                        <div>Mon - Sat: 9 AM - 9 PM</div>
                    </div>
                    <iframe class="a-map" src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d117235.18759521538!2d85.2493468!3d23.3440997!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x39f4e104aa5db7dd%3A0xdc09d49d6fee60df!2sRanchi%2C%20Jharkhand!5e0!3m2!1sen!2sin!4v1" allowfullscreen loading="lazy"></iframe>
                </div>
            </div>

            <div class="newsletter">
                <h3>Subscribe to Our Newsletter</h3>
                <p>Get updates on new arrivals, offers, and tips straight to your inbox.</p>
                <div class="nl-form">
                    <input type="email" placeholder="your@email.com">
                    <button type="button" onclick="alert('Subscribed! Thank you.')">Subscribe</button>
                </div>
            </div>
        </div>
    </section>

    <footer class="a-footer">
        <div class="container">
            <div class="a-footer-grid">
                <div class="a-footer-brand">
                    <div class="logo">{icon_markup(shop, "shop-icon")} {shop["name"]}</div>
                    <p>{shop["about"][:120]}...</p>
                </div>
                <div class="a-footer-col">
                    <h4>Quick Links</h4>
                    <a href="#features">Why Us</a>
                    <a href="#products">Products</a>
                    <a href="#testimonials">Reviews</a>
                    <a href="#blog">Blog</a>
                </div>
                <div class="a-footer-col">
                    <h4>Services</h4>
                    {"".join(f'<a href="#products">{p}</a>' for p in shop["products"][:4])}
                </div>
                <div class="a-footer-col">
                    <h4>Contact</h4>
                    <a href="#">info@example.com</a>
                    <a href="#">Ranchi, Jharkhand</a>
                </div>
            </div>
            <div class="a-footer-bottom">
                &copy; 2026 {shop["name"]}. All rights reserved. | Website by <a href="../../../index.html" style="color:rgba(255,255,255,0.6);">SA-Flow</a> | <a href="https://saflow.app" style="color:rgba(255,255,255,0.4)">saflow.app</a>
            </div>
        </div>
    </footer>
    {lucide_init_script("../../../")}
</body>
</html>'''


# ============================================================
# GENERATOR
# ============================================================
def generate_all():
    total = 0

    for shop in SHOPS:
        slug = shop["slug"]

        # 1. Brochure page
        brochure_dir = os.path.join(BASE_DIR, "brochures")
        os.makedirs(brochure_dir, exist_ok=True)
        with open(os.path.join(brochure_dir, f"{slug}.html"), "w", encoding="utf-8") as f:
            f.write(brochure_template(shop))
        total += 1

        # 2. Basic example
        basic_dir = os.path.join(BASE_DIR, "examples", slug, "basic")
        os.makedirs(basic_dir, exist_ok=True)
        with open(os.path.join(basic_dir, "index.html"), "w", encoding="utf-8") as f:
            f.write(basic_template(shop))
        total += 1

        # 3. Medium example
        medium_dir = os.path.join(BASE_DIR, "examples", slug, "medium")
        os.makedirs(medium_dir, exist_ok=True)
        with open(os.path.join(medium_dir, "index.html"), "w", encoding="utf-8") as f:
            f.write(medium_template(shop))
        total += 1

        # 4. Advanced example
        advanced_dir = os.path.join(BASE_DIR, "examples", slug, "advanced")
        os.makedirs(advanced_dir, exist_ok=True)
        with open(os.path.join(advanced_dir, "index.html"), "w", encoding="utf-8") as f:
            f.write(advanced_template(shop))
        total += 1

        print(f"  Generated {shop['name']} - brochure + 3 tiers")

    print(f"\n{'='*50}")
    print(f"  Generated {total} files for {len(SHOPS)} shop types!")
    print(f"  Brochures: {len(SHOPS)} files")
    print(f"  Examples: {len(SHOPS) * 3} files")
    print(f"{'='*50}")


if __name__ == "__main__":
    print("SA-Flow Website Generator")
    print("=" * 50)
    generate_all()
