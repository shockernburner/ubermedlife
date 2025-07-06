# Sample data for UberMed.Life

import os
import django

# Setup Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ubermed.settings')
django.setup()

from django.contrib.auth.models import User
from main.models import Doctor, Service, Testimonial, NewsArticle

# Create sample doctors
doctors_data = [
    {
        'name': 'Li Wei',
        'name_chinese': '李伟',
        'specialization': 'cardiology',
        'hospital': 'Beijing Fuwai Hospital',
        'city': 'Beijing',
        'experience_years': 15,
        'education': 'MD from Peking University, Fellowship in Interventional Cardiology',
        'biography': 'Dr. Li Wei is a renowned cardiologist with over 15 years of experience in treating complex cardiac conditions. He specializes in interventional cardiology and has performed over 2000 cardiac procedures.',
        'biography_bangla': 'ডঃ লি ওয়েই একজন বিখ্যাত হৃদরোগ বিশেষজ্ঞ যার ১৫ বছরের বেশি অভিজ্ঞতা রয়েছে জটিল হৃদরোগের চিকিৎসায়।',
        'consultation_fee': 150.00,
        'is_available': True,
    },
    {
        'name': 'Zhang Ming',
        'name_chinese': '张明',
        'specialization': 'oncology',
        'hospital': 'Shanghai Cancer Center',
        'city': 'Shanghai',
        'experience_years': 20,
        'education': 'MD, PhD from Fudan University, Oncology Fellowship at Memorial Sloan Kettering',
        'biography': 'Dr. Zhang Ming is a leading oncologist specializing in lung and liver cancers. He has published over 100 research papers and leads clinical trials for innovative cancer treatments.',
        'biography_bangla': 'ডঃ ঝাং মিং একজন শীর্ষস্থানীয় ক্যান্সার বিশেষজ্ঞ যিনি ফুসফুস ও লিভারের ক্যান্সারে বিশেষজ্ঞ।',
        'consultation_fee': 200.00,
        'is_available': True,
    },
    {
        'name': 'Wang Xiaoli',
        'name_chinese': '王小丽',
        'specialization': 'neurology',
        'hospital': 'Beijing Tiantan Hospital',
        'city': 'Beijing',
        'experience_years': 12,
        'education': 'MD from Capital Medical University, Neurology Residency at Johns Hopkins',
        'biography': 'Dr. Wang Xiaoli specializes in neurological disorders, particularly stroke and brain tumors. She is known for her expertise in minimally invasive neurosurgical techniques.',
        'biography_bangla': 'ডঃ ওয়াং শাওলি স্নায়ুরোগ বিশেষজ্ঞ, বিশেষত স্ট্রোক ও ব্রেইন টিউমারে বিশেষজ্ঞ।',
        'consultation_fee': 180.00,
        'is_available': True,
    },
    {
        'name': 'Chen Hao',
        'name_chinese': '陈浩',
        'specialization': 'orthopedics',
        'hospital': 'Shanghai Changzheng Hospital',
        'city': 'Shanghai',
        'experience_years': 18,
        'education': 'MD from Second Military Medical University, Orthopedic Surgery Fellowship',
        'biography': 'Dr. Chen Hao is an orthopedic surgeon specializing in joint replacement and spinal surgery. He has performed over 3000 successful surgeries.',
        'biography_bangla': 'ডঃ চেন হাও একজন অর্থোপেডিক সার্জন যিনি জয়েন্ট রিপ্লেসমেন্ট ও মেরুদণ্ডের সার্জারিতে বিশেষজ্ঞ।',
        'consultation_fee': 160.00,
        'is_available': True,
    },
    {
        'name': 'Liu Yanping',
        'name_chinese': '刘燕平',
        'specialization': 'gastroenterology',
        'hospital': 'Guangzhou First People\'s Hospital',
        'city': 'Guangzhou',
        'experience_years': 14,
        'education': 'MD from Sun Yat-sen University, GI Fellowship at Mayo Clinic',
        'biography': 'Dr. Liu Yanping is a gastroenterologist with expertise in liver diseases and endoscopic procedures. She has treated thousands of patients with digestive disorders.',
        'biography_bangla': 'ডঃ লিউ ইয়ানপিং একজন গ্যাস্ট্রোএন্টেরোলজিস্ট যিনি লিভারের রোগ ও এন্ডোস্কোপিক প্রসিডিউরে বিশেষজ্ঞ।',
        'consultation_fee': 140.00,
        'is_available': True,
    },
    {
        'name': 'Zhao Jun',
        'name_chinese': '赵军',
        'specialization': 'pediatrics',
        'hospital': 'Children\'s Hospital of Fudan University',
        'city': 'Shanghai',
        'experience_years': 16,
        'education': 'MD from Shanghai Medical University, Pediatric Residency at Boston Children\'s Hospital',
        'biography': 'Dr. Zhao Jun is a pediatric specialist with extensive experience in treating children with complex medical conditions. He is known for his compassionate care.',
        'biography_bangla': 'ডঃ ঝাও জুন একজন শিশু বিশেষজ্ঞ যার জটিল শিশু রোগের চিকিৎসায় ব্যাপক অভিজ্ঞতা রয়েছে।',
        'consultation_fee': 130.00,
        'is_available': True,
    }
]

