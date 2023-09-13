"""This file defines the dictionary which contains all of the information on the classes
L7-L113 : defining 'info' boxes
L162-L172 : defining the dictionary containing all information"""

### Defining the 'info' boxes for each class

info_box_737="""Role : Narrow-body airliner
National origin	: United States
Manufacturer : Boeing
First flight : April 9, 1967; 56 years ago
Introduction : February 10, 1968 (55 years ago), with Lufthansa
Status : In service
Primary users : Southwest Airlines, Ryanair, United Airlines, American Airlines
Produced : 1966–present
Number built : 11,513 as of July 2023[1]
Variants : Boeing T-43
Developed into : Boeing 737 Classic, Boeing 737 Next Generation, Boeing 737 MAX"""


info_box_747= """Role : Wide-body jet airliner
National origin : United States
Manufacturer : Boeing Commercial Airplanes
First flight : February 9, 1969
Introduction : January 22, 1970, with Pan Am
Status : In service
Primary users : Atlas Air, Lufthansa, Cargolux, UPS Airlines
Produced : 1968–2023
Number built : 1,574 (including prototype)
Variants : Boeing 747SP, Boeing 747-400, Boeing 747-8, Boeing VC-25, Boeing E-4, 747 Supertanker
Developed into : Boeing Dreamlifter, Boeing YA-1, Shuttle Carrier Aircraft, SOFIA"""


info_box_767= """Role : Wide-body airliner
National origin : United States
Manufacturer : Boeing Commercial Airplanes
First flight : September 26, 1981
Introduction : September 8, 1982, with United Airlines
Status : In service
Primary users : Delta Air Lines, FedEx Express, UPS Airlines, United Airlines
Produced : 1981–present; in cargo production as of 2023
Number built : 1,283 as of July 2023[1][2]
Variants : Boeing E-767, Boeing KC-46 Pegasus, Boeing KC-767, Northrop Grumman E-10 MC2A"""


info_box_A340= """Role : Wide-body jet airliner
National origin	: Multi-national
Manufacturer : Airbus
First flight : 25 October 1991; 31 years ago
Introduction : 15 March 1993; 30 years ago with Lufthansa & Air France
Status : In service
Primary users : Lufthansa, Mahan Air, Edelweiss Air, Swiss International Air Lines
Produced : 1991–2012[1]
Number built : 380 (377 delivered to airlines)[2]
Developed from : Airbus A300"""

info_box_CRJ= """Role : Regional jet
National origin	: Canada
Manufacturer : Bombardier Aviation
First flight : 10 May 1991
Introduction : 19 October 1992 with Lufthansa CityLine[1]
Status : In service
Primary users : SkyWest Airlines, Endeavor Air, PSA Airlines, Air Wisconsin
Produced : 1991-2020
Number built : 1945 [2]
Developed from : Canadair Challenger 600 series
Variants : Bombardier CRJ100/200, Bombardier CRJ700 series"""

info_box_DC= """Role : Wide-body airliner
National origin : United States
Manufacturer : McDonnell Douglas
First flight : August 29, 1970; 53 years ago
Introduction : August 5, 1971, with American Airlines
Status : In limited service
Primary users : FedEx Express (historical), American Airlines (historical), United Airlines (historical), Northwest Airlines (historical)
Produced : 1968–1989
Number built : DC-10 - 386[1]; KC-10 - 60[1]
Variants : McDonnell Douglas KC-10 Extender, DC-10 Air Tanker
Developed into : McDonnell Douglas MD-11"""

info_box_DHC= """Role : Turboprop regional airliner
National origin : Canada
Manufacturer : 	de Havilland Canada (1983–1992), Bombardier Aerospace (1992–2019), De Havilland Canada (2019–present)
First flight : June 20, 1983
Introduction : 1984 with NorOntair
Status : In production
Primary users : QantasLink, WestJet Encore, Air Canada Express, Widerøe
Produced : 1983–2005 (-100), 1995–2009 (-200), 1989–2009 (-300), 1999–present (-400)
Number built : 1,258 (as of March 31, 2019)[1]
Developed from : de Havilland Canada Dash 7"""

