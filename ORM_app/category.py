#-*- coding: utf-8-*-
# encoding=utf8
import sys

reload(sys)
sys.setdefaultencoding('utf8')





def digikala_category(category, category2):
    if category == 'Tablet-EBook-Reader':
        if category2 == "Accessories-Main":
            return 'Digital-Accessories'
        else:
            return 'Tablet'
    elif category == 'Mobile':
        if category2 == "Category-Mobile-Phone":
            return 'Mobile'
        else:
            return 'Digital-Accessories'
    elif category == 'Camera':
        if category2 == "Accessories-Main":
            return 'Digital-Accessories'
        else:
            return 'Camera'
    elif category == 'Computer-Parts':
        if category2 == "Category-Digital-Pen" or category2 == "Accessories-Main" or category2 == "Category-Gaming-Accessories" or category2 == "Video-Audio-Entertainment":
            masir_cat = 'Digital-Accessories'
        else:
            return 'Computer-Parts'
    elif category == 'Laptop':
        if category2 == "Category-Notebook-Netbook-Ultrabook":
            return 'Laptop'
        else:
            return 'Digital-Accessories'
    elif category == 'Office-Machines':
        if category2 == "Accessories-Main":
            return 'Digital-Accessories'
        else:
            return 'Office-Machines '

    else:
        digikala_categories = [
            'Accessories-Main'.upper(),
            'Baby-Bedding'.upper(),
            'Beauty'.upper(),
            'BedandBath'.upper(),
            'Bicycle'.upper(),
            'Camera'.upper(),
            'Car-Accessory-parts'.upper(),
            'Carpet'.upper(),
            'Cars'.upper(),
            'Children-and-Baby-Clothing'.upper(),
            'Cleaning'.upper(),
            'Computer-Parts'.upper(),
            'Consumable-Parts'.upper(),
            'Decorative'.upper(),
            'Digikala-Gift-Card'.upper(),
            'Dining-Accessories'.upper(),
            'Electrical-Personal-Care'.upper(),
            'Entertainment-and-Games-Equipment'.upper(),
            'Film-Video-Content'.upper(),
            'Gardening-Tools'.upper(),
            'Hair-Clipper'.upper(),
            'Handicraft'.upper(),
            'Health-and-Bathroom-Tools'.upper(),
            'Health-Care'.upper(),
            'Home-Appliance'.upper(),
            'Home-kitchen-Appliances'.upper(),
            'Jewelery'.upper(),
            'Laptop'.upper(),
            'Lighting'.upper(),
            'Mobile'.upper(),
            'Multimedia-Training-Pack'.upper(),
            'MusicalInstruments'.upper(),
            'Music-Audio-Content'.upper(),
            'Non-Electrical-Tools'.upper(),
            'Office-Machines'.upper(),
            'Perfume-All'.upper(),
            'Personal-Accessories'.upper(),
            'Pesonal-Appliance-Accessories'.upper(),
            'Power-Tools'.upper(),
            'Promenade-and-Travel-Accessories'.upper(),
            'Publication'.upper(),
            'Safety-and-Care'.upper(),
            'Serving'.upper(),
            'Software-Games'.upper(),
            'Sport'.upper(),
            'SportShoes'.upper(),
            'Sports-Wear'.upper(),
            'Stationery'.upper(),
            'Sunglasses'.upper(),
            'Tablet-EBook-Reader'.upper(),
            'Toys'.upper(),
            'Traveling-Equipment'.upper(),
            'Video-Audio-Entertainment'.upper(),
            'Watch-Clock'.upper(),
            'Motorbike'
        ]
        masir_categories = [
            'Digital-Accessories',
            'Kids',
            'Makeup',
            'Bed-Bath',
            'Bicycle',
            'Camera',
            'Car-Equipment',
            'Carpet',
            'Car',
            'Kids',
            'Clean',
            'Computer-Parts',
            'Car-Equipment',
            'Decorative',
            'Gift',
            'Kids',
            'Electrical-Personal',
            'Toy',
            'Film',
            'General-Tool',
            'Health',
            'Handcraft',
            'Bed-Bath',
            'Health',
            'Home-Electrical-Appliance',
            'Home-Kitchen-Appliance',
            'Jewerly',
            'Laptop',
            'General-Home',
            'Mobile',
            'Training',
            'Music-Tools',
            'Music',
            'General-Tool',
            'Office-Machines',
            'Perfume',
            'Kids',
            'Men-Accessories',
            'Electrical-Tool',
            'Travel',
            'Publications',
            'Kids',
            'General-Home',
            'Software-Game',
            'Sport-Tools',
            'Sport-Shoes',
            'Sport-Clothes',
            'staitionery',
            'Glass',
            'Tablet',
            'Toy',
            'Travel',
            'Video-Audio',
            'Watch-Clock',
            'Motorbike'
        ]
        try:
            return masir_categories[digikala_categories.index(category.upper())]
        except:
            return "None"

