adb wait-for-device
adb root
adb wait-for-device
adb remount
adb wait-for-device
:: get current flord path.
:: remove service config file.

adb pull data/data/com.android.providers.telephony/databases/mmssms.db C:\rcs 

adb pull data/data/com.suntek.mway.rcs.app.service/databases/rcs.db C:/rcs

adb pull /data/data/com.android.providers.contacts/databases/contacts2.db C:/rcs