info_box_E= """Role	: Narrow-body airliner
National origin : Brazil
Manufacturer : Embraer
First flight : 19 February 2002
Introduction : 17 March 2004 with LOT Polish Airlines
Status : In service
Primary users : SkyWest Airlines, Republic Airways, Envoy Air, Mesa Airlines, Arkia Israeli Airlines
Produced : 2001–present
Number built : 1,671 as of 30 June 2023[1][2]
Variants : Embraer Lineage 1000
Developed into : Embraer E-Jet E2 family"""

info_box_MD= """Role : Narrow-body jet airliner
National origin : United States
Manufacturer : McDonnell Douglas, Boeing Commercial Airplanes (from Aug. 1997)
First flight : October 18, 1979
Introduction : October 10, 1980, with Swissair
Status : In service; mostly for cargo transport
Primary users : Aeronaves TSM, World Atlantic Airlines, LASER Airlines, European Air Charter[1]
Produced : 1979–1999
Number built : 1,191
Developed from : McDonnell Douglas DC-9
Developed into : McDonnell Douglas MD-90, Boeing 717, Comac ARJ21"""

### Creating one dictionary containg all of the information to be referenced

aircraft_data = {
    '737': {
        'display_name': 'Boeing 737',
        'info_box': info_box_737,
        'image_url': 'https://wallpapercave.com/dwp1x/wp4735573.jpg',
        'wiki_link': 'https://en.wikipedia.org/wiki/Boeing_737',
    },
    '747': {
        'display_name': 'Boeing 747',
        'info_box': info_box_747,
        'image_url': 'https://getwallpapers.com/wallpaper/full/a/f/b/991203-download-free-boeing-747-wallpaper-2560x1600-for-phones.jpg',
        'wiki_link': 'https://en.wikipedia.org/wiki/Boeing_747',
    },
    '767': {
        'display_name': 'Boeing 767',
        'info_box': info_box_767,
        'image_url': 'https://wallpapercave.com/wp/wp4307909.jpg',
        'wiki_link': 'https://en.wikipedia.org/wiki/Boeing_767',
    },
    'A340': {
        'display_name': 'Airbus A340',
        'info_box': info_box_A340,
        'image_url': 'https://wallpapercave.com/dwp1x/wp6957458.jpg',
        'wiki_link': 'https://en.wikipedia.org/wiki/Airbus_A340',
    },
    'CRJ': {
        'display_name': 'Bombardier CRJ',
        'info_box': info_box_CRJ,
        'image_url': 'https://wallpapercave.com/dwp1x/wp3966996.jpg',
        'wiki_link': 'https://en.wikipedia.org/wiki/Bombardier_CRJ',
    },
    'DC': {
        'display_name': 'McDonnell Douglas DC-10',
        'info_box': info_box_DC,
        'image_url': 'https://wallpapercave.com/dwp1x/wp8871021.jpg',
        'wiki_link': 'https://en.wikipedia.org/wiki/McDonnell_Douglas_DC-10',
    },
    'DHC': {
        'display_name': 'De Havilland Canada Dash 8 (DHC-8)',
        'info_box': info_box_DHC,
        'image_url': 'https://www.aerospace-technology.com/wp-content/uploads/sites/15/2020/05/original.jpg',
        'wiki_link': 'https://en.wikipedia.org/wiki/De_Havilland_Canada_Dash_8',
    },
    'E': {
        'display_name': 'Embraer E-Jet',
        'info_box': info_box_E,
        'image_url': 'https://wallpapercave.com/dwp1x/wp11101571.jpg',
        'wiki_link': 'https://en.wikipedia.org/wiki/Embraer_E-Jet_family',
    },
    'MD': {
        'display_name': 'McDonnell Douglas MD-80',
        'info_box': info_box_MD,
        'image_url': 'https://wallpapercave.com/dwp1x/wp12288582.jpg',
        'wiki_link': 'https://en.wikipedia.org/wiki/McDonnell_Douglas_MD-80',
    },
}

aircraft_classes = ['737', '747', '767', 'A340', 'CRJ', 'DC', 'DHC', 'E', 'MD']
