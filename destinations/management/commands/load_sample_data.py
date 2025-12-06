"""
Management command to load sample tour & travel data in 3 languages (uz, en, ru).
Usage: python manage.py load_sample_data
"""
from django.core.management.base import BaseCommand
from django.utils.text import slugify
from destinations.models import Destination
from packages.models import Package
from gallery.models import GalleryImage
from decimal import Decimal


class Command(BaseCommand):
    help = 'Load sample destinations, packages, and gallery images with multilingual content'

    def handle(self, *args, **kwargs):
        self.stdout.write('Loading sample data...')

        # Create Destinations
        destinations_data = [
            {
                'title_uz': 'Samarqand',
                'title_en': 'Samarkand',
                'title_ru': 'Самарканд',
                'short_description_uz': 'Buyuk Ipak Yo\'li markazidagi qadimiy shahar',
                'short_description_en': 'Ancient city on the Great Silk Road',
                'short_description_ru': 'Древний город на Великом Шелковом пути',
                'description_uz': 'Samarqand - O\'zbekistonning eng qadimiy va go\'zal shaharlaridan biri. Registon maydoni, Gur-Amir maqbarasi va Bibi-Xonim masjidi bu yerning mashhur obidalaridandir.',
                'description_en': 'Samarkand is one of the oldest and most beautiful cities in Uzbekistan. Registan Square, Gur-Emir Mausoleum, and Bibi-Khanum Mosque are among its famous monuments.',
                'description_ru': 'Самарканд - один из древнейших и красивейших городов Узбекистана. Площадь Регистан, мавзолей Гур-Эмир и мечеть Биби-Ханум - его знаменитые памятники.',
                'published': True,
                'featured': True,
            },
            {
                'title_uz': 'Buxoro',
                'title_en': 'Bukhara',
                'title_ru': 'Бухара',
                'short_description_uz': 'Sharqning Muqaddas shahri',
                'short_description_en': 'The Holy City of the East',
                'short_description_ru': 'Священный город Востока',
                'description_uz': 'Buxoro 2500 yillik tarixga ega qadimiy shahar. Ark qal\'asi, Po\'i Kalon majmuasi va Lyabi Hauz - bu yerning diqqatga sazovor joylari.',
                'description_en': 'Bukhara is an ancient city with 2500 years of history. The Ark Fortress, Poi Kalon complex, and Lyabi Hauz are its notable attractions.',
                'description_ru': 'Бухара - древний город с 2500-летней историей. Крепость Арк, комплекс Пои Калон и Ляби Хауз - его достопримечательности.',
                'published': True,
                'featured': True,
            },
            {
                'title_uz': 'Xiva',
                'title_en': 'Khiva',
                'title_ru': 'Хива',
                'short_description_uz': 'Ochiq osmon ostidagi muzey-shahar',
                'short_description_en': 'Open-air museum city',
                'short_description_ru': 'Город-музей под открытым небом',
                'description_uz': 'Xiva - Xorazm oazisidagi noyob muzey-shahar. Ichan Qal\'a - YUNESKO tomonidan himoya qilinadigan tarixiy kompleks.',
                'description_en': 'Khiva is a unique museum city in the Khorezm oasis. Ichan Kala is a UNESCO-protected historical complex.',
                'description_ru': 'Хива - уникальный город-музей в Хорезмском оазисе. Ичан-Кала - исторический комплекс под защитой ЮНЕСКО.',
                'published': True,
                'featured': True,
            },
        ]

        destinations = []
        for data in destinations_data:
            slug = slugify(data['title_en'])
            dest, created = Destination.objects.get_or_create(
                slug=slug,
                defaults=data
            )
            destinations.append(dest)
            self.stdout.write(f'✓ Created destination: {dest.title_en}')

        # Create Packages
        packages_data = [
            {
                'destination': destinations[0],  # Samarkand
                'title_uz': 'Samarqand Klassik Tur',
                'title_en': 'Samarkand Classic Tour',
                'title_ru': 'Классический тур в Самарканд',
                'description_uz': '3 kunlik Samarqandni o\'rganish safari. Registon, Gur-Amir va boshqa mashhur joylarni ko\'ring.',
                'description_en': '3-day exploration of Samarkand. Visit Registan, Gur-Emir, and other famous sites.',
                'description_ru': '3-дневное знакомство с Самаркандом. Посетите Регистан, Гур-Эмир и другие знаменитые места.',
                'duration_uz': '3 kun 2 kecha',
                'duration_en': '3 days 2 nights',
                'duration_ru': '3 дня 2 ночи',
                'duration_days': 3,
                'price': Decimal('299.00'),
                'currency': 'USD',
                'published': True,
                'available': True,
                'featured': True,
            },
            {
                'destination': destinations[1],  # Bukhara
                'title_uz': 'Buxoro Tarixiy Safari',
                'title_en': 'Bukhara Historical Journey',
                'title_ru': 'Историческое путешествие по Бухаре',
                'description_uz': '2 kunlik Buxoroning qadimiy obidalarini ziyorat qilish.',
                'description_en': '2-day visit to Bukhara\'s ancient monuments.',
                'description_ru': '2-дневное посещение древних памятников Бухары.',
                'duration_uz': '2 kun 1 kecha',
                'duration_en': '2 days 1 night',
                'duration_ru': '2 дня 1 ночь',
                'duration_days': 2,
                'price': Decimal('199.00'),
                'currency': 'USD',
                'published': True,
                'available': True,
                'featured': True,
            },
            {
                'destination': destinations[2],  # Khiva
                'title_uz': 'Xiva - Qadimiy Shahar',
                'title_en': 'Khiva - Ancient City',
                'title_ru': 'Хива - Древний Город',
                'description_uz': 'Ichan Qal\'ani to\'liq o\'rganish: 1 kunlik ekskursiya.',
                'description_en': 'Complete exploration of Ichan Kala: 1-day excursion.',
                'description_ru': 'Полное изучение Ичан-Калы: 1-дневная экскурсия.',
                'duration_uz': '1 kun',
                'duration_en': '1 day',
                'duration_ru': '1 день',
                'duration_days': 1,
                'price': Decimal('149.00'),
                'currency': 'USD',
                'published': True,
                'available': True,
                'featured': False,
            },
            {
                'destination': destinations[0],  # Samarkand
                'title_uz': 'Samarqand VIP Turi',
                'title_en': 'Samarkand VIP Tour',
                'title_ru': 'VIP тур в Самарканд',
                'description_uz': '5 kunlik premium Samarqand safari, 5 yulduzli mehmonxona bilan.',
                'description_en': '5-day premium Samarkand tour with 5-star hotel accommodation.',
                'description_ru': '5-дневный премиум тур в Самарканд с размещением в 5-звездочном отеле.',
                'duration_uz': '5 kun 4 kecha',
                'duration_en': '5 days 4 nights',
                'duration_ru': '5 дней 4 ночи',
                'duration_days': 5,
                'price': Decimal('699.00'),
                'currency': 'USD',
                'published': True,
                'available': True,
                'featured': True,
            },
        ]

        for data in packages_data:
            slug = slugify(data['title_en'])
            pkg, created = Package.objects.get_or_create(
                slug=slug,
                defaults=data
            )
            self.stdout.write(f'✓ Created package: {pkg.title_en}')

        self.stdout.write(self.style.SUCCESS('✓ Sample data loaded successfully!'))
        self.stdout.write('Run the server and visit /admin to see the data.')
        self.stdout.write('Default admin URL: http://localhost:8000/admin/')
