import pymongo

client = pymongo.MongoClient("mongodb+srv://admin:admin@cluster0.jv4sq.mongodb.net/test?retryWrites=true&w=majority")
db = client.bus_db

# db.bus_stop.drop()
# db.bus_stop.insert_many([
#     {'name':'Hall 2, Canteen 2', 'geocode':(1.349064853547057, 103.6853984081654)},
#     {'name':'Hall 2, Opp Hall 6', 'geocode':}
# ])

# db.driver.insert_many([
#     {'pin': '000000'},
#      {'pin': '111111'}
# ])

# db.bus.drop()
db.bus_stop.drop()
db.bus_stop.insert_many([{'name': 'Opp. Hall 14 & 15', 'geocode': (1.3532450354538075, 103.6817511460188)}, {'name': 'Hall 2, Canteen 2', 'geocode': (1.349064853547057, 103.6853984081654)}, {'name': 'Grad Hall 1 & 2 ', 'geocode': (1.3559756503677778, 103.68613237094836)}, {'name': 'Hall 12 & 13', 'geocode': (1.3520178455918637, 103.68060357011329)}, {'name': 'Opp. Hall 4 & 5', 'geocode': (1.3436876712347094, 103.68688998639655)}, {'name': 'NIE, Opp. LWN Lib.', 'geocode': (1.3482857200855363, 103.68027616083977)}, {'name': 'Hall 6', 'geocode': (1.3471628118101884, 103.68661508230949)}, {'name': 'Opp. Canteen 2', 'geocode': (1.349049105311344, 103.68543512918576)}, {'name': 'Hall 10 & 11', 'geocode': (1.3543457121335314, 103.68687161806753)}, {'name': 'Lee Wee Nam Lib', 'geocode': (1.3481778767403785, 103.68030203715091)}, {'name': 'Hall 1', 'geocode': (1.3456501981368578, 103.6877476934832)}, {'name': 'Opp. Hall 8', 'geocode': (1.351252443041732, 103.68579245703778)}, {'name': 'Pioneer MRT ', 'geocode': (1.3374501776122738, 103.69777878870597)}, {'name': 'Tan Chin Tuan ', 'geocode': (1.3449218641438432, 103.681560309621)}, {'name': 'Hall 7 & Saraca', 'geocode': (1.3552062386582817, 103.68452729337072)}, {'name': 'Hall 2, Opp Hall 6', 'geocode': (1.3477616609435055, 103.68651420713161)}, {'name': 'Hall 8', 'geocode': (1.3515182028743289, 103.68568147028408)}, {'name': 'Pioneer MRT Exit A', 'geocode': (1.3374501776122738, 103.69777878870597)}, {'name': 'North Hill Halls', 'geocode': (1.3546164292552554, 103.6872404655602)}, {'name': 'Opp. SPMS', 'geocode': (1.3402781778936885, 103.6817645969678)}, {'name': 'Hall 6 ', 'geocode': (1.3471628118101884, 103.68661508230949)}, {'name': 'Opp. Yunnan Garden', 'geocode': (1.3418354965848212, 103.68468060227495)}, {'name': 'Yunnan Garden', 'geocode': (1.3416547922987085, 103.6842841234978)}, {'name': 'Nanyang Heights', 'geocode': (1.351252443041732, 103.68579245703778)}, {'name': 'Opp. Hall 7 & Saraca', 'geocode': (1.3551571510383482, 103.68445271573061)}, {'name': 'Pioneer MRT Exit B', 'geocode': (1.3378187465675202, 103.69727564163622)}, {'name': 'SBS, Opp. LKCSOM', 'geocode': (1.3423375499787011, 103.67925088644385)}, {'name': 'Opp. CEE', 'geocode': (1.3459768309492703, 103.67836459026944)}, {'name': 'Hall 2, Opp. Hall 6', 'geocode': (1.3477616609435055, 103.68651420713161)}, {'name': 'Uni. Health Services', 'geocode': (1.3457689034716975, 103.68292649566975)}, {'name': 'Opp. Hall 3 & 12', 'geocode': (1.3506557900186384, 103.68027336430929)}, {'name': 'Hall 2, Canteen 2 ', 'geocode': (1.349064853547057, 103.6853984081654)}, {'name': 'Opp. WKKWSCI', 'geocode': (1.341860542085121, 103.67903968419424)}, {'name': 'WKWSCI, EEE', 'geocode': (1.342101580353032, 103.67926608129234)}, {'name': 'Tan Chin Tuant LT', 'geocode': (1.3449218641438432, 103.681560309621)}, {'name': 'Hall 4 & 5', 'geocode': (1.3441746909393444, 103.68754227086998)}, {'name': 'Opp. Yunnan Garden ', 'geocode': (1.3418354965848212, 103.68468060227495)}])
lol = {'campus_red': ['Hall 2, Canteen 2 ', 'Hall 2, Opp Hall 6', 'Hall 1', 'Hall 4 & 5', 'Yunnan Garden', 'Opp. SPMS', 'WKWSCI, EEE', 'SBS, Opp. LKCSOM', 'Lee Wee Nam Lib', 'Hall 12 & 13', 'Hall 7 & Saraca', 'Grad Hall 1 & 2 ', 'Hall 10 & 11', 'Hall 8'], 'campus_red_express_1': ['Hall 10 & 11', 'Grad Hall 1 & 2 ', 'Lee Wee Nam Lib'], 'campus_red_express_2': ['Hall 7 & Saraca', 'Hall 12 & 13', 'Lee Wee Nam Lib'], 'campus_red_lunch_express': ['NIE, Opp. LWN Lib.', 'North Hill Halls', 'Nanyang Heights', 'Opp. Hall 4 & 5', 'Opp. Yunnan Garden'], 'campus_blue': ['Hall 6', 'Opp. Hall 4 & 5', 'Opp. Yunnan Garden ', 'Opp. SPMS', 'Opp. WKKWSCI', 'Opp. CEE', 'NIE, Opp. LWN Lib.', 'Opp. Hall 3 & 12', 'Opp. Hall 14 & 15', 'Opp. Hall 7 & Saraca', 'North Hill Halls', 'Nanyang Heights'], 'campus_blue_express_1': ['North Hill Halls', 'Opp. Hall 8', 'Hall 6 ', 'Opp. Hall 4 & 5', 'Opp. Yunnan Garden', 'NIE, Opp. LWN Lib.'], 'campus_green': ['Pioneer MRT Exit B', 'Opp. Canteen 2', 'Tan Chin Tuant LT', 'Uni. Health Services', 'Hall 2, Canteen 2', 'Hall 2, Opp. Hall 6', 'Hall 1', 'Pioneer MRT Exit A'], 'campus_green_express_1': ['Tan Chin Tuan ', 'Pioneer MRT ']}
for key in lol.keys():
    for name in lol[key]:
        db.bus_stop.find_one_and_update(
            {'name': name},
            { '$push': {'bus_types': key}}
        )