#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script to add translations to .po files
"""

import polib
import os

# Uzbek translations
UZ_TRANSLATIONS = {
    # Base template
    "Tourly - Travel Agency": "Tourly - Sayohat Agentligi",
    "For Further Inquires :": "Qo'shimcha ma'lumot uchun:",
    "Home": "Bosh sahifa",
    "About Us": "Biz haqimizda",
    "Destinations": "Sayohat joylari",
    "Packages": "Paketlar",
    "Gallery": "Galereya",
    "Contact Us": "Bog'lanish",
    "Book Now": "Buyurtma qiling",
    "Discover amazing destinations around the world with Tourly. We provide the best travel packages and unforgettable experiences for every traveler.": "Tourly bilan dunyoning ajoyib joylarini kashf eting. Biz har bir sayohatchi uchun eng yaxshi sayohat paketlari va unutilmas tajribalarni taqdim etamiz.",
    "Feel free to contact and reach us !!": "Biz bilan bog'laning, biz doim tayyormiz !!",
    "Tashkent, Uzbekistan": "Toshkent, O'zbekiston",
    "Subscribe our newsletter for more update & news !!": "Yangiliklar va takliflar uchun obuna bo'ling !!",
    "Enter Your Email": "Emailingizni kiriting",
    "Subscribe": "Obuna bo'lish",
    "All rights reserved": "Barcha huquqlar himoyalangan",
    "Privacy Policy": "Maxfiylik siyosati",
    "Term & Condition": "Shartlar va qoidalar",
    "FAQ": "Ko'p beriladigan savollar",

    # Index page
    "Journey to explore world": "Dunyoni kashf qilish sayohati",
    "Discover amazing destinations and create unforgettable memories with our carefully curated travel packages.": "Ajoyib joylarni kashf eting va bizning ehtiyotkorlik bilan tanlangan sayohat paketlarimiz bilan unutilmas xotiralar yarating.",
    "Learn more": "Batafsil",
    "Book now": "Buyurtma berish",
    "Search Destination": "Joyni qidirish",
    "Enter Destination": "Joyni kiriting",
    "Pax Number": "Odamlar soni",
    "No.of People": "Necha kishi",
    "Checkin Date": "Kelish sanasi",
    "Checkout Date": "Ketish sanasi",
    "Inquire now": "Hozir so'rov yuborish",
    "Uncover place": "Joylarni kashf eting",
    "Popular destination": "Mashhur joylar",
    "Explore our most popular travel destinations around the world. Find the perfect place for your next adventure and create unforgettable memories.": "Dunyoning eng mashhur sayohat joylarini kashf eting. Keyingi sayohatingiz uchun ideal joyni toping va unutilmas xotiralar yarating.",
    "More destinations": "Barcha joylar",
    "Popular Packages": "Mashhur paketlar",
    "Checkout Our Packages": "Bizning paketlarimiz",
    "Browse our carefully curated travel packages designed to give you the best experience. Each package includes accommodations, activities, and guided tours.": "Sizga eng yaxshi tajribani taqdim etish uchun mo'ljallangan sayohat paketlarimizni ko'rib chiqing. Har bir paket turar joy, faoliyat va ekskursiyalarni o'z ichiga oladi.",
    "pax:": "Odamlar:",
    "reviews": "sharh",
    "/ per person": "/ kishi uchun",
    "View All Packages": "Barcha paketlar",
    "Photo Gallery": "Foto galereya",
    "Photos From Travellers": "Sayohatchilardan fotolar",
    "Check out beautiful moments captured by our travelers from around the world. Share your travel memories with us and inspire others to explore.": "Sayohatchilarimiz tomonidan dunyoning turli burchaklaridan olingan go'zal lahzalarni ko'ring. Bizning sayohatga kiriting va boshqalarni ilhomlantiring.",
    "Our Partners": "Hamkorlarimiz",
    "Trusted by Leading Companies": "Yetakchi kompaniyalar ishonadi",
    "Call To Action": "Harakatga chaqiruv",
    "Ready For Unforgettable Travel. Remember Us!": "Unutilmas sayohat uchun tayyormisiz? Bizni eslang!",
    "Contact us today to start planning your dream vacation": "Orzuingizdagi ta'tilni rejalashtirishni bugun boshlash uchun biz bilan bog'laning",
    "Contact Us!": "Bog'laning!",

    # Contact page
    "Get in touch with us for any inquiries about our tours and travel packages": "Sayohatlarimiz va paketlarimiz haqida har qanday savol uchun biz bilan bog'laning",
    "Get In Touch": "Biz bilan bog'laning",
    "Have questions? We'd love to hear from you. Send us a message and we'll respond as soon as possible.": "Savollaringiz bormi? Sizdan eshitishdan mamnun bo'lamiz. Bizga xabar yuboring va biz imkon qadar tezroq javob beramiz.",
    "Your Name": "Ismingiz",
    "Enter your name": "Ismingizni kiriting",
    "Your Email": "Emailingiz",
    "Enter your email": "Emailingizni kiriting",
    "Subject": "Mavzu",
    "Message": "Xabar",
    "Your message...": "Xabaringiz...",
    "Send Message": "Xabar yuborish",
    "Contact Information": "Aloqa ma'lumotlari",
    "Address": "Manzil",
    "Phone": "Telefon",
    "Email": "Email",
    "Working Hours": "Ish vaqti",
    "Mon - Sat: 9:00 AM - 6:00 PM": "Dush - Shan: 9:00 dan 18:00 gacha",
    "Follow Us": "Bizni kuzating",

    # About page
    "Learn more about our journey and commitment to making your travel dreams come true": "Bizning sayohatimiz va sayohat orzularingizni amalga oshirishga bo'lgan sodiqligimiz haqida ko'proq bilib oling",
    "Explore All Tour of the World with Us": "Biz bilan dunyo bo'ylab barcha sayohatlarni kashf eting",
    "We are a professional travel agency dedicated to making your travel dreams come true. With years of experience in the tourism industry, we provide exceptional travel packages to the most beautiful destinations around the world.": "Biz sizning sayohat orzularingizni amalga oshirishga bag'ishlangan professional sayohat agentligimiz. Turizm sohasida ko'p yillik tajribaga ega bo'lib, biz dunyoning eng go'zal joylariga ajoyib sayohat paketlarini taqdim etamiz.",
    "Our team of travel experts carefully curates each tour package to ensure you have an unforgettable experience. From exotic beach destinations to cultural heritage sites, we have something for every traveler.": "Bizning sayohat mutaxassislari jamoasi har bir tur paketini ehtiyotkorlik bilan tanlaydi, shunda siz unutilmas tajribaga ega bo'lasiz. Ekzotik plyaj joylaridan madaniy meros joylarigacha, biz har bir sayohatchi uchun biror narsa taqdim etamiz.",
    "Professional and experienced tour guides": "Professional va tajribali gidlar",
    "Carefully selected destinations": "Ehtiyotkorlik bilan tanlangan joylar",
    "Competitive prices and great value": "Raqobatbardosh narxlar va ajoyib qiymat",
    "Happy Customers": "Mamnun mijozlar",
    "Years": "Yil",
}

# Russian translations
RU_TRANSLATIONS = {
    # Base template
    "Tourly - Travel Agency": "Tourly - Туристическое Агентство",
    "For Further Inquires :": "Для дополнительной информации:",
    "Home": "Главная",
    "About Us": "О нас",
    "Destinations": "Направления",
    "Packages": "Пакеты",
    "Gallery": "Галерея",
    "Contact Us": "Свяжитесь с нами",
    "Book Now": "Забронировать",
    "Discover amazing destinations around the world with Tourly. We provide the best travel packages and unforgettable experiences for every traveler.": "Откройте для себя удивительные направления по всему миру с Tourly. Мы предоставляем лучшие туристические пакеты и незабываемые впечатления для каждого путешественника.",
    "Feel free to contact and reach us !!": "Не стесняйтесь обращаться к нам !!",
    "Tashkent, Uzbekistan": "Ташкент, Узбекистан",
    "Subscribe our newsletter for more update & news !!": "Подпишитесь на нашу рассылку для получения новостей и обновлений !!",
    "Enter Your Email": "Введите ваш email",
    "Subscribe": "Подписаться",
    "All rights reserved": "Все права защищены",
    "Privacy Policy": "Политика конфиденциальности",
    "Term & Condition": "Условия и положения",
    "FAQ": "Часто задаваемые вопросы",

    # Index page
    "Journey to explore world": "Путешествие по миру",
    "Discover amazing destinations and create unforgettable memories with our carefully curated travel packages.": "Откройте для себя удивительные места и создайте незабываемые воспоминания с нашими тщательно подобранными туристическими пакетами.",
    "Learn more": "Подробнее",
    "Book now": "Забронировать",
    "Search Destination": "Поиск направления",
    "Enter Destination": "Введите направление",
    "Pax Number": "Количество людей",
    "No.of People": "Кол-во людей",
    "Checkin Date": "Дата заезда",
    "Checkout Date": "Дата выезда",
    "Inquire now": "Отправить запрос",
    "Uncover place": "Откройте места",
    "Popular destination": "Популярные направления",
    "Explore our most popular travel destinations around the world. Find the perfect place for your next adventure and create unforgettable memories.": "Исследуйте наши самые популярные туристические направления по всему миру. Найдите идеальное место для вашего следующего приключения и создайте незабываемые воспоминания.",
    "More destinations": "Все направления",
    "Popular Packages": "Популярные пакеты",
    "Checkout Our Packages": "Наши пакеты",
    "Browse our carefully curated travel packages designed to give you the best experience. Each package includes accommodations, activities, and guided tours.": "Просмотрите наши тщательно подобранные туристические пакеты, предназначенные для того, чтобы дать вам лучший опыт. Каждый пакет включает проживание, мероприятия и экскурсии.",
    "pax:": "Человек:",
    "reviews": "отзывов",
    "/ per person": "/ на человека",
    "View All Packages": "Все пакеты",
    "Photo Gallery": "Фотогалерея",
    "Photos From Travellers": "Фото от путешественников",
    "Check out beautiful moments captured by our travelers from around the world. Share your travel memories with us and inspire others to explore.": "Посмотрите красивые моменты, запечатленные нашими путешественниками со всего мира. Поделитесь своими воспоминаниями о путешествиях с нами и вдохновите других на исследования.",
    "Our Partners": "Наши партнеры",
    "Trusted by Leading Companies": "Нам доверяют ведущие компании",
    "Call To Action": "Призыв к действию",
    "Ready For Unforgettable Travel. Remember Us!": "Готовы к незабываемому путешествию? Помните о нас!",
    "Contact us today to start planning your dream vacation": "Свяжитесь с нами сегодня, чтобы начать планировать отпуск своей мечты",
    "Contact Us!": "Свяжитесь с нами!",

    # Contact page
    "Get in touch with us for any inquiries about our tours and travel packages": "Свяжитесь с нами по любым вопросам о наших турах и туристических пакетах",
    "Get In Touch": "Свяжитесь с нами",
    "Have questions? We'd love to hear from you. Send us a message and we'll respond as soon as possible.": "Есть вопросы? Мы будем рады услышать от вас. Отправьте нам сообщение, и мы ответим как можно скорее.",
    "Your Name": "Ваше имя",
    "Enter your name": "Введите ваше имя",
    "Your Email": "Ваш email",
    "Enter your email": "Введите ваш email",
    "Subject": "Тема",
    "Message": "Сообщение",
    "Your message...": "Ваше сообщение...",
    "Send Message": "Отправить сообщение",
    "Contact Information": "Контактная информация",
    "Address": "Адрес",
    "Phone": "Телефон",
    "Email": "Email",
    "Working Hours": "Рабочие часы",
    "Mon - Sat: 9:00 AM - 6:00 PM": "Пн - Сб: 9:00 - 18:00",
    "Follow Us": "Следите за нами",

    # About page
    "Learn more about our journey and commitment to making your travel dreams come true": "Узнайте больше о нашем пути и приверженности воплощению ваших мечт о путешествиях",
    "Explore All Tour of the World with Us": "Исследуйте все туры мира с нами",
    "We are a professional travel agency dedicated to making your travel dreams come true. With years of experience in the tourism industry, we provide exceptional travel packages to the most beautiful destinations around the world.": "Мы профессиональное туристическое агентство, посвященное воплощению ваших мечт о путешествиях. С многолетним опытом в туристической индустрии мы предоставляем исключительные туристические пакеты в самые красивые места по всему миру.",
    "Our team of travel experts carefully curates each tour package to ensure you have an unforgettable experience. From exotic beach destinations to cultural heritage sites, we have something for every traveler.": "Наша команда экспертов по путешествиям тщательно подбирает каждый туристический пакет, чтобы обеспечить вам незабываемые впечатления. От экзотических пляжных направлений до объектов культурного наследия - у нас есть что-то для каждого путешественника.",
    "Professional and experienced tour guides": "Профессиональные и опытные гиды",
    "Carefully selected destinations": "Тщательно отобранные направления",
    "Competitive prices and great value": "Конкурентные цены и отличное качество",
    "Happy Customers": "Довольные клиенты",
    "Years": "Лет",
}


def update_po_file(po_path, translations):
    """Update a .po file with translations"""
    po = polib.pofile(po_path)

    # Remove fuzzy flag from header
    po.metadata['Language'] = po_path.split('/')[-3]  # Extract language code
    if hasattr(po, 'metadata_is_fuzzy'):
        po.metadata_is_fuzzy = []

    # Update translations
    translated_count = 0
    for entry in po:
        if entry.msgid in translations and not entry.msgstr:
            entry.msgstr = translations[entry.msgid]
            translated_count += 1
            # Remove fuzzy flag if present
            if 'fuzzy' in entry.flags:
                entry.flags.remove('fuzzy')

    po.save()
    print(f"Updated {po_path}: {translated_count} translations added")
    return translated_count


def main():
    base_dir = '/home/user/travel-site/locale'

    # Update Uzbek translations
    uz_po = os.path.join(base_dir, 'uz', 'LC_MESSAGES', 'django.po')
    if os.path.exists(uz_po):
        uz_count = update_po_file(uz_po, UZ_TRANSLATIONS)
        print(f"✓ Uzbek: {uz_count} strings translated")

    # Update Russian translations
    ru_po = os.path.join(base_dir, 'ru', 'LC_MESSAGES', 'django.po')
    if os.path.exists(ru_po):
        ru_count = update_po_file(ru_po, RU_TRANSLATIONS)
        print(f"✓ Russian: {ru_count} strings translated")

    print("\nTranslation update complete!")


if __name__ == '__main__':
    main()
