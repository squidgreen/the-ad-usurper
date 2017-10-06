#!/usr/bin/python
import requests
import cgi, cgitb

def url_grabber(zipcode):
    base_request_url = "http://locator.safeway.com/ajax?&xml_request=%3Crequest%3E%3Cappkey%3EC8EBB30E-9CDD-11E0-9770-6DB40E5AF53B%3C%2Fappkey%3E%3Cformdata+id%3D%22locatorsearch%22%3E%3Cevents%3E%3Cwhere%3E%3Ceventstartdate%3E%3Cge%3Enow()%3C%2Fge%3E%3C%2Feventstartdate%3E%3C%2Fwhere%3E%3Climit%3E2%3C%2Flimit%3E%3C%2Fevents%3E%3Cdataview%3Estore_default%3C%2Fdataview%3E%3Cgeolocs%3E%3Cgeoloc%3E%3Caddressline%3Ezippp%3C%2Faddressline%3E%3Clongitude%3E%3C%2Flongitude%3E%3Clatitude%3E%3C%2Flatitude%3E%3Ccountry%3EUS%3C%2Fcountry%3E%3C%2Fgeoloc%3E%3C%2Fgeolocs%3E%3Csearchradius%3E15%7C25%7C50%7C100%7C250%3C%2Fsearchradius%3E%3Cstateonly%3E1%3C%2Fstateonly%3E%3Climit%3E20%3C%2Flimit%3E%3Cwhere%3E%3Ccountry%3EUS%3C%2Fcountry%3E%3Cclosed%3E%3Cdistinctfrom%3E1%3C%2Fdistinctfrom%3E%3C%2Fclosed%3E%3Cfuelparticipating%3E%3Cdistinctfrom%3E1%3C%2Fdistinctfrom%3E%3C%2Ffuelparticipating%3E%3Cbakery%3E%3Ceq%3E%3C%2Feq%3E%3C%2Fbakery%3E%3Cdeli%3E%3Ceq%3E%3C%2Feq%3E%3C%2Fdeli%3E%3Cfloral%3E%3Ceq%3E%3C%2Feq%3E%3C%2Ffloral%3E%3Cliquor%3E%3Ceq%3E%3C%2Feq%3E%3C%2Fliquor%3E%3Cmeat%3E%3Ceq%3E%3C%2Feq%3E%3C%2Fmeat%3E%3Cpharmacy%3E%3Ceq%3E%3C%2Feq%3E%3C%2Fpharmacy%3E%3Cproduce%3E%3Ceq%3E%3C%2Feq%3E%3C%2Fproduce%3E%3Cjamba%3E%3Ceq%3E%3C%2Feq%3E%3C%2Fjamba%3E%3Cseafood%3E%3Ceq%3E%3C%2Feq%3E%3C%2Fseafood%3E%3Cstarbucks%3E%3Ceq%3E%3C%2Feq%3E%3C%2Fstarbucks%3E%3Cvideo%3E%3Ceq%3E%3C%2Feq%3E%3C%2Fvideo%3E%3Cfuelstation%3E%3Ceq%3E%3C%2Feq%3E%3C%2Ffuelstation%3E%3Cdvdplay_kiosk%3E%3Ceq%3E%3C%2Feq%3E%3C%2Fdvdplay_kiosk%3E%3Ccoinmaster%3E%3Ceq%3E%3C%2Feq%3E%3C%2Fcoinmaster%3E%3Cwifi%3E%3Ceq%3E%3C%2Feq%3E%3C%2Fwifi%3E%3Cbank%3E%3Ceq%3E%3C%2Feq%3E%3C%2Fbank%3E%3Cseattlesbestcoffee%3E%3Ceq%3E%3C%2Feq%3E%3C%2Fseattlesbestcoffee%3E%3Cbeveragestewards%3E%3Ceq%3E%3C%2Feq%3E%3C%2Fbeveragestewards%3E%3Cphoto%3E%3Ceq%3E%3C%2Feq%3E%3C%2Fphoto%3E%3Cwu%3E%3Ceq%3E%3C%2Feq%3E%3C%2Fwu%3E%3Cdebi_lilly_design%3E%3Ceq%3E%3C%2Feq%3E%3C%2Fdebi_lilly_design%3E%3Cdelivery%3E%3Ceq%3E%3C%2Feq%3E%3C%2Fdelivery%3E%3Cfresh_cut_produce%3E%3Ceq%3E%3C%2Feq%3E%3C%2Ffresh_cut_produce%3E%3C%2Fwhere%3E%3C%2Fformdata%3E%3C%2Frequest%3E"

# replace the first occurrence
    request_url = base_request_url.replace("zippp", zipcode, 1)
    print(request_url)
#r = requests.post("http://www.vons.com/ShopStores/tools/store-locator.page", data=payload)
# HTTP request for nearest vons stores given zipcode
    location_response = requests.get(request_url)

#print(r.text.encode('utf-8'))
    start_index = location_response.text.find("weekly")
    end_index = location_response.text.find("<", start_index);
    print(start_index, end_index)

    containing_str = location_response.text[start_index:end_index]
    parsed_str = containing_str.split(">");

    print(parsed_str)
    return parsed_str[1]
