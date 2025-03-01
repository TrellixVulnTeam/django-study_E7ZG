from django.db import models

#사용자가 구간 조회 후 예약을 위하여 선택하는 페이지 구현 - 관리자 레벨에서 컨트롤 하여 페이지 수정 가능

## QuerySet조회
###from airline_cousrse_search.models import *
###CargoAll.objects.filter(cargo_flight_section_test__contains='김포(GMP)-부산(PUS)')

class CargoAll(models.Model):
    # 비행구간
    SECTION = (
        ('김포(GMP) - 제주(CJU)', '김포(GMP) - 제주(CJU)'),
        ('김포(GMP) - 부산(PUS)', '김포(GMP) - 부산(PUS)'),
        ('부산(PUS) - 제주(CJU)', '부산(PUS) - 제주(CJU)'),
        ('부산(PUS) - 김포(GMP)', '부산(PUS) - 김포(GMP)'),
        ('제주(CJU) - 김포(GMP)', '제주(CJU) - 김포(GMP)'),
        ('제주(CJU) - 부산(PUS)', '제주(CJU) - 부산(PUS)'),
    )

    # 비행기종 - 비행기 편명
    EMPHYSEMA = (
        ('KE1201,B737-800', 'KE1201,B737-800'),
        ('KE1203,B737-220ER', 'KE1203,B737-220ER'),
        ('KE1205,A330-300', 'KE1205,A330-300'),
        ('KE1209,B737-900', 'KE1209,B737-900'),
        ('KE1211,B737-200ER', 'KE1211,B737-200ER'),
        ('KE1213,A330-200', 'KE1213,A330-200'),
        ('KE1215,A220-300', 'KE1215,A220-300'),
        ('KE1217,B777-200ER', 'KE1217,B777-200ER'),
        ('KE1221,A220-300', 'KE1221,A220-300'),
        ('KE1223,A220-300', 'KE1223,A220-300'),
    )

    # -- Document
    # 출발/도착시간(06:20~07:30) dept_arr_time = models.DateField()
    # 비행구간(김포-제주) flight_section = models.
    # 비행기편명/기종(KE1201 : A220-300) flight_number =
    # 출발/도착시간 dept_arr_time =
    # 특별운임(80,500원/1석) special_fare =
    # 정상운임(126,500원/1석) normal_fare =

    cargo_departure_test = models.DateTimeField()
    cargo_arrival_test = models.DateTimeField()
    cargo_flight_section_test = models.CharField(choices=SECTION, max_length=300)
    cargo_flight_number_test = models.CharField(choices=EMPHYSEMA, max_length=300)
    cargo_special_fare_test = models.IntegerField()
    cargo_normal_fare_test = models.IntegerField()


class GmptoCju(models.Model):

    #비행구간 
    SECTION = (
        ('김포(GMP) - 제주(CJU)','김포(GMP) - 제주(CJU)'),
    )

    #비행기종 - 비행기 편명
    EMPHYSEMA = (
        ('KE1201,B737-800','KE1201,B737-800'),
        ('KE1203,B737-220ER','KE1203,B737-220ER'),
        ('KE1205,A330-300','KE1205,A330-300'),
        ('KE1209,B737-900','KE1209,B737-900'),
        ('KE1211,B737-200ER','KE1211,B737-200ER'),
        ('KE1213,A330-200','KE1213,A330-200'),
        ('KE1215,A220-300','KE1215,A220-300'),
        ('KE1217,B777-200ER','KE1217,B777-200ER'),
        ('KE1221,A220-300','KE1221,A220-300'),
        ('KE1223,A220-300','KE1223,A220-300'),
    )
    
    #-- Document
    #출발/도착시간(06:20~07:30) dept_arr_time = models.DateField()
    #비행구간(김포-제주) flight_section = models.
    #비행기편명/기종(KE1201 : A220-300) flight_number =  
    #출발/도착시간 dept_arr_time =     
    #특별운임(80,500원/1석) special_fare = 
    #정상운임(126,500원/1석) normal_fare = 
    

    departure_time = models.DateTimeField()
    arrival_time = models.DateTimeField()
    flight_section = models.CharField(choices=SECTION, max_length=300)
    flight_number = models.CharField(choices=EMPHYSEMA, max_length=300)
    special_fare = models.IntegerField()
    normal_fare = models.IntegerField() 