# Create sample services
services_data = [
    {
        'name': 'Teleconsultation',
        'name_bangla': 'টেলিকনসালটেশন',
        'service_type': 'consultation',
        'description': 'Connect with top Chinese doctors from the comfort of your home. Get expert medical advice through secure video consultations.',
        'description_bangla': 'ঘরে বসেই চীনের শীর্ষ চিকিৎসকদের সাথে যোগাযোগ করুন। নিরাপদ ভিডিও কনসালটেশনের মাধ্যমে বিশেষজ্ঞ চিকিৎসা পরামর্শ নিন।',
        'price_range': '$100 - $250 USD',
        'duration': '30-60 minutes',
        'is_active': True,
    },
    {
        'name': 'Second Opinion',
        'name_bangla': 'দ্বিতীয় মতামত',
        'service_type': 'second_opinion',
        'description': 'Get a second opinion from Chinese medical experts to confirm diagnosis and explore additional treatment options.',
        'description_bangla': 'রোগ নির্ণয় নিশ্চিত করতে এবং অতিরিক্ত চিকিৎসার বিকল্প খোঁজার জন্য চীনা চিকিৎসা বিশেষজ্ঞদের কাছ থেকে দ্বিতীয় মতামত নিন।',
        'price_range': '$200 - $400 USD',
        'duration': '45-90 minutes',
        'is_active': True,
    },
    {
        'name': 'Medical Travel to China',
        'name_bangla': 'চীনে চিকিৎসা ভ্রমণ',
        'service_type': 'travel',
        'description': 'Complete assistance for medical travel to China including hospital coordination, visa support, and accommodation.',
        'description_bangla': 'চীনে চিকিৎসা ভ্রমণের জন্য সম্পূর্ণ সহায়তা যার মধ্যে রয়েছে হাসপাতাল সমন্বয়, ভিসা সহায়তা এবং থাকার ব্যবস্থা।',
        'price_range': 'Varies by treatment',
        'duration': '1-4 weeks',
        'is_active': True,
    },
    {
        'name': 'Advanced Surgery',
        'name_bangla': 'উন্নত সার্জারি',
        'service_type': 'surgery',
        'description': 'Access to cutting-edge surgical procedures performed by top Chinese surgeons in state-of-the-art facilities.',
        'description_bangla': 'অত্যাধুনিক সুবিধাসহ চীনের শীর্ষ সার্জনদের দ্বারা সম্পাদিত অত্যাধুনিক সার্জিক্যাল প্রসিডিউরে প্রবেশাধিকার।',
        'price_range': '$5,000 - $50,000 USD',
        'duration': '1-3 weeks',
        'is_active': True,
    },
    {
        'name': 'Diagnostic Services',
        'name_bangla': 'ডায়াগনস্টিক সেবা',
        'service_type': 'diagnostics',
        'description': 'Comprehensive diagnostic services using the latest medical technology and equipment available in China.',
        'description_bangla': 'চীনে উপলব্ধ সর্বশেষ চিকিৎসা প্রযুক্তি ও যন্ত্রপাতি ব্যবহার করে ব্যাপক ডায়াগনস্টিক সেবা।',
        'price_range': '$500 - $3,000 USD',
        'duration': '1-3 days',
        'is_active': True,
    },
    {
        'name': 'Medication Access',
        'name_bangla': 'ঔষধ প্রাপ্তি',
        'service_type': 'medication',
        'description': 'Access to innovative medications and treatments not yet available in Bangladesh through our pharmaceutical logistics system.',
        'description_bangla': 'আমাদের ফার্মাসিউটিক্যাল লজিস্টিক সিস্টেমের মাধ্যমে বাংলাদেশে এখনও পাওয়া যায়নি এমন উদ্ভাবনী ঔষধ ও চিকিৎসায় প্রবেশাধিকার।',
        'price_range': 'Varies by medication',
        'duration': '2-4 weeks delivery',
        'is_active': True,
    }
]