def digikala_categorize(category1,category2):
    if category1 == 'Mobile':
        if category2 == 'Mobile-Phone':
            return 'Mobile'
        elif category2 == 'Mobile-Accessories':
            return 'Digital_Accessories'
    elif category1 == 'Tablet-EBook-Reader':
        if category2 == 'Tablet-Accessories':
            return 'Digital_Accessories'
        else:
            return 'Tablet'
    elif category1 == 'Laptop':
        if category2 == 'Laptop-Accessories':
            return 'Digital_Accessories'
        else:
            return 'Laptop'
    elif category1 == 'Camera':
        if category2 == 'Camera-Accessories':
            return 'Digital_Accessories'
        else:
            return 'Camera'
    elif category1 == 'Computer-Parts':
        if category2 in ['Data-Storage', 'headphone']:
            return 'Digital_Accessories'
        elif category2 == 'Network':
            return 'Office_Machines'
        else:
            return "Computer_Parts"
    elif category1 == 'Office-Machines':
        return "Office_Machines"
    elif category1 == 'Accessories-Main':
        return "Digital_Accessories"
    elif category1 == 'Video-Audio-Entertainment':
        if category2 == 'Game-Console':
            return "Game_Console"
        else:
            return "Home_Electrical_Appliance"
    elif category1 == 'Home-Appliance':
        return "Home_Electrical_Appliance"
    elif category1 == 'Home-kitchen-Appliances':
        return "Home_kitchen_Appliances"
    elif category1 == 'Serving':
        return "Home_kitchen_Appliances"
    elif category1 == 'Decorative':
        return "Decorative"
    elif category1 == 'Carpet':
        return "Carpet"
    elif category1 == 'BedandBath':
        return "Bed_Bath"
    elif category1 == 'Cleaning':
        return "Clean"
    elif category1 == 'Beauty':
        return "Makeup"
    elif category1 == 'Perfume-All':
        return "Perfume"
    elif category1 == 'Hair-Clipper':
        if category2 in ['face-and-body-cream']:
            return "Skin_Nail"
        elif category2 in ['dental-hygienist', 'anti-sweat', 'body-care']:
            return "Health"
        elif category2 in ["hair-care", "hair-shaving-kit"]:
            return "Hair_Care"
    elif category1 == 'Electrical-Personal-Care':
        return "Electrical_Personal"
    elif category1 == 'Watch-Clock':
        if category2 == "Clocks":
            return "Decorative"
        else:
            return "Watch"
    elif category1 == 'Sunglasses':
        return "Glass"
    elif category1 == 'Jewelery':
        return "Jewelery"
    elif category1 == 'Health-Care':
        return "Health"
    elif category1 == 'Pesonal-Appliance-Accessories':
        return "Men_Women_Accessories"
    elif category1 == 'Publication':
        return "Publication"
    elif category1 == 'Stationery':
        return "Stationery"
    elif category1 == 'Handicraft':
        return "Handcraft"
    elif category1 == 'Carpet':
        return "Carpet"
    elif category1 == 'MusicalInstruments':
        return "Music_Tool"
    elif category1 == 'Music-Audio-Content':
        return "Film_Music"
    elif category1 == 'Film-Video-Content':
        return "Film_Music"
    elif category1 == 'Software-Games':
        return "Software_Game"
    elif category1 == 'Multimedia-Training-Pack':
        return "Training"
    elif category1 == 'Sports-Wear':
        if category2 == "Men":
            return "Men_Sport_Clothes"
        elif category2 == "Ladies":
            return "Women_Sport_Clothes"
        else:
            return "Sport_tools"
    elif category1 == 'SportShoes':
        return "Sport_Shoes"
    elif category1 == 'Sport':
        if category2 in ["hiking-and-camping", "sport-bag-and-backpack"]:
            return "Travel"
        else:
            return "Sport_Tools"
    elif category1 == 'Bicycle':
        return "Bicycle"
    elif category1 == 'Traveling-Equipment':
        return "Traveling_Equipment"
    elif category1 == 'Toys':
        return "Toy"
    elif category1 in ['Baby-Bedding', 'Entertainment-and-Games-Equipment','Promenade-and-Travel-Accessories','Children-and-Baby-Clothing','Health-and-Bathroom-Tools','Personal-Accessories','Dining-Accessories','Safety-and-Care']:
        return "Kid"
    elif category1 == 'Lighting':
        return "General_Home"
    elif category1 == 'Gardening-Tools':
        if category2 in ['hedge-cutters','brush-cutters','lawnmower','chain-saws']:
            return "Electrical_Tool"
        else:
            return "Hand_Tool"
    elif category1 == 'Power-Tools':
        return "Electrical_Tool"
    elif category1 == 'Non-Electrical-Tools':
        return "Hand_Tool"
    elif category1 in ['Consumable-Parts', 'Car-Accessory-parts']:
        return "Car_Equipment"
    elif category1 == 'Cars':
        return "Car"
    elif category1 == 'Motorbike':
        return "Motorbike"