class GmptoPus(models.Model):

    #비행구간 
    SECTION = (
        ('김포(GMP) - 부산(PUS)','김포(GMP) - 부산(PUS)'),
    )

    #비행기종 - 비행기 편명
    EMPHYSEMA = (
        ('KE1201,B737-800','KE1201,B737-800'),
        ('KE1203,B737-220ER','KE1203,B737-220ER'),
        ('KE1205,A330-300','KE1205,A330-300'),
        ('KE1209,B737-900','KE1209,B737-900'),
        ('KE1211,B737-200ER','KE1211,B737-200ER'),
        ('KE1213,A330-200','KE1213,A330-200'),
        ('KE1215,A220-300','KE1215,A220-300'),
        ('KE1217,B777-200ER','KE1217,B777-200ER'),
        ('KE1221,A220-300','KE1221,A220-300'),
        ('KE1223,A220-300','KE1223,A220-300'),
    )
    
    #-- Document
    #출발/도착시간(06:20~07:30) dept_arr_time = models.DateField()
    #비행구간(김포-제주) flight_section = models.
    #비행기편명/기종(KE1201 : A220-300) flight_number =  
    #출발/도착시간 dept_arr_time =     
    #특별운임(80,500원/1석) special_fare = 
    #정상운임(126,500원/1석) normal_fare = 
    

    departure_time = models.DateTimeField()
    arrival_time = models.DateTimeField()
    flight_section = models.CharField(choices=SECTION, max_length=300)
    flight_number = models.CharField(choices=EMPHYSEMA, max_length=300)
    special_fare = models.IntegerField()
    normal_fare = models.IntegerField() 


class PustoCju(models.Model):

    #비행구간 
    SECTION = (
        ('부산(PUS) - 제주(CJU)','부산(PUS) - 제주(CJU)'),
    )

    #비행기종 - 비행기 편명
    EMPHYSEMA = (
        ('KE1201,B737-800','KE1201,B737-800'),
        ('KE1203,B737-220ER','KE1203,B737-220ER'),
        ('KE1205,A330-300','KE1205,A330-300'),
        ('KE1209,B737-900','KE1209,B737-900'),
        ('KE1211,B737-200ER','KE1211,B737-200ER'),
        ('KE1213,A330-200','KE1213,A330-200'),
        ('KE1215,A220-300','KE1215,A220-300'),
        ('KE1217,B777-200ER','KE1217,B777-200ER'),
        ('KE1221,A220-300','KE1221,A220-300'),
        ('KE1223,A220-300','KE1223,A220-300'),
    )
    
    #-- Document
    #출발/도착시간(06:20~07:30) dept_arr_time = models.DateField()
    #비행구간(김포-제주) flight_section = models.
    #비행기편명/기종(KE1201 : A220-300) flight_number =  
    #출발/도착시간 dept_arr_time =     
    #특별운임(80,500원/1석) special_fare = 
    #정상운임(126,500원/1석) normal_fare = 
    

    departure_time = models.DateTimeField()
    arrival_time = models.DateTimeField()
    flight_section = models.CharField(choices=SECTION, max_length=300)
    flight_number = models.CharField(choices=EMPHYSEMA, max_length=300)
    special_fare = models.IntegerField()
    normal_fare = models.IntegerField() 


