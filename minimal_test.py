from __future__ import print_function
from scapy.all import *

class ASN1_Class_MMS(ASN1_Class_UNIVERSAL):
    name = "MMS"

    CONFIRMED_REQUEST_PDU = 0xa0
    TEST_INTEGER = 0xa1

class ASN1_CONFIRMED_REQUEST_PDU(ASN1_SEQUENCE):
    tag = ASN1_Class_MMS.CONFIRMED_REQUEST_PDU

class BERcodec_CONFIRMED_REQUEST_PDU(BERcodec_SEQUENCE):
    tag = ASN1_Class_MMS.CONFIRMED_REQUEST_PDU

	
class ASN1_TEST_INTEGER(ASN1_INTEGER):
    tag = ASN1_Class_MMS.TEST_INTEGER

class BERcodec_TEST_INTEGER(BERcodec_INTEGER):
    tag = ASN1_Class_MMS.TEST_INTEGER


x=ASN1_SEQUENCE([ASN1_INTEGER(7), ASN1_STRING("egg"), ASN1_SEQUENCE([ASN1_BOOLEAN(False)])])
x.show()
hexdump(x)

y=ASN1_CONFIRMED_REQUEST_PDU([ASN1_INTEGER(7), ASN1_STRING("egg"), ASN1_SEQUENCE([ASN1_BOOLEAN(False)])])
y.show()
hexdump(y)


z=ASN1_CONFIRMED_REQUEST_PDU([ASN1_TEST_INTEGER(7), ASN1_STRING("egg"), ASN1_SEQUENCE([ASN1_BOOLEAN(False)])])
z.show()
hexdump(z)