def bamilo_categorize(category1, category2):
    if category1 == 'men_clothes':
        return 'Men_Clothes'
    elif category1 == 'women_clothes':
        return 'Women_Clothes'
    elif category1 == 'mens_shoes':
        return 'Men_Shoes'
    elif category1 == 'women_shoes':
        return 'Women_Shoes'
    elif category1 in ['women_bags_wallets','men_bags_wallets_covers', 'luggages-bags']:
        return 'Bag'
    elif category1 == 'fashion_men_accessories':
        if category2 == 'men_watches':
            return 'Watch'
        elif category2 == 'men_shades_glasses':
            return 'Glass'
        else:
            return 'Men_Accessories'
    elif category1 == 'fashion_women_accessories':
        if category2 == 'women_jewelry':
            return 'Jewelry'
        elif category2 == 'women_watches':
            return 'Watch'
        elif category2 == 'women_shades_glasses':
            return 'Glass'
        else:
            return 'Women_Accessories'
    elif category1 == 'kidsfashion':
        return 'Kid'
    elif category1 == 'luggages-bags':
        return 'Bag'
    elif category1 == 'smartphone_tablet_mobile':
        if category2 == 'mobile_phones':
            return 'Mobile'
        elif category2 == 'mobile_lte_devices':
            return 'None'
        elif category2 == 'tablet_os':
            return 'Tablet'
        elif category2 == 'sim_card':
            return 'Simcard'
    elif category1 == 'electronic_accessories':
        return "Digital_Accessories"
    elif category1 == 'computer_office_equipment_printer_scanner':
        if category2 == 'portable_pc_computer':
            return 'Laptop'
        elif category2 == 'storage_accessories_flash_hdd':
            return 'Digital_Accessiries'
        elif category2 in ['computer_parts', 'desktop_computer']:
            return 'Computer_Parts'
        else:
            return 'Office_Machines'
    elif category1 == 'camera_equipment_photography_imaging':
        if category2 in ['lens','accessories_equipment_photography']:
            return 'Camera_Accessories'
        else:
            return 'Camera'
    elif category1 == 'tv_entertainment_game_console_camera':
        if category2 == 'camera_equipment_photography_imaging':
            return 'Camera'
        elif category2 in ['radio','security-systems','home-cinema-speaker','tv','tv_accessory_3dglass', 'disk_digital_player_dvd_setupbox']:
            return 'Home_Electrical_Appliance'
        elif category2 == 'car-electronic-accessories':
            return 'Car_Equipment'
        elif category2 == 'console_gaming':
            return 'Console_Game'
        elif category2 == 'video_projector':
            return 'Office_Machines'
        elif category2 == 'digital_frame':
            return 'General_Home'
    elif category1 == 'console_gaming':
        return 'Console_Game'
    elif category1 == 'kitchen_kitchenware':
        return 'Home_Kitchen_Appliance'
    elif category1 == 'house_general_goods':
        return 'General_Home'
    elif category1 == 'home-decorating':
        if category2 == 'carpet_kilim':
            return 'Carpet'
        elif category2 == 'home_living_handcrafts':
            return 'Handcraft'
        else:
            return 'Decorative'
    elif category1 == 'bedroom_bed_furniture':
        return 'Bed_Bath'
    elif category1 == 'cleaning_dusting':
        return 'Clean'
    elif category1 in ['home_appliance', 'kitchen_appliance']:
        return 'Home_Electrical_Appliance'
    elif category1 == 'perfumes':
        return 'Perfume'
    elif category1 in ['skin_care','hand_feet_nails']:
        return 'Skin_Nail'
    elif category1 == 'makeup':
        return 'Makeup'
    elif category1 in ['oral_care','human_health']:
        return 'Health'
    elif category1 == 'hair_care':
        return 'Hair_Care'
    elif category1 == 'shaving_grooming':
        return 'Electrical_Personal'
    elif category1 == 'toddler':
        return 'Kid'
    elif category1 == 'men_sportswear':
        return 'Men_Sport-Clothes'
    elif category1 == 'women_sportswear':
        return 'Women_Sport-Clothes'
    elif category1 in ['sports_apparel']:
        if category2 == "sports_shoes":
            return "Sport_Shoes"
        else:
            return 'Sport_tools'
    elif category1 == 'sports-outdoors':
        if category2 == 'bicycle-and-accessories':
            return 'Bicycle'
        elif category2 == 'camping-climbing':
            return 'Travel_Camp'
        else:
            return 'Sport_tools'
    elif category1 == 'camping-climbing':
        return 'Travel_Camp'
    elif category1 == 'toys_main':
        return 'Toy'
    elif category1 == 'books_main':
        return 'Publications'
    elif category1 == 'stationery':
        return 'Stationery'
    elif category1 == 'multimedia':
        if category2 in ['software', 'pc_console_games']:
            return 'Software_Game'
        elif category2 == 'music_video':
            return 'Film_Music'
        elif category2 == 'multimedia_reference_packs':
            return 'Training'
        elif category2 == 'audiobooks':
            return 'Publications'
    elif category1 == 'home_living_handcrafts':
        return 'Handcraft'
    elif category1 == 'tools-parent':
        if category2 in ['urban-and-industrial-lighting', 'electrical_tool','power_saw', 'power_grinder']:
            return 'Electrical_Tool'
        else:
            return 'Hand_Tool'
    elif category1 == 'car_equipment':
        return 'Car_Equipment'
    elif category1 in ['drinks','junk-food','breakfast','spice','pet-shop']:
        return 'Supermarket'
    elif category1 == 'cleaning_dusting':
        return 'Clean'


