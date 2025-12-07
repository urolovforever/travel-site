"""
Management command to load sample destination data in 3 languages (uz, en, ru).
Usage: python manage.py load_sample_data
"""
from django.core.management.base import BaseCommand
from django.utils.text import slugify
from destinations.models import Destination


class Command(BaseCommand):
    help = 'Load sample destinations with multilingual content (uz, en, ru)'

    def handle(self, *args, **kwargs):
        self.stdout.write('Loading sample data...')

        # Create Destinations
        destinations_data = [
            {
                'name_uz': 'Samarqand',
                'name_en': 'Samarkand',
                'name_ru': 'Самарканд',
                'title_uz': 'Afrosiyob Shahri',
                'title_en': 'City of Afrosiyob',
                'title_ru': 'Город Афросиаб',
                'country_uz': 'O\'zbekiston',
                'country_en': 'Uzbekistan',
                'country_ru': 'Узбекистан',
                'city_uz': 'Samarqand',
                'city_en': 'Samarkand',
                'city_ru': 'Самарканд',
                'region_uz': 'Samarqand viloyati',
                'region_en': 'Samarkand Region',
                'region_ru': 'Самаркандская область',
                'short_description_uz': 'Buyuk Ipak Yo\'li markazidagi qadimiy shahar',
                'short_description_en': 'Ancient city on the Great Silk Road',
                'short_description_ru': 'Древний город на Великом Шелковом пути',
                'description_uz': 'Samarqand - O\'zbekistonning eng qadimiy va go\'zal shaharlaridan biri. Registon maydoni, Gur-Amir maqbarasi va Bibi-Xonim masjidi bu yerning mashhur obidalaridandir.',
                'description_en': 'Samarkand is one of the oldest and most beautiful cities in Uzbekistan. Registan Square, Gur-Emir Mausoleum, and Bibi-Khanum Mosque are among its famous monuments.',
                'description_ru': 'Самарканд - один из древнейших и красивейших городов Узбекистана. Площадь Регистан, мавзолей Гур-Эмир и мечеть Биби-Ханум - его знаменитые памятники.',
                'things_to_do_uz': 'Registon maydonini ko\'ring\nGur-Amir maqbarasiga tashrif buyuring\nBibi-Xonim masjidini ko\'rib chiqing\nSiyob bozorida xarid qiling\nAfrosiyob muzeyini ziyorat qiling',
                'things_to_do_en': 'Visit Registan Square\nExplore Gur-Emir Mausoleum\nDiscover Bibi-Khanum Mosque\nShop at Siyob Bazaar\nVisit Afrosiyob Museum',
                'things_to_do_ru': 'Посетите площадь Регистан\nИсследуйте мавзолей Гур-Эмир\nОткройте мечеть Биби-Ханум\nПосетите базар Сиёб\nПосетите музей Афросиаб',
                'best_time_to_visit_uz': 'Mart-May va Sentyabr-Noyabr',
                'best_time_to_visit_en': 'March-May and September-November',
                'best_time_to_visit_ru': 'Март-Май и Сентябрь-Ноябрь',
                'average_cost_uz': 'Bir kishi uchun 250-400 dollar',
                'average_cost_en': '$250-$400 per person',
                'average_cost_ru': '$250-$400 на человека',
                'meta_title_uz': 'Samarqand - Ipak Yo\'lidagi Qadimiy Shahar | Sayohat',
                'meta_title_en': 'Samarkand - Ancient City on Silk Road | Travel',
                'meta_title_ru': 'Самарканд - Древний Город на Шелковом Пути | Туризм',
                'meta_description_uz': 'Samarqandga sayohat qiling va Registon, Gur-Amir, Bibi-Xonimni kashf eting',
                'meta_description_en': 'Visit Samarkand and discover Registan, Gur-Emir, Bibi-Khanum',
                'meta_description_ru': 'Посетите Самарканд и откройте Регистан, Гур-Эмир, Биби-Ханум',
                'meta_keywords_uz': 'samarqand, registon, ipak yo\'li, o\'zbekiston sayohati',
                'meta_keywords_en': 'samarkand, registan, silk road, uzbekistan travel',
                'meta_keywords_ru': 'самарканд, регистан, шелковый путь, узбекистан туризм',
                'published': True,
                'featured': True,
            },
            {
                'name_uz': 'Buxoro',
                'name_en': 'Bukhara',
                'name_ru': 'Бухара',
                'title_uz': 'Sharqning Muqaddas Shahri',
                'title_en': 'The Holy City of the East',
                'title_ru': 'Священный Город Востока',
                'country_uz': 'O\'zbekiston',
                'country_en': 'Uzbekistan',
                'country_ru': 'Узбекистан',
                'city_uz': 'Buxoro',
                'city_en': 'Bukhara',
                'city_ru': 'Бухара',
                'region_uz': 'Buxoro viloyati',
                'region_en': 'Bukhara Region',
                'region_ru': 'Бухарская область',
                'short_description_uz': 'Sharqning Muqaddas shahri va madaniyat markazi',
                'short_description_en': 'The Holy City of the East and cultural center',
                'short_description_ru': 'Священный город Востока и культурный центр',
                'description_uz': 'Buxoro 2500 yillik tarixga ega qadimiy shahar. Ark qal\'asi, Po\'i Kalon majmuasi va Lyabi Hauz - bu yerning diqqatga sazovor joylari.',
                'description_en': 'Bukhara is an ancient city with 2500 years of history. The Ark Fortress, Poi Kalon complex, and Lyabi Hauz are its notable attractions.',
                'description_ru': 'Бухара - древний город с 2500-летней историей. Крепость Арк, комплекс Пои Калон и Ляби Хауз - его достопримечательности.',
                'things_to_do_uz': 'Ark qal\'asini ziyorat qiling\nPo\'i Kalon majmuasini ko\'ring\nLyabi Hauzda dam oling\nMagoki Attori masjidini ko\'rib chiqing\nChor Minor va Samoniylar maqbarasiga boring',
                'things_to_do_en': 'Visit the Ark Fortress\nExplore Poi Kalon complex\nRelax at Lyabi Hauz\nDiscover Magoki Attori Mosque\nVisit Chor Minor and Samanid Mausoleum',
                'things_to_do_ru': 'Посетите крепость Арк\nИсследуйте комплекс Пои Калон\nОтдохните в Ляби Хауз\nОткройте мечеть Магоки Аттори\nПосетите Чор Минор и мавзолей Саманидов',
                'best_time_to_visit_uz': 'Aprel-May va Sentyabr-Oktyabr',
                'best_time_to_visit_en': 'April-May and September-October',
                'best_time_to_visit_ru': 'Апрель-Май и Сентябрь-Октябрь',
                'average_cost_uz': 'Bir kishi uchun 200-350 dollar',
                'average_cost_en': '$200-$350 per person',
                'average_cost_ru': '$200-$350 на человека',
                'meta_title_uz': 'Buxoro - Sharqning Muqaddas Shahri | O\'zbekiston Sayohati',
                'meta_title_en': 'Bukhara - Holy City of the East | Uzbekistan Travel',
                'meta_title_ru': 'Бухара - Священный Город Востока | Узбекистан Туризм',
                'meta_description_uz': 'Buxoroni kashf eting: Ark, Po\'i Kalon, Lyabi Hauz va ko\'plab tarixiy yodgorliklar',
                'meta_description_en': 'Discover Bukhara: Ark, Poi Kalon, Lyabi Hauz and many historical monuments',
                'meta_description_ru': 'Откройте Бухару: Арк, Пои Калон, Ляби Хауз и многие исторические памятники',
                'meta_keywords_uz': 'buxoro, ark qal\'asi, poi kalon, o\'zbekiston',
                'meta_keywords_en': 'bukhara, ark fortress, poi kalon, uzbekistan',
                'meta_keywords_ru': 'бухара, крепость арк, пои калон, узбекистан',
                'published': True,
                'featured': True,
            },
            {
                'name_uz': 'Xiva',
                'name_en': 'Khiva',
                'name_ru': 'Хива',
                'title_uz': 'Ochiq Osmon Ostidagi Muzey',
                'title_en': 'Open-Air Museum City',
                'title_ru': 'Город-Музей под Открытым Небом',
                'country_uz': 'O\'zbekiston',
                'country_en': 'Uzbekistan',
                'country_ru': 'Узбекистан',
                'city_uz': 'Xiva',
                'city_en': 'Khiva',
                'city_ru': 'Хива',
                'region_uz': 'Xorazm viloyati',
                'region_en': 'Khorezm Region',
                'region_ru': 'Хорезмская область',
                'short_description_uz': 'Ochiq osmon ostidagi muzey-shahar',
                'short_description_en': 'Open-air museum city',
                'short_description_ru': 'Город-музей под открытым небом',
                'description_uz': 'Xiva - Xorazm oazisidagi noyob muzey-shahar. Ichan Qal\'a - YUNESKO tomonidan himoya qilinadigan tarixiy kompleks.',
                'description_en': 'Khiva is a unique museum city in the Khorezm oasis. Ichan Kala is a UNESCO-protected historical complex.',
                'description_ru': 'Хива - уникальный город-музей в Хорезмском оазисе. Ичан-Кала - исторический комплекс под защитой ЮНЕСКО.',
                'things_to_do_uz': 'Ichan Qal\'ani aylanib chiqing\nKalta Minor minorasini ko\'ring\nTosh Hovli saroyiga tashrif buyuring\nJuma masjidini ziyorat qiling\nQo\'hna Ark qal\'asini ko\'rib chiqing',
                'things_to_do_en': 'Explore Ichan Kala\nSee Kalta Minor minaret\nVisit Tash Hovli palace\nDiscover Juma Mosque\nExplore Kuhna Ark fortress',
                'things_to_do_ru': 'Исследуйте Ичан-Калу\nПосмотрите минарет Кальта Минор\nПосетите дворец Таш-Ховли\nОткройте мечеть Джума\nИсследуйте крепость Кухна Арк',
                'best_time_to_visit_uz': 'Aprel-Iyun va Sentyabr-Oktyabr',
                'best_time_to_visit_en': 'April-June and September-October',
                'best_time_to_visit_ru': 'Апрель-Июнь и Сентябрь-Октябрь',
                'average_cost_uz': 'Bir kishi uchun 150-300 dollar',
                'average_cost_en': '$150-$300 per person',
                'average_cost_ru': '$150-$300 на человека',
                'meta_title_uz': 'Xiva - YUNESKO Muzey Shahri | O\'zbekiston',
                'meta_title_en': 'Khiva - UNESCO Museum City | Uzbekistan',
                'meta_title_ru': 'Хива - Город-Музей ЮНЕСКО | Узбекистан',
                'meta_description_uz': 'Xivaga sayohat qiling va Ichan Qal\'a tarixiy kompleksini kashf eting',
                'meta_description_en': 'Visit Khiva and discover the historical complex of Ichan Kala',
                'meta_description_ru': 'Посетите Хиву и откройте исторический комплекс Ичан-Кала',
                'meta_keywords_uz': 'xiva, ichan qal\'a, yunesko, xorazm',
                'meta_keywords_en': 'khiva, ichan kala, unesco, khorezm',
                'meta_keywords_ru': 'хива, ичан кала, юнеско, хорезм',
                'published': True,
                'featured': True,
            },
        ]

        for data in destinations_data:
            slug = slugify(data['title_en'])
            dest, created = Destination.objects.get_or_create(
                slug=slug,
                defaults=data
            )
            if created:
                self.stdout.write(self.style.SUCCESS(f'✓ Created destination: {dest.title_en}'))
            else:
                self.stdout.write(f'  Destination already exists: {dest.title_en}')

        self.stdout.write(self.style.SUCCESS('\n✓ Sample destination data loaded successfully!'))
        self.stdout.write('Run the server and visit /admin to see the data.')
        self.stdout.write('Default admin URL: http://localhost:8000/admin/')
        self.stdout.write('\nNote: Use the packages app management command to load package sample data.')
