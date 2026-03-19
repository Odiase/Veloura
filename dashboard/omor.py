me = [
{
    "model": "contenttypes.contenttype",
    "fields": {
        "app_label": "admin",
        "model": "logentry"
    }
},
{
    "model": "contenttypes.contenttype",
    "fields": {
        "app_label": "auth",
        "model": "group"
    }
},
{
    "model": "contenttypes.contenttype",
    "fields": {
        "app_label": "auth",
        "model": "permission"
    }
},
{
    "model": "contenttypes.contenttype",
    "fields": {
        "app_label": "auth",
        "model": "user"
    }
},
{
    "model": "contenttypes.contenttype",
    "fields": {
        "app_label": "contenttypes",
        "model": "contenttype"
    }
},
{
    "model": "contenttypes.contenttype",
    "fields": {
        "app_label": "sessions",
        "model": "session"
    }
},
{
    "model": "contenttypes.contenttype",
    "fields": {
        "app_label": "dashboard",
        "model": "dashboardstats"
    }
},
{
    "model": "contenttypes.contenttype",
    "fields": {
        "app_label": "store",
        "model": "category"
    }
},
{
    "model": "contenttypes.contenttype",
    "fields": {
        "app_label": "store",
        "model": "customer"
    }
},
{
    "model": "contenttypes.contenttype",
    "fields": {
        "app_label": "store",
        "model": "order"
    }
},
{
    "model": "contenttypes.contenttype",
    "fields": {
        "app_label": "store",
        "model": "orderitem"
    }
},
{
    "model": "contenttypes.contenttype",
    "fields": {
        "app_label": "store",
        "model": "product"
    }
},
{
    "model": "sessions.session",
    "pk": "5w6ros1qwje7t61gceg0pmr305i2zgwm",
    "fields": {
        "session_data": ".eJxVjDEOwjAMAP_iGUVOKE3Skb1viOzYkAJKpaadEH9HlTrAene6NyTa1pK2pkuaBAawcPplTPmpdRfyoHqfTZ7rukxs9sQctplxFn1dj_ZvUKgVGKDL6lE5EIdeKXhn_Vn0El2MKhgy2cjZEhORlxic7_0NETUGRlLs4PMF_Pc4Yg:1w3CxS:_mpf9ecrunyHUTBhwu3uR4vPsA2sepgkn7LRgvljGcc",
        "expire_date": "2026-04-02T12:58:38.554Z"
    }
},
{
    "model": "dashboard.dashboardstats",
    "pk": 2,
    "fields": {
        "total_revenue": "2450.00",
        "total_orders": 90,
        "total_customers": 75,
        "conversion_rate": 4.5,
        "avg_order_value": "27.00",
        "business_age_months": 3,
        "initial_investment": "900.00",
        "current_revenue": "2450.00",
        "monthly_revenue": [
            700,
            800,
            950
        ],
        "monthly_orders": [
            25,
            30,
            35
        ],
        "category_revenue": {
            "Makeup": 1000,
            "Skincare": 900,
            "Haircare": 550
        },
        "category_orders": {
            "Makeup": 35,
            "Skincare": 30,
            "Haircare": 25
        },
        "updated_at": "2026-03-19T14:36:24.787Z"
    }
},
{
    "model": "store.category",
    "pk": 1,
    "fields": {
        "name": "skincare"
    }
},
{
    "model": "store.category",
    "pk": 2,
    "fields": {
        "name": "haircare"
    }
},
{
    "model": "store.category",
    "pk": 3,
    "fields": {
        "name": "makeup"
    }
},
{
    "model": "store.category",
    "pk": 4,
    "fields": {
        "name": "Haircare"
    }
},
{
    "model": "store.category",
    "pk": 5,
    "fields": {
        "name": "Skincare"
    }
},
{
    "model": "store.category",
    "pk": 6,
    "fields": {
        "name": "Makeup"
    }
},
{
    "model": "store.product",
    "pk": 93,
    "fields": {
        "category": 5,
        "name": "Night Cream",
        "description": "A luxury night cream for your daily routine.",
        "price": "18.00",
        "old_price": "21.99",
        "image": "https://www.cerave.com/-/media/project/loreal/brand-sites/cerave/americas/us/skincare/2025/skin-renewing-night-cream/700x785/skin-renewing-night-cream-packshot-front-700x785-v1.jpg?rev=e26e5d7b923b47a",
        "is_best_selling": False,
        "created_at": "2026-03-19T15:15:11.850Z"
    }
},
{
    "model": "store.product",
    "pk": 94,
    "fields": {
        "category": 4,
        "name": "Multi-Action Foam Cleanser",
        "description": "A luxury oat cleanser for your daily routine.",
        "price": "68.78",
        "old_price": "82.54",
        "image": "https://images.unsplash.com/photo-1598440947619-2c35fc9aa908?q=80&w=800",
        "is_best_selling": False,
        "created_at": "2026-03-19T15:15:11.853Z"
    }
},
{
    "model": "store.product",
    "pk": 95,
    "fields": {
        "category": 5,
        "name": "Brightening Mask",
        "description": "A luxury brightening mask for your daily routine.",
        "price": "5.00",
        "old_price": "8.00",
        "image": "https://static.beautytocare.com/cdn-cgi/image/width=1440,height=1200,f=auto/media/catalog/product//y/o/youth-lab-brightening-boom-mask-23g.jpg",
        "is_best_selling": False,
        "created_at": "2026-03-19T15:15:11.857Z"
    }
},
{
    "model": "store.product",
    "pk": 96,
    "fields": {
        "category": 5,
        "name": "Hyaluronic Drops",
        "description": "A luxury hyaluronic drops for your daily routine.",
        "price": "50.00",
        "old_price": "65.00",
        "image": "https://groziokosmetika.lt/462-large_default/fusion-hyaluronic-drops.jpg",
        "is_best_selling": True,
        "created_at": "2026-03-19T15:15:11.859Z"
    }
},
{
    "model": "store.product",
    "pk": 97,
    "fields": {
        "category": 5,
        "name": "Facial Mist",
        "description": "A luxury facial mist for your daily routine.",
        "price": "1.50",
        "old_price": "4.00",
        "image": "https://i5.walmartimages.com/seo/Garnier-SkinActive-Soothing-Facial-Mist-4-4-fl-oz_f26ff991-6594-4256-b6d7-a46fe7bcc2d8_1.8b9ec05960a0cfdfc1d8af2e784d2fe4.jpeg",
        "is_best_selling": False,
        "created_at": "2026-03-19T15:15:11.863Z"
    }
},
{
    "model": "store.product",
    "pk": 98,
    "fields": {
        "category": 5,
        "name": "Gentle Cleanser",
        "description": "A luxury mineral spf for your daily routine.",
        "price": "8.00",
        "old_price": "12.00",
        "image": "https://images.unsplash.com/photo-1556228720-195a672e8a03?q=80&w=800",
        "is_best_selling": False,
        "created_at": "2026-03-19T15:15:11.866Z"
    }
},
{
    "model": "store.product",
    "pk": 99,
    "fields": {
        "category": 5,
        "name": "Body Lotion",
        "description": "A luxury renewal oil for your daily routine.",
        "price": "25.00",
        "old_price": "30.00",
        "image": "https://images.unsplash.com/photo-1620916566398-39f1143ab7be?q=80&w=800",
        "is_best_selling": True,
        "created_at": "2026-03-19T15:15:11.869Z"
    }
},
{
    "model": "store.product",
    "pk": 100,
    "fields": {
        "category": 5,
        "name": "Detox Scrub",
        "description": "A luxury detox scrub for your daily routine.",
        "price": "12.00",
        "old_price": "15.00",
        "image": "https://images.ctfassets.net/xvcg1y2kwpfh/J127ms9Vec6dO2uDOAsco/50a600e86b7492b21ee61cae87aedd70/skin-detox-cooling-scrub-en-ae?fm=webp&w=1024",
        "is_best_selling": True,
        "created_at": "2026-03-19T15:15:11.872Z"
    }
},
{
    "model": "store.product",
    "pk": 101,
    "fields": {
        "category": 5,
        "name": "Caffeine Gel",
        "description": "A luxury caffeine gel for your daily routine.",
        "price": "9.50",
        "old_price": "13.50",
        "image": "https://www.scienceinsport.com/media/catalog/product/c/a/caff_gel_citrus_render.jpg?optimize=medium&fit=bounds&height=680&width=680&canvas=680:680",
        "is_best_selling": False,
        "created_at": "2026-03-19T15:15:11.875Z"
    }
},
{
    "model": "store.product",
    "pk": 106,
    "fields": {
        "category": 4,
        "name": "bamboo fibers shampoo",
        "description": "A luxury defense moisturizer for your daily routine.",
        "price": "10.79",
        "old_price": "14.99",
        "image": "https://images.unsplash.com/photo-1535585209827-a15fcdbc4c2d?q=80&w=800",
        "is_best_selling": True,
        "created_at": "2026-03-19T15:15:11.891Z"
    }
},
{
    "model": "store.product",
    "pk": 109,
    "fields": {
        "category": 5,
        "name": "Seaweed Mask",
        "description": "A luxury seaweed mask for your daily routine.",
        "price": "1.00",
        "old_price": "3.00",
        "image": "https://ng.jumia.is/unsafe/fit-in/500x500/filters:fill(white)/product/73/5374763/1.jpg?1966",
        "is_best_selling": False,
        "created_at": "2026-03-19T15:15:11.900Z"
    }
},
{
    "model": "store.product",
    "pk": 110,
    "fields": {
        "category": 5,
        "name": "Face Oil",
        "description": "A luxury face oil for your daily routine.",
        "price": "31.00",
        "old_price": "38.00",
        "image": "https://www.scratchgoods.com/cdn/shop/products/DSC_6636_840x.jpg?v=1573445355",
        "is_best_selling": False,
        "created_at": "2026-03-19T15:15:11.903Z"
    }
},
{
    "model": "store.product",
    "pk": 112,
    "fields": {
        "category": 6,
        "name": "Matte Lipstick",
        "description": "A luxury matte lipstick for your daily routine.",
        "price": "77.16",
        "old_price": "92.59",
        "image": "https://images.unsplash.com/photo-1512496015851-a90fb38ba796?q=80&w=800",
        "is_best_selling": True,
        "created_at": "2026-03-19T15:15:11.909Z"
    }
},
{
    "model": "store.product",
    "pk": 113,
    "fields": {
        "category": 6,
        "name": "Silk Foundation",
        "description": "A luxury silk foundation for your daily routine.",
        "price": "55.28",
        "old_price": "66.34",
        "image": "https://images.unsplash.com/photo-1522335789203-aabd1fc54bc9?q=80&w=800",
        "is_best_selling": False,
        "created_at": "2026-03-19T15:15:11.913Z"
    }
},
{
    "model": "store.product",
    "pk": 114,
    "fields": {
        "category": 6,
        "name": "Volumizing Mascara",
        "description": "A luxury volumizing mascara for your daily routine.",
        "price": "12.00",
        "old_price": "15.00",
        "image": "https://cloudinary.images-iherb.com/image/upload/f_auto,q_auto:eco/images/loe/loe01934/v/21.jpg",
        "is_best_selling": False,
        "created_at": "2026-03-19T15:15:11.916Z"
    }
},
{
    "model": "store.product",
    "pk": 115,
    "fields": {
        "category": 6,
        "name": "Finishing Powder",
        "description": "A luxury finishing powder for your daily routine.",
        "price": "64.36",
        "old_price": "77.23",
        "image": "https://images.unsplash.com/photo-1516975080664-ed2fc6a32937?q=80&w=800",
        "is_best_selling": False,
        "created_at": "2026-03-19T15:15:11.919Z"
    }
},
{
    "model": "store.product",
    "pk": 118,
    "fields": {
        "category": 6,
        "name": "Blush Palette",
        "description": "A luxury blush palette for your daily routine.",
        "price": "10.00",
        "old_price": "18.00",
        "image": "https://m.media-amazon.com/images/I/41I0GKG3OjL._SY300_SX300_QL70_FMwebp_.jpg",
        "is_best_selling": False,
        "created_at": "2026-03-19T15:15:11.929Z"
    }
},
{
    "model": "store.product",
    "pk": 119,
    "fields": {
        "category": 6,
        "name": "Liquid Eyeliner",
        "description": "A luxury liquid eyeliner for your daily routine.",
        "price": "52.19",
        "old_price": "62.63",
        "image": "https://images.unsplash.com/photo-1627384113743-6bd5a479fffd?q=80&w=800",
        "is_best_selling": False,
        "created_at": "2026-03-19T15:15:11.932Z"
    }
},
{
    "model": "store.product",
    "pk": 120,
    "fields": {
        "category": 6,
        "name": "Hydrating Lip Oil",
        "description": "A luxury hydrating lip oil for your daily routine.",
        "price": "1.00",
        "old_price": "1.50",
        "image": "https://i5.walmartimages.com/seo/Kiss-hydrating-clear-lip-gloss-lip-oil-treatment-0-34oz_d4eaeaf5-d6c0-4ec3-896d-ba0498fbd2e2.249740be6cc7bf81a8d9fe5ab61b278e.jpeg",
        "is_best_selling": True,
        "created_at": "2026-03-19T15:15:11.935Z"
    }
},
{
    "model": "store.product",
    "pk": 121,
    "fields": {
        "category": 6,
        "name": "Primer Base",
        "description": "A luxury primer base for your daily routine.",
        "price": "41.12",
        "old_price": "45.00",
        "image": "https://www.lancome-usa.com/dw/image/v2/AANG_PRD/on/demandware.static/-/Sites-lancome-us-master-catalog/default/dwc2f8a258/pdp/1000205/La-Base-Pro_Packshot.jpg?sw=1356&sh=1356&sm=cut&sfrm=png&q=70",
        "is_best_selling": True,
        "created_at": "2026-03-19T15:15:11.938Z"
    }
},
{
    "model": "store.product",
    "pk": 122,
    "fields": {
        "category": 6,
        "name": "Matte Lipstick",
        "description": "A luxury brow gel for your daily routine.",
        "price": "2.00",
        "old_price": "4.00",
        "image": "https://images.unsplash.com/photo-1625093742435-6fa192b6fb10?q=80&w=800",
        "is_best_selling": False,
        "created_at": "2026-03-19T15:15:11.941Z"
    }
},
{
    "model": "store.product",
    "pk": 123,
    "fields": {
        "category": 6,
        "name": "Brown Skin Powder",
        "description": "A luxury brow pencil for your daily routine.",
        "price": "39.21",
        "old_price": "47.05",
        "image": "https://images.unsplash.com/photo-1515688594390-b649af70d282?q=80&w=800",
        "is_best_selling": False,
        "created_at": "2026-03-19T15:15:11.944Z"
    }
},
{
    "model": "store.product",
    "pk": 128,
    "fields": {
        "category": 6,
        "name": "Lip Liner",
        "description": "A luxury lip liner for your daily routine.",
        "price": "14.99",
        "old_price": "22.00",
        "image": "https://www.vievebeauty.com/cdn/shop/files/vieve-tailored-dark-brown-lip-liner-5_4c54a049-9ce7-49e5-8612-f091a4da8d0f.jpg?v=1743695882&width=990",
        "is_best_selling": True,
        "created_at": "2026-03-19T15:15:11.959Z"
    }
},
{
    "model": "store.product",
    "pk": 130,
    "fields": {
        "category": 6,
        "name": "Lip Stain",
        "description": "A luxury lip stain for your daily routine.",
        "price": "18.19",
        "old_price": "25.00",
        "image": "https://images-na.ssl-images-amazon.com/images/I/71QN+W-iLzL._AC_UL900_SR900,600_.jpg",
        "is_best_selling": False,
        "created_at": "2026-03-19T15:15:11.965Z"
    }
},
{
    "model": "store.product",
    "pk": 131,
    "fields": {
        "category": 6,
        "name": "Eye Primer",
        "description": "A luxury eye primer for your daily routine.",
        "price": "15.00",
        "old_price": "23.50",
        "image": "https://static.beautytocare.com/cdn-cgi/image/width=1440,height=1200,f=auto/media/catalog/product//f/l/flormar-good-lids-only-eyeshadow-primer-01-nude-7-5ml.jpg",
        "is_best_selling": False,
        "created_at": "2026-03-19T15:15:11.969Z"
    }
},
{
    "model": "store.product",
    "pk": 132,
    "fields": {
        "category": 4,
        "name": "Argan Shampoo",
        "description": "A luxury argan shampoo for your daily routine.",
        "price": "17.00",
        "old_price": "19.95",
        "image": "https://www.colornow.net/wp-content/uploads/2018/04/argandeluxe-argan-oil-nourishing-shampoo.jpg",
        "is_best_selling": True,
        "created_at": "2026-03-19T15:15:11.972Z"
    }
},
{
    "model": "store.product",
    "pk": 134,
    "fields": {
        "category": 4,
        "name": "Volumizing Mist",
        "description": "A luxury volumizing mist for your daily routine.",
        "price": "15.00",
        "old_price": "22.00",
        "image": "https://www.lojaglamourosa.com/resources/medias/shop/products/thumbnails/shop-image-large/shop-cb-04267-01-volumizing-mist---160ml--1.jpg",
        "is_best_selling": True,
        "created_at": "2026-03-19T15:15:11.978Z"
    }
},
{
    "model": "store.product",
    "pk": 135,
    "fields": {
        "category": 4,
        "name": "Keratin Mask",
        "description": "A luxury keratin mask for your daily routine.",
        "price": "20.00",
        "old_price": "22.14",
        "image": "https://image-cdn.ubuy.com/collagen-conditioner-hair-mask-collagen/400_400_100/66086ba0c030834fe3591123.jpg",
        "is_best_selling": False,
        "created_at": "2026-03-19T15:15:11.981Z"
    }
},
{
    "model": "store.product",
    "pk": 136,
    "fields": {
        "category": 4,
        "name": "Peppermint Scrub",
        "description": "A luxury peppermint scrub for your daily routine.",
        "price": "12.83",
        "old_price": "18.12",
        "image": "https://greenkoala.net/cdn/shop/files/9oz-peppermint-eucalyptus-sugar-scrub.jpg?v=1749057040&width=1100",
        "is_best_selling": True,
        "created_at": "2026-03-19T15:15:11.984Z"
    }
},
{
    "model": "store.product",
    "pk": 137,
    "fields": {
        "category": 4,
        "name": "Protein Leave-in",
        "description": "A luxury protein leave-in for your daily routine.",
        "price": "18.50",
        "old_price": "23.50",
        "image": "https://www.lockenbox.com/cdn/shop/files/CurlySecret_ProteinBombLeave-In_2.jpg?v=1747659547&width=1000",
        "is_best_selling": False,
        "created_at": "2026-03-19T15:15:11.988Z"
    }
},
{
    "model": "store.product",
    "pk": 138,
    "fields": {
        "category": 4,
        "name": "Glossing Serum",
        "description": "A luxury glossing serum for your daily routine.",
        "price": "10.05",
        "old_price": "15.20",
        "image": "https://thebodyshop.ng/cdn/shop/files/GRAPESEED_GLOSSING_SERUM_60ML_1_INECMPS446_1800x1800_aec5308a-6cda-47b0-9049-54cae236bf24_900x.webp?v=1740380640",
        "is_best_selling": False,
        "created_at": "2026-03-19T15:15:11.991Z"
    }
},
{
    "model": "store.product",
    "pk": 139,
    "fields": {
        "category": 4,
        "name": "Coconut Detangler",
        "description": "A luxury coconut detangler for your daily routine.",
        "price": "15.00",
        "old_price": "20.05",
        "image": "https://static.beautytocare.com/cdn-cgi/image/width=1440,height=1200,f=auto/media/catalog/product//u/m/umberto-giannini-banana-coconut-detangler-leave-in-conditioner-250ml.png",
        "is_best_selling": False,
        "created_at": "2026-03-19T15:15:11.994Z"
    }
},
{
    "model": "store.product",
    "pk": 140,
    "fields": {
        "category": 4,
        "name": "Tea Tree Wash",
        "description": "A luxury tea tree wash for your daily routine.",
        "price": "15.50",
        "old_price": "26.80",
        "image": "https://thebodyshop.ng/cdn/shop/files/TEA_TREE_PURIFYING___BALANCING_SHAMPOO_250ml_1_INROIPS350_1800x1800_e52944cd-65a8-41e4-9298-f68037cca929_900x.jpg?v=1740380720",
        "is_best_selling": True,
        "created_at": "2026-03-19T15:15:11.997Z"
    }
},
{
    "model": "store.product",
    "pk": 141,
    "fields": {
        "category": 4,
        "name": "Anti-Frizz Gel",
        "description": "A luxury anti-frizz gel for your daily routine.",
        "price": "30.00",
        "old_price": "35.00",
        "image": "https://us.phyto.com/cdn/shop/files/CURLSINTENSEGEL_1296x.png?v=1752603012",
        "is_best_selling": False,
        "created_at": "2026-03-19T15:15:12.000Z"
    }
},
{
    "model": "store.product",
    "pk": 142,
    "fields": {
        "category": 4,
        "name": "Dry Shampoo",
        "description": "A luxury dry shampoo for your daily routine.",
        "price": "4.00",
        "old_price": "6.00",
        "image": "https://cdn.shopify.com/s/files/1/0523/2735/0457/files/cantu-amazon",
        "is_best_selling": False,
        "created_at": "2026-03-19T15:15:12.003Z"
    }
},
{
    "model": "store.product",
    "pk": 149,
    "fields": {
        "category": 4,
        "name": "Curl Definer",
        "description": "A luxury curl definer for your daily routine.",
        "price": "62.38",
        "old_price": "74.86",
        "image": "https://images.unsplash.com/photo-1505944270255-bd2b896e3e34?q=80&w=800",
        "is_best_selling": False,
        "created_at": "2026-03-19T15:15:12.025Z"
    }
},
{
    "model": "store.product",
    "pk": 150,
    "fields": {
        "category": 4,
        "name": "Repair Serum",
        "description": "A luxury repair serum for your daily routine.",
        "price": "61.03",
        "old_price": "73.24",
        "image": "https://images.unsplash.com/photo-1508381623145-59f55027bc03?q=80&w=800",
        "is_best_selling": False,
        "created_at": "2026-03-19T15:15:12.028Z"
    }
},
{
    "model": "auth.permission",
    "fields": {
        "name": "Can add log entry",
        "content_type": [
            "admin",
            "logentry"
        ],
        "codename": "add_logentry"
    }
},
{
    "model": "auth.permission",
    "fields": {
        "name": "Can change log entry",
        "content_type": [
            "admin",
            "logentry"
        ],
        "codename": "change_logentry"
    }
},
{
    "model": "auth.permission",
    "fields": {
        "name": "Can delete log entry",
        "content_type": [
            "admin",
            "logentry"
        ],
        "codename": "delete_logentry"
    }
},
{
    "model": "auth.permission",
    "fields": {
        "name": "Can view log entry",
        "content_type": [
            "admin",
            "logentry"
        ],
        "codename": "view_logentry"
    }
},
{
    "model": "auth.permission",
    "fields": {
        "name": "Can add permission",
        "content_type": [
            "auth",
            "permission"
        ],
        "codename": "add_permission"
    }
},
{
    "model": "auth.permission",
    "fields": {
        "name": "Can change permission",
        "content_type": [
            "auth",
            "permission"
        ],
        "codename": "change_permission"
    }
},
{
    "model": "auth.permission",
    "fields": {
        "name": "Can delete permission",
        "content_type": [
            "auth",
            "permission"
        ],
        "codename": "delete_permission"
    }
},
{
    "model": "auth.permission",
    "fields": {
        "name": "Can view permission",
        "content_type": [
            "auth",
            "permission"
        ],
        "codename": "view_permission"
    }
},
{
    "model": "auth.permission",
    "fields": {
        "name": "Can add group",
        "content_type": [
            "auth",
            "group"
        ],
        "codename": "add_group"
    }
},
{
    "model": "auth.permission",
    "fields": {
        "name": "Can change group",
        "content_type": [
            "auth",
            "group"
        ],
        "codename": "change_group"
    }
},
{
    "model": "auth.permission",
    "fields": {
        "name": "Can delete group",
        "content_type": [
            "auth",
            "group"
        ],
        "codename": "delete_group"
    }
},
{
    "model": "auth.permission",
    "fields": {
        "name": "Can view group",
        "content_type": [
            "auth",
            "group"
        ],
        "codename": "view_group"
    }
},
{
    "model": "auth.permission",
    "fields": {
        "name": "Can add user",
        "content_type": [
            "auth",
            "user"
        ],
        "codename": "add_user"
    }
},
{
    "model": "auth.permission",
    "fields": {
        "name": "Can change user",
        "content_type": [
            "auth",
            "user"
        ],
        "codename": "change_user"
    }
},
{
    "model": "auth.permission",
    "fields": {
        "name": "Can delete user",
        "content_type": [
            "auth",
            "user"
        ],
        "codename": "delete_user"
    }
},
{
    "model": "auth.permission",
    "fields": {
        "name": "Can view user",
        "content_type": [
            "auth",
            "user"
        ],
        "codename": "view_user"
    }
},
{
    "model": "auth.permission",
    "fields": {
        "name": "Can add content type",
        "content_type": [
            "contenttypes",
            "contenttype"
        ],
        "codename": "add_contenttype"
    }
},
{
    "model": "auth.permission",
    "fields": {
        "name": "Can change content type",
        "content_type": [
            "contenttypes",
            "contenttype"
        ],
        "codename": "change_contenttype"
    }
},
{
    "model": "auth.permission",
    "fields": {
        "name": "Can delete content type",
        "content_type": [
            "contenttypes",
            "contenttype"
        ],
        "codename": "delete_contenttype"
    }
},
{
    "model": "auth.permission",
    "fields": {
        "name": "Can view content type",
        "content_type": [
            "contenttypes",
            "contenttype"
        ],
        "codename": "view_contenttype"
    }
},
{
    "model": "auth.permission",
    "fields": {
        "name": "Can add session",
        "content_type": [
            "sessions",
            "session"
        ],
        "codename": "add_session"
    }
},
{
    "model": "auth.permission",
    "fields": {
        "name": "Can change session",
        "content_type": [
            "sessions",
            "session"
        ],
        "codename": "change_session"
    }
},
{
    "model": "auth.permission",
    "fields": {
        "name": "Can delete session",
        "content_type": [
            "sessions",
            "session"
        ],
        "codename": "delete_session"
    }
},
{
    "model": "auth.permission",
    "fields": {
        "name": "Can view session",
        "content_type": [
            "sessions",
            "session"
        ],
        "codename": "view_session"
    }
},
{
    "model": "auth.permission",
    "fields": {
        "name": "Can add dashboard stats",
        "content_type": [
            "dashboard",
            "dashboardstats"
        ],
        "codename": "add_dashboardstats"
    }
},
{
    "model": "auth.permission",
    "fields": {
        "name": "Can change dashboard stats",
        "content_type": [
            "dashboard",
            "dashboardstats"
        ],
        "codename": "change_dashboardstats"
    }
},
{
    "model": "auth.permission",
    "fields": {
        "name": "Can delete dashboard stats",
        "content_type": [
            "dashboard",
            "dashboardstats"
        ],
        "codename": "delete_dashboardstats"
    }
},
{
    "model": "auth.permission",
    "fields": {
        "name": "Can view dashboard stats",
        "content_type": [
            "dashboard",
            "dashboardstats"
        ],
        "codename": "view_dashboardstats"
    }
},
{
    "model": "auth.permission",
    "fields": {
        "name": "Can add category",
        "content_type": [
            "store",
            "category"
        ],
        "codename": "add_category"
    }
},
{
    "model": "auth.permission",
    "fields": {
        "name": "Can change category",
        "content_type": [
            "store",
            "category"
        ],
        "codename": "change_category"
    }
},
{
    "model": "auth.permission",
    "fields": {
        "name": "Can delete category",
        "content_type": [
            "store",
            "category"
        ],
        "codename": "delete_category"
    }
},
{
    "model": "auth.permission",
    "fields": {
        "name": "Can view category",
        "content_type": [
            "store",
            "category"
        ],
        "codename": "view_category"
    }
},
{
    "model": "auth.permission",
    "fields": {
        "name": "Can add customer",
        "content_type": [
            "store",
            "customer"
        ],
        "codename": "add_customer"
    }
},
{
    "model": "auth.permission",
    "fields": {
        "name": "Can change customer",
        "content_type": [
            "store",
            "customer"
        ],
        "codename": "change_customer"
    }
},
{
    "model": "auth.permission",
    "fields": {
        "name": "Can delete customer",
        "content_type": [
            "store",
            "customer"
        ],
        "codename": "delete_customer"
    }
},
{
    "model": "auth.permission",
    "fields": {
        "name": "Can view customer",
        "content_type": [
            "store",
            "customer"
        ],
        "codename": "view_customer"
    }
},
{
    "model": "auth.permission",
    "fields": {
        "name": "Can add order",
        "content_type": [
            "store",
            "order"
        ],
        "codename": "add_order"
    }
},
{
    "model": "auth.permission",
    "fields": {
        "name": "Can change order",
        "content_type": [
            "store",
            "order"
        ],
        "codename": "change_order"
    }
},
{
    "model": "auth.permission",
    "fields": {
        "name": "Can delete order",
        "content_type": [
            "store",
            "order"
        ],
        "codename": "delete_order"
    }
},
{
    "model": "auth.permission",
    "fields": {
        "name": "Can view order",
        "content_type": [
            "store",
            "order"
        ],
        "codename": "view_order"
    }
},
{
    "model": "auth.permission",
    "fields": {
        "name": "Can add product",
        "content_type": [
            "store",
            "product"
        ],
        "codename": "add_product"
    }
},
{
    "model": "auth.permission",
    "fields": {
        "name": "Can change product",
        "content_type": [
            "store",
            "product"
        ],
        "codename": "change_product"
    }
},
{
    "model": "auth.permission",
    "fields": {
        "name": "Can delete product",
        "content_type": [
            "store",
            "product"
        ],
        "codename": "delete_product"
    }
},
{
    "model": "auth.permission",
    "fields": {
        "name": "Can view product",
        "content_type": [
            "store",
            "product"
        ],
        "codename": "view_product"
    }
},
{
    "model": "auth.permission",
    "fields": {
        "name": "Can add order item",
        "content_type": [
            "store",
            "orderitem"
        ],
        "codename": "add_orderitem"
    }
},
{
    "model": "auth.permission",
    "fields": {
        "name": "Can change order item",
        "content_type": [
            "store",
            "orderitem"
        ],
        "codename": "change_orderitem"
    }
},
{
    "model": "auth.permission",
    "fields": {
        "name": "Can delete order item",
        "content_type": [
            "store",
            "orderitem"
        ],
        "codename": "delete_orderitem"
    }
},
{
    "model": "auth.permission",
    "fields": {
        "name": "Can view order item",
        "content_type": [
            "store",
            "orderitem"
        ],
        "codename": "view_orderitem"
    }
},
{
    "model": "auth.user",
    "fields": {
        "password": "pbkdf2_sha256$1200000$8YT3Q5LxZOX9ZpKu44gaxU$TBFnS5yXM7zjDqLDYRvkeS315dalJHO+/otOiKmIkuY=",
        "last_login": "2026-03-19T12:58:38.545Z",
        "is_superuser": True,
        "username": "efosa",
        "first_name": "",
        "last_name": "",
        "email": "odiase@gmail.com",
        "is_staff": True,
        "is_active": True,
        "date_joined": "2026-03-19T12:48:46.139Z",
        "groups": [],
        "user_permissions": []
    }
},
{
    "model": "admin.logentry",
    "pk": 1,
    "fields": {
        "action_time": "2026-03-19T12:59:30.904Z",
        "user": [
            "efosa"
        ],
        "content_type": [
            "dashboard",
            "dashboardstats"
        ],
        "object_id": "1",
        "object_repr": "Veloura Dashboard Stats",
        "action_flag": 3,
        "change_message": ""
    }
},
{
    "model": "admin.logentry",
    "pk": 2,
    "fields": {
        "action_time": "2026-03-19T14:14:01.110Z",
        "user": [
            "efosa"
        ],
        "content_type": [
            "dashboard",
            "dashboardstats"
        ],
        "object_id": "1",
        "object_repr": "Veloura Dashboard Stats",
        "action_flag": 3,
        "change_message": ""
    }
},
{
    "model": "admin.logentry",
    "pk": 3,
    "fields": {
        "action_time": "2026-03-19T14:36:07.828Z",
        "user": [
            "efosa"
        ],
        "content_type": [
            "dashboard",
            "dashboardstats"
        ],
        "object_id": "1",
        "object_repr": "Veloura Dashboard Stats",
        "action_flag": 3,
        "change_message": ""
    }
},
{
    "model": "admin.logentry",
    "pk": 4,
    "fields": {
        "action_time": "2026-03-19T14:38:25.824Z",
        "user": [
            "efosa"
        ],
        "content_type": [
            "store",
            "category"
        ],
        "object_id": "1",
        "object_repr": "skincare",
        "action_flag": 1,
        "change_message": "[{\"added\": {}}]"
    }
},
{
    "model": "admin.logentry",
    "pk": 5,
    "fields": {
        "action_time": "2026-03-19T14:38:33.079Z",
        "user": [
            "efosa"
        ],
        "content_type": [
            "store",
            "category"
        ],
        "object_id": "2",
        "object_repr": "haircare",
        "action_flag": 1,
        "change_message": "[{\"added\": {}}]"
    }
},
{
    "model": "admin.logentry",
    "pk": 6,
    "fields": {
        "action_time": "2026-03-19T14:38:52.751Z",
        "user": [
            "efosa"
        ],
        "content_type": [
            "store",
            "category"
        ],
        "object_id": "3",
        "object_repr": "makeup",
        "action_flag": 1,
        "change_message": "[{\"added\": {}}]"
    }
},
{
    "model": "admin.logentry",
    "pk": 7,
    "fields": {
        "action_time": "2026-03-19T15:09:57.389Z",
        "user": [
            "efosa"
        ],
        "content_type": [
            "store",
            "product"
        ],
        "object_id": "31",
        "object_repr": "Haircar Product 10",
        "action_flag": 3,
        "change_message": ""
    }
},
{
    "model": "admin.logentry",
    "pk": 8,
    "fields": {
        "action_time": "2026-03-19T15:09:57.389Z",
        "user": [
            "efosa"
        ],
        "content_type": [
            "store",
            "product"
        ],
        "object_id": "30",
        "object_repr": "Haircar Product 9",
        "action_flag": 3,
        "change_message": ""
    }
},
{
    "model": "admin.logentry",
    "pk": 9,
    "fields": {
        "action_time": "2026-03-19T15:09:57.389Z",
        "user": [
            "efosa"
        ],
        "content_type": [
            "store",
            "product"
        ],
        "object_id": "29",
        "object_repr": "Haircar Product 8",
        "action_flag": 3,
        "change_message": ""
    }
},
{
    "model": "admin.logentry",
    "pk": 10,
    "fields": {
        "action_time": "2026-03-19T15:09:57.389Z",
        "user": [
            "efosa"
        ],
        "content_type": [
            "store",
            "product"
        ],
        "object_id": "28",
        "object_repr": "Haircar Product 7",
        "action_flag": 3,
        "change_message": ""
    }
},
{
    "model": "admin.logentry",
    "pk": 11,
    "fields": {
        "action_time": "2026-03-19T15:09:57.389Z",
        "user": [
            "efosa"
        ],
        "content_type": [
            "store",
            "product"
        ],
        "object_id": "27",
        "object_repr": "Haircar Product 6",
        "action_flag": 3,
        "change_message": ""
    }
},
{
    "model": "admin.logentry",
    "pk": 12,
    "fields": {
        "action_time": "2026-03-19T15:09:57.389Z",
        "user": [
            "efosa"
        ],
        "content_type": [
            "store",
            "product"
        ],
        "object_id": "26",
        "object_repr": "Haircar Product 5",
        "action_flag": 3,
        "change_message": ""
    }
},
{
    "model": "admin.logentry",
    "pk": 13,
    "fields": {
        "action_time": "2026-03-19T15:09:57.389Z",
        "user": [
            "efosa"
        ],
        "content_type": [
            "store",
            "product"
        ],
        "object_id": "25",
        "object_repr": "Haircar Product 4",
        "action_flag": 3,
        "change_message": ""
    }
},
{
    "model": "admin.logentry",
    "pk": 14,
    "fields": {
        "action_time": "2026-03-19T15:09:57.389Z",
        "user": [
            "efosa"
        ],
        "content_type": [
            "store",
            "product"
        ],
        "object_id": "24",
        "object_repr": "Haircar Product 3",
        "action_flag": 3,
        "change_message": ""
    }
},
{
    "model": "admin.logentry",
    "pk": 15,
    "fields": {
        "action_time": "2026-03-19T15:09:57.389Z",
        "user": [
            "efosa"
        ],
        "content_type": [
            "store",
            "product"
        ],
        "object_id": "23",
        "object_repr": "Haircar Product 2",
        "action_flag": 3,
        "change_message": ""
    }
},
{
    "model": "admin.logentry",
    "pk": 16,
    "fields": {
        "action_time": "2026-03-19T15:09:57.389Z",
        "user": [
            "efosa"
        ],
        "content_type": [
            "store",
            "product"
        ],
        "object_id": "22",
        "object_repr": "Haircar Product 1",
        "action_flag": 3,
        "change_message": ""
    }
},
{
    "model": "admin.logentry",
    "pk": 17,
    "fields": {
        "action_time": "2026-03-19T15:09:57.389Z",
        "user": [
            "efosa"
        ],
        "content_type": [
            "store",
            "product"
        ],
        "object_id": "21",
        "object_repr": "Makeu Product 11",
        "action_flag": 3,
        "change_message": ""
    }
},
{
    "model": "admin.logentry",
    "pk": 18,
    "fields": {
        "action_time": "2026-03-19T15:09:57.389Z",
        "user": [
            "efosa"
        ],
        "content_type": [
            "store",
            "product"
        ],
        "object_id": "20",
        "object_repr": "Makeu Product 10",
        "action_flag": 3,
        "change_message": ""
    }
},
{
    "model": "admin.logentry",
    "pk": 19,
    "fields": {
        "action_time": "2026-03-19T15:09:57.389Z",
        "user": [
            "efosa"
        ],
        "content_type": [
            "store",
            "product"
        ],
        "object_id": "19",
        "object_repr": "Makeu Product 9",
        "action_flag": 3,
        "change_message": ""
    }
},
{
    "model": "admin.logentry",
    "pk": 20,
    "fields": {
        "action_time": "2026-03-19T15:09:57.389Z",
        "user": [
            "efosa"
        ],
        "content_type": [
            "store",
            "product"
        ],
        "object_id": "18",
        "object_repr": "Makeu Product 8",
        "action_flag": 3,
        "change_message": ""
    }
},
{
    "model": "admin.logentry",
    "pk": 21,
    "fields": {
        "action_time": "2026-03-19T15:09:57.389Z",
        "user": [
            "efosa"
        ],
        "content_type": [
            "store",
            "product"
        ],
        "object_id": "17",
        "object_repr": "Makeu Product 7",
        "action_flag": 3,
        "change_message": ""
    }
},
{
    "model": "admin.logentry",
    "pk": 22,
    "fields": {
        "action_time": "2026-03-19T15:09:57.389Z",
        "user": [
            "efosa"
        ],
        "content_type": [
            "store",
            "product"
        ],
        "object_id": "16",
        "object_repr": "Makeu Product 6",
        "action_flag": 3,
        "change_message": ""
    }
},
{
    "model": "admin.logentry",
    "pk": 23,
    "fields": {
        "action_time": "2026-03-19T15:09:57.389Z",
        "user": [
            "efosa"
        ],
        "content_type": [
            "store",
            "product"
        ],
        "object_id": "15",
        "object_repr": "Makeu Product 5",
        "action_flag": 3,
        "change_message": ""
    }
},
{
    "model": "admin.logentry",
    "pk": 24,
    "fields": {
        "action_time": "2026-03-19T15:09:57.389Z",
        "user": [
            "efosa"
        ],
        "content_type": [
            "store",
            "product"
        ],
        "object_id": "14",
        "object_repr": "Makeu Product 4",
        "action_flag": 3,
        "change_message": ""
    }
},
{
    "model": "admin.logentry",
    "pk": 25,
    "fields": {
        "action_time": "2026-03-19T15:09:57.389Z",
        "user": [
            "efosa"
        ],
        "content_type": [
            "store",
            "product"
        ],
        "object_id": "13",
        "object_repr": "Makeu Product 3",
        "action_flag": 3,
        "change_message": ""
    }
},
{
    "model": "admin.logentry",
    "pk": 26,
    "fields": {
        "action_time": "2026-03-19T15:09:57.389Z",
        "user": [
            "efosa"
        ],
        "content_type": [
            "store",
            "product"
        ],
        "object_id": "12",
        "object_repr": "Makeu Product 2",
        "action_flag": 3,
        "change_message": ""
    }
},
{
    "model": "admin.logentry",
    "pk": 27,
    "fields": {
        "action_time": "2026-03-19T15:09:57.389Z",
        "user": [
            "efosa"
        ],
        "content_type": [
            "store",
            "product"
        ],
        "object_id": "11",
        "object_repr": "Makeu Product 1",
        "action_flag": 3,
        "change_message": ""
    }
},
{
    "model": "admin.logentry",
    "pk": 28,
    "fields": {
        "action_time": "2026-03-19T15:09:57.389Z",
        "user": [
            "efosa"
        ],
        "content_type": [
            "store",
            "product"
        ],
        "object_id": "10",
        "object_repr": "Skincar Product 10",
        "action_flag": 3,
        "change_message": ""
    }
},
{
    "model": "admin.logentry",
    "pk": 29,
    "fields": {
        "action_time": "2026-03-19T15:09:57.389Z",
        "user": [
            "efosa"
        ],
        "content_type": [
            "store",
            "product"
        ],
        "object_id": "9",
        "object_repr": "Skincar Product 9",
        "action_flag": 3,
        "change_message": ""
    }
},
{
    "model": "admin.logentry",
    "pk": 30,
    "fields": {
        "action_time": "2026-03-19T15:09:57.389Z",
        "user": [
            "efosa"
        ],
        "content_type": [
            "store",
            "product"
        ],
        "object_id": "8",
        "object_repr": "Skincar Product 8",
        "action_flag": 3,
        "change_message": ""
    }
},
{
    "model": "admin.logentry",
    "pk": 31,
    "fields": {
        "action_time": "2026-03-19T15:09:57.389Z",
        "user": [
            "efosa"
        ],
        "content_type": [
            "store",
            "product"
        ],
        "object_id": "7",
        "object_repr": "Skincar Product 7",
        "action_flag": 3,
        "change_message": ""
    }
},
{
    "model": "admin.logentry",
    "pk": 32,
    "fields": {
        "action_time": "2026-03-19T15:09:57.389Z",
        "user": [
            "efosa"
        ],
        "content_type": [
            "store",
            "product"
        ],
        "object_id": "6",
        "object_repr": "Skincar Product 6",
        "action_flag": 3,
        "change_message": ""
    }
},
{
    "model": "admin.logentry",
    "pk": 33,
    "fields": {
        "action_time": "2026-03-19T15:09:57.389Z",
        "user": [
            "efosa"
        ],
        "content_type": [
            "store",
            "product"
        ],
        "object_id": "5",
        "object_repr": "Skincar Product 5",
        "action_flag": 3,
        "change_message": ""
    }
},
{
    "model": "admin.logentry",
    "pk": 34,
    "fields": {
        "action_time": "2026-03-19T15:09:57.389Z",
        "user": [
            "efosa"
        ],
        "content_type": [
            "store",
            "product"
        ],
        "object_id": "4",
        "object_repr": "Skincar Product 4",
        "action_flag": 3,
        "change_message": ""
    }
},
{
    "model": "admin.logentry",
    "pk": 35,
    "fields": {
        "action_time": "2026-03-19T15:09:57.389Z",
        "user": [
            "efosa"
        ],
        "content_type": [
            "store",
            "product"
        ],
        "object_id": "3",
        "object_repr": "Skincar Product 3",
        "action_flag": 3,
        "change_message": ""
    }
},
{
    "model": "admin.logentry",
    "pk": 36,
    "fields": {
        "action_time": "2026-03-19T15:09:57.389Z",
        "user": [
            "efosa"
        ],
        "content_type": [
            "store",
            "product"
        ],
        "object_id": "2",
        "object_repr": "Skincar Product 2",
        "action_flag": 3,
        "change_message": ""
    }
},
{
    "model": "admin.logentry",
    "pk": 37,
    "fields": {
        "action_time": "2026-03-19T15:09:57.389Z",
        "user": [
            "efosa"
        ],
        "content_type": [
            "store",
            "product"
        ],
        "object_id": "1",
        "object_repr": "Skincar Product 1",
        "action_flag": 3,
        "change_message": ""
    }
},
{
    "model": "admin.logentry",
    "pk": 38,
    "fields": {
        "action_time": "2026-03-19T15:10:18.802Z",
        "user": [
            "efosa"
        ],
        "content_type": [
            "store",
            "product"
        ],
        "object_id": "91",
        "object_repr": "Hydrating Bamboo Water",
        "action_flag": 2,
        "change_message": "[]"
    }
},
{
    "model": "admin.logentry",
    "pk": 39,
    "fields": {
        "action_time": "2026-03-19T15:15:05.809Z",
        "user": [
            "efosa"
        ],
        "content_type": [
            "store",
            "product"
        ],
        "object_id": "91",
        "object_repr": "Hydrating Bamboo Water",
        "action_flag": 3,
        "change_message": ""
    }
},
{
    "model": "admin.logentry",
    "pk": 40,
    "fields": {
        "action_time": "2026-03-19T15:15:05.810Z",
        "user": [
            "efosa"
        ],
        "content_type": [
            "store",
            "product"
        ],
        "object_id": "90",
        "object_repr": "Overnight Repair Serum",
        "action_flag": 3,
        "change_message": ""
    }
},
{
    "model": "admin.logentry",
    "pk": 41,
    "fields": {
        "action_time": "2026-03-19T15:15:05.810Z",
        "user": [
            "efosa"
        ],
        "content_type": [
            "store",
            "product"
        ],
        "object_id": "89",
        "object_repr": "Weightless Curl Definer",
        "action_flag": 3,
        "change_message": ""
    }
},
{
    "model": "admin.logentry",
    "pk": 42,
    "fields": {
        "action_time": "2026-03-19T15:15:05.810Z",
        "user": [
            "efosa"
        ],
        "content_type": [
            "store",
            "product"
        ],
        "object_id": "88",
        "object_repr": "Silver Toning Shampoo",
        "action_flag": 3,
        "change_message": ""
    }
},
{
    "model": "admin.logentry",
    "pk": 43,
    "fields": {
        "action_time": "2026-03-19T15:15:05.810Z",
        "user": [
            "efosa"
        ],
        "content_type": [
            "store",
            "product"
        ],
        "object_id": "87",
        "object_repr": "Thickening Fiber Cream",
        "action_flag": 3,
        "change_message": ""
    }
},
{
    "model": "admin.logentry",
    "pk": 44,
    "fields": {
        "action_time": "2026-03-19T15:15:05.810Z",
        "user": [
            "efosa"
        ],
        "content_type": [
            "store",
            "product"
        ],
        "object_id": "86",
        "object_repr": "Honey Infused Hair Mask",
        "action_flag": 3,
        "change_message": ""
    }
},
{
    "model": "admin.logentry",
    "pk": 45,
    "fields": {
        "action_time": "2026-03-19T15:15:05.810Z",
        "user": [
            "efosa"
        ],
        "content_type": [
            "store",
            "product"
        ],
        "object_id": "85",
        "object_repr": "Rosemary Scalp Treatment",
        "action_flag": 3,
        "change_message": ""
    }
},
{
    "model": "admin.logentry",
    "pk": 46,
    "fields": {
        "action_time": "2026-03-19T15:15:05.810Z",
        "user": [
            "efosa"
        ],
        "content_type": [
            "store",
            "product"
        ],
        "object_id": "84",
        "object_repr": "Heat Shield Styling Spray",
        "action_flag": 3,
        "change_message": ""
    }
},
{
    "model": "admin.logentry",
    "pk": 47,
    "fields": {
        "action_time": "2026-03-19T15:15:05.810Z",
        "user": [
            "efosa"
        ],
        "content_type": [
            "store",
            "product"
        ],
        "object_id": "83",
        "object_repr": "Castor Oil Growth Treatment",
        "action_flag": 3,
        "change_message": ""
    }
},
{
    "model": "admin.logentry",
    "pk": 48,
    "fields": {
        "action_time": "2026-03-19T15:15:05.810Z",
        "user": [
            "efosa"
        ],
        "content_type": [
            "store",
            "product"
        ],
        "object_id": "82",
        "object_repr": "Dry Shampoo Volumizer",
        "action_flag": 3,
        "change_message": ""
    }
},
{
    "model": "admin.logentry",
    "pk": 49,
    "fields": {
        "action_time": "2026-03-19T15:15:05.810Z",
        "user": [
            "efosa"
        ],
        "content_type": [
            "store",
            "product"
        ],
        "object_id": "81",
        "object_repr": "Anti-Frizz Control Gel",
        "action_flag": 3,
        "change_message": ""
    }
},
{
    "model": "admin.logentry",
    "pk": 50,
    "fields": {
        "action_time": "2026-03-19T15:15:05.810Z",
        "user": [
            "efosa"
        ],
        "content_type": [
            "store",
            "product"
        ],
        "object_id": "80",
        "object_repr": "Tea Tree Clarifying Wash",
        "action_flag": 3,
        "change_message": ""
    }
},
{
    "model": "admin.logentry",
    "pk": 51,
    "fields": {
        "action_time": "2026-03-19T15:15:05.810Z",
        "user": [
            "efosa"
        ],
        "content_type": [
            "store",
            "product"
        ],
        "object_id": "79",
        "object_repr": "Coconut Milk Detangler",
        "action_flag": 3,
        "change_message": ""
    }
},
{
    "model": "admin.logentry",
    "pk": 52,
    "fields": {
        "action_time": "2026-03-19T15:15:05.810Z",
        "user": [
            "efosa"
        ],
        "content_type": [
            "store",
            "product"
        ],
        "object_id": "78",
        "object_repr": "Color Protect Glossing Serum",
        "action_flag": 3,
        "change_message": ""
    }
},
{
    "model": "admin.logentry",
    "pk": 53,
    "fields": {
        "action_time": "2026-03-19T15:15:05.810Z",
        "user": [
            "efosa"
        ],
        "content_type": [
            "store",
            "product"
        ],
        "object_id": "77",
        "object_repr": "Silk Protein Leave-in",
        "action_flag": 3,
        "change_message": ""
    }
},
{
    "model": "admin.logentry",
    "pk": 54,
    "fields": {
        "action_time": "2026-03-19T15:15:05.810Z",
        "user": [
            "efosa"
        ],
        "content_type": [
            "store",
            "product"
        ],
        "object_id": "76",
        "object_repr": "Scalp Refresh Peppermint Scrub",
        "action_flag": 3,
        "change_message": ""
    }
},
{
    "model": "admin.logentry",
    "pk": 55,
    "fields": {
        "action_time": "2026-03-19T15:15:05.810Z",
        "user": [
            "efosa"
        ],
        "content_type": [
            "store",
            "product"
        ],
        "object_id": "75",
        "object_repr": "Repairing Keratin Mask",
        "action_flag": 3,
        "change_message": ""
    }
},
{
    "model": "admin.logentry",
    "pk": 56,
    "fields": {
        "action_time": "2026-03-19T15:15:05.810Z",
        "user": [
            "efosa"
        ],
        "content_type": [
            "store",
            "product"
        ],
        "object_id": "74",
        "object_repr": "Biotin Volumizing Mist",
        "action_flag": 3,
        "change_message": ""
    }
},
{
    "model": "admin.logentry",
    "pk": 57,
    "fields": {
        "action_time": "2026-03-19T15:15:05.810Z",
        "user": [
            "efosa"
        ],
        "content_type": [
            "store",
            "product"
        ],
        "object_id": "73",
        "object_repr": "Shea Butter Deep Conditioner",
        "action_flag": 3,
        "change_message": ""
    }
},
{
    "model": "admin.logentry",
    "pk": 58,
    "fields": {
        "action_time": "2026-03-19T15:15:05.810Z",
        "user": [
            "efosa"
        ],
        "content_type": [
            "store",
            "product"
        ],
        "object_id": "72",
        "object_repr": "Argan Oil Nourishing Shampoo",
        "action_flag": 3,
        "change_message": ""
    }
},
{
    "model": "admin.logentry",
    "pk": 59,
    "fields": {
        "action_time": "2026-03-19T15:15:05.810Z",
        "user": [
            "efosa"
        ],
        "content_type": [
            "store",
            "product"
        ],
        "object_id": "71",
        "object_repr": "Gold Leaf Eyeshadow Primer",
        "action_flag": 3,
        "change_message": ""
    }
},
{
    "model": "admin.logentry",
    "pk": 60,
    "fields": {
        "action_time": "2026-03-19T15:15:05.810Z",
        "user": [
            "efosa"
        ],
        "content_type": [
            "store",
            "product"
        ],
        "object_id": "70",
        "object_repr": "Glossy Nude Lip Stain",
        "action_flag": 3,
        "change_message": ""
    }
},
{
    "model": "admin.logentry",
    "pk": 61,
    "fields": {
        "action_time": "2026-03-19T15:15:05.810Z",
        "user": [
            "efosa"
        ],
        "content_type": [
            "store",
            "product"
        ],
        "object_id": "69",
        "object_repr": "Full Coverage Palette",
        "action_flag": 3,
        "change_message": ""
    }
},
{
    "model": "admin.logentry",
    "pk": 62,
    "fields": {
        "action_time": "2026-03-19T15:15:05.810Z",
        "user": [
            "efosa"
        ],
        "content_type": [
            "store",
            "product"
        ],
        "object_id": "68",
        "object_repr": "Satin Finish Lip Liner",
        "action_flag": 3,
        "change_message": ""
    }
},
{
    "model": "admin.logentry",
    "pk": 63,
    "fields": {
        "action_time": "2026-03-19T15:15:05.810Z",
        "user": [
            "efosa"
        ],
        "content_type": [
            "store",
            "product"
        ],
        "object_id": "67",
        "object_repr": "Sheer Tinted Moisturizer",
        "action_flag": 3,
        "change_message": ""
    }
},
{
    "model": "admin.logentry",
    "pk": 64,
    "fields": {
        "action_time": "2026-03-19T15:15:05.810Z",
        "user": [
            "efosa"
        ],
        "content_type": [
            "store",
            "product"
        ],
        "object_id": "66",
        "object_repr": "Contour & Sculpt Stick",
        "action_flag": 3,
        "change_message": ""
    }
},
{
    "model": "admin.logentry",
    "pk": 65,
    "fields": {
        "action_time": "2026-03-19T15:15:05.810Z",
        "user": [
            "efosa"
        ],
        "content_type": [
            "store",
            "product"
        ],
        "object_id": "65",
        "object_repr": "Shimmer Eye Pigment",
        "action_flag": 3,
        "change_message": ""
    }
},
{
    "model": "admin.logentry",
    "pk": 66,
    "fields": {
        "action_time": "2026-03-19T15:15:05.810Z",
        "user": [
            "efosa"
        ],
        "content_type": [
            "store",
            "product"
        ],
        "object_id": "64",
        "object_repr": "Matte Setting Spray",
        "action_flag": 3,
        "change_message": ""
    }
},
{
    "model": "admin.logentry",
    "pk": 67,
    "fields": {
        "action_time": "2026-03-19T15:15:05.810Z",
        "user": [
            "efosa"
        ],
        "content_type": [
            "store",
            "product"
        ],
        "object_id": "63",
        "object_repr": "Precision Brow Pencil",
        "action_flag": 3,
        "change_message": ""
    }
},
{
    "model": "admin.logentry",
    "pk": 68,
    "fields": {
        "action_time": "2026-03-19T15:15:05.810Z",
        "user": [
            "efosa"
        ],
        "content_type": [
            "store",
            "product"
        ],
        "object_id": "62",
        "object_repr": "Tinted Brow Grooming Gel",
        "action_flag": 3,
        "change_message": ""
    }
},
{
    "model": "admin.logentry",
    "pk": 69,
    "fields": {
        "action_time": "2026-03-19T15:15:05.810Z",
        "user": [
            "efosa"
        ],
        "content_type": [
            "store",
            "product"
        ],
        "object_id": "61",
        "object_repr": "Smoothing Primer Base",
        "action_flag": 3,
        "change_message": ""
    }
},
{
    "model": "admin.logentry",
    "pk": 70,
    "fields": {
        "action_time": "2026-03-19T15:15:05.810Z",
        "user": [
            "efosa"
        ],
        "content_type": [
            "store",
            "product"
        ],
        "object_id": "60",
        "object_repr": "Hydrating Lip Oil",
        "action_flag": 3,
        "change_message": ""
    }
},
{
    "model": "admin.logentry",
    "pk": 71,
    "fields": {
        "action_time": "2026-03-19T15:15:05.810Z",
        "user": [
            "efosa"
        ],
        "content_type": [
            "store",
            "product"
        ],
        "object_id": "59",
        "object_repr": "Defining Liquid Eyeliner",
        "action_flag": 3,
        "change_message": ""
    }
},
{
    "model": "admin.logentry",
    "pk": 72,
    "fields": {
        "action_time": "2026-03-19T15:15:05.810Z",
        "user": [
            "efosa"
        ],
        "content_type": [
            "store",
            "product"
        ],
        "object_id": "58",
        "object_repr": "Sunset Rose Blush Palette",
        "action_flag": 3,
        "change_message": ""
    }
},
{
    "model": "admin.logentry",
    "pk": 73,
    "fields": {
        "action_time": "2026-03-19T15:15:05.810Z",
        "user": [
            "efosa"
        ],
        "content_type": [
            "store",
            "product"
        ],
        "object_id": "57",
        "object_repr": "Starlight Liquid Highlighter",
        "action_flag": 3,
        "change_message": ""
    }
},
{
    "model": "admin.logentry",
    "pk": 74,
    "fields": {
        "action_time": "2026-03-19T15:15:05.810Z",
        "user": [
            "efosa"
        ],
        "content_type": [
            "store",
            "product"
        ],
        "object_id": "56",
        "object_repr": "Creamy Radiant Concealer",
        "action_flag": 3,
        "change_message": ""
    }
},
{
    "model": "admin.logentry",
    "pk": 75,
    "fields": {
        "action_time": "2026-03-19T15:15:05.810Z",
        "user": [
            "efosa"
        ],
        "content_type": [
            "store",
            "product"
        ],
        "object_id": "55",
        "object_repr": "HD Finishing Powder",
        "action_flag": 3,
        "change_message": ""
    }
},
{
    "model": "admin.logentry",
    "pk": 76,
    "fields": {
        "action_time": "2026-03-19T15:15:05.810Z",
        "user": [
            "efosa"
        ],
        "content_type": [
            "store",
            "product"
        ],
        "object_id": "54",
        "object_repr": "Waterproof Volumizing Mascara",
        "action_flag": 3,
        "change_message": ""
    }
},
{
    "model": "admin.logentry",
    "pk": 77,
    "fields": {
        "action_time": "2026-03-19T15:15:05.810Z",
        "user": [
            "efosa"
        ],
        "content_type": [
            "store",
            "product"
        ],
        "object_id": "53",
        "object_repr": "Luminous Silk Foundation",
        "action_flag": 3,
        "change_message": ""
    }
},
{
    "model": "admin.logentry",
    "pk": 78,
    "fields": {
        "action_time": "2026-03-19T15:15:05.810Z",
        "user": [
            "efosa"
        ],
        "content_type": [
            "store",
            "product"
        ],
        "object_id": "52",
        "object_repr": "Velvet Matte Lipstick",
        "action_flag": 3,
        "change_message": ""
    }
},
{
    "model": "admin.logentry",
    "pk": 79,
    "fields": {
        "action_time": "2026-03-19T15:15:05.810Z",
        "user": [
            "efosa"
        ],
        "content_type": [
            "store",
            "product"
        ],
        "object_id": "51",
        "object_repr": "Exfoliating Fruit Acid Peel",
        "action_flag": 3,
        "change_message": ""
    }
},
{
    "model": "admin.logentry",
    "pk": 80,
    "fields": {
        "action_time": "2026-03-19T15:15:05.810Z",
        "user": [
            "efosa"
        ],
        "content_type": [
            "store",
            "product"
        ],
        "object_id": "50",
        "object_repr": "Antioxidant Face Oil",
        "action_flag": 3,
        "change_message": ""
    }
},
{
    "model": "admin.logentry",
    "pk": 81,
    "fields": {
        "action_time": "2026-03-19T15:15:05.810Z",
        "user": [
            "efosa"
        ],
        "content_type": [
            "store",
            "product"
        ],
        "object_id": "49",
        "object_repr": "Seaweed Clay Mask",
        "action_flag": 3,
        "change_message": ""
    }
},
{
    "model": "admin.logentry",
    "pk": 82,
    "fields": {
        "action_time": "2026-03-19T15:15:05.810Z",
        "user": [
            "efosa"
        ],
        "content_type": [
            "store",
            "product"
        ],
        "object_id": "48",
        "object_repr": "Bakuchiol Natural Alternative",
        "action_flag": 3,
        "change_message": ""
    }
},
{
    "model": "admin.logentry",
    "pk": 83,
    "fields": {
        "action_time": "2026-03-19T15:15:05.810Z",
        "user": [
            "efosa"
        ],
        "content_type": [
            "store",
            "product"
        ],
        "object_id": "47",
        "object_repr": "Deep Cleansing Balm",
        "action_flag": 3,
        "change_message": ""
    }
},
{
    "model": "admin.logentry",
    "pk": 84,
    "fields": {
        "action_time": "2026-03-19T15:15:05.810Z",
        "user": [
            "efosa"
        ],
        "content_type": [
            "store",
            "product"
        ],
        "object_id": "46",
        "object_repr": "Daily Defense Moisturizer",
        "action_flag": 3,
        "change_message": ""
    }
},
{
    "model": "admin.logentry",
    "pk": 85,
    "fields": {
        "action_time": "2026-03-19T15:15:05.810Z",
        "user": [
            "efosa"
        ],
        "content_type": [
            "store",
            "product"
        ],
        "object_id": "45",
        "object_repr": "Soothing Aloe Vera Mist",
        "action_flag": 3,
        "change_message": ""
    }
},
{
    "model": "admin.logentry",
    "pk": 86,
    "fields": {
        "action_time": "2026-03-19T15:15:05.810Z",
        "user": [
            "efosa"
        ],
        "content_type": [
            "store",
            "product"
        ],
        "object_id": "44",
        "object_repr": "Smoothing Peptide Lotion",
        "action_flag": 3,
        "change_message": ""
    }
},
{
    "model": "admin.logentry",
    "pk": 87,
    "fields": {
        "action_time": "2026-03-19T15:15:05.810Z",
        "user": [
            "efosa"
        ],
        "content_type": [
            "store",
            "product"
        ],
        "object_id": "43",
        "object_repr": "Niacinamide Pore Refiner",
        "action_flag": 3,
        "change_message": ""
    }
},
{
    "model": "admin.logentry",
    "pk": 88,
    "fields": {
        "action_time": "2026-03-19T15:15:05.810Z",
        "user": [
            "efosa"
        ],
        "content_type": [
            "store",
            "product"
        ],
        "object_id": "42",
        "object_repr": "Ceramide Barrier Balm",
        "action_flag": 3,
        "change_message": ""
    }
},
{
    "model": "admin.logentry",
    "pk": 89,
    "fields": {
        "action_time": "2026-03-19T15:15:05.810Z",
        "user": [
            "efosa"
        ],
        "content_type": [
            "store",
            "product"
        ],
        "object_id": "41",
        "object_repr": "Under-Eye Caffeine Gel",
        "action_flag": 3,
        "change_message": ""
    }
},
{
    "model": "admin.logentry",
    "pk": 90,
    "fields": {
        "action_time": "2026-03-19T15:15:05.810Z",
        "user": [
            "efosa"
        ],
        "content_type": [
            "store",
            "product"
        ],
        "object_id": "40",
        "object_repr": "Clarifying Detox Scrub",
        "action_flag": 3,
        "change_message": ""
    }
},
{
    "model": "admin.logentry",
    "pk": 91,
    "fields": {
        "action_time": "2026-03-19T15:15:05.810Z",
        "user": [
            "efosa"
        ],
        "content_type": [
            "store",
            "product"
        ],
        "object_id": "39",
        "object_repr": "Retinol Renewal Oil",
        "action_flag": 3,
        "change_message": ""
    }
},
{
    "model": "admin.logentry",
    "pk": 92,
    "fields": {
        "action_time": "2026-03-19T15:15:05.810Z",
        "user": [
            "efosa"
        ],
        "content_type": [
            "store",
            "product"
        ],
        "object_id": "38",
        "object_repr": "Mineral SPF 50 Sunscreen",
        "action_flag": 3,
        "change_message": ""
    }
},
{
    "model": "admin.logentry",
    "pk": 93,
    "fields": {
        "action_time": "2026-03-19T15:15:05.810Z",
        "user": [
            "efosa"
        ],
        "content_type": [
            "store",
            "product"
        ],
        "object_id": "37",
        "object_repr": "Rosewater Facial Mist",
        "action_flag": 3,
        "change_message": ""
    }
},
{
    "model": "admin.logentry",
    "pk": 94,
    "fields": {
        "action_time": "2026-03-19T15:15:05.811Z",
        "user": [
            "efosa"
        ],
        "content_type": [
            "store",
            "product"
        ],
        "object_id": "36",
        "object_repr": "Hyaluronic Acid Plump Drops",
        "action_flag": 3,
        "change_message": ""
    }
},
{
    "model": "admin.logentry",
    "pk": 95,
    "fields": {
        "action_time": "2026-03-19T15:15:05.811Z",
        "user": [
            "efosa"
        ],
        "content_type": [
            "store",
            "product"
        ],
        "object_id": "35",
        "object_repr": "Vitamin C Brightening Mask",
        "action_flag": 3,
        "change_message": ""
    }
},
{
    "model": "admin.logentry",
    "pk": 96,
    "fields": {
        "action_time": "2026-03-19T15:15:05.811Z",
        "user": [
            "efosa"
        ],
        "content_type": [
            "store",
            "product"
        ],
        "object_id": "34",
        "object_repr": "Gentle Oat Cleanser",
        "action_flag": 3,
        "change_message": ""
    }
},
{
    "model": "admin.logentry",
    "pk": 97,
    "fields": {
        "action_time": "2026-03-19T15:15:05.811Z",
        "user": [
            "efosa"
        ],
        "content_type": [
            "store",
            "product"
        ],
        "object_id": "33",
        "object_repr": "Rejuvenating Night Cream",
        "action_flag": 3,
        "change_message": ""
    }
},
{
    "model": "admin.logentry",
    "pk": 98,
    "fields": {
        "action_time": "2026-03-19T15:15:05.811Z",
        "user": [
            "efosa"
        ],
        "content_type": [
            "store",
            "product"
        ],
        "object_id": "32",
        "object_repr": "Hydrating Glow Serum",
        "action_flag": 3,
        "change_message": ""
    }
},
{
    "model": "admin.logentry",
    "pk": 99,
    "fields": {
        "action_time": "2026-03-19T15:20:49.329Z",
        "user": [
            "efosa"
        ],
        "content_type": [
            "store",
            "product"
        ],
        "object_id": "92",
        "object_repr": "Gentle Cleanser",
        "action_flag": 2,
        "change_message": "[{\"changed\": {\"fields\": [\"Name\", \"Price\", \"Old price\"]}}]"
    }
},
{
    "model": "admin.logentry",
    "pk": 100,
    "fields": {
        "action_time": "2026-03-19T15:21:33.295Z",
        "user": [
            "efosa"
        ],
        "content_type": [
            "store",
            "product"
        ],
        "object_id": "98",
        "object_repr": "Gentle Cleanser",
        "action_flag": 2,
        "change_message": "[{\"changed\": {\"fields\": [\"Name\", \"Price\", \"Old price\"]}}]"
    }
},
{
    "model": "admin.logentry",
    "pk": 101,
    "fields": {
        "action_time": "2026-03-19T15:21:56.105Z",
        "user": [
            "efosa"
        ],
        "content_type": [
            "store",
            "product"
        ],
        "object_id": "92",
        "object_repr": "Gentle Cleanser",
        "action_flag": 3,
        "change_message": ""
    }
},
{
    "model": "admin.logentry",
    "pk": 102,
    "fields": {
        "action_time": "2026-03-19T15:23:14.526Z",
        "user": [
            "efosa"
        ],
        "content_type": [
            "store",
            "product"
        ],
        "object_id": "99",
        "object_repr": "Body Lotion",
        "action_flag": 2,
        "change_message": "[{\"changed\": {\"fields\": [\"Name\", \"Price\", \"Old price\", \"Is best selling\"]}}]"
    }
},
{
    "model": "admin.logentry",
    "pk": 103,
    "fields": {
        "action_time": "2026-03-19T15:25:36.756Z",
        "user": [
            "efosa"
        ],
        "content_type": [
            "store",
            "product"
        ],
        "object_id": "106",
        "object_repr": "bamboo fibers shampoo",
        "action_flag": 2,
        "change_message": "[{\"changed\": {\"fields\": [\"Category\", \"Name\", \"Price\", \"Old price\", \"Is best selling\"]}}]"
    }
},
{
    "model": "admin.logentry",
    "pk": 104,
    "fields": {
        "action_time": "2026-03-19T15:26:41.272Z",
        "user": [
            "efosa"
        ],
        "content_type": [
            "store",
            "product"
        ],
        "object_id": "94",
        "object_repr": "Multi-Action Foam Cleanser",
        "action_flag": 2,
        "change_message": "[{\"changed\": {\"fields\": [\"Category\", \"Name\"]}}]"
    }
},
{
    "model": "admin.logentry",
    "pk": 105,
    "fields": {
        "action_time": "2026-03-19T15:27:02.564Z",
        "user": [
            "efosa"
        ],
        "content_type": [
            "store",
            "product"
        ],
        "object_id": "133",
        "object_repr": "Shea Conditioner",
        "action_flag": 3,
        "change_message": ""
    }
},
{
    "model": "admin.logentry",
    "pk": 106,
    "fields": {
        "action_time": "2026-03-19T15:29:55.570Z",
        "user": [
            "efosa"
        ],
        "content_type": [
            "store",
            "product"
        ],
        "object_id": "132",
        "object_repr": "Argan Shampoo",
        "action_flag": 2,
        "change_message": "[{\"changed\": {\"fields\": [\"Price\", \"Old price\", \"Image\"]}}]"
    }
},
{
    "model": "admin.logentry",
    "pk": 107,
    "fields": {
        "action_time": "2026-03-19T15:31:28.381Z",
        "user": [
            "efosa"
        ],
        "content_type": [
            "store",
            "product"
        ],
        "object_id": "134",
        "object_repr": "Volumizing Mist",
        "action_flag": 2,
        "change_message": "[{\"changed\": {\"fields\": [\"Price\", \"Old price\", \"Image\", \"Is best selling\"]}}]"
    }
},
{
    "model": "admin.logentry",
    "pk": 108,
    "fields": {
        "action_time": "2026-03-19T15:32:37.313Z",
        "user": [
            "efosa"
        ],
        "content_type": [
            "store",
            "product"
        ],
        "object_id": "135",
        "object_repr": "Keratin Mask",
        "action_flag": 2,
        "change_message": "[{\"changed\": {\"fields\": [\"Image\"]}}]"
    }
},
{
    "model": "admin.logentry",
    "pk": 109,
    "fields": {
        "action_time": "2026-03-19T15:33:59.427Z",
        "user": [
            "efosa"
        ],
        "content_type": [
            "store",
            "product"
        ],
        "object_id": "135",
        "object_repr": "Keratin Mask",
        "action_flag": 2,
        "change_message": "[{\"changed\": {\"fields\": [\"Price\", \"Old price\"]}}]"
    }
},
{
    "model": "admin.logentry",
    "pk": 110,
    "fields": {
        "action_time": "2026-03-19T15:35:28.684Z",
        "user": [
            "efosa"
        ],
        "content_type": [
            "store",
            "product"
        ],
        "object_id": "136",
        "object_repr": "Peppermint Scrub",
        "action_flag": 2,
        "change_message": "[{\"changed\": {\"fields\": [\"Image\"]}}]"
    }
},
{
    "model": "admin.logentry",
    "pk": 111,
    "fields": {
        "action_time": "2026-03-19T15:35:57.512Z",
        "user": [
            "efosa"
        ],
        "content_type": [
            "store",
            "product"
        ],
        "object_id": "136",
        "object_repr": "Peppermint Scrub",
        "action_flag": 2,
        "change_message": "[{\"changed\": {\"fields\": [\"Price\", \"Old price\"]}}]"
    }
},
{
    "model": "admin.logentry",
    "pk": 112,
    "fields": {
        "action_time": "2026-03-19T15:37:52.104Z",
        "user": [
            "efosa"
        ],
        "content_type": [
            "store",
            "product"
        ],
        "object_id": "137",
        "object_repr": "Protein Leave-in",
        "action_flag": 2,
        "change_message": "[{\"changed\": {\"fields\": [\"Price\", \"Old price\", \"Image\"]}}]"
    }
},
{
    "model": "admin.logentry",
    "pk": 113,
    "fields": {
        "action_time": "2026-03-19T15:39:21.520Z",
        "user": [
            "efosa"
        ],
        "content_type": [
            "store",
            "product"
        ],
        "object_id": "138",
        "object_repr": "Glossing Serum",
        "action_flag": 2,
        "change_message": "[{\"changed\": {\"fields\": [\"Price\", \"Old price\", \"Image\"]}}]"
    }
},
{
    "model": "admin.logentry",
    "pk": 114,
    "fields": {
        "action_time": "2026-03-19T15:41:20.309Z",
        "user": [
            "efosa"
        ],
        "content_type": [
            "store",
            "product"
        ],
        "object_id": "139",
        "object_repr": "Coconut Detangler",
        "action_flag": 2,
        "change_message": "[{\"changed\": {\"fields\": [\"Price\", \"Old price\", \"Image\"]}}]"
    }
},
{
    "model": "admin.logentry",
    "pk": 115,
    "fields": {
        "action_time": "2026-03-19T15:43:08.033Z",
        "user": [
            "efosa"
        ],
        "content_type": [
            "store",
            "product"
        ],
        "object_id": "140",
        "object_repr": "Tea Tree Wash",
        "action_flag": 2,
        "change_message": "[{\"changed\": {\"fields\": [\"Price\", \"Old price\", \"Image\"]}}]"
    }
},
{
    "model": "admin.logentry",
    "pk": 116,
    "fields": {
        "action_time": "2026-03-19T15:44:19.200Z",
        "user": [
            "efosa"
        ],
        "content_type": [
            "store",
            "product"
        ],
        "object_id": "141",
        "object_repr": "Anti-Frizz Gel",
        "action_flag": 2,
        "change_message": "[{\"changed\": {\"fields\": [\"Price\", \"Old price\", \"Image\"]}}]"
    }
},
{
    "model": "admin.logentry",
    "pk": 117,
    "fields": {
        "action_time": "2026-03-19T15:45:44.632Z",
        "user": [
            "efosa"
        ],
        "content_type": [
            "store",
            "product"
        ],
        "object_id": "142",
        "object_repr": "Dry Shampoo",
        "action_flag": 2,
        "change_message": "[{\"changed\": {\"fields\": [\"Price\", \"Old price\", \"Image\"]}}]"
    }
},
{
    "model": "admin.logentry",
    "pk": 118,
    "fields": {
        "action_time": "2026-03-19T15:46:42.423Z",
        "user": [
            "efosa"
        ],
        "content_type": [
            "store",
            "product"
        ],
        "object_id": "151",
        "object_repr": "Bamboo Water",
        "action_flag": 3,
        "change_message": ""
    }
},
{
    "model": "admin.logentry",
    "pk": 119,
    "fields": {
        "action_time": "2026-03-19T15:46:42.423Z",
        "user": [
            "efosa"
        ],
        "content_type": [
            "store",
            "product"
        ],
        "object_id": "148",
        "object_repr": "Toning Shampoo",
        "action_flag": 3,
        "change_message": ""
    }
},
{
    "model": "admin.logentry",
    "pk": 120,
    "fields": {
        "action_time": "2026-03-19T15:46:42.423Z",
        "user": [
            "efosa"
        ],
        "content_type": [
            "store",
            "product"
        ],
        "object_id": "147",
        "object_repr": "Fiber Cream",
        "action_flag": 3,
        "change_message": ""
    }
},
{
    "model": "admin.logentry",
    "pk": 121,
    "fields": {
        "action_time": "2026-03-19T15:46:42.423Z",
        "user": [
            "efosa"
        ],
        "content_type": [
            "store",
            "product"
        ],
        "object_id": "146",
        "object_repr": "Honey Hair Mask",
        "action_flag": 3,
        "change_message": ""
    }
},
{
    "model": "admin.logentry",
    "pk": 122,
    "fields": {
        "action_time": "2026-03-19T15:46:42.423Z",
        "user": [
            "efosa"
        ],
        "content_type": [
            "store",
            "product"
        ],
        "object_id": "145",
        "object_repr": "Scalp Treatment",
        "action_flag": 3,
        "change_message": ""
    }
},
{
    "model": "admin.logentry",
    "pk": 123,
    "fields": {
        "action_time": "2026-03-19T15:46:42.423Z",
        "user": [
            "efosa"
        ],
        "content_type": [
            "store",
            "product"
        ],
        "object_id": "144",
        "object_repr": "Heat Shield",
        "action_flag": 3,
        "change_message": ""
    }
},
{
    "model": "admin.logentry",
    "pk": 124,
    "fields": {
        "action_time": "2026-03-19T15:46:42.423Z",
        "user": [
            "efosa"
        ],
        "content_type": [
            "store",
            "product"
        ],
        "object_id": "143",
        "object_repr": "Castor Oil",
        "action_flag": 3,
        "change_message": ""
    }
},
{
    "model": "admin.logentry",
    "pk": 125,
    "fields": {
        "action_time": "2026-03-19T15:50:18.820Z",
        "user": [
            "efosa"
        ],
        "content_type": [
            "store",
            "product"
        ],
        "object_id": "93",
        "object_repr": "Night Cream",
        "action_flag": 2,
        "change_message": "[{\"changed\": {\"fields\": [\"Price\", \"Old price\", \"Image\"]}}]"
    }
},
{
    "model": "admin.logentry",
    "pk": 126,
    "fields": {
        "action_time": "2026-03-19T15:51:16.324Z",
        "user": [
            "efosa"
        ],
        "content_type": [
            "store",
            "product"
        ],
        "object_id": "95",
        "object_repr": "Brightening Mask",
        "action_flag": 2,
        "change_message": "[{\"changed\": {\"fields\": [\"Price\", \"Old price\", \"Image\"]}}]"
    }
},
{
    "model": "admin.logentry",
    "pk": 127,
    "fields": {
        "action_time": "2026-03-19T15:52:21.644Z",
        "user": [
            "efosa"
        ],
        "content_type": [
            "store",
            "product"
        ],
        "object_id": "96",
        "object_repr": "Hyaluronic Drops",
        "action_flag": 2,
        "change_message": "[{\"changed\": {\"fields\": [\"Price\", \"Old price\", \"Image\"]}}]"
    }
},
{
    "model": "admin.logentry",
    "pk": 128,
    "fields": {
        "action_time": "2026-03-19T15:53:27.443Z",
        "user": [
            "efosa"
        ],
        "content_type": [
            "store",
            "product"
        ],
        "object_id": "97",
        "object_repr": "Facial Mist",
        "action_flag": 2,
        "change_message": "[{\"changed\": {\"fields\": [\"Price\", \"Old price\", \"Image\"]}}]"
    }
},
{
    "model": "admin.logentry",
    "pk": 129,
    "fields": {
        "action_time": "2026-03-19T15:54:38.836Z",
        "user": [
            "efosa"
        ],
        "content_type": [
            "store",
            "product"
        ],
        "object_id": "100",
        "object_repr": "Detox Scrub",
        "action_flag": 2,
        "change_message": "[{\"changed\": {\"fields\": [\"Price\", \"Old price\", \"Image\"]}}]"
    }
},
{
    "model": "admin.logentry",
    "pk": 130,
    "fields": {
        "action_time": "2026-03-19T15:55:45.924Z",
        "user": [
            "efosa"
        ],
        "content_type": [
            "store",
            "product"
        ],
        "object_id": "101",
        "object_repr": "Caffeine Gel",
        "action_flag": 2,
        "change_message": "[{\"changed\": {\"fields\": [\"Price\", \"Old price\"]}}]"
    }
},
{
    "model": "admin.logentry",
    "pk": 131,
    "fields": {
        "action_time": "2026-03-19T15:56:05.944Z",
        "user": [
            "efosa"
        ],
        "content_type": [
            "store",
            "product"
        ],
        "object_id": "101",
        "object_repr": "Caffeine Gel",
        "action_flag": 2,
        "change_message": "[{\"changed\": {\"fields\": [\"Image\"]}}]"
    }
},
{
    "model": "admin.logentry",
    "pk": 132,
    "fields": {
        "action_time": "2026-03-19T15:58:04.170Z",
        "user": [
            "efosa"
        ],
        "content_type": [
            "store",
            "product"
        ],
        "object_id": "107",
        "object_repr": "Cleansing Balm",
        "action_flag": 3,
        "change_message": ""
    }
},
{
    "model": "admin.logentry",
    "pk": 133,
    "fields": {
        "action_time": "2026-03-19T15:58:04.170Z",
        "user": [
            "efosa"
        ],
        "content_type": [
            "store",
            "product"
        ],
        "object_id": "104",
        "object_repr": "Peptide Lotion",
        "action_flag": 3,
        "change_message": ""
    }
},
{
    "model": "admin.logentry",
    "pk": 134,
    "fields": {
        "action_time": "2026-03-19T15:58:04.170Z",
        "user": [
            "efosa"
        ],
        "content_type": [
            "store",
            "product"
        ],
        "object_id": "103",
        "object_repr": "Pore Refiner",
        "action_flag": 3,
        "change_message": ""
    }
},
{
    "model": "admin.logentry",
    "pk": 135,
    "fields": {
        "action_time": "2026-03-19T15:58:04.170Z",
        "user": [
            "efosa"
        ],
        "content_type": [
            "store",
            "product"
        ],
        "object_id": "102",
        "object_repr": "Barrier Balm",
        "action_flag": 3,
        "change_message": ""
    }
},
{
    "model": "admin.logentry",
    "pk": 136,
    "fields": {
        "action_time": "2026-03-19T15:58:36.833Z",
        "user": [
            "efosa"
        ],
        "content_type": [
            "store",
            "product"
        ],
        "object_id": "111",
        "object_repr": "Fruit Peel",
        "action_flag": 3,
        "change_message": ""
    }
},
{
    "model": "admin.logentry",
    "pk": 137,
    "fields": {
        "action_time": "2026-03-19T15:58:36.833Z",
        "user": [
            "efosa"
        ],
        "content_type": [
            "store",
            "product"
        ],
        "object_id": "108",
        "object_repr": "Natural Bakuchiol",
        "action_flag": 3,
        "change_message": ""
    }
},
{
    "model": "admin.logentry",
    "pk": 138,
    "fields": {
        "action_time": "2026-03-19T15:58:36.833Z",
        "user": [
            "efosa"
        ],
        "content_type": [
            "store",
            "product"
        ],
        "object_id": "105",
        "object_repr": "Aloe Mist",
        "action_flag": 3,
        "change_message": ""
    }
},
{
    "model": "admin.logentry",
    "pk": 139,
    "fields": {
        "action_time": "2026-03-19T15:59:41.424Z",
        "user": [
            "efosa"
        ],
        "content_type": [
            "store",
            "product"
        ],
        "object_id": "109",
        "object_repr": "Seaweed Mask",
        "action_flag": 2,
        "change_message": "[{\"changed\": {\"fields\": [\"Price\", \"Old price\", \"Image\"]}}]"
    }
},
{
    "model": "admin.logentry",
    "pk": 140,
    "fields": {
        "action_time": "2026-03-19T16:00:51.273Z",
        "user": [
            "efosa"
        ],
        "content_type": [
            "store",
            "product"
        ],
        "object_id": "110",
        "object_repr": "Face Oil",
        "action_flag": 2,
        "change_message": "[{\"changed\": {\"fields\": [\"Price\", \"Old price\", \"Image\"]}}]"
    }
},
{
    "model": "admin.logentry",
    "pk": 141,
    "fields": {
        "action_time": "2026-03-19T16:02:55.457Z",
        "user": [
            "efosa"
        ],
        "content_type": [
            "store",
            "product"
        ],
        "object_id": "114",
        "object_repr": "Volumizing Mascara",
        "action_flag": 2,
        "change_message": "[{\"changed\": {\"fields\": [\"Price\", \"Old price\", \"Image\"]}}]"
    }
},
{
    "model": "admin.logentry",
    "pk": 142,
    "fields": {
        "action_time": "2026-03-19T16:03:49.269Z",
        "user": [
            "efosa"
        ],
        "content_type": [
            "store",
            "product"
        ],
        "object_id": "122",
        "object_repr": "Matte Lipstick",
        "action_flag": 2,
        "change_message": "[{\"changed\": {\"fields\": [\"Name\"]}}]"
    }
},
{
    "model": "admin.logentry",
    "pk": 143,
    "fields": {
        "action_time": "2026-03-19T16:05:05.121Z",
        "user": [
            "efosa"
        ],
        "content_type": [
            "store",
            "product"
        ],
        "object_id": "123",
        "object_repr": "Brown Skin Powder",
        "action_flag": 2,
        "change_message": "[{\"changed\": {\"fields\": [\"Name\"]}}]"
    }
},
{
    "model": "admin.logentry",
    "pk": 144,
    "fields": {
        "action_time": "2026-03-19T16:05:24.608Z",
        "user": [
            "efosa"
        ],
        "content_type": [
            "store",
            "product"
        ],
        "object_id": "122",
        "object_repr": "Matte Lipstick",
        "action_flag": 2,
        "change_message": "[{\"changed\": {\"fields\": [\"Price\", \"Old price\"]}}]"
    }
},
{
    "model": "admin.logentry",
    "pk": 145,
    "fields": {
        "action_time": "2026-03-19T16:06:50.964Z",
        "user": [
            "efosa"
        ],
        "content_type": [
            "store",
            "product"
        ],
        "object_id": "120",
        "object_repr": "Hydrating Lip Oil",
        "action_flag": 2,
        "change_message": "[{\"changed\": {\"fields\": [\"Price\", \"Old price\", \"Image\"]}}]"
    }
},
{
    "model": "admin.logentry",
    "pk": 146,
    "fields": {
        "action_time": "2026-03-19T16:07:54.637Z",
        "user": [
            "efosa"
        ],
        "content_type": [
            "store",
            "product"
        ],
        "object_id": "121",
        "object_repr": "Primer Base",
        "action_flag": 2,
        "change_message": "[{\"changed\": {\"fields\": [\"Old price\", \"Image\", \"Is best selling\"]}}]"
    }
},
{
    "model": "admin.logentry",
    "pk": 147,
    "fields": {
        "action_time": "2026-03-19T16:08:41.294Z",
        "user": [
            "efosa"
        ],
        "content_type": [
            "store",
            "product"
        ],
        "object_id": "131",
        "object_repr": "Eye Primer",
        "action_flag": 2,
        "change_message": "[{\"changed\": {\"fields\": [\"Price\", \"Old price\", \"Image\"]}}]"
    }
},
{
    "model": "admin.logentry",
    "pk": 148,
    "fields": {
        "action_time": "2026-03-19T16:09:46.483Z",
        "user": [
            "efosa"
        ],
        "content_type": [
            "store",
            "product"
        ],
        "object_id": "128",
        "object_repr": "Lip Liner",
        "action_flag": 2,
        "change_message": "[{\"changed\": {\"fields\": [\"Price\", \"Old price\", \"Image\"]}}]"
    }
},
{
    "model": "admin.logentry",
    "pk": 149,
    "fields": {
        "action_time": "2026-03-19T16:11:32.205Z",
        "user": [
            "efosa"
        ],
        "content_type": [
            "store",
            "product"
        ],
        "object_id": "118",
        "object_repr": "Blush Palette",
        "action_flag": 2,
        "change_message": "[{\"changed\": {\"fields\": [\"Price\", \"Old price\", \"Image\"]}}]"
    }
},
{
    "model": "admin.logentry",
    "pk": 150,
    "fields": {
        "action_time": "2026-03-19T16:11:59.673Z",
        "user": [
            "efosa"
        ],
        "content_type": [
            "store",
            "product"
        ],
        "object_id": "127",
        "object_repr": "Tinted Moisturizer",
        "action_flag": 3,
        "change_message": ""
    }
},
{
    "model": "admin.logentry",
    "pk": 151,
    "fields": {
        "action_time": "2026-03-19T16:11:59.673Z",
        "user": [
            "efosa"
        ],
        "content_type": [
            "store",
            "product"
        ],
        "object_id": "126",
        "object_repr": "Sculpt Stick",
        "action_flag": 3,
        "change_message": ""
    }
},
{
    "model": "admin.logentry",
    "pk": 152,
    "fields": {
        "action_time": "2026-03-19T16:11:59.673Z",
        "user": [
            "efosa"
        ],
        "content_type": [
            "store",
            "product"
        ],
        "object_id": "125",
        "object_repr": "Eye Pigment",
        "action_flag": 3,
        "change_message": ""
    }
},
{
    "model": "admin.logentry",
    "pk": 153,
    "fields": {
        "action_time": "2026-03-19T16:11:59.673Z",
        "user": [
            "efosa"
        ],
        "content_type": [
            "store",
            "product"
        ],
        "object_id": "124",
        "object_repr": "Setting Spray",
        "action_flag": 3,
        "change_message": ""
    }
},
{
    "model": "admin.logentry",
    "pk": 154,
    "fields": {
        "action_time": "2026-03-19T16:12:57.158Z",
        "user": [
            "efosa"
        ],
        "content_type": [
            "store",
            "product"
        ],
        "object_id": "130",
        "object_repr": "Lip Stain",
        "action_flag": 2,
        "change_message": "[{\"changed\": {\"fields\": [\"Price\", \"Old price\", \"Image\"]}}]"
    }
},
{
    "model": "admin.logentry",
    "pk": 155,
    "fields": {
        "action_time": "2026-03-19T16:13:13.820Z",
        "user": [
            "efosa"
        ],
        "content_type": [
            "store",
            "product"
        ],
        "object_id": "129",
        "object_repr": "Coverage Palette",
        "action_flag": 3,
        "change_message": ""
    }
},
{
    "model": "admin.logentry",
    "pk": 156,
    "fields": {
        "action_time": "2026-03-19T16:13:29.263Z",
        "user": [
            "efosa"
        ],
        "content_type": [
            "store",
            "product"
        ],
        "object_id": "117",
        "object_repr": "Liquid Highlighter",
        "action_flag": 3,
        "change_message": ""
    }
},
{
    "model": "admin.logentry",
    "pk": 157,
    "fields": {
        "action_time": "2026-03-19T16:13:29.263Z",
        "user": [
            "efosa"
        ],
        "content_type": [
            "store",
            "product"
        ],
        "object_id": "116",
        "object_repr": "Radiant Concealer",
        "action_flag": 3,
        "change_message": ""
    }
}
]



print(len(me))