# def bamilo_category(category1, category2, category3):
#     if category1 == 'fashion':
#         if category2 == "fashion_for_men":
#             if category3 == "men_clothes":
#                 return "Men-Clothes"
#             elif category3 == "men-shoes":
#                 return "Men-Shoes"
#             elif category3 == "fashion_men_accessories":
#                 return "Men-Accessories"
#             elif category3 == "kidsfashion":
#                 return "Kid"
#             else:
#                 return "Men-Accessories"
#         elif category2== "fashion_for_women":
#             if category3 == "women_clothes":
#                 return "Women-Clothes"
#             elif category3 == "women-shoes":
#                 return "Women-Shoes"
#             elif category3 == "fashion_women_accessories":
#                 return "Women-Accessories"
#             else:
#                 return "Women-Accessories"
#         elif category2 == "luggages-bags":
#             return "Bag"
#         elif category2 == "kidsfashion":
#             return "Kid"
#         else:
#             return "General-Clothes"
#     elif category1 == 'smartphone_tablet_mobile':
#         if category2 == "mobile_phones":
#             return "Mobile"
#         elif category2 == "tablet_os":
#             return "Tablet"
#         elif category2 == "sim_card":
#             return "SimCard"
#         else:
#             return "Mobile"
#     elif category1 == 'electronic_accessories':
#         return "Digital-Accessories"
#     elif category1 == 'computer_office_equipment_printer_scanner':
#         if category2 == "portable_pc_computer":
#             return "Laptop"
#         elif category2 in ["desktop_computer", "computer_parts", "store_equipment"]:
#             return "Computer-Parts"
#         else:
#             return "Office-Machines"
#     elif category1 == 'tv_entertainment_game_console_camera':
#         if category2 == "console_gaming":
#             return "Console"
#         elif category2 == "car-electronic-accessories":
#             return "Car-Equipment"
#         else:
#             return "Digital-Accessories"
#     elif category1 == 'tools-automotives':
#         if category2 == "car_equipment":
#             return "Car-Equipment"
#         elif category2 == "tools-parent":
#             if category3 in ["moving_accessories", "industrial-lab-equipment","measuring_tools"]:
#                 return "General-Home"
#             elif category3 == "car_equipment":
#                 return "Car-Equipment"
#             elif category3 in ["electrical_tool", "urban-and-industrial-lighting", "power_tools_consumables"]:
#                 return "Electrical-Tool"
#             else:
#                 return "General-Tool"
#         else:
#             return "General-Tool"
#     elif category1 == 'sports-outdoors':
#         if category2 in ["sports_apparel", "training-accessories", "fun-and-entertaiment"]:
#             return "Sport-Tool"
#         else:
#             return "Travel"
#     elif category1 == "home_kitchen_appliance":
#         if category2 == "kitchen_appliance":
#             return "Home-Kitchen-Appliance"
#         elif category2 == "home_appliance":
#             return "Home-Electrical-Appliance"
#     elif category1 == 'home_furniture_lifestyle':
#         if category2 == "home-decorating":
#             return "Decorative"
#         elif category2 == "cleaning_dusting":
#             return "Clean"
#         elif category2 == "bedroom_bed_furniture":
#             return "Bed-Bath"
#         elif category2 in ["house_general_goods"]:
#             return "General-Home"
#         elif category2 == "supermarket":
#             return "Supermarket"
#         elif category2 == "outdoor_furniture":
#             return "Travel"
#         else:
#             "kitchen_appliance"
#     elif category1 == 'health_beauty_personal_care':
#         if category2 == "makeup":
#             return "Makeup"
#         elif category2 == "perfumes":
#             return "Perfume"
#         elif category2 in ["human_health", "oral_care", "shaving_grooming", "women-care"]:
#             return "Health"
#         elif category2  == "hair_care":
#             return "Electrical-Personal"
#         elif category2 in ["skin_care","hand_feet_nails"]:
#             return "Skin-Nail"
#         else:
#             return 'General-Health-Beauty'
#     elif category1 == "children":
#         return 'Toy'
#     elif category1 == 'books_digitalconent_education':
#         if category2 == "books_main":
#             return "Publications"
#         elif category2 == "stationery":
#             return "Stationery"
#         elif category2 == "multimedia":
#             if category3 == "music_video":
#                 return "Film"
#             else:
#                 return "Software-Game"
#
#
#
#
#
#
#
#     bamilo_categories = [
#         'ابزارآلات',
#         'ابزار و لوازم آرایشی بهداشتی',
#         'اتاق خواب',
#         'اتاق کودک',
#         'آرایشی',
#         'اسباب بازی و سرگرمی',
#         'آشپزخانه',
#         'اصلاح سر، صورت و بدن',
#         'اقلام مذهبی',
#         'اقلام هواداری',
#         'اکسسوری باشگاهی',
#         'باتری',
#         'بچگانه',
#         'بهداشت بانوان',
#         'پخش کننده دیجیتال و دیسک',
#         'پرینتر و اسکنر',
#         'تبلت',
#         'تجهیزات باشگاهی',
#         'تجهیزات شبکه',
#         'تجهیزات فروشگاهی و بانکی',
#         'تجهیزات مدیریت مدارک',
#         'تفریحی',
#         'تقویم و سررسید',
#         'تلفن و فکس',
#         'تناسب اندام و بدنسازی',
#         'چند رسانه ای',
#         'دست، پا و ناخن',
#         'دکوراسیون داخلی منزل',
#         'دهان و دندان',
#         'دوچرخه و لوازم جانبی دوچرخه',
#         'دوربین و تجهیزات تصویربرداری',
#         'دئودورانت',
#         'سرگرمی های مستقل از سن',
#         'سلامت',
#         'سیم کارت',
#         'عطر',
#         'قطعات کامپیوتر',
#         'قمقمه',
#         'کامپیوتر رومیزی',
#         'کامپیوتر قابل حمل',
#         'کتاب',
#         'کیف و چمدان',
#         'کنسولهای بازی و لوازم جانبی',
#         'کوهنوردی و طبیعت گردی',
#         'گجت و ابزارهای پوشیدنی',
#         'لباس، کیف و کفش',
#         'لوازم الکترونیکی خودرو',
#         'لوازم برقی آشپزخانه',
#         'لوازم برقی خانه',
#         'لوازم تحریر',
#         'لوازم جانبی اپل',
#         'لوازم جانبی تلویزیون',
#         'لوازم جانبی لپ تاپ',
#         'لوازم جانبی موبایل و تبلت',
#         'لوازم جشن، مهمانی و تولد',
#         'لوازم خودرو',
#         'لوازم ذخیره سازی اطلاعات',
#         'لوازم عمومی منزل',
#         'لوازم ورزش های آبی',
#         'ماشین های اداری',
#         'مبلمان اداری',
#         'مجله',
#         'محصولات 4 جی',
#         'محصولات کمک آموزشی',
#         'مراقبت از پوست',
#         'مواد غذایی',
#         'موبایل',
#         'موی سر',
#         'نظافت و گردگیری منزل',
#         'نوزاد و کودک',
#         'ویدیو پروژکتور',
#         'ورزش های زمستانی'
#     ]
#     masir_categories = [
#         'General-Tool',
#         'Makeup',
#         'Bed-Bath',
#         'Bed-Bath',
#         'Makeup',
#         'Toy',
#         'Home-Kitchen-Appliance',
#         'Electrical-Personal',
#         'Religious',
#         'General-Home',
#         'Sport-Tools',
#         'General-Home',
#         'Kids',
#         'Health',
#         'Digital-Accessories',
#         'OfficeMachines',
#         'Tablet',
#         'Sport-Tools',
#         'OfficeMachines',
#         'OfficeMachines',
#         'OfficeMachines',
#         'Sport-Tools',
#         'Publications',
#         'OfficeMachines',
#         'Sport-Tools',
#         'Software-Game',
#         'Skin-Nail',
#         'Decorative',
#         'Health',
#         'Bicycle',
#         'Camera',
#         'Health',
#         'Kid',
#         'Health',
#         'OtherDigital',
#         'Perfume',
#         'Computer-Parts',
#         'Travel',
#         'Computer-Parts',
#         'Laptop',
#         'Publications',
#         'Bag',
#         'Console',
#         'Travel',
#         'Digital-Accessories',
#         'Travel',
#         'Car-Equipment',
#         'Home-Electrical-Appliance',
#         'Home-Electrical-Appliance',
#         'Stationery',
#         'Digital-Accessories',
#         'Digital-Accessories',
#         'Digital-Accessories',
#         'Digital-Accessories',
#         'General-Home',
#         'Car-Equipment',
#         'Digital-Accessories',
#         'General-Home',
#         'Sport-tools',
#         'OfficeMachines',
#         'OfficeMachines',
#         'Publications',
#         'OtherDigital',
#         'Training',
#         'Skin-Nail',
#         'Supermarket',
#         'Mobile',
#         'Makeup',
#         'Clean',
#         'Kid',
#         'OtherDigital',
#         'Sport-Tools'
#     ]
#     try:
#         return masir_categories[bamilo_categories.index(categoryfa1.upper())]
#     except:
#         return "None"