# Create sample testimonials
testimonials_data = [
    {
        'patient_name': 'Rahman Ahmed',
        'patient_name_bangla': 'রহমান আহমেদ',
        'treatment': 'Heart Surgery',
        'testimonial': 'UberMed.Life saved my life. Dr. Li Wei performed a complex heart surgery that was not possible in Bangladesh. The entire process was smooth and professional.',
        'testimonial_bangla': 'উবারমেড.লাইফ আমার জীবন বাঁচিয়েছে। ডঃ লি ওয়েই একটি জটিল হৃদযন্ত্রের অস্ত্রোপচার করেছেন যা বাংলাদেশে সম্ভব ছিল না। পুরো প্রক্রিয়াটি মসৃণ এবং পেশাদার ছিল।',
        'rating': 5,
        'is_featured': True,
        'is_published': True,
    },
    {
        'patient_name': 'Fatima Begum',
        'patient_name_bangla': 'ফাতিমা বেগম',
        'treatment': 'Cancer Treatment',
        'testimonial': 'Dr. Zhang Ming provided exceptional care during my cancer treatment. The teleconsultation service helped me get expert advice without traveling initially.',
        'testimonial_bangla': 'ডঃ ঝাং মিং আমার ক্যান্সার চিকিৎসার সময় ব্যতিক্রমী যত্ন প্রদান করেছেন। টেলিকনসালটেশন সেবা আমাকে প্রাথমিকভাবে ভ্রমণ না করেই বিশেষজ্ঞ পরামর্শ পেতে সাহায্য করেছে।',
        'rating': 5,
        'is_featured': True,
        'is_published': True,
    },
    {
        'patient_name': 'Karim Hassan',
        'patient_name_bangla': 'করিম হাসান',
        'treatment': 'Orthopedic Surgery',
        'testimonial': 'Dr. Chen Hao performed my knee replacement surgery perfectly. I can walk pain-free now. The medical tourism package was well-organized.',
        'testimonial_bangla': 'ডঃ চেন হাও আমার হাঁটু প্রতিস্থাপন অস্ত্রোপচার নিখুঁতভাবে সম্পাদন করেছেন। আমি এখন ব্যথা ছাড়াই হাঁটতে পারি। চিকিৎসা পর্যটন প্যাকেজটি সুসংগঠিত ছিল।',
        'rating': 5,
        'is_featured': True,
        'is_published': True,
    },
    {
        'patient_name': 'Nasir Uddin',
        'patient_name_bangla': 'নাসির উদ্দিন',
        'treatment': 'Liver Treatment',
        'testimonial': 'Dr. Liu Yanping helped me with my liver condition. Her expertise and the treatment I received in Guangzhou exceeded my expectations.',
        'testimonial_bangla': 'ডঃ লিউ ইয়ানপিং আমার লিভারের অবস্থার সাথে আমাকে সাহায্য করেছেন। তার দক্ষতা এবং গুয়াংঝুতে আমি যে চিকিৎসা পেয়েছি তা আমার প্রত্যাশা ছাড়িয়ে গেছে।',
        'rating': 5,
        'is_featured': False,
        'is_published': True,
    },
]

# Create sample news articles
def create_sample_data():
    # Create doctors
    for doctor_data in doctors_data:
        doctor, created = Doctor.objects.get_or_create(
            name=doctor_data['name'],
            defaults=doctor_data
        )
        if created:
            print(f"Created doctor: {doctor.name}")

    # Create services
    for service_data in services_data:
        service, created = Service.objects.get_or_create(
            name=service_data['name'],
            defaults=service_data
        )
        if created:
            print(f"Created service: {service.name}")

    # Create testimonials
    for testimonial_data in testimonials_data:
        testimonial, created = Testimonial.objects.get_or_create(
            patient_name=testimonial_data['patient_name'],
            defaults=testimonial_data
        )
        if created:
            print(f"Created testimonial: {testimonial.patient_name}")

    # Create sample news articles
    try:
        admin_user = User.objects.get(username='admin')
        
        news_articles = [
            {
                'title': 'UberMed.Life Partners with Leading Chinese Hospitals',
                'title_bangla': 'উবারমেড.লাইফ শীর্ষস্থানীয় চীনা হাসপাতালগুলির সাথে অংশীদারিত্ব করেছে',
                'slug': 'ubermed-partners-chinese-hospitals',
                'content': 'UberMed.Life is proud to announce partnerships with over 20 leading Chinese hospitals, providing Bangladeshi patients with access to world-class medical care.',
                'content_bangla': 'উবারমেড.লাইফ গর্বের সাথে ২০টিরও বেশি শীর্ষস্থানীয় চীনা হাসপাতালের সাথে অংশীদারিত্বের ঘোষণা দিচ্ছে।',
                'excerpt': 'Expanding access to Chinese medical expertise for Bangladeshi patients.',
                'author': admin_user,
                'is_published': True,
                'is_featured': True,
            },
            {
                'title': 'Breakthrough Cancer Treatment Now Available',
                'title_bangla': 'যুগান্তকারী ক্যান্সার চিকিৎসা এখন উপলব্ধ',
                'slug': 'breakthrough-cancer-treatment-available',
                'content': 'New immunotherapy treatments for cancer are now accessible to Bangladeshi patients through our partnership with Shanghai Cancer Center.',
                'content_bangla': 'ক্যান্সারের জন্য নতুন ইমিউনোথেরাপি চিকিৎসা এখন আমাদের সাংহাই ক্যান্সার সেন্টারের সাথে অংশীদারিত্বের মাধ্যমে বাংলাদেশী রোগীদের জন্য প্রবেশযোগ্য।',
                'excerpt': 'Advanced cancer treatments bringing new hope to patients.',
                'author': admin_user,
                'is_published': True,
                'is_featured': False,
            }
        ]
        
        for article_data in news_articles:
            article, created = NewsArticle.objects.get_or_create(
                slug=article_data['slug'],
                defaults=article_data
            )
            if created:
                print(f"Created news article: {article.title}")
                
    except User.DoesNotExist:
        print("Admin user not found. Please create a superuser first.")

if __name__ == "__main__":
    create_sample_data()
    print("Sample data created successfully!")