class PustoGmp(models.Model):

    #비행구간 
    SECTION = (
        ('부산(PUS) - 김포(GMP)','부산(PUS) - 김포(GMP)'),
    )

    #비행기종 - 비행기 편명
    EMPHYSEMA = (
        ('KE1201,B737-800','KE1201,B737-800'),
        ('KE1203,B737-220ER','KE1203,B737-220ER'),
        ('KE1205,A330-300','KE1205,A330-300'),
        ('KE1209,B737-900','KE1209,B737-900'),
        ('KE1211,B737-200ER','KE1211,B737-200ER'),
        ('KE1213,A330-200','KE1213,A330-200'),
        ('KE1215,A220-300','KE1215,A220-300'),
        ('KE1217,B777-200ER','KE1217,B777-200ER'),
        ('KE1221,A220-300','KE1221,A220-300'),
        ('KE1223,A220-300','KE1223,A220-300'),
    )
    
    #-- Document
    #출발/도착시간(06:20~07:30) dept_arr_time = models.DateField()
    #비행구간(김포-제주) flight_section = models.
    #비행기편명/기종(KE1201 : A220-300) flight_number =  
    #출발/도착시간 dept_arr_time =     
    #특별운임(80,500원/1석) special_fare = 
    #정상운임(126,500원/1석) normal_fare = 
    

    departure_time = models.DateTimeField()
    arrival_time = models.DateTimeField()
    flight_section = models.CharField(choices=SECTION, max_length=300)
    flight_number = models.CharField(choices=EMPHYSEMA, max_length=300)
    special_fare = models.IntegerField()
    normal_fare = models.IntegerField() 


class CjutoGmp(models.Model):

    #비행구간 
    SECTION = (
        ('제주(CJU) - 김포(GMP)','제주(CJU) - 김포(GMP)'),
    )

    #비행기종 - 비행기 편명
    EMPHYSEMA = (
        ('KE1201,B737-800','KE1201,B737-800'),
        ('KE1203,B737-220ER','KE1203,B737-220ER'),
        ('KE1205,A330-300','KE1205,A330-300'),
        ('KE1209,B737-900','KE1209,B737-900'),
        ('KE1211,B737-200ER','KE1211,B737-200ER'),
        ('KE1213,A330-200','KE1213,A330-200'),
        ('KE1215,A220-300','KE1215,A220-300'),
        ('KE1217,B777-200ER','KE1217,B777-200ER'),
        ('KE1221,A220-300','KE1221,A220-300'),
        ('KE1223,A220-300','KE1223,A220-300'),
    )
    
    #-- Document
    #출발/도착시간(06:20~07:30) dept_arr_time = models.DateField()
    #비행구간(김포-제주) flight_section = models.
    #비행기편명/기종(KE1201 : A220-300) flight_number =  
    #출발/도착시간 dept_arr_time =     
    #특별운임(80,500원/1석) special_fare = 
    #정상운임(126,500원/1석) normal_fare = 
    

    departure_time = models.DateTimeField()
    arrival_time = models.DateTimeField()
    flight_section = models.CharField(choices=SECTION, max_length=300)
    flight_number = models.CharField(choices=EMPHYSEMA, max_length=300)
    special_fare = models.IntegerField()
    normal_fare = models.IntegerField() 


class CjutoPus(models.Model):

    #비행구간 
    SECTION = (
        ('제주(CJU) - 부산(PUS)','제주(CJU) - 부산(PUS)'),
    )

    #비행기종 - 비행기 편명
    EMPHYSEMA = (
        ('KE1201,B737-800','KE1201,B737-800'),
        ('KE1203,B737-220ER','KE1203,B737-220ER'),
        ('KE1205,A330-300','KE1205,A330-300'),
        ('KE1209,B737-900','KE1209,B737-900'),
        ('KE1211,B737-200ER','KE1211,B737-200ER'),
        ('KE1213,A330-200','KE1213,A330-200'),
        ('KE1215,A220-300','KE1215,A220-300'),
        ('KE1217,B777-200ER','KE1217,B777-200ER'),
        ('KE1221,A220-300','KE1221,A220-300'),
        ('KE1223,A220-300','KE1223,A220-300'),
    )
    
    #-- Document
    #출발/도착시간(06:20~07:30) dept_arr_time = models.DateField()
    #비행구간(김포-제주) flight_section = models.
    #비행기편명/기종(KE1201 : A220-300) flight_number =  
    #출발/도착시간 dept_arr_time =     
    #특별운임(80,500원/1석) special_fare = 
    #정상운임(126,500원/1석) normal_fare = 
    

    departure_time = models.DateTimeField()
    arrival_time = models.DateTimeField()
    flight_section = models.CharField(choices=SECTION, max_length=300)
    flight_number = models.CharField(choices=EMPHYSEMA, max_length=300)
    special_fare = models.IntegerField()
    normal_fare = models.IntegerField() 
    


