def add_vat(price, vat_percent=18):
    """Qiymətə ƏDV əlavə edib qaytarır"""
    return price * (1 + vat_percent / 100)
def build_username(first, last, year=""):
    """İstifadəçi adı yaradır"""
    return first.lower() + "." + last.lower() + str(year)
def add_bonus(scores, bonus):
    """Listi yerində dəyişərək bonus əlavə edir"""
    for i in range(len(scores)):
        scores[i] = min(100, scores[i] + bonus)
def with_bonus(scores, bonus):
    """Orijinal listi dəyişmədən yeni list qaytarır"""
    return [min(100, s + bonus) for s in scores]
def average(*numbers):
    """Verilən ədədlərin ortalamasını tapır"""
    return sum(numbers) / len(numbers) if numbers else 0
def make_course(code, **details):
    """Kurs məlumatlarını lüğət şəklində qaytarır"""
    details["code"] = code
    return details
