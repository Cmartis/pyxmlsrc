#!/usr/bin/python3
#Author: Chris Martis


import randomizer
import random
import string
import uuid
from faker import Faker

from xml.dom import minidom
import os

def GenerateXML(filename):
    digits = string.digits
    fake = Faker()
    xmlns = 'urn:iso:std:iso:20022:tech:xsd:pacs.008.001.10'
    xmlns_xsi =  'http://www.w3.org/2001/XMLSchema-instance'
    xsi_schemaLocation =  'urn:iso:std:iso:20022:tech:xsd:pacs.008.001.10 pacs.008.001.10.xsd'
    root = minidom.Document()

    doc = root.createElement('Document')
    doc.setAttribute('xmlns', xmlns)
    doc.setAttribute('xmlns:xsi', xmlns_xsi)
    doc.setAttribute('xsi:schemaLocation', xsi_schemaLocation)
    root.appendChild(doc)

    fi2fi = root.createElement('FIToFICstmrCdtTrf')
    doc.appendChild(fi2fi)

    #----start  Grphdr
    grphdr = root.createElement('GrpHdr')
    fi2fi.appendChild(grphdr)

    msgid = root.createElement('MsgId') 
    grphdr.appendChild(msgid)
    #msgIdVal = root.createTextNode('111111111111111')
    msgIdVal = root.createTextNode(str(randomizer.randomizer(digits, 15)))
    msgid.appendChild(msgIdVal)

    credtm = root.createElement('CreDtTm')
    grphdr.appendChild(credtm)
    credtmVal = root.createTextNode('2021-06-23T02:03:03.000Z')
    credtm.appendChild(credtmVal)


    nboftxs = root.createElement('NbOfTxs')
    grphdr.appendChild(nboftxs)
    nboftxsVal = root.createTextNode('1')
    nboftxs.appendChild(nboftxsVal)


    sttlminf = root.createElement('SttlmInf')
    grphdr.appendChild(sttlminf)

    sttlmmtd = root.createElement('SttlmMtd')
    sttlminf.appendChild(sttlmmtd)
    sttlmmtdVal = root.createTextNode('INDA')
    sttlmmtd.appendChild(sttlmmtdVal)

    instgrmbrsmntagt = root.createElement('InstgRmbrsmntAgt')
    sttlminf.appendChild(instgrmbrsmntagt)

    fininstnid = root.createElement('FinInstnId')
    instgrmbrsmntagt.appendChild(fininstnid)

    bicfi = root.createElement('BICFI')
    fininstnid.appendChild(bicfi)
    bicfiVal = root.createTextNode('SNFSUS33')
    bicfi.appendChild(bicfiVal)

    instgrmbrsmntagtacct = root.createElement('InstgRmbrsmntAgtAcct')
    sttlminf.appendChild(instgrmbrsmntagtacct)

    id = root.createElement('Id')
    instgrmbrsmntagtacct.appendChild(id)

    othr = root.createElement('Othr')
    id.appendChild(othr)
    id = root.createElement('Id')
    othr.appendChild(id)
    #idVal = root.createTextNode('REIMBAGTO111111111111111111111')
    idVal = root.createTextNode("REIMBAGT" + str(randomizer.randomizer(digits, 25)))
    #msgIdVal = root.createTextNode(str(randomizer.randomizer(digits, 15)))
    id.appendChild(idVal)

    #----finish Grphdr
    #----start Cdtrftxinf

    cdttrftxinf = root.createElement('CdtTrfTxInf')
    fi2fi.appendChild(cdttrftxinf)

    #----start PmtId
    pmtid = root.createElement('PmtId')
    cdttrftxinf.appendChild(pmtid)

    instrid = root.createElement('InstrId')
    pmtid.appendChild(instrid)
    instridVal = root.createTextNode('TransactionID-1')
    instrid.appendChild(instridVal)

    endtoendid = root.createElement('EndToEndId')
    pmtid.appendChild(endtoendid)
    #endtoendidVal = root.createTextNode('E2E-111111111111111')
    endtoendidVal = root.createTextNode("E2E-" + str(randomizer.randomizer(digits, 15)))
    #idVal = root.createTextNode("REIMBAGT" + str(randomizer.randomizer(digits, 25)))
    endtoendid.appendChild(endtoendidVal)

    uetr = root.createElement('UETR')
    pmtid.appendChild(uetr)
    #uetrVal = root.createTextNode('00000000-0000-4000-8000-000000000000')
    uetrVal = root.createTextNode(str(uuid.uuid4()))
    uetr.appendChild(uetrVal)


    #----finish  PmtId
    #----start  pmtpinf
    
    pmttpinf = root.createElement('PmtTpInf')
    cdttrftxinf.appendChild(pmttpinf)
    svclvl = root.createElement('SvcLvl')
    pmttpinf.appendChild(svclvl)
    cd = root.createElement('Cd')
    svclvl.appendChild(cd)
    cdVal = root.createTextNode('G001')
    cd.appendChild(cdVal)


    #----finish  pmtpinf

    intrbksttlmamt = root.createElement('IntrBkSttlmAmt')
    #intrbksttlmamt.setAttribute('Ccy', 'USD')
    intrbksttlmamt.setAttribute('Ccy', str(random.choice(['USD', 'EUR', 'AUD', 'CAD', 'HKD', 'CNY'])))
    cdttrftxinf.appendChild(intrbksttlmamt)
    #intrbksttlmamtVal = root.createTextNode('600000000.00')
    intrbksttlmamtVal = root.createTextNode(str(randomizer.randomizer(digits, random.randint(5,10))+str("." + randomizer.randomizer(digits,2))))
    #endtoendidVal = root.createTextNode("E2E-" + str(randomizer.randomizer(digits, 15)))
    intrbksttlmamt.appendChild(intrbksttlmamtVal)

    intrbksttlmdt = root.createElement('IntrBkSttlmDt')
    cdttrftxinf.appendChild(intrbksttlmdt)
    intrbksttlmdtVal = root.createTextNode('2020-06-23')
    intrbksttlmdt.appendChild(intrbksttlmdtVal)
   
   #----start SttlmTmIndctn

    sttlmtmindctn = root.createElement('SttlmTmIndctn')
    cdttrftxinf.appendChild(sttlmtmindctn)

    dbtdttm = root.createElement('DbtDtTm')
    sttlmtmindctn.appendChild(dbtdttm)
    dbtdttmVal = root.createTextNode('2021-04-23T17:20:39:000z')
    dbtdttm.appendChild(dbtdttmVal)

    cdtdttm = root.createElement('CdtDtTm')
    sttlmtmindctn.appendChild(cdtdttm)
    cdtdttmVal =  root.createTextNode('2021-04-23T23:40:39:000z')
    cdtdttm.appendChild(cdtdttmVal)

    sttlmtmreq = root.createElement('SttlmTmReq')
    cdttrftxinf.appendChild(sttlmtmreq)
    clstm = root.createElement('CLSTm')
    sttlmtmreq.appendChild(clstm)
    clstmVal =  root.createTextNode('23:40:39z')
    clstm.appendChild(clstmVal)

    instdamt = root.createElement('InstdAmt')
    #instdamt.setAttribute('Ccy', 'EUR')
    instdamt.setAttribute('Ccy', str(random.choice(['USD', 'EUR', 'AUD', 'CAD', 'HKD', 'CNY'])))
    cdttrftxinf.appendChild(instdamt)
    #instdAmtVal = root.createTextNode('500000000.00')
    instdAmtVal = root.createTextNode(str(randomizer.randomizer(digits, random.randint(5,10))+str("." + randomizer.randomizer(digits,2))))
    instdamt.appendChild(instdAmtVal)

    xchgrate = root.createElement('XchgRate')
    cdttrftxinf.appendChild(xchgrate)
    xchgrateVal = root.createTextNode('0.135')
    xchgrate.appendChild(xchgrateVal)

    chrgbr = root.createElement('ChrgBr')
    cdttrftxinf.appendChild(chrgbr)
    chrbrVal = root.createTextNode('CRED')
    chrgbr.appendChild(chrbrVal)

    chrgsinf = root.createElement('ChrgsInf')
    cdttrftxinf.appendChild(chrgsinf)

    amt = root.createElement('Amt')
    amt.setAttribute('Ccy', 'USD')
    chrgsinf.appendChild(amt)
    amtVal = root.createTextNode('l0.00')
    amt.appendChild(amtVal)

    agt = root.createElement('Agt')
    chrgsinf.appendChild(agt)
    fininstnid = root.createElement('FinInstnId')
    agt.appendChild(fininstnid)
    bicfi = root.createElement('BICFI')
    fininstnid.appendChild(bicfi)
    #bicfiVal = root.createTextNode('SNFSUS22')
    bicfiVal = root.createTextNode(str(random.choice(['BOFA', 'CHAS', 'CITI', 'WFBI', 'BARC','RBSS', 'BNPA', 'SOGE','DEUT','MHCB']) + str(random.choice(['US', 'BE', 'CA', 'CN', 'HK', 'JP', 'GB'])) + str(randomizer.randomizer(digits, 2))))
    bicfi.appendChild(bicfiVal)

    prvsinstgagt1 = root.createElement('PrvsInstgAgt1')
    cdttrftxinf.appendChild(prvsinstgagt1)
    fininstnid = root.createElement('FinInstnId')
    prvsinstgagt1.appendChild(fininstnid)
    bicfi = root.createElement('BICFI')
    fininstnid.appendChild(bicfi)
    #bicfiVal = root.createTextNode('SNFSUS88')
    #bicfiVal = root.createTextNode(str(randomizer.randomizer(string.ascii_uppercase, 4) + str(random.choice(['US', 'BE', 'CA', 'CN', 'HK', 'JP', 'GB'])) + str(randomizer.randomizer(digits, 2))))
    bicfiVal = root.createTextNode(str(random.choice(['BOFA', 'CHAS', 'CITI', 'WFBI', 'BARC','RBSS', 'BNPA', 'SOGE','DEUT','MHCB']) + str(random.choice(['US', 'BE', 'CA', 'CN', 'HK', 'JP', 'GB'])) + str(randomizer.randomizer(digits, 2))))
    bicfi.appendChild(bicfiVal)


    prvsinstgagt2 = root.createElement('PrvsInstgAgt2')
    cdttrftxinf.appendChild(prvsinstgagt2)
    fininstnid = root.createElement('FinInstnId')
    prvsinstgagt2.appendChild(fininstnid)
    bicfi = root.createElement('BICFI')
    fininstnid.appendChild(bicfi)
    #bicfiVal = root.createTextNode('SNFSUSA1')
    #bicfiVal = root.createTextNode(str(randomizer.randomizer(string.ascii_uppercase, 4) + str(random.choice(['US', 'BE', 'CA', 'CN', 'HK', 'JP', 'GB'])) + str(randomizer.randomizer(digits, 2))))
    bicfiVal = root.createTextNode(str(random.choice(['BOFA', 'CHAS', 'CITI', 'WFBI', 'BARC','RBSS', 'BNPA', 'SOGE','DEUT','MHCB']) + str(random.choice(['US', 'BE', 'CA', 'CN', 'HK', 'JP', 'GB'])) + str(randomizer.randomizer(digits, 2))))
    bicfi.appendChild(bicfiVal)

    prvsinstgagt3 = root.createElement('PrvsInstgAgt3')
    cdttrftxinf.appendChild(prvsinstgagt3)
    fininstnid = root.createElement('FinInstnId')
    prvsinstgagt3.appendChild(fininstnid)
    bicfi = root.createElement('BICFI')
    fininstnid.appendChild(bicfi)
    #bicfiVal = root.createTextNode('SNFSUSB1')
    #bicfiVal = root.createTextNode(str(randomizer.randomizer(string.ascii_uppercase, 4) + str(random.choice(['US', 'BE', 'CA', 'CN', 'HK', 'JP', 'GB'])) + str(randomizer.randomizer(digits, 2))))
    bicfiVal = root.createTextNode(str(random.choice(['BOFA', 'CHAS', 'CITI', 'WFBI', 'BARC','RBSS', 'BNPA', 'SOGE','DEUT','MHCB']) + str(random.choice(['US', 'BE', 'CA', 'CN', 'HK', 'JP', 'GB'])) + str(randomizer.randomizer(digits, 2))))
    bicfi.appendChild(bicfiVal)

    instgagt = root.createElement('InstgAgt')
    cdttrftxinf.appendChild(instgagt)
    fininstnid = root.createElement('FinInstnId')
    instgagt.appendChild(fininstnid)
    bicfi = root.createElement('BICFI')
    fininstnid.appendChild(bicfi)
    #bicfiVal = root.createTextNode('SNFSUS22')
    #bicfiVal = root.createTextNode(str(randomizer.randomizer(string.ascii_uppercase, 4) + str(random.choice(['US', 'BE', 'CA', 'CN', 'HK', 'JP', 'GB'])) + str(randomizer.randomizer(digits, 2))))
    bicfiVal = root.createTextNode(str(random.choice(['BOFA', 'CHAS', 'CITI', 'WFBI', 'BARC','RBSS', 'BNPA', 'SOGE','DEUT','MHCB']) + str(random.choice(['US', 'BE', 'CA', 'CN', 'HK', 'JP', 'GB'])) + str(randomizer.randomizer(digits, 2))))
    bicfi.appendChild(bicfiVal)

    instgagt = root.createElement('InstgAgt')
    cdttrftxinf.appendChild(instgagt)
    fininstnid = root.createElement('FinInstnId')
    instgagt.appendChild(fininstnid)
    bicfi = root.createElement('BICFI')
    fininstnid.appendChild(bicfi)
    #bicfiVal = root.createTextNode('SNFSUS44')
    #bicfiVal = root.createTextNode(str(randomizer.randomizer(string.ascii_uppercase, 4) + str(random.choice(['US', 'BE', 'CA', 'CN', 'HK', 'JP', 'GB'])) + str(randomizer.randomizer(digits, 2))))
    bicfiVal = root.createTextNode(str(random.choice(['BOFA', 'CHAS', 'CITI', 'WFBI', 'BARC','RBSS', 'BNPA', 'SOGE','DEUT','MHCB']) + str(random.choice(['US', 'BE', 'CA', 'CN', 'HK', 'JP', 'GB'])) + str(randomizer.randomizer(digits, 2))))
    bicfi.appendChild(bicfiVal)

    intrmyagt1 = root.createElement('IntrmyAgt1')
    cdttrftxinf.appendChild(intrmyagt1)
    fininstnid = root.createElement('FinInstnId')
    intrmyagt1.appendChild(fininstnid)
    bicfi = root.createElement('BICFI')
    fininstnid.appendChild(bicfi)
    #picfiVal = root.createTextNode('SNFSUS55')
    #bicfiVal = root.createTextNode(str(randomizer.randomizer(string.ascii_uppercase, 4) + str(random.choice(['US', 'BE', 'CA', 'CN', 'HK', 'JP', 'GB'])) + str(randomizer.randomizer(digits, 2))))
    bicfiVal = root.createTextNode(str(random.choice(['BOFA', 'CHAS', 'CITI', 'WFBI', 'BARC','RBSS', 'BNPA', 'SOGE','DEUT','MHCB']) + str(random.choice(['US', 'BE', 'CA', 'CN', 'HK', 'JP', 'GB'])) + str(randomizer.randomizer(digits, 2))))
    bicfi.appendChild(bicfiVal)

    intrmyagt2 = root.createElement('IntrmyAgt2')
    cdttrftxinf.appendChild(intrmyagt2)
    fininstnid = root.createElement('FinInstnId')
    intrmyagt2.appendChild(fininstnid)
    bicfi = root.createElement('BICFI')
    fininstnid.appendChild(bicfi)
    #bicfiVal = root.createTextNode('SNFSUS66XXX')
    #bicfiVal = root.createTextNode(str(randomizer.randomizer(string.ascii_uppercase, 4) + str(random.choice(['US', 'BE', 'CA', 'CN', 'HK', 'JP', 'GB'])) 
    bicfiVal = root.createTextNode(str(random.choice(['BOFA', 'CHAS', 'CITI', 'WFBI', 'BARC','RBSS', 'BNPA', 'SOGE','DEUT','MHCB']) + str(random.choice(['US', 'BE', 'CA', 'CN', 'HK', 'JP', 'GB']))
                                                                                                + str(randomizer.randomizer(digits, 2) + str(randomizer.randomizer(string.ascii_uppercase,3)))))
    bicfi.appendChild(bicfiVal)

    intrmyagt3 = root.createElement('IntrmyAgt3')
    cdttrftxinf.appendChild(intrmyagt3)
    fininstnid = root.createElement('FinInstnId')
    intrmyagt3.appendChild(fininstnid)
    bicfi = root.createElement('BICFI')
    fininstnid.appendChild(bicfi)
    #bicfiVal = root.createTextNode('SNFSUS77XXX')
    #bicfiVal = root.createTextNode(str(randomizer.randomizer(string.ascii_uppercase, 4) + str(random.choice(['US', 'BE', 'CA', 'CN', 'HK', 'JP', 'GB'])) 
    #                                                                                        + str(randomizer.randomizer(digits, 2) + str(randomizer.randomizer(string.ascii_uppercase,2)))))
    bicfiVal = root.createTextNode(str(random.choice(['BOFA', 'CHAS', 'CITI', 'WFBI', 'BARC','RBSS', 'BNPA', 'SOGE','DEUT','MHCB']) + str(random.choice(['US', 'BE', 'CA', 'CN', 'HK', 'JP', 'GB']))
                                                                                                + str(randomizer.randomizer(digits, 2) + str(randomizer.randomizer(string.ascii_uppercase,3)))))
    bicfi.appendChild(bicfiVal)

    #---- start dbtr

    dbtr = root.createElement('Dbtr')
    cdttrftxinf.appendChild(dbtr)
    nm = root.createElement('Nm')
    dbtr.appendChild(nm)
    #nmVal = root.createTextNode('Debtor Name corporation - ABC LLC, Washington D.C, Columbia - This is 140 text field tested for the field length. If is goes test is passed.')
    nmVal = root.createTextNode(str(fake.name() + " " + fake.address()))
    nm.appendChild(nmVal)

    pstladr = root.createElement('PstlAdr')
    dbtr.appendChild(pstladr)
    strtnm = root.createElement('StrtNm')
    pstladr.appendChild(strtnm)
    #strtnmVal = root.createTextNode('MainLane')
    strtnmVal = root.createTextNode(str(fake.address()))
    strtnm.appendChild(strtnmVal)
    bldgnb = root.createElement('BldgNb')
    pstladr.appendChild(bldgnb)
    #bldgnbVal = root.createTextNode('4')
    bldgnbVal = root.createTextNode(str(fake.building_number()))
    bldgnb.appendChild(bldgnbVal)
    twnnm = root.createElement('TwnNm')
    pstladr.appendChild(twnnm)
    #twnnmVal = root.createTextNode('Ottowa')
    twnnmVal = root.createTextNode(str(fake.city()))
    twnnm.appendChild(twnnmVal)
    ctry = root.createElement('Ctry')
    pstladr.appendChild(ctry)
    #ctryVal = root.createTextNode('CA')
    ctryVal = root.createTextNode(str(fake.country_code()))
    ctry.appendChild(ctryVal)

    id = root.createElement('Id')
    dbtr.appendChild(id)
    orgid = root.createElement('OrgId')
    id.appendChild(orgid)
    anybic = root.createElement('AnyBIC')
    orgid.appendChild(anybic)
    #anybicVal = root.createTextNode('SNFSUS88')
    #anybicVal = root.createTextNode(str(randomizer.randomizer(string.ascii_uppercase, 4) + str(random.choice(['US', 'BE', 'CA', 'CN', 'HK', 'JP', 'GB'])) + str(randomizer.randomizer(digits, 2))))
    anybicVal = root.createTextNode(str(random.choice(['BOFA', 'CHAS', 'CITI', 'WFBI', 'BARC','RBSS', 'BNPA', 'SOGE','DEUT','MHCB']) + str(random.choice(['US', 'BE', 'CA', 'CN', 'HK', 'JP', 'GB'])) + str(randomizer.randomizer(digits, 2))))
    anybic.appendChild(anybicVal)

    #---- finish dbtr
    #---- start dbtracct

    dbtracct = root.createElement('DbtrAcct')
    cdttrftxinf.appendChild(dbtracct)
    id = root.createElement('Id')
    dbtracct.appendChild(id)
    iban = root.createElement('IBAN')
    id.appendChild(iban)
    #ibanVal = root.createTextNode('AD1200012030200359100100')
    ibanVal = root.createTextNode(str(random.choice(['US', 'BE', 'CA', 'CN', 'HK', 'JP', 'GB'])) + str(randomizer.randomizer(digits, 20)))
    iban.appendChild(ibanVal)

    #---- finish dbtracct
    #---- start dbtragt

    dbtragt = root.createElement('DbtrAgt')
    cdttrftxinf.appendChild(dbtragt)
    fininstnid = root.createElement('FinInstnId')
    instgagt.appendChild(fininstnid)
    bicfi = root.createElement('BICFI')
    fininstnid.appendChild(bicfi)
    #bicfiVal = root.createTextNode('SNFSUS22')
    bicfiVal = root.createTextNode(str(random.choice(['BOFA', 'CHAS', 'CITI', 'WFBI', 'BARC','RBSS', 'BNPA', 'SOGE','DEUT','MHCB']) + str(random.choice(['US', 'BE', 'CA', 'CN', 'HK', 'JP', 'GB'])) + str(randomizer.randomizer(digits, 2))))
    bicfi.appendChild(bicfiVal)

    #---- finish dbtragt
    #---- start dbtragtacct

    dbtragtacct = root.createElement('DbtrAgtAcct')
    cdttrftxinf.appendChild(dbtragtacct)

    id = root.createElement('Id')
    dbtragtacct.appendChild(id)

    othr = root.createElement('Othr')
    id.appendChild(othr)
    id = root.createElement('Id')
    othr.appendChild(id)
    #idVal = root.createTextNode('DBTRAGNTOTHR111111111111111111111111')
    idVal = root.createTextNode("DBTRAGNTOTHR" + str(randomizer.randomizer(digits, 25)))
    id.appendChild(idVal)

    #---- finish dbtragtacct
    #---- start cdtragt

    cdtragt = root.createElement('CdtrAgt')
    cdttrftxinf.appendChild(cdtragt)
    fininstnid = root.createElement('FinInstnId')
    instgagt.appendChild(fininstnid)
    bicfi = root.createElement('BICFI')
    fininstnid.appendChild(bicfi)
    #bicfiVal = root.createTextNode('SNFSUS44')
    bicfiVal = root.createTextNode(str(random.choice(['BOFA', 'CHAS', 'CITI', 'WFBI', 'BARC','RBSS', 'BNPA', 'SOGE','DEUT','MHCB']) + str(random.choice(['US', 'BE', 'CA', 'CN', 'HK', 'JP', 'GB'])) + str(randomizer.randomizer(digits, 2))))
    bicfi.appendChild(bicfiVal)

    #---- finish cdtragt
    #---- start cdtragtacct

    cdtragtacct = root.createElement('cdtrAgtAcct')
    cdttrftxinf.appendChild(cdtragtacct)

    id = root.createElement('Id')
    cdtragtacct.appendChild(id)

    othr = root.createElement('Othr')
    id.appendChild(othr)
    id = root.createElement('Id')
    othr.appendChild(id)
    #idVal = root.createTextNode('CRTRAGNT1111111111111111111111')
    idVal = root.createTextNode("CRTRAGNT" + str(randomizer.randomizer(digits, 25)))
    id.appendChild(idVal)


    #---- finish cdtragtacct
    #---- start cdtr

    cdtr = root.createElement('Cdtr')
    cdttrftxinf.appendChild(cdtr)
    nm = root.createElement('Nm')
    cdtr.appendChild(nm)
    #nmVal = root.createTextNode('Creditor Name corporation - ABC LLC, Washington D.C, Columbia - This is 140 text field tested for the field length. If is goes test is passed.')
    nmVal = root.createTextNode(str(fake.name() + " " + fake.address()))
    nm.appendChild(nmVal)

    pstladr = root.createElement('PstlAdr')
    dbtr.appendChild(pstladr)
    strtnm = root.createElement('StrtNm')
    pstladr.appendChild(strtnm)
    #strtnmVal = root.createTextNode('SomeStreet')
    strtnmVal = root.createTextNode(str(fake.address()))
    strtnm.appendChild(strtnmVal)
    bldgnb = root.createElement('BldgNb')
    pstladr.appendChild(bldgnb)
    #bldgnbVal = root.createTextNode('65')
    bldgnbVal = root.createTextNode(str(fake.building_number()))
    bldgnb.appendChild(bldgnbVal)
    twnnm = root.createElement('TwnNm')
    pstladr.appendChild(twnnm)
    #twnnmVal = root.createTextNode('Manhattan')
    twnnmVal = root.createTextNode(str(fake.city()))
    twnnm.appendChild(twnnmVal)
    ctry = root.createElement('Ctry')
    pstladr.appendChild(ctry)
    #ctryVal = root.createTextNode('US')
    ctryVal = root.createTextNode(str(fake.country_code()))
    ctry.appendChild(ctryVal)

    id = root.createElement('Id')
    cdtr.appendChild(id)
    orgid = root.createElement('OrgId')
    id.appendChild(orgid)
    anybic = root.createElement('AnyBIC')
    orgid.appendChild(anybic)
    #anybicVal = root.createTextNode('SNFSUS99')
    anybicVal = root.createTextNode(str(random.choice(['BOFA', 'CHAS', 'CITI', 'WFBI', 'BARC','RBSS', 'BNPA', 'SOGE','DEUT','MHCB']) + str(random.choice(['US', 'BE', 'CA', 'CN', 'HK', 'JP', 'GB'])) + str(randomizer.randomizer(digits, 2))))
    anybic.appendChild(anybicVal)

    #---- finish cdtr
    #---- start cdtrAgtAcct
    cdtragtacct = root.createElement('cdtrAgtAcct')
    cdttrftxinf.appendChild(cdtragtacct)

    id = root.createElement('Id')
    cdtragtacct.appendChild(id)

    othr = root.createElement('Othr')
    id.appendChild(othr)
    id = root.createElement('Id')
    othr.appendChild(id)
    #idVal = root.createTextNode('BENEFICIARY12345667784734343323433')
    idVal = root.createTextNode("BENEFICIARY" + str(randomizer.randomizer(digits, 25)))
    id.appendChild(idVal)

    #---- finish cdtrAgtAcct
    #---- start RmtInf

    rmtinf = root.createElement('RmtInf')
    cdttrftxinf.appendChild(rmtinf)
    ustrd = root.createElement('Ustrd')
    rmtinf.appendChild(ustrd)
    ustrdVal = root.createTextNode('Unstructured Remittance information-Description of this field may contain 140 characters. Testing for the field len. If is go test is passed.')
    rmtinf.appendChild(ustrdVal)

    #---- finish RmtInf
    xml_str = root.toprettyxml(indent ="\t")

    #save_path_file = "gfg.xml"

    with open(filename, "w") as f:
            f.write(xml_str)

#Drive Code
if __name__ == "__main__":
    for countInt in range(10):
        filename = "pacs008_filename%d.xml" %countInt
        GenerateXML(filename)
