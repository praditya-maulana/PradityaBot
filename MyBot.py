import telebot
import mysql.connector
import MyToken

from datetime import datetime
TOKEN = MyToken.TOKEN
MyBot = telebot.TeleBot(TOKEN)
myDb = mysql.connector.connect(host ='localhost', user ='root', password='', database ='belajar_bot')
sql = myDb.cursor()
from telebot import apihelper
waktusekarang = datetime.now()

class mybot:
    def __init__(self):
        self.message

    @MyBot.message_handler(commands=['start', 'help'])
    def start(message):
        teks = MyToken.JAWAB + "\n-- Admin & Developer @pradityamaulana - #dirumahaja -- "+"\n" \
                                "Hari ini tanggal : "+str(waktusekarang) +"\n" \
                                "Untuk melihat data siswa SMK Taruna Bhakti, silahkan klik /datasiswa"

        MyBot.reply_to(message,teks)

    @MyBot.message_handler(commands=['datasiswa'])
    def menu_data_siswa(message):
        query = "select nipd,nama,kelas from tabel_siswa"
        sql.execute(query)
        data = sql.fetchall()
        jumlahdata = sql.rowcount
        kumpuldata = ''
        if(jumlahdata>0):
            no = 0
            for x in data:
                no += 1
                kumpuldata = kumpuldata + str(x)
                print(kumpuldata)
                kumpuldata = kumpuldata.replace('(','')
                kumpuldata = kumpuldata.replace(')','')
                kumpuldata = kumpuldata.replace("'",'')
                kumpuldata = kumpuldata.replace(",",'')
        else:
            print('Data siswa tidak tersedia')
        MyBot.reply_to(message,str(kumpuldata))

print(myDb)
print("--Bot sedang berjalan--")
MyBot.polling(none_stop=True)