def category(cat):
    if (any("مردانه" in x for x in cat) and (any("لباس" in x for x in cat) or any("پوشاک" in x for x in cat))) or (any("men".upper() in x for x in cat) and any("cloth" in x for x in cat)):
        masir_cat = "Men-Clothes"
    elif (any("مردانه" in x for x in cat) and any("کفش" in x for x in cat)) or (any("men".upper() in x for x in cat) and any("shoe".upper() in x for x in cat)):
        masir_cat = "Men-Shoes"
    elif (any("زنانه" in x for x in cat) and (any("لباس" in x for x in cat) or any("پوشاک" in x for x in cat))) or (any("women".upper() in x for x in cat) and any("cloth" in x for x in cat)):
        masir_cat = "Women-Clothes"
    elif (any("زنانه" in x for x in cat) and any("کفش" in x for x in cat)) or (any("women".upper() in x for x in cat) and any("shoe".upper() in x for x in cat)):
        masir_cat = "Women-Shoes"
    elif (any("زنانه" in x for x in cat) and (any("لباس" in x for x in cat) or any("پوشاک" in x for x in cat))) or (any("women".upper() in x for x in cat) and any("cloth" in x for x in cat)):
        masir_cat = "Women-Clothes"
    elif any("کیف" in x for x in cat) or any("کيف" in x for x in cat) or any("bag".upper() in x for x in cat):
        masir_cat = "Bag"
    elif (any("مردانه" in x for x in cat) and any("اکسس" in x for x in cat)) or (any("men".upper() in x for x in cat) and any("accessor" in x for x in cat)):
        masir_cat = "Men-Accessories"
    elif (any("زنانه" in x for x in cat) and any("اکسس" in x for x in cat)) or (any("women".upper() in x for x in cat) and any("accessor" in x for x in cat)):
        masir_cat = "Women-Accessories"
    elif any("بچگانه" in x for x in cat) or any("کودک" in x for x in cat) or any("baby".upper() in x for x in cat) and any("kid" in x for x in cat):
        masir_cat = "Kids"

    elif any("home".upper() in x for x in cat) or any("خانه" in x for x in cat) or any("خانگ" in x for x in cat):
        if any("صوتی" in x for x in cat) or any("تصويری" in x for x in cat) or any("صوتي" in x for x in cat) or any("تصويري" in x for x in cat) or any("video".upper() in x for x in cat) or any("audio".upper() in x for x in cat):
            masir_cat = "Video-Audio"
        elif any("آشپزخانه" in x for x in cat) or any("kitche".upper() in x for x in cat):
            masir_cat = "Kitchen"
        elif any("برق" in x for x in cat):
            masir_cat = "Electrical-Appliance"
        elif any("خواب" in x for x in cat) or any("bed".upper() in x for x in cat) or any("حمام" in x for x in cat) or any("bath".upper() in x for x in cat):
            masir_cat = "Bed-Bath"
        elif any("دکور" in x for x in cat) or any("decorat".upper() in x for x in cat):
            masir_cat = "Decorative"
        elif any("نظافت" in x for x in cat) or any("clean".upper() in x for x in cat):
            masir_cat = "Clean"
        elif any("فرش" in x for x in cat) or any("carpet".upper() in x for x in cat):
            masir_cat = "Carpet"
        else:
            masir_cat = "General-Home"

    elif any("فرهنگ" in x for x in cat) or any("هنر" in x for x in cat) or any("culture".upper() in x for x in cat) or any("art".upper() in x for x in cat):
        if any("کتاب" in x for x in cat) or any("book".upper() in x for x in cat):
            masir_cat = "Book"
        elif any("موسیقی" in x for x in cat) or any("موسيقي" in x for x in cat) or any("music".upper() in x for x in cat):
            masir_cat = "Music"
        elif any("فیلم" in x for x in cat) or any("فيلم" in x for x in cat) or any("film".upper() in x for x in cat) or any("movie".upper() in x for x in cat):
            masir_cat = "Film"
        elif any("نرم افزار" in x for x in cat) or any("software".upper() in x for x in cat):
            masir_cat = "Software"
        elif any("صنایع دستی" in x for x in cat) or any("صنايع دستي" in x for x in cat) or (any("hand".upper() in x for x in cat) and any("craft".upper() in x for x in cat)):
            masir_cat = "Handcraft"
        elif any("آموزش" in x for x in cat) or any("training".upper() in x for x in cat):
            masir_cat = "Training"
        else:
            masir_cat = "General-Culture"

    elif any("زیبایی" in x for x in cat) or any("زيبايي" in x for x in cat) or any("سلامت" in x for x in cat):
        if any("عطر" in x for x in cat) or any("perfume".upper() in x for x in cat):
            masir_cat = "Perfume"
        elif any("آرایش" in x for x in cat) or any("آرايش" in x for x in cat) or any("makeup".upper() in x for x in cat):
            masir_cat = "Makeup"
        elif any("بهداشت" in x for x in cat):
            masir_cat = "Health"
        elif any("ناخن" in x for x in cat) or any("پوست" in x for x in cat) or any("دست" in x for x in cat) or any("پا" in x for x in cat):
            masir_cat = "Skin-Nail"
        elif any("برق" in x for x in cat) or any("electric".upper() in x for x in cat):
            masir_cat = "Electrical-Personal"
        elif any("عینک" in x for x in cat) or any("عينک" in x for x in cat) or any("glass".upper() in x for x in cat):
            masir_cat = "Glass"
        elif any("جواهر" in x for x in cat) or any("jeweller".upper() in x for x in cat):
            masir_cat = "Jewellery"
        elif any("مچی" in x for x in cat) or any("مچي" in x for x in cat) or any("watch".upper() in x for x in cat):
            masir_cat = "Watch"
        else:
            masir_cat = "General-Health-Beauty"


    elif any("ورزش" in x for x in cat) or any("sport".upper() in x for x in cat) or any("سرگرمي" in x for x in cat) or any("entertainment".upper() in x for x in cat):
        if any("لباس" in x for x in cat) or any("پوشاک" in x for x in cat) or any("clothes".upper() in x for x in cat):
            masir_cat = "Sport-Clothes"
        elif any("کفش" in x for x in cat) or any("shoe".upper() in x for x in cat):
            masir_cat = "Sport-Shoes"
        elif any("دوچرخه" in x for x in cat) or any("bike".upper() in x for x in cat) or any("bicycle".upper() in x for x in cat):
            masir_cat = "Bicycle"
        elif any("سفر" in x for x in cat) or any("travel".upper() in x for x in cat):
            masir_cat = "Travel"
        elif any("بازی" in x for x in cat) or any("بازي" in x for x in cat) or (any("Toy".upper() in x for x in cat) and (any("اسباب بازی" in x for x in cat) or any("اسباب بازي" in x for x in cat))):
            masir_cat = "Toy"
        else:
            masir_cat = "Sport-Tools"


    elif any("خودرو" in x for x in cat) or any("vehicle".upper() in x for x in cat) or any("ابزار" in x for x in cat) or any("tools".upper() in x for x in cat):
        if any("cars".upper() in x for x in cat):
            masir_cat = "Car"
        elif (any("لوازم" in x for x in cat) and any("خودرو" in x for x in cat)) or (any("Equipment".upper() in x for x in cat) and any("car".upper() in x for x in cat)):
            masir_cat = "Car-Equipment"
        elif any("موتورسیکلت" in x for x in cat) or any("موتورسيکلت" in x for x in cat) or any("motorbike".upper() in x for x in cat) or any("motorcycle".upper() in x for x in cat):
            masir_cat = "/Motorbike"
        elif (any("ابزار" in x for x in cat) and any("برق" in x for x in cat)) or (any("tool".upper() in x for x in cat) and (any("power".upper() in x for x in cat) or any("electric".upper() in x for x in cat))):
            masir_cat = "Electrical-Tool"
        elif any("ابزار" in x for x in cat) or (any("Tool".upper() in x for x in cat) and any("hand".upper() in x for x in cat)):
            masir_cat = "General-Tool"
        else:
            masir_cat = "Other-Car-Tool"
    elif any("لوازم جانب" in x for x in cat):
        masir_cat = "Accessories"
    elif (any("تبلت" in x for x in cat) or any("tablet".upper() in x for x in cat)) and not (any("موبایل" in x for x in cat) or any("موبايل" in x for x in cat) or any("mobile" in x for x in cat)):
        masir_cat = "Tablet"
    elif any("موبایل" in x for x in cat) or any("موبايل" in x for x in cat) or any("mobile" in x for x in cat):
        masir_cat = "Mobile"
    elif any("لپتاپ" in x for x in cat) or any("laptop".upper() in x for x in cat) or any("notebook".upper() in x for x in cat) or any("نوت بوک" in x for x in cat):
        masir_cat = "Laptop"
    elif any("اداری" in x for x in cat) or any("اداري" in x for x in cat) or any("office".upper() in x for x in cat):
        masir_cat = "OfficeMachines"
    elif any("کامپیوتر" in x for x in cat) or any("کامپيوتر" in x for x in cat) or any("computer".upper() in x for x in cat):
        masir_cat = "Computer-Parts"
    elif any("دوربین" in x for x in cat) or any("دوربين" in x for x in cat) or any("camera".upper() in x for x in cat):
        masir_cat = "Camera"
    elif any("کنسول" in x for x in cat) or any("console".upper() in x for x in cat):
        masir_cat = "Console"
    elif any("دیجیتال" in x for x in cat) or any("ديجيتال" in x for x in cat) or any("digital".upper() in x for x in cat):
        masir_cat = "OtherDigital"
    elif any("سوپرمارکت" in x for x in cat) or any("supermarket".upper() in x for x in cat):
        masir_cat = "Supermarket"
    else:
        masir_cat = "Other"
    return masir_cat













