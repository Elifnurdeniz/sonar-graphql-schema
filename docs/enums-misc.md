```graphql
"""A geographical country, represented as a two character ISO code."""
enum Country {
  """United States"""
  US
  """Canada"""
  CA
  """Afghanistan"""
  AF
  """Albania"""
  AL
  """Algeria"""
  DZ
  """Andorra"""
  AD
  """Angola"""
  AO
  """Anguilla"""
  AI
  """Antarctica"""
  AQ
  """Antigua and/or Barbuda"""
  AG
  """Argentina"""
  AR
  """Armenia"""
  AM
  """Aruba"""
  AW
  """Australia"""
  AU
  """Austria"""
  AT
  """Azerbaijan"""
  AZ
  """Bahamas"""
  BS
  """Bahrain"""
  BH
  """Bangladesh"""
  BD
  """Barbados"""
  BB
  """Belarus"""
  BY
  """Belgium"""
  BE
  """Belize"""
  BZ
  """Benin"""
  BJ
  """Bermuda"""
  BM
  """Bhutan"""
  BT
  """Bolivia"""
  BO
  """Bosnia and Herzegovina"""
  BA
  """Botswana"""
  BW
  """Bouvet Island"""
  BV
  """Brazil"""
  BR
  """British Indian Ocean Territory"""
  IO
  """Brunei Darussalam"""
  BN
  """Bulgaria"""
  BG
  """Burkina Faso"""
  BF
  """Burundi"""
  BI
  """Cambodia"""
  KH
  """Cameroon"""
  CM
  """Cape Verde"""
  CV
  """Cayman Islands"""
  KY
  """Central African Republic"""
  CF
  """Chad"""
  TD
  """Chile"""
  CL
  """China"""
  CN
  """Christmas Island"""
  CX
  """Cocos (Keeling) Islands"""
  CC
  """Colombia"""
  CO
  """Comoros"""
  KM
  """Congo"""
  CG
  """Cook Islands"""
  CK
  """Costa Rica"""
  CR
  """Croatia (Hrvatska)"""
  HR
  """Cuba"""
  CU
  """Cyprus"""
  CY
  """Czech Republic"""
  CZ
  """Denmark"""
  DK
  """Djibouti"""
  DJ
  """Dominica"""
  DM
  """Dominican Republic"""
  DO
  """East Timor"""
  TP
  """Ecuador"""
  EC
  """Egypt"""
  EG
  """El Salvador"""
  SV
  """Equatorial Guinea"""
  GQ
  """Eritrea"""
  ER
  """Estonia"""
  EE
  """Ethiopia"""
  ET
  """Falkland Islands (Malvinas)"""
  FK
  """Faroe Islands"""
  FO
  """Fiji"""
  FJ
  """Finland"""
  FI
  """France"""
  FR
  """France, Metropolitan"""
  FX
  """French Guiana"""
  GF
  """French Polynesia"""
  PF
  """French Southern Territories"""
  TF
  """Gabon"""
  GA
  """Gambia"""
  GM
  """Georgia"""
  GE
  """Germany"""
  DE
  """Ghana"""
  GH
  """Gibraltar"""
  GI
  """Greece"""
  GR
  """Greenland"""
  GL
  """Grenada"""
  GD
  """Guadeloupe"""
  GP
  """Guatemala"""
  GT
  """Guinea"""
  GN
  """Guinea-Bissau"""
  GW
  """Guyana"""
  GY
  """Haiti"""
  HT
  """Heard and Mc Donald Islands"""
  HM
  """Honduras"""
  HN
  """Hong Kong"""
  HK
  """Hungary"""
  HU
  """Iceland"""
  IS
  """India"""
  IN
  """Indonesia"""
  ID
  """Iran (Islamic Republic of)"""
  IR
  """Iraq"""
  IQ
  """Ireland"""
  IE
  """Israel"""
  IL
  """Italy"""
  IT
  """Ivory Coast"""
  CI
  """Jamaica"""
  JM
  """Japan"""
  JP
  """Jordan"""
  JO
  """Kazakhstan"""
  KZ
  """Kenya"""
  KE
  """Kiribati"""
  KI
  """Korea, Democratic People's Republic of"""
  KP
  """Korea, Republic of"""
  KR
  """Kuwait"""
  KW
  """Kyrgyzstan"""
  KG
  """Lao People's Democratic Republic"""
  LA
  """Latvia"""
  LV
  """Lebanon"""
  LB
  """Lesotho"""
  LS
  """Liberia"""
  LR
  """Libyan Arab Jamahiriya"""
  LY
  """Liechtenstein"""
  LI
  """Lithuania"""
  LT
  """Luxembourg"""
  LU
  """Macau"""
  MO
  """Macedonia"""
  MK
  """Madagascar"""
  MG
  """Malawi"""
  MW
  """Malaysia"""
  MY
  """Maldives"""
  MV
  """Mali"""
  ML
  """Malta"""
  MT
  """Marshall Islands"""
  MH
  """Martinique"""
  MQ
  """Mauritania"""
  MR
  """Mauritius"""
  MU
  """Mayotte"""
  TY
  """Mexico"""
  MX
  """Micronesia, Federated States of"""
  FM
  """Moldova, Republic of"""
  MD
  """Monaco"""
  MC
  """Mongolia"""
  MN
  """Montserrat"""
  MS
  """Morocco"""
  MA
  """Mozambique"""
  MZ
  """Myanmar"""
  MM
  """Namibia"""
  NA
  """Nauru"""
  NR
  """Nepal"""
  NP
  """Netherlands"""
  NL
  """Netherlands Antilles"""
  AN
  """New Caledonia"""
  NC
  """New Zealand"""
  NZ
  """Nicaragua"""
  NI
  """Niger"""
  NE
  """Nigeria"""
  NG
  """Niue"""
  NU
  """Norfork Island"""
  NF
  """Norway"""
  NO
  """Oman"""
  OM
  """Pakistan"""
  PK
  """Palau"""
  PW
  """Panama"""
  PA
  """Papua New Guinea"""
  PG
  """Paraguay"""
  PY
  """Peru"""
  PE
  """Philippines"""
  PH
  """Pitcairn"""
  PN
  """Poland"""
  PL
  """Portugal"""
  PT
  """Puerto Rico"""
  PR
  """Qatar"""
  QA
  """Reunion"""
  RE
  """Romania"""
  RO
  """Russian Federation"""
  RU
  """Rwanda"""
  RW
  """Saint Kitts and Nevis"""
  KN
  """Saint Lucia"""
  LC
  """Saint Vincent and the Grenadines"""
  VC
  """Samoa"""
  WS
  """San Marino"""
  SM
  """Sao Tome and Principe"""
  ST
  """Saudi Arabia"""
  SA
  """Senegal"""
  SN
  """Serbia"""
  RS
  """Seychelles"""
  SC
  """Sierra Leone"""
  SL
  """Singapore"""
  SG
  """Slovakia"""
  SK
  """Slovenia"""
  SI
  """Solomon Islands"""
  SB
  """Somalia"""
  SO
  """South Africa"""
  ZA
  """South Georgia South Sandwich Islands"""
  GS
  """Spain"""
  ES
  """Sri Lanka"""
  LK
  """St. Helena"""
  SH
  """St. Pierre and Miquelon"""
  PM
  """Sudan"""
  SD
  """Suriname"""
  SR
  """Svalbard and Jan Mayen Islands"""
  SJ
  """Swaziland"""
  SZ
  """Sweden"""
  SE
  """Switzerland"""
  CH
  """Syrian Arab Republic"""
  SY
  """Taiwan"""
  TW
  """Tajikistan"""
  TJ
  """Tanzania, United Republic of"""
  TZ
  """Thailand"""
  TH
  """Togo"""
  TG
  """Tokelau"""
  TK
  """Tonga"""
  TO
  """Trinidad and Tobago"""
  TT
  """Tunisia"""
  TN
  """Turkey"""
  TR
  """Turkmenistan"""
  TM
  """Turks and Caicos Islands"""
  TC
  """Tuvalu"""
  TV
  """Uganda"""
  UG
  """Ukraine"""
  UA
  """United Arab Emirates"""
  AE
  """United Kingdom"""
  GB
  """Uruguay"""
  UY
  """Uzbekistan"""
  UZ
  """Vanuatu"""
  VU
  """Vatican City State"""
  VA
  """Venezuela"""
  VE
  """Vietnam"""
  VN
  """Virgin Islands (British)"""
  VG
  """Wallis and Futuna Islands"""
  WF
  """Western Sahara"""
  EH
  """Yemen"""
  YE
  """Yugoslavia"""
  YU
  """Zaire"""
  ZR
  """Zambia"""
  ZM
  """Zimbabwe"""
  ZW
}

"""A type of currency."""
enum Currency {
  """UAE Dirham"""
  AED
  """Afghani"""
  AFN
  """Lek"""
  ALL
  """Armenian Dram"""
  AMD
  """Netherlands Antillean Guilder"""
  ANG
  """Kwanza"""
  AOA
  """Argentine Peso"""
  ARS
  """Australian Dollar"""
  AUD
  """Aruban Florin"""
  AWG
  """Azerbaijan Manat"""
  AZN
  """Convertible Mark"""
  BAM
  """Barbados Dollar"""
  BBD
  """Taka"""
  BDT
  """Bulgarian Lev"""
  BGN
  """Bermudian Dollar"""
  BMD
  """Brunei Dollar"""
  BND
  """Boliviano"""
  BOB
  """Brazilian Real"""
  BRL
  """Bahamian Dollar"""
  BSD
  """Ngultrum"""
  BTN
  """Pula"""
  BWP
  """Belarusian Ruble"""
  BYN
  """Belize Dollar"""
  BZD
  """Canadian Dollar"""
  CAD
  """Congolese Franc"""
  CDF
  """Swiss Franc"""
  CHF
  """Yuan Renminbi"""
  CNY
  """Colombian Peso"""
  COP
  """Costa Rican Colon"""
  CRC
  """Peso Convertible"""
  CUC
  """Cuban Peso"""
  CUP
  """Cabo Verde Escudo"""
  CVE
  """Czech Koruna"""
  CZK
  """Danish Krone"""
  DKK
  """Dominican Peso"""
  DOP
  """Algerian Dinar"""
  DZD
  """Egyptian Pound"""
  EGP
  """Nakfa"""
  ERN
  """Ethiopian Birr"""
  ETB
  """Euro"""
  EUR
  """Fiji Dollar"""
  FJD
  """Falkland Islands Pound"""
  FKP
  """Pound Sterling"""
  GBP
  """Lari"""
  GEL
  """Ghana Cedi"""
  GHS
  """Gibraltar Pound"""
  GIP
  """Dalasi"""
  GMD
  """Quetzal"""
  GTQ
  """Hong Kong Dollar"""
  HKD
  """Lempira"""
  HNL
  """Gourde"""
  HTG
  """Forint"""
  HUF
  """Rupiah"""
  IDR
  """New Israeli Sheqel"""
  ILS
  """Indian Rupee"""
  INR
  """Iranian Rial"""
  IRR
  """Jamaican Dollar"""
  JMD
  """Kenyan Shilling"""
  KES
  """Som"""
  KGS
  """Riel"""
  KHR
  """North Korean Won"""
  KPW
  """Cayman Islands Dollar"""
  KYD
  """Tenge"""
  KZT
  """Lao Kip"""
  LAK
  """Lebanese Pound"""
  LBP
  """Sri Lanka Rupee"""
  LKR
  """Liberian Dollar"""
  LRD
  """Loti"""
  LSL
  """Moroccan Dirham"""
  MAD
  """Moldovan Leu"""
  MDL
  """Malagasy Ariary"""
  MGA
  """Denar"""
  MKD
  """Kyat"""
  MMK
  """Tugrik"""
  MNT
  """Pataca"""
  MOP
  """Ouguiya"""
  MRU
  """Mauritius Rupee"""
  MUR
  """Rufiyaa"""
  MVR
  """Malawi Kwacha"""
  MWK
  """Mexican Peso"""
  MXN
  """Malaysian Ringgit"""
  MYR
  """Mozambique Metical"""
  MZN
  """Namibia Dollar"""
  NAD
  """Naira"""
  NGN
  """Cordoba Oro"""
  NIO
  """Norwegian Krone"""
  NOK
  """Nepalese Rupee"""
  NPR
  """New Zealand Dollar"""
  NZD
  """Balboa"""
  PAB
  """Sol"""
  PEN
  """Kina"""
  PGK
  """Philippine Peso"""
  PHP
  """Pakistan Rupee"""
  PKR
  """Zloty"""
  PLN
  """Qatari Rial"""
  QAR
  """Romanian Leu"""
  RON
  """Serbian Dinar"""
  RSD
  """Russian Ruble"""
  RUB
  """Saudi Riyal"""
  SAR
  """Solomon Islands Dollar"""
  SBD
  """Seychelles Rupee"""
  SCR
  """Sudanese Pound"""
  SDG
  """Swedish Krona"""
  SEK
  """Singapore Dollar"""
  SGD
  """Saint Helena Pound"""
  SHP
  """Leone"""
  SLL
  """Somali Shilling"""
  SOS
  """Surinam Dollar"""
  SRD
  """South Sudanese Pound"""
  SSP
  """Dobra"""
  STN
  """El Salvador Colon"""
  SVC
  """Syrian Pound"""
  SYP
  """Lilangeni"""
  SZL
  """Baht"""
  THB
  """Somoni"""
  TJS
  """Turkmenistan New Manat"""
  TMT
  """Pa’anga"""
  TOP
  """Turkish Lira"""
  TRY
  """Trinidad and Tobago Dollar"""
  TTD
  """New Taiwan Dollar"""
  TWD
  """Tanzanian Shilling"""
  TZS
  """Hryvnia"""
  UAH
  """US Dollar"""
  USD
  """Peso Uruguayo"""
  UYU
  """Uzbekistan Sum"""
  UZS
  """Bolívar Soberano"""
  VES
  """Tala"""
  WST
  """East Caribbean Dollar"""
  XCD
  """Yemeni Rial"""
  YER
  """Rand"""
  ZAR
  """Zambian Kwacha"""
  ZMW
  """Zimbabwe Dollar"""
  ZWL
}

"""A day of the week."""
enum Day {
  """Sunday."""
  SUNDAY
  """Monday."""
  MONDAY
  """Tuesday."""
  TUESDAY
  """Wednesday."""
  WEDNESDAY
  """Thursday."""
  THURSDAY
  """Friday."""
  FRIDAY
  """Saturday."""
  SATURDAY
}

"""A simple icon, used in the user interface for quick identification."""
enum Icon {
  """Activity, Pulse"""
  ACTIVITY759902
  """Add, New, Insert"""
  ADD759610
  """Alarm, Add, Notification"""
  ADDALARM759611
  """Cart, Add, Shopping"""
  ADDCART759856
  """Add, Document"""
  ADDFILE759478
  """Inbox, Add, Mailbox"""
  ADDINBOX759799
  """Calendar, Add, Date"""
  ADDMEETING759787
  """Airplane, Plane, Travel"""
  AIRPLANE759930
  """Airplay"""
  AIRPLAY759822
  """Alarm, Clock, Time"""
  ALARM759357
  """Alarm, Notification, Time"""
  ALARM759615
  """Alert, Warning"""
  ALERT759619
  """Anchor"""
  ANCHOR759433
  """Broadcast, Tower, Antenna"""
  ANTENNA759818
  """Apple, Fruit, Healthy"""
  APPLE759516
  """App, Store"""
  APPSTORE759879
  """Artboard"""
  ARTBOARD759449
  """Artwork, Frame, Hanging"""
  ARTWORK759814
  """Nuclear, Energy, Atom"""
  ATOM759499
  """Attachment, Clip"""
  ATTACHMENT759782
  """Medicine, Bowl, Ayurveda"""
  AYURVEDA759572
  """Backward, Right, Navigation"""
  BACKWARD759406
  """Bandaid, Bandage, Medical"""
  BANDAID759557
  """Bandaids, Bandage, Medicine"""
  BANDAIDS759559
  """Bank"""
  BANK759322
  """Bank"""
  BANK759324
  """Money, Banknote"""
  BANKNOTE759344
  """Barcode, Product, Identification"""
  BARCODE759851
  """Baseball, Bat, Game"""
  BASEBALL759306
  """Baseball, Ball, Game"""
  BASEBALL759307
  """Picnic, Basket"""
  BASKET759535
  """Basketball, Ball, Game"""
  BASKETBALL759305
  """Battery, Charge, Hardware"""
  BATTERY759620
  """Battery, Full, Hardware"""
  BATTERY759621
  """Battery, Empty, Hardware"""
  BATTERY759622
  """Battery, Half, Hardware"""
  BATTERY759624
  """Battery, Time, Timeout"""
  BATTERYTIMEOUT759627
  """Bikini, Bra, Undergarment"""
  BIKINI759423
  """Birdhouse, House"""
  BIRDHOUSE759900
  """Bits, Binary, Number"""
  BITS759671
  """Blocks, Alphabet"""
  BLOCKS759663
  """Boarding, Pass, Travel"""
  BOARDINGPASS759428
  """Dog, Bone, Pet"""
  BONE759579
  """Reading, Book, Education"""
  BOOK759649
  """Book, Education, Learning"""
  BOOK759652
  """Tag, Label, Bookmark"""
  BOOKMARK759901
  """Star, Folder, Collection"""
  BOOKMARKFOLDER759475
  """Bookmarks, Book, Read"""
  BOOKMARKS759905
  """Library, Book, Study"""
  BOOKS759654
  """Bowling, Ball, Game"""
  BOWLING759308
  """Project, Box"""
  BOX759780
  """Brainpower, Brainstorming, Thinking"""
  BRAINPOWER759651
  """Bread, Breakfast"""
  BREAD759509
  """Briefcase"""
  BRIEFCASE759327
  """Brightness, Interface, User"""
  BRIGHTNESS759816
  """Broken, Bone"""
  BROKENBONE759560
  """Paintbrush, Brush, Tool"""
  BRUSH759464
  """Bug, Virus"""
  BUG759666
  """Bullhorn, Megaphone, Advertising"""
  BULLHORN759326
  """Bullhorn, Megaphone, Advertising"""
  BULLHORN759328
  """Burger, Food, Breakfast"""
  BURGER759511
  """Bus, Transport, Vehicle"""
  BUS759933
  """Butterfly, Insect"""
  BUTTERFLY759506
  """Button"""
  BUTTON759587
  """Buttons, Large, Menu"""
  BUTTONS759623
  """Buttons, Medium, Menu"""
  BUTTONS759625
  """Buttons, Small, Menu"""
  BUTTONS759626
  """Plus, Minus, Calculation"""
  CALCULATION759351
  """Math, Calculation"""
  CALCULATION759650
  """Calculator"""
  CALCULATOR759329
  """Calendar, Available, Schedule"""
  CALENDAR759785
  """Calendar, Unavailable, Schedule"""
  CALENDAR759786
  """Calendar, Schedule, Date"""
  CALENDAR759789
  """Service, Call, Helpline"""
  CALLSERVICE759877
  """Camera, Photography, Device"""
  CAMERA759819
  """Flip, Camera, Rotate"""
  CAMERA759827
  """Campfire, Bonfire, Fire"""
  CAMPFIRE759431
  """Car, Transport, Vehicle"""
  CAR759939
  """Car, Battery, Automobile"""
  CARBATTERY759507
  """Carrot"""
  CARROT759522
  """Cash, Money, Finance"""
  CASH759858
  """Bookcase, Speaker, Cd"""
  CD759817
  """Center, Align, Text"""
  CENTERALIGN759450
  """Certified, Badge, Sticker"""
  CERTIFIED759330
  """Chalkboard, Study, Board"""
  CHALKBOARD759656
  """Plug, Charging, Energy"""
  CHARGING759502
  """Chat, Chatting, Message"""
  CHAT759903
  """Chat, Chatting, Message"""
  CHAT759911
  """Ask, Question, Chat"""
  CHATTING759878
  """Chat, Quote, Chatting"""
  CHATTING759910
  """Checkmark, Box, Checkbox"""
  CHECKBOX759793
  """Checkmark, Accept, Verify"""
  CHECKMARK759628
  """Checkmark, Accept, Verify"""
  CHECKMARK759790
  """Checkmark, Document, Collection"""
  CHECKMARKFILE759479
  """Chef, Hat"""
  CHEFHAT759517
  """Chopsticks"""
  CHOPSTICKS759512
  """Circle"""
  CIRCLE
  """Clipboard"""
  CLIPBOARD759451
  """Clipboard, Todo, Task"""
  CLIPBOARD759792
  """Clock, Time, Watch"""
  CLOCK759361
  """Cloud, Weather"""
  CLOUD759379
  """Code"""
  CODE759439
  """Code, Coding, Development"""
  CODE759452
  """Html, Doc, Coding"""
  CODING759461
  """Coffee, Mug, Cup"""
  COFFEEMUG759528
  """Coin, Cash, Dollar"""
  COIN759333
  """Coins, Money, Finance"""
  COINS759335
  """Command, Line, Coding"""
  COMMANDLINE759678
  """Safari, Compass"""
  COMPASS759373
  """Computer, Device, Monitor"""
  COMPUTER759675
  """Computer, Device"""
  COMPUTER759681
  """Contacts, Star, Book"""
  CONTACTBOOK759907
  """Contacts, Contact, Book"""
  CONTACTBOOK759912
  """Control, Pad, Navigation"""
  CONTROL759629
  """Corkscrew"""
  CORKSCREW759519
  """Credit, Card, Debit"""
  CREDITCARD759860
  """Crop"""
  CROP759453
  """Crown, King, Royal"""
  CROWN759585
  """Bike, Transportation, Cycle"""
  CYCLE759927
  """Cyclist, Cycling, Cycle"""
  CYCLIST759938
  """Network, Activity, Data"""
  DATATRANSFER759687
  """Network, Activity, Data"""
  DATATRANSFER759688
  """Delete, Document, File"""
  DELETEFILE759481
  """Delete, Tag, Label"""
  DELETELABEL759630
  """Delivery, Truck, Transport"""
  DELIVERYTRUCK759853
  """Desk, Lamp, Light"""
  DESKLAMP759794
  """Diamond"""
  DIAMOND759334
  """Diamond, Ring"""
  DIAMONDRING759591
  """Dice, Gambling"""
  DICE759284
  """Fork, Direction, Path"""
  DIRECTION759919
  """Directions, Direction, Board"""
  DIRECTIONBOARD759934
  """Percent, Discount"""
  DISCOUNT759347
  """Dislike, Thumbs, Down"""
  DISLIKE759913
  """Dna, Genetics"""
  DNA759561
  """Document, File"""
  DOCUMENT759480
  """Dog, Collar"""
  DOGCOLLAR759580
  """Dog, Food, Bowl"""
  DOGFOOD759583
  """Dollar, Euro"""
  DOLLAR759336
  """Dollar, Sign"""
  DOLLAR759337
  """Do, Not, Disturb"""
  DONOTDISTURB759676
  """Door, Open, Entry"""
  DOOR759631
  """Door, Entry, Gate"""
  DOOR759636
  """Down, Navigation, Direction"""
  DOWN759409
  """Down, Arrow, Direction"""
  DOWNARROW759403
  """Download, File, Down"""
  DOWNLOAD759677
  """Download, Hd, Hard-disk"""
  DOWNLOAD759685
  """Download"""
  DOWNLOAD759861
  """Book, Download, School"""
  DOWNLOADBOOK759665
  """Download, Folder, Collection"""
  DOWNLOADFOLDER759482
  """Cloud, Download, Storage"""
  DOWNLOADFROMCLOUD759667
  """Inbox, Mail, Message"""
  DOWNLOADINBOX759801
  """Navigate, Down"""
  DOWNNAVIGATE759415
  """File, Drawer, Document"""
  DRAWER759795
  """File, Cabinet"""
  DRAWER759797
  """Dress, Fashion, Woman"""
  DRESS759581
  """Drink, Glass, Water"""
  DRINK759521
  """Drumstick, Chicken, Leg"""
  DRUMSTICK759523
  """Fitness, Dumbbell, Gym"""
  DUMBBELL759562
  """Wastebasket, Basket, Dustbin"""
  DUSTBIN759783
  """Earth, Globe, Planet"""
  EARTH759508
  """Egg, Food, Boil"""
  EGG759520
  """Eject, Sign"""
  EJECT759823
  """Elevator, Direction, Arrow"""
  ELEVATORSIGN759401
  """Email, Message, Mail"""
  EMAIL759362
  """Enter, Entry, Login"""
  ENTER759632
  """Eraser"""
  ERASER759455
  """Exit, Signout"""
  EXIT759634
  """Zoom, Screen"""
  EXPAND759614
  """Red, Eye, Filter"""
  EYE759847
  """Eyedropper, Dropper, Tool"""
  EYEDROPPER759456
  """Factory, Industry, Plant"""
  FACTORY759338
  """In, Love, Face"""
  FALLINLOVE759888
  """Fan"""
  FAN759584
  """Fast, Forward, Sign"""
  FASTFORWARD759820
  """Favorites, Folder, Collection"""
  FAVORITEFOLDER759470
  """Contacts, Favorites, Book"""
  FAVOURITEBOOK759906
  """Chat, Heart, Chatting"""
  FAVOURITEMESSAGE759909
  """Compose, Tweet, Quill"""
  FEATHER759904
  """Female, Symbol, Gender"""
  FEMALEGENDER759563
  """Film, Roll, Video"""
  FILM759825
  """Filmstrip, Movie, Film"""
  FILMSTRIP759826
  """Find, Home, Estate"""
  FINDESTATE759598
  """Fingerprint, Scan, Biometric"""
  FINGERPRINT759679
  """Fire, Escape, Stair"""
  FIREESCAPE759405
  """Medical, Bag, First-aid"""
  FIRSTAIDBAG759569
  """Heart, Monitor, Fitness"""
  FITNESSTRACKER759564
  """Pennant, Flag, Checkpoint"""
  FLAG759300
  """Flag"""
  FLAG759796
  """Torch, Flame, Fire"""
  FLAME759301
  """Flashlight, Torch, Light"""
  FLASHLIGHT759582
  """Beaker, Flask, Science"""
  FLASK759664
  """Flight, Departure, Plane"""
  FLIGHTDEPARTURE759430
  """Airplane, Mode, Flight"""
  FLIGHTMODE759603
  """Flower, Nature"""
  FLOWER759483
  """Folder, Collection"""
  FOLDER759468
  """Font, Size, Text"""
  FONT759635
  """Fonts, Folder, Collection"""
  FONTSFOLDER759471
  """Football, Rugby, Ball"""
  FOOTBALL759286
  """Soccer, Player, Football"""
  FOOTBALL759295
  """Sports, Field, Football"""
  FOOTBALLGROUND759290
  """Forward, Left, Direction"""
  FORWARD759402
  """Navigate, Forward, Navigation"""
  FORWARDNAVIGATION759411
  """Fries, French, Food"""
  FRENCHFRIES759525
  """Fried, Egg, Food"""
  FRIEDEGG759527
  """Pan, Frying"""
  FRYINGPAN759537
  """Hours, Fullday, Service"""
  FULLDAYSERVICE759323
  """Effects, Function"""
  FUNCTION759821
  """Gauge, Performance, Speedometer"""
  GAUGE759486
  """Passcode, Gesture, Touchpad"""
  GESTURE759693
  """Gift, Present"""
  GIFT759915
  """Gift, Certificate, Giftcard"""
  GIFTCARD759863
  """Glasses"""
  GLASSES759800
  """Globe"""
  GLOBE759339
  """Globe, Web, World"""
  GLOBE759358
  """Oven, Mitt, Gloves"""
  GLOVES759533
  """Golf, Game, Sport"""
  GOLF759287
  """Education, School, Graduate"""
  GRADUATE759653
  """Grapes, Fruit"""
  GRAPES759524
  """Bar, Graph, Chart"""
  GRAPH759325
  """Grass, Plant"""
  GRASS759487
  """Grater"""
  GRATER759531
  """Grid, Large"""
  GRID759638
  """Grid, Medium"""
  GRID759639
  """Grid, Small"""
  GRID759640
  """Grill, Tandoor, Cooking"""
  GRILL759529
  """Hamburger, Menu, List"""
  HAMBURGERMENU759641
  """Hand, Palm, Gesture"""
  HAND759457
  """Raised, Hand, Gesture"""
  HAND759655
  """Hand, Truck, Hand-truck"""
  HANDTRUCK759862
  """Hanger"""
  HANGER759586
  """Happy, Face, Emoji"""
  HAPPY759916
  """Hashtag"""
  HASHTAG759917
  """Haze, Wave, Tide"""
  HAZE759380
  """Headphones, Earphone, Equipment"""
  HEADPHONES759829
  """Healthy, Heart, Heartbeat"""
  HEALTHY759565
  """Heart, Love, Valentine"""
  HEART759880
  """Heart, Add, Love"""
  HEART759914
  """Cards, Card, Gambling"""
  HEARTCARD759285
  """Heartrate, Heartbeat, Heart"""
  HEARTRATE759566
  """Hearts, Love, Valentine"""
  HEARTS759881
  """Help"""
  HELP759642
  """Hide, Eye, Vision"""
  HIDE759643
  """Hide, Keyboard, Interface"""
  HIDEKEYBOARD759644
  """Temp, Increase, Temperature"""
  HIGHTEMPERATURE759394
  """Volume, High, Sound"""
  HIGHVOLUME759811
  """Hockey, Game, Sport"""
  HOCKEY759288
  """Hospital, Medical, Plus"""
  HOSPITALSIGN759567
  """Temp, Drop, Temperature"""
  HOT759393
  """Hot, Fire, Flame"""
  HOT759865
  """Hourglass, Sandclock, Time"""
  HOURGLASS759645
  """House, Home, Building"""
  HOUSE759590
  """Id, Card, Identification"""
  IDCARD759798
  """Light, Bulb"""
  IDEA759340
  """Employee, Id, Identification"""
  IDENTIFICATIONCARD759341
  """Gallery"""
  IMAGEFRAME759828
  """Inbox, Email, Message"""
  INBOX759791
  """Inbox, Todo"""
  INBOX759803
  """Inboxes, Mail"""
  INBOXES759802
  """Incoming, Call, Communication"""
  INCOMINGCALL759363
  """Syringe, Injection"""
  INJECTION759553
  """Invoice, Bill, Report"""
  INVOICE759342
  """Invoice, Bill, Receipt"""
  INVOICE759867
  """Island, Beach, Tree"""
  ISLAND759429
  """Jersey, Player, Sport"""
  JERSEY759299
  """Key, Secure, Lock"""
  KEY759683
  """Show, Keyboard, Typing"""
  KEYBOARD759602
  """Keyboard, Typing"""
  KEYBOARD759684
  """Keyhole, Security, Privacy"""
  KEYHOLE759682
  """Keypad"""
  KEYPAD759364
  """Chess, Horse, Knight"""
  KNIGHT759281
  """Lady, Bug, Ladybug"""
  LADYBUG759490
  """Flight, Arrival, Plane"""
  LANDINGFLIGHT759432
  """Landscape, Picture, Image"""
  LANDSCAPE759830
  """Laptop, Device"""
  LAPTOP759689
  """Layers, Stack, Tool"""
  LAYERS759458
  """Leaf, Nature, Ecology"""
  LEAF759492
  """Leaf, Nature, Ecology"""
  LEAF759494
  """Left, Align, Text"""
  LEFTALIGN759459
  """Left, Arrow, Direction"""
  LEFTARROW759404
  """Left, Down, Arrow"""
  LEFTARROW759407
  """Navigate, Back, Direction"""
  LEFTNAVIGATION759419
  """Left, Up, Arrow"""
  LEFTUPARROW759410
  """Lego, Robot"""
  LEGO759657
  """Lens"""
  LENS759832
  """Lightbulb, Light, Bulb"""
  LIGHTBULB759491
  """Lightbulb, Cfl, Led"""
  LIGHTBULB759493
  """Like, Thumbs, Up"""
  LIKE759882
  """Link"""
  LINK759365
  """List, Document, File"""
  LIST759473
  """Bullet, List"""
  LIST759788
  """Location, Pin, Navigation"""
  LOCATIONPIN759883
  """Lock, Security, Protection"""
  LOCK759686
  """Phone, Secure, Lock"""
  LOCKPHONE759690
  """Loss, Down, Graph"""
  LOSS759310
  """Loupe, Search, Magnifying"""
  LOUPE759460
  """Volume, Low, Sound"""
  LOWVOLUME759807
  """Loyalty, Card, Discount"""
  LOYALTYCARD759864
  """Auto, Correct, Magic"""
  MAGICWAND759815
  """Magnet, Attraction"""
  MAGNET759592
  """Mail, Email, Message"""
  MAIL759367
  """At, Symbol, Mail"""
  MAILSIGN759899
  """Male, Symbol, Gender"""
  MALEGENDER759571
  """Pirate, Map, Navigation"""
  MAP759920
  """Map, Street, Location"""
  MAP759932
  """Map, Location, Navigation"""
  MAP759937
  """Marijuana, Leaf, Ayurveda"""
  MARIJUANA759568
  """Full, Screen, Maximize"""
  MAXIMIZE759637
  """Measuring, Cup, Jar"""
  MEASURINGCUP759530
  """Medal, Award"""
  MEDAL759291
  """Medical, Symbol, Sign"""
  MEDICALSIGN759575
  """Microphone, Mic, Record"""
  MICROPHONE759831
  """Microphone, Mic, Record"""
  MICROPHONE759833
  """Exit, Full, Screen"""
  MINIMIZE759633
  """Minimize, Screen"""
  MINIMIZE759647
  """Mixer, Adjustment, Control"""
  MIXER759836
  """Nest, Egg, Money"""
  MONEY759345
  """Money, Bag, Finance"""
  MONEYBAG759343
  """Clean, Mop"""
  MOP759673
  """Move, Select"""
  MOVE759646
  """Mug, Heart, Coffee"""
  MUG759805
  """Music, Note, Tune"""
  MUSIC759838
  """Music, Collection, Album"""
  MUSICALBUM759835
  """Music, Folder, Collection"""
  MUSICFOLDER759469
  """Mute, Sound, Volume"""
  MUTE759840
  """Landscape, Nature, Mountainside"""
  NATURE759489
  """Navigation, Alt, Direction"""
  NAVIGATION759922
  """Navigation, Direction, Pin"""
  NAVIGATION759923
  """Network, Hierarchy"""
  NETWORK759366
  """Neutral, Face, Emoji"""
  NEUTRALFACE759889
  """New, Badge, Sticker"""
  NEW759866
  """News, Newspaper, Media"""
  NEWS759890
  """Night, Moon, Star"""
  NIGHT759381
  """Night, Time, Mode"""
  NIGHTMODE759837
  """No, Entry, Sign"""
  NOENTRY759924
  """North, Arrow, Direction"""
  NORTHDIRECTION759422
  """Notifications"""
  NOTIFICATIONS759368
  """Business, Office"""
  OFFICE759331
  """Phone, Off, Communication"""
  OFFPHONE759370
  """Olive"""
  OLIVE759532
  """Onesy, Baby, Jumper"""
  ONESY759589
  """Orange, Fruit"""
  ORANGE759536
  """Outbox, Mailbox, Mail"""
  OUTBOX759804
  """Outgoing, Call, Phone"""
  OUTGOINGCALL759369
  """Oven, Kitchen, Appliance"""
  OVEN759534
  """Package, Delivery, Box"""
  PACKAGE759855
  """Paintbrush, Paint, Brush"""
  PAINTBRUSH759463
  """Paint, Roller"""
  PAINTROLLER759462
  """Palette, Color"""
  PALETTE759465
  """Shredder, Paper, Hardware"""
  PAPERSHREDDER759781
  """Download, Product, Parcel"""
  PARCEL759859
  """Partly, Sunny, Cloud"""
  PARTLYSUNNY759385
  """Passport, Visa, Document"""
  PASSPORT759427
  """Pause, Control, Music"""
  PAUSE759839
  """Chess, Pawn, Game"""
  PAWN759282
  """Peace, Sign, Symbol"""
  PEACE759597
  """Pen"""
  PEN759346
  """Pen"""
  PEN759466
  """Pencil, Design, Tool"""
  PENCIL759467
  """Gas, Pump, Petrol"""
  PETROLPUMP759485
  """Phone, Communication, Call"""
  PHONE759371
  """Phone, Ringing, Communication"""
  PHONE759372
  """Cell, Tower, Phone"""
  PHONESIGNAL759360
  """Photobook, Scrape, Book"""
  PHOTOBOOK759841
  """Photos, Album, Photo"""
  PHOTOS759842
  """Piano, Music, Instrument"""
  PIANO759843
  """Picnic, Table, Bench"""
  PICNICBENCH759538
  """Chart, Pie-chart, Graph"""
  PIECHART759348
  """Chart, Pie-chart, Graph"""
  PIECHART759349
  """Piggy, Bank"""
  PIGGYBANKING759350
  """Pill, Medicine, Medical"""
  PILL759573
  """Pills, Medicine"""
  PILLS759574
  """Pingpong, Ping, Pong"""
  PINGPONG759292
  """Pizza, Food"""
  PIZZA759539
  """Play, Music, Player"""
  PLAY759844
  """Plug, Cable, Power"""
  PLUG759498
  """Pocket, Knife, Tool"""
  POCKETKNIFE759425
  """Podium, Speaker"""
  PODIUM759352
  """Pointer, Up"""
  POINTING759416
  """Pointer, Right, Direction"""
  POINTING759418
  """Poop"""
  POOP759596
  """Popsicle, Candy, Ice-cream"""
  POPSICLE759540
  """Portfolio"""
  PORTFOLIO759353
  """Portrait, Image, Picture"""
  PORTRAIT759845
  """Standings, Podium, Position"""
  POSITION759297
  """Power, On, Off"""
  POWER759692
  """Preferences"""
  PREFERENCES759599
  """Presentation, Board"""
  PRESENTATIONBOARD759309
  """Presentation, Chart, Board"""
  PRESENTATIONBOARD759354
  """Price, Tag, Label"""
  PRICETAG759854
  """Print, Printer, Device"""
  PRINTER759774
  """Print, Printer, Device"""
  PRINTER759775
  """Printer, Device, Equipment"""
  PRINTER759776
  """Privacy, Fence, Security"""
  PRIVACY759694
  """Profile, User"""
  PROFILE759885
  """Profit, Up, Graph"""
  PROFIT759311
  """Profit, Up, Graph"""
  PROFIT759313
  """Stock, Profit, Up"""
  PROFIT759317
  """Puzzle, Piece"""
  PUZZLE759314
  """Quote"""
  QUOTE759434
  """Quote"""
  QUOTE759435
  """Radio, Fm"""
  RADIO759846
  """Rain, Water, Drip"""
  RAIN759382
  """Rain, Cloud, Water"""
  RAIN759386
  """Rating, Half"""
  RATING759886
  """Rating, Review, Feedback"""
  RATING759891
  """Ratings, Review, Feedback"""
  RATINGS759893
  """Reading, Book, Education"""
  READING759658
  """Receipt, Bill, Invoice"""
  RECEIPT759868
  """Voice, Assistant, Sound"""
  RECORDING759808
  """Refresh, Reload"""
  REFRESH759600
  """Cloud, Refresh, Reload"""
  REFRESHCLOUD759670
  """Cart, Remove, Shopping"""
  REMOVECART759857
  """Medical, Chart, Report"""
  REPORT759570
  """Restaurant, Cutlery, Sign"""
  RESTAURANT759541
  """Restaurant, Alt, Cutlery"""
  RESTAURANT759542
  """Restaurant, Cutlery, Sign"""
  RESTAURANTSIGN759544
  """Restricted, Ban, Block"""
  RESTRICTED759695
  """Ribbon, Aids"""
  RIBBON759576
  """Right, Align, Text"""
  RIGHTALIGN759438
  """Right, Arrow, Direction"""
  RIGHTARROW759412
  """Right, Down, Arrow"""
  RIGHTDOWNARROW759413
  """Road, Traffic, Direction"""
  ROAD759935
  """Chess, Rook, Game"""
  ROOK759283
  """Route, Navigation, Location"""
  ROUTE759577
  """Router, Modem"""
  ROUTER759696
  """Ruler"""
  RULER759436
  """Rulers, Tool, Scale"""
  RULERS759440
  """Running, Exercise, Health"""
  RUNNING759578
  """Sad, Face, Emoji"""
  SAD759894
  """Sale, Badge, Sticker"""
  SALE759869
  """Sandals, Flipflop"""
  SANDALS759426
  """Sat, Dish, Satellite"""
  SATELLITE759374
  """Scales, Balance, Justice"""
  SCALES759315
  """Cut, Scissor"""
  SCISSOR759454
  """Search, Tool, Zoom"""
  SEARCH759604
  """Cloud, Secure, Lock"""
  SECURECLOUD759668
  """Computer, Secure, Device"""
  SECURECOMPUTER759680
  """Locked, Folder, Collection"""
  SECUREFOLDER759474
  """Secure, Home, House"""
  SECUREHOME759595
  """Phone, Secure, Lock"""
  SECUREPHONE759691
  """Seeds, Gardening, Garden"""
  SEEDS759496
  """Send, Mail, Communication"""
  SENDMAIL759375
  """Servers, Hard-disk, Database"""
  SERVERS759697
  """Settings, Optimization, Preferences"""
  SETTINGS759601
  """Share"""
  SHARE759607
  """Share, Data, File"""
  SHARE759617
  """Team, Share"""
  SHARE759777
  """Network, Share, Communication"""
  SHARE759884
  """Shield, Security, Protection"""
  SHIELD759698
  """Shocked, Face, Emoji"""
  SHOCKEDFACE759892
  """Shooting, Star"""
  SHOOTINGSTAR759383
  """Shop, Shopping, Store"""
  SHOPPING759871
  """Shopping, Bag, Handbag"""
  SHOPPINGBAG759872
  """Shopping, Tote, Bag"""
  SHOPPINGBAG759874
  """Shopping, Bag, Heart"""
  SHOPPINGBAG759875
  """Shopping, Basket, Wishlist"""
  SHOPPINGBASKET759873
  """Cart, Shopping, Ecommerce"""
  SHOPPINGCART759852
  """Secure, Shield, Shopping"""
  SHOPPINGINSURANCE759870
  """Signature"""
  SIGNATURE759316
  """Alarm, Silent, Mute"""
  SILENT759616
  """Skull, Ghost"""
  SKULL759547
  """Sleep, Sleeping"""
  SLEEP759552
  """Smartphone, Phone, Mobile"""
  SMARTPHONE759701
  """Smartwatch, Wristwatch, Time"""
  SMARTWATCH759376
  """Alarm, Snooze, Notification"""
  SNOOZEALARM759618
  """Snow, Snowfall, Weather"""
  SNOWFALL759387
  """Snowflake"""
  SNOWFLAKE759384
  """Softdrink, Cup, Drink"""
  SOFTDRINK759545
  """Solar, Panel, Energy"""
  SOLARPANEL759497
  """Sound, Wave"""
  SOUNDWAVE759848
  """Soup, Bowl"""
  SOUP759543
  """Spatula, Tool, Kitchen"""
  SPATULA759546
  """Speaker, Music, Sound"""
  SPEAKER759849
  """Chat, Bolt, Speed"""
  SPEEDCHAT759908
  """Splat, Splash"""
  SPLAT759441
  """Sprayer, Spray, Toolcolor"""
  SPRAY759442
  """Square"""
  SQUARE
  """Stairs, Down, Steps"""
  STAIRS759414
  """Stairs, Up"""
  STAIRS759417
  """Stamp"""
  STAMP759443
  """Star, Badge"""
  STAR759813
  """Rating, Star, Review"""
  STAR759887
  """Stars"""
  STARS759388
  """Steps, Foot, Footsteps"""
  STEPS759548
  """Stethoscope, Medical, Tool"""
  STETHOSCOPE759550
  """Post, It, Sticky"""
  STICKYNOTES759779
  """Stop, Sign, Symbol"""
  STOP759926
  """Stoplight, Traffic, Light"""
  STOPLIGHT759921
  """Strategy, Tactics"""
  STRATEGY759289
  """Chess, Piece, Strategy"""
  STRATEGY759332
  """Strawberry, Fruit, Sweet"""
  STRAWBERRY759513
  """Stroller, Baby"""
  STROLLER759876
  """Student, Study, Education"""
  STUDENT759661
  """Suitcase, Briefcase, Luggage"""
  SUITCASE759424
  """Sun, Weather, Summer"""
  SUN759389
  """Happy, Sun"""
  SUN759488
  """Sunrise, Nature"""
  SUNRISE759390
  """Sunset, Sun, Weather"""
  SUNSET759395
  """Supplies, Ruler, Tool"""
  SUPPLIES759662
  """Suv, Car, Transportation"""
  SUV759928
  """Swatch"""
  SWATCH759437
  """Swatchbook, Color, Theme"""
  SWATCHBOOK759444
  """Swimming, Sport"""
  SWIMMING759549
  """Swipe, Left, Gesture"""
  SWIPE759605
  """Off, Switch, Energy"""
  SWITCH759500
  """Switch, Electric"""
  SWITCH759501
  """On, Off, Switch"""
  SWITCH759648
  """Sword, Game"""
  SWORD759294
  """Sync, Folder, Collection"""
  SYNCFOLDER759472
  """Sync, Synchronize"""
  SYNCHRONIZE759608
  """Cloud, Sync, Synchronize"""
  SYNCHRONIZECLOUD759674
  """Tablet, Device"""
  TABLET759699
  """Tag, Label"""
  TAG759895
  """Tags, Label, Bookmark"""
  TAGS759850
  """Coffee, Cup, Takeaway"""
  TAKEAWAYCOFFEE759518
  """Tally"""
  TALLY759296
  """Target, Aim, Goal"""
  TARGET759293
  """Location, Target"""
  TARGET759918
  """Taxi, Cab"""
  TAXI759925
  """Temperature, Weather, Forecast"""
  TEMPERATURE759551
  """Tennis, Ball, Game"""
  TENNISBALL759298
  """Text, Tool, Font"""
  TEXT759445
  """Text, Document, File"""
  TEXT759476
  """Thermometer, Temperature, Weather"""
  THERMOMETER759392
  """Thermometer, Temperature"""
  THERMOMETER759396
  """Thought, Bubble, Thinking"""
  THINKING759660
  """Pin, Thumbpin"""
  THUMBPIN759778
  """Thunder, Cloud, Weather"""
  THUNDER759391
  """Lightning, Bolt, Thunder"""
  THUNDER759484
  """Tie"""
  TIE759319
  """Camera, Timer"""
  TIMER759824
  """Toolbox, Tool, Kit"""
  TOOLBOX759594
  """Tools, Construction, Repair"""
  TOOLS759700
  """Tornado, Storm"""
  TORNADO759397
  """Toy, Car, Vehicle"""
  TOYCAR759659
  """Tractor, Transport, Vehicle"""
  TRACTOR759929
  """Train, Transport, Railway"""
  TRAIN759931
  """Transfer, Up, Down"""
  TRANSFER759318
  """Trashcan, Trash, Can"""
  TRASHCAN759784
  """Tree, Pine, Nature"""
  TREE759495
  """Tree, Nature, Plant"""
  TREE759503
  """Trending, Up, Profit"""
  TRENDING759320
  """Trending, Progress, Growth"""
  TRENDING759896
  """Triangle"""
  TRIANGLE
  """Trophy, Winner, Prize"""
  TROPHY759303
  """Truck, Vehicle, Transport"""
  TRUCK759936
  """Tshirt, Cloth, Wear"""
  TSHIRT759588
  """Tweet, Social, Message"""
  TWEET759897
  """Umbrella, Protection, Safety"""
  UMBRELLA759398
  """Unlocked, Unlock, Security"""
  UNLOCK759702
  """Up, Direction, Arrow"""
  UP759400
  """Up, Right, Arrow"""
  UP759420
  """Navigate, Up, Direction"""
  UPARROW759408
  """Up, Arrow, Direction"""
  UPARROW759421
  """Upload, File, Data"""
  UPLOAD759703
  """Upload, Folder, Collection"""
  UPLOADFOLDER759477
  """Cloud, Upload, Data"""
  UPLOADTOCLOUD759669
  """Usa, Flag, Country"""
  USAFLAG759593
  """Safe, Vault, Locker"""
  VAULT759312
  """Vector, Tool"""
  VECTOR759446
  """Video, Camera, Multimedia"""
  VIDEOCAMERA759806
  """Video, Camera, Multimedia"""
  VIDEOCAMERA759809
  """Movie, Camera, Video"""
  VIDEOCAMERA759834
  """Video, Chat"""
  VIDEOCHAT759359
  """View, Eye, Filter"""
  VIEW759447
  """View, Eye, Vision"""
  VIEW759606
  """Voicemail, Record"""
  VOICEMAIL759356
  """Volleyball, Ball, Game"""
  VOLLEYBALL759302
  """Volume, Audio, Speaker"""
  VOLUME759810
  """Wallet, Purse"""
  WALLET759321
  """Water, Drop"""
  WATERDROP759504
  """Watermellon, Fruit, Sweet"""
  WATERMELLON759514
  """Camera, Video, Webcam"""
  WEBCAM759355
  """Weight, Scale, Kg"""
  WEIGHT759555
  """Food, Scale, Weight"""
  WEIGHTSCALE759526
  """Weight, Scale, Measurement"""
  WEIGHTSCALE759554
  """Wheelchair, Active, Disabled"""
  WHEELCHAIR759556
  """Whistle"""
  WHISTLE759304
  """Wind, Weather"""
  WIND759399
  """Windsock, Wind, Direction"""
  WINDDIRECTION759377
  """Wind, Turbine, Windmill"""
  WINDMILL759505
  """Wine, Drink, Glass"""
  WINE759515
  """Wink, Face, Emoji"""
  WINK759898
  """Winter, Water, Drop"""
  WINTER759378
  """Wisk, Mixer"""
  WISK759510
  """Wrench, Tool, Repair"""
  WRENCH759609
  """Watch, Wristwatch, Clock"""
  WRISTWATCH759672
  """Ying, Yang, Spinner"""
  YINGYANG759558
  """Youtube, Video"""
  YOUTUBE759812
  """Zoom, Search, Tool"""
  ZOOM759448
  """Zoom, In, Zoomin"""
  ZOOMIN759613
  """Zoom, Out, Zoomout"""
  ZOOMOUT759612
  """Link"""
  EXTERNALLINK
}

"""Languages."""
enum Language {
  """English"""
  en
  """French"""
  fr
}

"""A permission associated with a `Role`."""
enum Permission {
  """View all log files, regardless of the entity they are attached to"""
  READ_ALL_LOGS
  """Manage Sonar billing"""
  MANAGE_SONAR_BILLING
  """Update system settings."""
  UPDATE_SYSTEM_SETTINGS
  """Update password policy."""
  UPDATE_PASSWORD_POLICY
  """Create a new account, and related entities"""
  CREATE_ACCOUNT
  """View accounts and related entities"""
  READ_ACCOUNT
  """Update an account and related entities"""
  UPDATE_ACCOUNT
  """Create a new account status."""
  CREATE_ACCOUNT_STATUS
  """View account statuses."""
  READ_ACCOUNT_STATUS
  """Update an account status."""
  UPDATE_ACCOUNT_STATUS
  """Delete an account status."""
  DELETE_ACCOUNT_STATUS
  """Create a new account group."""
  CREATE_ACCOUNT_GROUP
  """View account groups."""
  READ_ACCOUNT_GROUP
  """Update an account group."""
  UPDATE_ACCOUNT_GROUP
  """Delete an account group."""
  DELETE_ACCOUNT_GROUP
  """Create a new account type."""
  CREATE_ACCOUNT_TYPE
  """View account types."""
  READ_ACCOUNT_TYPE
  """Update an account type."""
  UPDATE_ACCOUNT_TYPE
  """Delete an account type."""
  DELETE_ACCOUNT_TYPE
  """Create a new custom field."""
  CREATE_CUSTOM_FIELD
  """View all custom fields."""
  READ_CUSTOM_FIELD
  """Update a custom field."""
  UPDATE_CUSTOM_FIELD
  """Delete a custom field."""
  DELETE_CUSTOM_FIELD
  """Create a new custom link."""
  CREATE_CUSTOM_LINK
  """View all custom links."""
  READ_CUSTOM_LINK
  """Update a custom link."""
  UPDATE_CUSTOM_LINK
  """Delete a custom link."""
  DELETE_CUSTOM_LINK
  """Create a new phone number type."""
  CREATE_PHONE_NUMBER_TYPE
  """View phone number types."""
  READ_PHONE_NUMBER_TYPE
  """Update a phone number type."""
  UPDATE_PHONE_NUMBER_TYPE
  """Delete a phone number type."""
  DELETE_PHONE_NUMBER_TYPE
  """Read account calix service detail."""
  READ_ACCOUNT_CALIX_SERVICE_DETAIL
  """Create account calix service detail."""
  CREATE_ACCOUNT_CALIX_SERVICE_DETAIL
  """Update account calix service detail."""
  UPDATE_ACCOUNT_CALIX_SERVICE_DETAIL
  """Delete account calix service detail."""
  DELETE_ACCOUNT_CALIX_SERVICE_DETAIL
  """View FiberMap service locations"""
  READ_FIBERMAP_SERVICE_LOCATION
  """View all network site serviceable address lists"""
  READ_NETWORK_SITE_SERVICEABLE_ADDRESS_LIST
  """Create a new triggered email"""
  CREATE_TRIGGERED_EMAIL
  """View triggered emails"""
  READ_TRIGGERED_EMAIL
  """Update a triggered email"""
  UPDATE_TRIGGERED_EMAIL
  """Delete a triggered email"""
  DELETE_TRIGGERED_EMAIL
  """Create a new saved message category."""
  CREATE_SAVED_MESSAGE_CATEGORY
  """View saved message category."""
  READ_SAVED_MESSAGE_CATEGORY
  """Update a saved message category."""
  UPDATE_SAVED_MESSAGE_CATEGORY
  """Delete a saved message category."""
  DELETE_SAVED_MESSAGE_CATEGORY
  """Create a new saved message"""
  CREATE_EMAIL_MESSAGE
  """View saved messages"""
  READ_EMAIL_MESSAGE
  """Update a saved message"""
  UPDATE_EMAIL_MESSAGE
  """Delete a saved message"""
  DELETE_EMAIL_MESSAGE
  """Create a new serviceable address"""
  CREATE_SERVICEABLE_ADDRESS
  """View serviceable addresses"""
  READ_SERVICEABLE_ADDRESS
  """Update a serviceable address"""
  UPDATE_SERVICEABLE_ADDRESS
  """Delete a serviceable address"""
  DELETE_SERVICEABLE_ADDRESS
  """Create a new general ledger code"""
  CREATE_GENERAL_LEDGER_CODE
  """View general ledger codes"""
  READ_GENERAL_LEDGER_CODE
  """Update a general ledger code"""
  UPDATE_GENERAL_LEDGER_CODE
  """Delete a general ledger code"""
  DELETE_GENERAL_LEDGER_CODE
  """Create a new service"""
  CREATE_SERVICE
  """View services"""
  READ_SERVICE
  """Update a service"""
  UPDATE_SERVICE
  """Delete a service"""
  DELETE_SERVICE
  """Create a voice service details generic parameter."""
  CREATE_VOICE_SERVICE_GENERIC_PARAMETER
  """Update a voice service details generic parameter."""
  UPDATE_VOICE_SERVICE_GENERIC_PARAMETER
  """Delete a voice service details generic parameter."""
  DELETE_VOICE_SERVICE_GENERIC_PARAMETER
  """Create a new tax provider"""
  CREATE_TAX_PROVIDER
  """View tax providers"""
  READ_TAX_PROVIDER
  """Update a tax provider"""
  UPDATE_TAX_PROVIDER
  """Delete a tax provider"""
  DELETE_TAX_PROVIDER
  """Create a new tax exemption"""
  CREATE_TAX_EXEMPTION
  """View tax exemptions"""
  READ_TAX_EXEMPTION
  """Update a tax exemption"""
  UPDATE_TAX_EXEMPTION
  """Delete a tax exemption"""
  DELETE_TAX_EXEMPTION
  """Create a new tax"""
  CREATE_TAX
  """View taxes"""
  READ_TAX
  """Update a tax"""
  UPDATE_TAX
  """Delete a tax"""
  DELETE_TAX
  """Add and remove account services"""
  MODIFY_ACCOUNT_SERVICES
  """
  Modify account service parameters, such as quantity, name override, and proration
  """
  UPDATE_ACCOUNT_SERVICE_PARAMETERS
  """Update the billing parameters on an account"""
  UPDATE_ACCOUNT_BILLING_PARAMETERS
  """Create a new set of billing defaults"""
  CREATE_BILLING_DEFAULT
  """View billing defaults"""
  READ_BILLING_DEFAULT
  """Update a set of billing defaults"""
  UPDATE_BILLING_DEFAULT
  """Delete a set billing default"""
  DELETE_BILLING_DEFAULT
  """View configured payment processors"""
  READ_PAYMENT_PROCESSOR
  """Update a payment processor"""
  UPDATE_PAYMENT_PROCESSOR
  """Create a new payment processor"""
  CREATE_PAYMENT_PROCESSOR
  """Delete a payment processor"""
  DELETE_PAYMENT_PROCESSOR
  """Create a new payment method (e.g. credit card.)"""
  CREATE_PAYMENT_METHOD
  """View all payment methods"""
  READ_PAYMENT_METHOD
  """Update a payment method"""
  UPDATE_PAYMENT_METHOD
  """Delete a payment method"""
  DELETE_PAYMENT_METHOD
  """View all disbursements"""
  READ_DISBURSEMENT
  """View all disputes"""
  READ_DISPUTE
  """Create a FiberMap plan"""
  CREATE_FIBERMAP_PLAN
  """View all FiberMap plans"""
  READ_FIBERMAP_PLAN
  """Update a FiberMap plan"""
  UPDATE_FIBERMAP_PLAN
  """Delete a FiberMap plan"""
  DELETE_FIBERMAP_PLAN
  """Create a FiberMap Integration"""
  CREATE_FIBERMAP_INTEGRATION
  """View all FiberMap Integrations"""
  READ_FIBERMAP_INTEGRATION
  """Update a FiberMap Integration"""
  UPDATE_FIBERMAP_INTEGRATION
  """Delete a FiberMap Integration"""
  DELETE_FIBERMAP_INTEGRATION
  """
  Perform an action that creates an account transaction (e.g. a payment, debit, discount.)
  """
  CREATE_ACCOUNT_TRANSACTIONS
  """View all account transactions"""
  READ_ACCOUNT_TRANSACTIONS
  """Update an account transaction"""
  UPDATE_ACCOUNT_TRANSACTIONS
  """Delete an account transaction"""
  DELETE_ACCOUNT_TRANSACTIONS
  """Whether a user can reverse transactions"""
  REVERSE_ACCOUNT_TRANSACTIONS
  """Update the system billing settings"""
  UPDATE_BILLING_SETTINGS
  """Create a new company"""
  CREATE_COMPANY
  """Update a company"""
  UPDATE_COMPANY
  """Create a new task"""
  CREATE_TASK
  """Update a task"""
  UPDATE_TASK
  """Delete a task"""
  DELETE_TASK
  """Whether a user can complete tasks that are not assigned to them"""
  COMPLETE_OTHERS_TASKS
  """
  Whether a user can override the default proration on account status change
  """
  OVERRIDE_ACCOUNT_STATUS_PRORATION
  """Can alter notes created by other users"""
  ALTER_OTHERS_NOTES
  """Create a new note"""
  CREATE_NOTE
  """Update a note"""
  UPDATE_NOTE
  """Delete a note"""
  DELETE_NOTE
  """Can alter Files created by other users"""
  ALTER_OTHERS_FILES
  """Read Files"""
  READ_FILE
  """Create a new File"""
  CREATE_FILE
  """Update a File"""
  UPDATE_FILE
  """Delete a File"""
  DELETE_FILE
  """Create a new contact"""
  CREATE_CONTACT
  """Update a contact"""
  UPDATE_CONTACT
  """Delete a contact"""
  DELETE_CONTACT
  """Resend a contract"""
  RESEND_CONTRACT
  """Create a new network site"""
  CREATE_NETWORK_SITE
  """View all network sites"""
  READ_NETWORK_SITE
  """Update a network site"""
  UPDATE_NETWORK_SITE
  """Delete a network site"""
  DELETE_NETWORK_SITE
  """Update links between accounts and invoices"""
  UPDATE_ACCOUNT_LINK
  """Create a new delinquency exclusion"""
  CREATE_DELINQUENCY_EXCLUSION
  """View all delinquency exclusions"""
  READ_DELINQUENCY_EXCLUSION
  """Update a delinquency exclusion"""
  UPDATE_DELINQUENCY_EXCLUSION
  """Delete a delinquency exclusion"""
  DELETE_DELINQUENCY_EXCLUSION
  """Create a new payment"""
  CREATE_PAYMENT
  """Update a payment"""
  UPDATE_PAYMENT
  """Whether a user can issue payment refunds"""
  REFUND_PAYMENTS
  """View all inventory"""
  READ_ALL_INVENTORY
  """
  Only view inventory assigned to accounts and network sites that you have
  permission to view, to yourself, or assigned to a vehicle that you are a driver of
  """
  READ_LIMITED_INVENTORY
  """Create a new manufacturer"""
  CREATE_MANUFACTURER
  """Update a manufacturer"""
  UPDATE_MANUFACTURER
  """Delete a manufacturer"""
  DELETE_MANUFACTURER
  """Create a new inventory model category"""
  CREATE_INVENTORY_MODEL_CATEGORY
  """Update an inventory model category"""
  UPDATE_INVENTORY_MODEL_CATEGORY
  """Delete an inventory model category"""
  DELETE_INVENTORY_MODEL_CATEGORY
  """Read a global inventory model min/max"""
  READ_GLOBAL_INVENTORY_MODEL_MIN_MAX
  """Create a global inventory model min/max"""
  CREATE_GLOBAL_INVENTORY_MODEL_MIN_MAX
  """Update a global inventory model min/max"""
  UPDATE_GLOBAL_INVENTORY_MODEL_MIN_MAX
  """Delete a global inventory model min/max"""
  DELETE_GLOBAL_INVENTORY_MODEL_MIN_MAX
  """Create a new inventory model"""
  CREATE_INVENTORY_MODEL
  """Update an inventory model"""
  UPDATE_INVENTORY_MODEL
  """Delete an inventory model"""
  DELETE_INVENTORY_MODEL
  """Create a new vehicle"""
  CREATE_VEHICLE
  """Update a vehicle"""
  UPDATE_VEHICLE
  """Delete a vehicle"""
  DELETE_VEHICLE
  """Create a new inventory location"""
  CREATE_INVENTORY_LOCATION
  """Update an inventory location"""
  UPDATE_INVENTORY_LOCATION
  """Delete an inventory location"""
  DELETE_INVENTORY_LOCATION
  """Create a generic inventory assignee"""
  CREATE_GENERIC_INVENTORY_ASSIGNEE
  """Update a generic inventory assignee"""
  UPDATE_GENERIC_INVENTORY_ASSIGNEE
  """Delete a generic inventory assignee"""
  DELETE_GENERIC_INVENTORY_ASSIGNEE
  """Create a new inventory item"""
  CREATE_INVENTORY_ITEM
  """Update an inventory item"""
  UPDATE_INVENTORY_ITEM
  """Delete an inventory item"""
  DELETE_INVENTORY_ITEM
  """Change claim status of inventory items"""
  CLAIM_INVENTORY_ITEM
  """Update the drivers of a vehicle"""
  UPDATE_DRIVERS
  """Can assign inventory to accounts, yourself, or a vehicle you drive"""
  ASSIGN_ACCOUNT_INVENTORY
  """View all IP assignments"""
  READ_IP_ASSIGNMENT
  """Create an IP assignment"""
  CREATE_IP_ASSIGNMENT
  """Update an IP assignment"""
  UPDATE_IP_ASSIGNMENT
  """Delete an IP assignment"""
  DELETE_IP_ASSIGNMENT
  """Create an element in IPAM"""
  CREATE_IPAM_ELEMENT
  """Update an element in IPAM"""
  UPDATE_IPAM_ELEMENT
  """Delete an element in IPAM"""
  DELETE_IPAM_ELEMENT
  """View all RADIUS accounts"""
  READ_RADIUS_ACCOUNT
  """Create a RADIUS account"""
  CREATE_RADIUS_ACCOUNT
  """Update a RADIUS account"""
  UPDATE_RADIUS_ACCOUNT
  """Delete a RADIUS account"""
  DELETE_RADIUS_ACCOUNT
  """View all uninventoried MAC addresses"""
  READ_UNINVENTORIED_MAC_ADDRESS
  """Create an uninventoried MAC address"""
  CREATE_UNINVENTORIED_MAC_ADDRESS
  """Update an uninventoried MAC address"""
  UPDATE_UNINVENTORIED_MAC_ADDRESS
  """Delete an uninventoried MAC address"""
  DELETE_UNINVENTORIED_MAC_ADDRESS
  """View all non-private tickets"""
  READ_TICKET
  """Create a ticket"""
  CREATE_TICKET
  """Update a ticket"""
  UPDATE_TICKET
  """Delete a ticket"""
  DELETE_TICKET
  """View all ticket groups"""
  READ_TICKET_GROUP
  """Create a ticket group"""
  CREATE_TICKET_GROUP
  """Update a ticket group"""
  UPDATE_TICKET_GROUP
  """Delete a ticket group"""
  DELETE_TICKET_GROUP
  """View all ticket categories"""
  READ_TICKET_CATEGORY
  """Create a ticket category"""
  CREATE_TICKET_CATEGORY
  """Update a ticket category"""
  UPDATE_TICKET_CATEGORY
  """Delete a ticket category"""
  DELETE_TICKET_CATEGORY
  """View all email domains"""
  READ_EMAIL_DOMAIN
  """Create an email domain"""
  CREATE_EMAIL_DOMAIN
  """Delete an email domain"""
  DELETE_EMAIL_DOMAIN
  """View all inbound mailboxes"""
  READ_INBOUND_MAILBOX
  """Update an inbound mailbox"""
  UPDATE_INBOUND_MAILBOX
  """Create an inbound mailbox"""
  CREATE_INBOUND_MAILBOX
  """Delete an inbound mailbox"""
  DELETE_INBOUND_MAILBOX
  """View all canned replies"""
  READ_CANNED_REPLY
  """Update a canned reply"""
  UPDATE_CANNED_REPLY
  """Create a new canned reply"""
  CREATE_CANNED_REPLY
  """Delete a canned reply"""
  DELETE_CANNED_REPLY
  """View all job types"""
  READ_JOB_TYPE
  """Update a job type"""
  UPDATE_JOB_TYPE
  """Create a job type"""
  CREATE_JOB_TYPE
  """Delete a job type"""
  DELETE_JOB_TYPE
  """View all geofences"""
  READ_GEOFENCE
  """Update a geofence"""
  UPDATE_GEOFENCE
  """Create a geofence"""
  CREATE_GEOFENCE
  """Delete a geofence"""
  DELETE_GEOFENCE
  """View all schedule availabilities"""
  READ_SCHEDULE_AVAILABILITY
  """Update a schedule availability"""
  UPDATE_SCHEDULE_AVAILABILITY
  """Create a schedule availability"""
  CREATE_SCHEDULE_AVAILABILITY
  """Delete a schedule availability"""
  DELETE_SCHEDULE_AVAILABILITY
  """View all jobs"""
  READ_JOB
  """Update a job"""
  UPDATE_JOB
  """Update a job skipping validation"""
  UPDATE_JOB_SKIPS_VALIDATION
  """Create a job"""
  CREATE_JOB
  """Delete a job"""
  DELETE_JOB
  """View all schedule time offs"""
  READ_SCHEDULE_TIME_OFF
  """Update a schedule time off"""
  UPDATE_SCHEDULE_TIME_OFF
  """Create a schedule time off"""
  CREATE_SCHEDULE_TIME_OFF
  """Delete a schedule time off"""
  DELETE_SCHEDULE_TIME_OFF
  """View all schedule blockers"""
  READ_SCHEDULE_BLOCKER
  """Update a schedule blocker"""
  UPDATE_SCHEDULE_BLOCKER
  """Create a schedule blocker"""
  CREATE_SCHEDULE_BLOCKER
  """Delete a schedule blocker"""
  DELETE_SCHEDULE_BLOCKER
  """Reschedule a schedule blocker"""
  RESCHEDULE_SCHEDULE_BLOCKER
  """Allows a user to check themselves in to a job"""
  CHECK_IN_OWN_JOB
  """Allows a user to check anyone in to a job"""
  CHECK_IN_ANY_JOB
  """Allows a user to complete their own job"""
  COMPLETE_OWN_JOB
  """Allows a user to complete any job"""
  COMPLETE_ANY_JOB
  """View all schedule addresses"""
  READ_SCHEDULE_ADDRESS
  """Update a schedule address"""
  UPDATE_SCHEDULE_ADDRESS
  """Create a schedule address"""
  CREATE_SCHEDULE_ADDRESS
  """Delete a schedule address"""
  DELETE_SCHEDULE_ADDRESS
  """View all packages"""
  READ_PACKAGE
  """Update a package"""
  UPDATE_PACKAGE
  """Create a package"""
  CREATE_PACKAGE
  """Delete a package"""
  DELETE_PACKAGE
  """View all scheduled events"""
  READ_SCHEDULED_EVENT
  """Update a scheduled event"""
  UPDATE_SCHEDULED_EVENT
  """Create a scheduled event"""
  CREATE_SCHEDULED_EVENT
  """Delete a scheduled event"""
  DELETE_SCHEDULED_EVENT
  """View all account voice service details for a scheduled event"""
  READ_SCHEDULED_EVENT_ACCOUNT_VOICE_SERVICE_DETAIL
  """Update an account voice service detail for a scheduled event"""
  UPDATE_SCHEDULED_EVENT_ACCOUNT_VOICE_SERVICE_DETAIL
  """View all contract templates"""
  READ_CONTRACT_TEMPLATE
  """Update a contract template"""
  UPDATE_CONTRACT_TEMPLATE
  """Create a contract template"""
  CREATE_CONTRACT_TEMPLATE
  """Delete a contract template"""
  DELETE_CONTRACT_TEMPLATE
  """View all contracts"""
  READ_CONTRACT
  """Update a contract"""
  UPDATE_CONTRACT
  """Create a contract"""
  CREATE_CONTRACT
  """Delete a contract"""
  DELETE_CONTRACT
  """Update a tax override"""
  UPDATE_TAX_OVERRIDE
  """Create a tax override"""
  CREATE_TAX_OVERRIDE
  """Delete a tax override"""
  DELETE_TAX_OVERRIDE
  """View all address lists"""
  READ_ADDRESS_LIST
  """Update an address list"""
  UPDATE_ADDRESS_LIST
  """Create an address list"""
  CREATE_ADDRESS_LIST
  """Delete an address list"""
  DELETE_ADDRESS_LIST
  """View all DHCP servers"""
  READ_DHCP_SERVER
  """Update a DHCP server"""
  UPDATE_DHCP_SERVER
  """Create a DHCP server"""
  CREATE_DHCP_SERVER
  """Delete a DHCP server"""
  DELETE_DHCP_SERVER
  """View all call logs"""
  READ_CALL_LOG
  """Create a call log"""
  CREATE_CALL_LOG
  """Update a call log"""
  UPDATE_CALL_LOG
  """Delete a call log"""
  DELETE_CALL_LOG
  """View all task templates"""
  READ_TASK_TEMPLATE
  """Update a task template"""
  UPDATE_TASK_TEMPLATE
  """Create a task template"""
  CREATE_TASK_TEMPLATE
  """Delete a task template"""
  DELETE_TASK_TEMPLATE
  """View all LTE providers"""
  READ_LTE_PROVIDER
  """Update an LTE provider"""
  UPDATE_LTE_PROVIDER
  """Create an LTE provider"""
  CREATE_LTE_PROVIDER
  """Delete an LTE provider"""
  DELETE_LTE_PROVIDER
  """View all RADIUS servers"""
  READ_RADIUS_SERVER
  """Update a RADIUS server"""
  UPDATE_RADIUS_SERVER
  """Create a RADIUS server"""
  CREATE_RADIUS_SERVER
  """Delete a RADIUS server"""
  DELETE_RADIUS_SERVER
  """View all RADIUS groups"""
  READ_RADIUS_GROUP
  """Update a RADIUS group"""
  UPDATE_RADIUS_GROUP
  """Create a RADIUS group"""
  CREATE_RADIUS_GROUP
  """Delete a RADIUS group"""
  DELETE_RADIUS_GROUP
  """Read an external marketing integration"""
  READ_EXTERNAL_MARKETING
  """Create an external marketing integration"""
  CREATE_EXTERNAL_MARKETING
  """Update an external marketing integration"""
  UPDATE_EXTERNAL_MARKETING
  """Delete an external marketing integration"""
  DELETE_EXTERNAL_MARKETING
  """View all inline devices"""
  READ_INLINE_DEVICE
  """Update an inline device"""
  UPDATE_INLINE_DEVICE
  """Create an inline device"""
  CREATE_INLINE_DEVICE
  """Delete an inline device"""
  DELETE_INLINE_DEVICE
  """View all Calix integrations"""
  READ_CALIX_INTEGRATION
  """Update a Calix integration"""
  UPDATE_CALIX_INTEGRATION
  """Create a Calix integration"""
  CREATE_CALIX_INTEGRATION
  """Delete a Calix integration"""
  DELETE_CALIX_INTEGRATION
  """View all Calix Cloud setups"""
  READ_CALIX_CLOUD
  """Update a Calix Cloud setup"""
  UPDATE_CALIX_CLOUD
  """Create a Calix Cloud setup"""
  CREATE_CALIX_CLOUD
  """Delete a Calix Cloud setup"""
  DELETE_CALIX_CLOUD
  """View all integration field mappings"""
  READ_INTEGRATION_FIELD_MAPPING
  """Update an integration field mapping"""
  UPDATE_INTEGRATION_FIELD_MAPPING
  """Create an integration field mapping"""
  CREATE_INTEGRATION_FIELD_MAPPING
  """Delete an integration field mapping"""
  DELETE_INTEGRATION_FIELD_MAPPING
  """View all integration service mappings"""
  READ_INTEGRATION_SERVICE_MAPPING
  """Update an integration service mapping"""
  UPDATE_INTEGRATION_SERVICE_MAPPING
  """Create an integration service mapping"""
  CREATE_INTEGRATION_SERVICE_MAPPING
  """Delete an integration service mapping"""
  DELETE_INTEGRATION_SERVICE_MAPPING
  """View all cable modem provisioners"""
  READ_CABLE_MODEM_PROVISIONER
  """Update a cable modem provisioner"""
  UPDATE_CABLE_MODEM_PROVISIONER
  """Create a cable modem provisioner"""
  CREATE_CABLE_MODEM_PROVISIONER
  """Delete a cable modem provisioner"""
  DELETE_CABLE_MODEM_PROVISIONER
  """View all gps tracking providers"""
  READ_GPS_TRACKING_PROVIDER
  """Update a gps tracking provider"""
  UPDATE_GPS_TRACKING_PROVIDER
  """Create a gps tracking provider"""
  CREATE_GPS_TRACKING_PROVIDER
  """Delete a gps tracking provider"""
  DELETE_GPS_TRACKING_PROVIDER
  """View all network monitoring templates"""
  READ_NETWORK_MONITORING_TEMPLATE
  """Create a network monitoring template"""
  CREATE_NETWORK_MONITORING_TEMPLATE
  """Update a network monitoring template"""
  UPDATE_NETWORK_MONITORING_TEMPLATE
  """Delete a network monitoring template"""
  DELETE_NETWORK_MONITORING_TEMPLATE
  """View all invoice messages"""
  READ_INVOICE_MESSAGE
  """Create an invoice message"""
  CREATE_INVOICE_MESSAGE
  """Update an invoice message"""
  UPDATE_INVOICE_MESSAGE
  """Delete an invoice message"""
  DELETE_INVOICE_MESSAGE
  """View all invoice attachments"""
  READ_INVOICE_ATTACHMENT
  """Create an invoice attachment"""
  CREATE_INVOICE_ATTACHMENT
  """Update an invoice attachment"""
  UPDATE_INVOICE_ATTACHMENT
  """Delete an invoice attachment"""
  DELETE_INVOICE_ATTACHMENT
  """Resend an email invoice batch"""
  EMAIL_INVOICE_BATCH
  """View all printed invoice batches"""
  READ_PRINTED_INVOICE_BATCH
  """Create a printed invoice batch"""
  CREATE_PRINTED_INVOICE_BATCH
  """View all pollers"""
  READ_POLLER
  """Create a poller"""
  CREATE_POLLER
  """Update a poller"""
  UPDATE_POLLER
  """Delete a poller"""
  DELETE_POLLER
  """Update poller configuration settings"""
  UPDATE_POLLER_SETTINGS
  """View all SNMP overrides"""
  READ_SNMP_OVERRIDE
  """Create SNMP override"""
  CREATE_SNMP_OVERRIDE
  """Update SNMP override"""
  UPDATE_SNMP_OVERRIDE
  """Delete SNMP override"""
  DELETE_SNMP_OVERRIDE
  """View all application firewall rules"""
  READ_APPLICATION_FIREWALL_RULE
  """Create an application firewall rule"""
  CREATE_APPLICATION_FIREWALL_RULE
  """Update an application firewall rule"""
  UPDATE_APPLICATION_FIREWALL_RULE
  """Delete an application firewall rule"""
  DELETE_APPLICATION_FIREWALL_RULE
  """View all deposit slips"""
  READ_DEPOSIT_SLIP
  """Create a deposit slip"""
  CREATE_DEPOSIT_SLIP
  """Update a deposit slip"""
  UPDATE_DEPOSIT_SLIP
  """Delete a deposit slip"""
  DELETE_DEPOSIT_SLIP
  """View all alerting rotations"""
  READ_ALERTING_ROTATION
  """Create an alerting rotation"""
  CREATE_ALERTING_ROTATION
  """Update an alerting rotation"""
  UPDATE_ALERTING_ROTATION
  """Delete an alerting rotation"""
  DELETE_ALERTING_ROTATION
  """View all ACH batches"""
  READ_ACH_BATCH
  """Create an ACH batch"""
  CREATE_ACH_BATCH
  """Delete an ACH batch"""
  DELETE_ACH_BATCH
  """Update Preseem integration"""
  UPDATE_PRESEEM
  """View all timeseries data"""
  READ_TIMESERIES_DATA
  """Create data usage entries"""
  CREATE_DATA_USAGE
  """View all data usage history entries"""
  READ_DATA_USAGE_HISTORY
  """Update a data usage history entry"""
  UPDATE_DATA_USAGE_HISTORY
  """Create a data usage top off"""
  CREATE_DATA_USAGE_TOP_OFF
  """View all Netflow endpoints"""
  READ_NETFLOW_ENDPOINT
  """Create a Netflow endpoint"""
  CREATE_NETFLOW_ENDPOINT
  """Update a Netflow endpoint"""
  UPDATE_NETFLOW_ENDPOINT
  """Delete a Netflow endpoint"""
  DELETE_NETFLOW_ENDPOINT
  """View all mass emails"""
  READ_MASS_EMAIL
  """Create a mass email communication"""
  CREATE_MASS_EMAIL
  """View TowerCoverage integration"""
  READ_TOWERCOVERAGE_CONFIGURATION
  """Update TowerCoverage integration"""
  UPDATE_TOWERCOVERAGE_CONFIGURATION
  """View all TowerCoverage submissions"""
  READ_TOWERCOVERAGE_SUBMISSION
  """Update a TowerCoverage submission"""
  UPDATE_TOWERCOVERAGE_SUBMISSION
  """View generated FCC Form 477 reports."""
  READ_FCC_FORM_477_REPORT
  """Create a FCC Form 477 report"""
  CREATE_FCC_FORM_477_REPORT
  """View account reports."""
  READ_ACCOUNT_REPORTS
  """View financial reports."""
  READ_FINANCIAL_REPORTS
  """View all Voice Providers."""
  READ_VOICE_PROVIDER
  """Create a Voice Provider."""
  CREATE_VOICE_PROVIDER
  """Update a Voice Provider."""
  UPDATE_VOICE_PROVIDER
  """Delete a Voice Provider."""
  DELETE_VOICE_PROVIDER
  """View all DIDs."""
  READ_DID
  """Create a DID."""
  CREATE_DID
  """Update a DID."""
  UPDATE_DID
  """Delete a DID."""
  DELETE_DID
  """View all DID assignments."""
  READ_DID_ASSIGNMENT
  """Create a DID assignment."""
  CREATE_DID_ASSIGNMENT
  """Update a DID assignment."""
  UPDATE_DID_ASSIGNMENT
  """Delete a DID assignment."""
  DELETE_DID_ASSIGNMENT
  """View webhook endpoints."""
  READ_WEBHOOK_ENDPOINT
  """Create a webhook endpoint."""
  CREATE_WEBHOOK_ENDPOINT
  """Update a webhook endpoint."""
  UPDATE_WEBHOOK_ENDPOINT
  """Delete a webhook endpoint."""
  DELETE_WEBHOOK_ENDPOINT
  """View webhook endpoint events."""
  READ_WEBHOOK_ENDPOINT_EVENT
  """Create a webhook endpoint event."""
  CREATE_WEBHOOK_ENDPOINT_EVENT
  """Delete a webhook endpoint event."""
  DELETE_WEBHOOK_ENDPOINT_EVENT
  """View all daily aggregate values."""
  READ_DAILY_AGGREGATE_VALUES
  """Update the ticketing settings."""
  UPDATE_TICKETING_SETTINGS
  """Update the print to mail settings."""
  UPDATE_PRINT_TO_MAIL_SETTINGS
  """View a print to mail batch."""
  READ_PRINT_TO_MAIL_BATCH
  """View a print to mail order."""
  READ_PRINT_TO_MAIL_ORDER
  """View a print to mail order error."""
  READ_PRINT_TO_MAIL_ORDER_ERROR
  """Resend a print to mail batch."""
  RESEND_PRINT_TO_MAIL_BATCH
  """Cancel a print to mail batch."""
  CANCEL_PRINT_TO_MAIL_BATCH
  """Update a print to mail order error."""
  UPDATE_PRINT_TO_MAIL_ORDER_ERROR
  """Update the SMS settings."""
  UPDATE_SMS_SETTINGS
  """View an SMS outbound message."""
  READ_SMS_OUTBOUND_MESSAGE
  """View all access logs."""
  READ_ACCESS_LOG
  """Create an entry in the access log."""
  CREATE_ACCESS_LOG
  """Read all search filters."""
  READ_SEARCH_FILTER
  """Create a saved search filter."""
  CREATE_SEARCH_FILTER
  """Update an existing search filter."""
  UPDATE_SEARCH_FILTER
  """Delete an existing search filter."""
  DELETE_SEARCH_FILTER
  """Create a public saved filter."""
  CREATE_GLOBAL_STORED_VIEW
  """Update a public saved filter."""
  UPDATE_GLOBAL_STORED_VIEW
  """Delete a public saved filter."""
  DELETE_GLOBAL_STORED_VIEW
  """View all Voice Provider Rates."""
  READ_VOICE_PROVIDER_RATE
  """Create a Voice Provider Rate."""
  CREATE_VOICE_PROVIDER_RATE
  """Update a Voice Provider Rate."""
  UPDATE_VOICE_PROVIDER_RATE
  """Delete a Voice Provider Rate."""
  DELETE_VOICE_PROVIDER_RATE
  """View all Voice Provider Rate imports."""
  READ_VOICE_PROVIDER_RATE_IMPORT
  """View all call detail records (CDRs)."""
  READ_CALL_DETAIL_RECORD
  """Create a call detail record (CDR)."""
  CREATE_CALL_DETAIL_RECORD
  """Update a call detail record (CDR)."""
  UPDATE_CALL_DETAIL_RECORD
  """Delete a call detail record (CDR)."""
  DELETE_CALL_DETAIL_RECORD
  """View all call detail record (CDR) imports."""
  READ_CALL_DETAIL_RECORD_IMPORT
  """Update a RADIUS session history."""
  UPDATE_RADIUS_SESSION_HISTORY
  """Update an Auth provider"""
  UPDATE_AUTH_PROVIDER
  """View all Auth providers"""
  READ_AUTH_PROVIDER
  """Create an identity provider"""
  CREATE_IDENTITY_PROVIDER
  """Update an identity provider"""
  UPDATE_IDENTITY_PROVIDER
  """View all identity providers"""
  READ_IDENTITY_PROVIDER
  """Delete an identity provider"""
  DELETE_IDENTITY_PROVIDER
  """Create a vendor."""
  CREATE_VENDOR
  """Update an existing vendor."""
  UPDATE_VENDOR
  """Read all vendors."""
  READ_VENDOR
  """Create a vendor item."""
  CREATE_VENDOR_ITEM
  """Update an existing vendor item."""
  UPDATE_VENDOR_ITEM
  """Read all vendor items."""
  READ_VENDOR_ITEM
  """Delete an existing vendor item."""
  DELETE_VENDOR_ITEM
  """Create a purchase order."""
  CREATE_PURCHASE_ORDER
  """Update an existing purchase order."""
  UPDATE_PURCHASE_ORDER
  """Read all purchase order."""
  READ_PURCHASE_ORDER
  """Receive a purchase order and create inventory items."""
  PURCHASE_ORDER_RECEIVING
  """Modify purchase order items after they have been received."""
  EDIT_RECEIVED_PURCHASE_ORDER
  """Create a order group."""
  CREATE_ORDER_GROUP
  """Update an existing order group."""
  UPDATE_ORDER_GROUP
  """Read all order group."""
  READ_ORDER_GROUP
  """Delete an existing order group."""
  DELETE_ORDER_GROUP
  """Create a non-inventory item."""
  CREATE_NON_INVENTORY_ITEM
  """Read all non-inventory items."""
  READ_NON_INVENTORY_ITEM
  """Delete an existing non-inventory item."""
  DELETE_NON_INVENTORY_ITEM
  """Update an existing non-inventory item."""
  UPDATE_NON_INVENTORY_ITEM
  """Create a map overlay"""
  CREATE_MAP_OVERLAY
  """View all map overlays"""
  READ_MAP_OVERLAY
  """Delete a map overlay"""
  DELETE_MAP_OVERLAY
  """Update a map overlay"""
  UPDATE_MAP_OVERLAY
  """Create a Rate Center."""
  CREATE_RATE_CENTER
  """View all Rate Centers."""
  READ_RATE_CENTER
  """Update a Rate Center."""
  UPDATE_RATE_CENTER
  """Delete a Rate Center."""
  DELETE_RATE_CENTER
  """Create calendar settings."""
  CREATE_CALENDAR
  """View all of your calendar settings."""
  READ_CALENDAR
  """Update your calendar settings."""
  UPDATE_CALENDAR
  """Delete your calendar settings."""
  DELETE_CALENDAR
  """Create address status."""
  CREATE_ADDRESS_STATUS
  """Read address status."""
  READ_ADDRESS_STATUS
  """Update address status."""
  UPDATE_ADDRESS_STATUS
  """Delete address status."""
  DELETE_ADDRESS_STATUS
  """Create a call detail record (CDR) import."""
  CREATE_CALL_DETAIL_RECORD_IMPORT_RECIPE
  """View all call detail record (CDR) imports."""
  READ_CALL_DETAIL_RECORD_IMPORT_RECIPE
  """Create a DID import."""
  CREATE_DID_IMPORT_RECIPE
  """View all DID imports."""
  READ_DID_IMPORT_RECIPE
  """Create a Sonar Import."""
  CREATE_SONAR_IMPORT_RECIPE
  """Read a Sonar Import."""
  READ_SONAR_IMPORT_RECIPE
  """Create a Voice Provider Rate import."""
  CREATE_VOICE_PROVIDER_RATE_IMPORT_RECIPE
  """View all Voice Provider Rate imports."""
  READ_VOICE_PROVIDER_RATE_IMPORT_RECIPE
  """Delete a department"""
  DELETE_DEPARTMENT
  """Create a new SMS message"""
  CREATE_SMS_MESSAGE
  """View SMS messages"""
  READ_SMS_MESSAGE
  """Update a SMS message"""
  UPDATE_SMS_MESSAGE
  """Delete a SMS message"""
  DELETE_SMS_MESSAGE
  """Create a new triggered SMS message"""
  CREATE_TRIGGERED_SMS_MESSAGE
  """View triggered SMS messages"""
  READ_TRIGGERED_SMS_MESSAGE
  """Update a triggered SMS message"""
  UPDATE_TRIGGERED_SMS_MESSAGE
  """Delete a triggered SMS message"""
  DELETE_TRIGGERED_SMS_MESSAGE
  """Create a new messaging category"""
  CREATE_MESSAGE_CATEGORY
  """View messaging categories"""
  READ_MESSAGE_CATEGORY
  """Update a messaging category"""
  UPDATE_MESSAGE_CATEGORY
  """Delete a messaging category"""
  DELETE_MESSAGE_CATEGORY
  """Create Adtran Mosaic settings"""
  CREATE_ADTRAN_MOSAIC_SETTING
  """View Adtran Mosaic settings"""
  READ_ADTRAN_MOSAIC_SETTING
  """Update Adtran Mosaic settings"""
  UPDATE_ADTRAN_MOSAIC_SETTING
  """Delete Adtran Mosaic settings"""
  DELETE_ADTRAN_MOSAIC_SETTING
  """Read account Adtran Mosaic service detail."""
  READ_ACCOUNT_ADTRAN_MOSAIC_SERVICE_DETAIL
  """Create account Adtran Mosaic service detail."""
  CREATE_ACCOUNT_ADTRAN_MOSAIC_SERVICE_DETAIL
  """Update account Adtran Mosaic service detail."""
  UPDATE_ACCOUNT_ADTRAN_MOSAIC_SERVICE_DETAIL
  """Delete account Adtran Mosaic service detail."""
  DELETE_ACCOUNT_ADTRAN_MOSAIC_SERVICE_DETAIL
  """Create a new invoice template"""
  CREATE_INVOICE_TEMPLATE
  """View invoice templates"""
  READ_INVOICE_TEMPLATE
  """Update an invoice template"""
  UPDATE_INVOICE_TEMPLATE
  """Delete an invoice template"""
  DELETE_INVOICE_TEMPLATE
  """Create a new future serviceable address"""
  CREATE_SERVICEABLE_ADDRESS_ACCOUNT_ASSIGNMENT_FUTURE
  """View future serviceable addresses"""
  READ_SERVICEABLE_ADDRESS_ACCOUNT_ASSIGNMENT_FUTURE
  """Update a future serviceable address"""
  UPDATE_SERVICEABLE_ADDRESS_ACCOUNT_ASSIGNMENT_FUTURE
  """Delete a future serviceable address"""
  DELETE_SERVICEABLE_ADDRESS_ACCOUNT_ASSIGNMENT_FUTURE
  """Archive accounts."""
  ARCHIVE_ACCOUNTS
  """Unarchive accounts."""
  UNARCHIVE_ACCOUNTS
  """Update multi-factor authentication admin settings"""
  UPDATE_MFA_ADMIN_SETTINGS
}

"""A protocol."""
enum Protocol {
  """HTTP."""
  HTTP
  """HTTPS."""
  HTTPS
}

"""
A subdivision is a state, a province, or similar geographical region. The
section prior to the underscore is the country code.
"""
enum Subdivision {
  """Canillo"""
  AD_02
  """Sant Julià de Lòria"""
  AD_06
  """Escaldes-Engordany"""
  AD_08
  """Encamp"""
  AD_03
  """Andorra la Vella"""
  AD_07
  """La Massana"""
  AD_04
  """Ordino"""
  AD_05
  """Ra's al Khaymah"""
  AE_RK
  """Ash Shāriqah"""
  AE_SH
  """Al Fujayrah"""
  AE_FU
  """Dubayy"""
  AE_DU
  """Abū Z̧aby"""
  AE_AZ
  """Umm al Qaywayn"""
  AE_UQ
  """'Ajmān"""
  AE_AJ
  """Bāmyān"""
  AF_BAM
  """Kābul"""
  AF_KAB
  """Kāpīsā"""
  AF_KAP
  """Khōst"""
  AF_KHO
  """Kunar"""
  AF_KNR
  """Kandahār"""
  AF_KAN
  """Lōgar"""
  AF_LOG
  """Paktiyā"""
  AF_PIA
  """Samangān"""
  AF_SAM
  """Uruzgān"""
  AF_URU
  """Badakhshān"""
  AF_BDS
  """Fāryāb"""
  AF_FYB
  """Jowzjān"""
  AF_JOW
  """Kunduz"""
  AF_KDZ
  """Laghmān"""
  AF_LAG
  """Nīmrōz"""
  AF_NIM
  """Baghlān"""
  AF_BGL
  """Farāh"""
  AF_FRA
  """Helmand"""
  AF_HEL
  """Paktīkā"""
  AF_PKA
  """Sar-e Pul"""
  AF_SAR
  """Bādghīs"""
  AF_BDG
  """Ghaznī"""
  AF_GHA
  """Panjshayr"""
  AF_PAN
  """Takhār"""
  AF_TAK
  """Wardak"""
  AF_WAR
  """Balkh"""
  AF_BAL
  """Ghōr"""
  AF_GHO
  """Dāykundī"""
  AF_DAY
  """Herāt"""
  AF_HER
  """Nangarhār"""
  AF_NAN
  """Nūristān"""
  AF_NUR
  """Parwān"""
  AF_PAR
  """Zābul"""
  AF_ZAB
  """Saint John"""
  AG_04
  """Redonda"""
  AG_11
  """Saint George"""
  AG_03
  """Saint Paul"""
  AG_06
  """Barbuda"""
  AG_10
  """Saint Peter"""
  AG_07
  """Saint Philip"""
  AG_08
  """Saint Mary"""
  AG_05
  """Fier"""
  AL_04
  """Fier"""
  AL_FR
  """Mallakastër"""
  AL_MK
  """Lushnjë"""
  AL_LU
  """Tiranë"""
  AL_11
  """Tiranë"""
  AL_TR
  """Kavajë"""
  AL_KA
  """Vlorë"""
  AL_12
  """Delvinë"""
  AL_DL
  """Sarandë"""
  AL_SR
  """Vlorë"""
  AL_VL
  """Elbasan"""
  AL_03
  """Librazhd"""
  AL_LB
  """Gramsh"""
  AL_GR
  """Elbasan"""
  AL_EL
  """Peqin"""
  AL_PQ
  """Dibër"""
  AL_09
  """Dibër"""
  AL_DI
  """Bulqizë"""
  AL_BU
  """Mat"""
  AL_MT
  """Berat"""
  AL_01
  """Berat"""
  AL_BR
  """Kuçovë"""
  AL_KC
  """Skrapar"""
  AL_SK
  """Durrës"""
  AL_02
  """Krujë"""
  AL_KR
  """Durrës"""
  AL_DR
  """Lezhë"""
  AL_08
  """Lezhë"""
  AL_LE
  """Mirditë"""
  AL_MR
  """Kurbin"""
  AL_KB
  """Shkodër"""
  AL_10
  """Pukë"""
  AL_PU
  """Malësi e Madhe"""
  AL_MM
  """Shkodër"""
  AL_SH
  """Gjirokastër"""
  AL_05
  """Tepelenë"""
  AL_TE
  """Gjirokastër"""
  AL_GJ
  """Përmet"""
  AL_PR
  """Korçë"""
  AL_06
  """Devoll"""
  AL_DV
  """Kolonjë"""
  AL_ER
  """Korçë"""
  AL_KO
  """Pogradec"""
  AL_PG
  """Kukës"""
  AL_07
  """Tropojë"""
  AL_TP
  """Has"""
  AL_HA
  """Kukës"""
  AL_KU
  """Ararat"""
  AM_AR
  """Aragac̣otn"""
  AM_AG
  """Armavir"""
  AM_AV
  """Kotayk'"""
  AM_KT
  """Geġark'unik'"""
  AM_GR
  """Širak"""
  AM_SH
  """Syunik'"""
  AM_SU
  """Tavuš"""
  AM_TV
  """Loṙi"""
  AM_LO
  """Erevan"""
  AM_ER
  """Vayoć Jor"""
  AM_VD
  """Bié"""
  AO_BIE
  """Cabinda"""
  AO_CAB
  """Kuando Kubango"""
  AO_CCU
  """Zaire"""
  AO_ZAI
  """Lunda Norte"""
  AO_LNO
  """Lunda Sul"""
  AO_LSU
  """Moxico"""
  AO_MOX
  """Namibe"""
  AO_NAM
  """Uíge"""
  AO_UIG
  """Kwanza Norte"""
  AO_CNO
  """Huíla"""
  AO_HUI
  """Luanda"""
  AO_LUA
  """Malange"""
  AO_MAL
  """Bengo"""
  AO_BGO
  """Benguela"""
  AO_BGU
  """Cunene"""
  AO_CNN
  """Kwanza Sul"""
  AO_CUS
  """Huambo"""
  AO_HUA
  """San Luis"""
  AR_D
  """La Pampa"""
  AR_L
  """Mendoza"""
  AR_M
  """Neuquén"""
  AR_Q
  """Río Negro"""
  AR_R
  """Jujuy"""
  AR_Y
  """Misiones"""
  AR_N
  """Santa Fe"""
  AR_S
  """Santa Cruz"""
  AR_Z
  """Salta"""
  AR_A
  """Ciudad Autónoma de Buenos Aires"""
  AR_C
  """La Rioja"""
  AR_F
  """Buenos Aires"""
  AR_B
  """Santiago del Estero"""
  AR_G
  """Chaco"""
  AR_H
  """Formosa"""
  AR_P
  """Córdoba"""
  AR_X
  """San Juan"""
  AR_J
  """Tucumán"""
  AR_T
  """Entre Ríos"""
  AR_E
  """Catamarca"""
  AR_K
  """Tierra del Fuego"""
  AR_V
  """Corrientes"""
  AR_W
  """Chubut"""
  AR_U
  """Wien"""
  AT_9
  """Niederösterreich"""
  AT_3
  """Oberösterreich"""
  AT_4
  """Salzburg"""
  AT_5
  """Vorarlberg"""
  AT_8
  """Burgenland"""
  AT_1
  """Tirol"""
  AT_7
  """Kärnten"""
  AT_2
  """Steiermark"""
  AT_6
  """Victoria"""
  AU_VIC
  """Northern Territory"""
  AU_NT
  """Queensland"""
  AU_QLD
  """Tasmania"""
  AU_TAS
  """Australian Capital Territory"""
  AU_ACT
  """New South Wales"""
  AU_NSW
  """South Australia"""
  AU_SA
  """Western Australia"""
  AU_WA
  """Goranboy"""
  AZ_GOR
  """Naftalan"""
  AZ_NA
  """Qubadlı"""
  AZ_QBI
  """Şәki"""
  AZ_SA
  """Şamaxı"""
  AZ_SMI
  """Tovuz"""
  AZ_TOV
  """Yevlax"""
  AZ_YE
  """Abşeron"""
  AZ_ABS
  """Bakı"""
  AZ_BA
  """Balakən"""
  AZ_BAL
  """Bərdə"""
  AZ_BAR
  """Göyçay"""
  AZ_GOY
  """Masallı"""
  AZ_MAS
  """Şәmkir"""
  AZ_SKR
  """Şirvan"""
  AZ_SR
  """Xankәndi"""
  AZ_XA
  """Xızı"""
  AZ_XIZ
  """Ağcabәdi"""
  AZ_AGC
  """Ağsu"""
  AZ_AGU
  """Biləsuvar"""
  AZ_BIL
  """Gәncә"""
  AZ_GA
  """Qәbәlә"""
  AZ_QAB
  """Samux"""
  AZ_SMX
  """Xaçmaz"""
  AZ_XAC
  """Yardımlı"""
  AZ_YAR
  """Zәngilan"""
  AZ_ZAN
  """Ağstafa"""
  AZ_AGA
  """Füzuli"""
  AZ_FUZ
  """Gədəbəy"""
  AZ_GAD
  """Laçın"""
  AZ_LAC
  """Qax"""
  AZ_QAX
  """Ağdam"""
  AZ_AGM
  """Daşkəsən"""
  AZ_DAS
  """Göygöl"""
  AZ_GYG
  """Lәnkәran"""
  AZ_LA
  """Lənkəran"""
  AZ_LAN
  """Oğuz"""
  AZ_OGU
  """Quba"""
  AZ_QBA
  """Qusar"""
  AZ_QUS
  """Sabirabad"""
  AZ_SAB
  """Cəbrayıl"""
  AZ_CAB
  """Kürdəmir"""
  AZ_KUR
  """Salyan"""
  AZ_SAL
  """Şabran"""
  AZ_SBN
  """Sumqayıt"""
  AZ_SM
  """Ucar"""
  AZ_UCA
  """Xocalı"""
  AZ_XCI
  """Yevlax"""
  AZ_YEV
  """Ağdaş"""
  AZ_AGS
  """Astara"""
  AZ_AST
  """Beyləqan"""
  AZ_BEY
  """Hacıqabul"""
  AZ_HAC
  """İmişli"""
  AZ_IMI
  """İsmayıllı"""
  AZ_ISM
  """Lerik"""
  AZ_LER
  """Mingәçevir"""
  AZ_MI
  """Neftçala"""
  AZ_NEF
  """Naxçıvan"""
  AZ_NX
  """Kǝngǝrli"""
  AZ_KAN
  """Culfa"""
  AZ_CUL
  """Ordubad"""
  AZ_ORD
  """Sәdәrәk"""
  AZ_SAD
  """Şahbuz"""
  AZ_SAH
  """Babək"""
  AZ_BAB
  """Şәrur"""
  AZ_SAR
  """Naxçıvan"""
  AZ_NV
  """Qazax"""
  AZ_QAZ
  """Şәki"""
  AZ_SAK
  """Saatlı"""
  AZ_SAT
  """Tәrtәr"""
  AZ_TAR
  """Xocavәnd"""
  AZ_XVD
  """Zәrdab"""
  AZ_ZAR
  """Cəlilabad"""
  AZ_CAL
  """Kəlbəcər"""
  AZ_KAL
  """Qobustan"""
  AZ_QOB
  """Siyәzәn"""
  AZ_SIY
  """Şuşa"""
  AZ_SUS
  """Zaqatala"""
  AZ_ZAQ
  """Brčko distrikt"""
  BA_BRC
  """Federacija Bosne i Hercegovine"""
  BA_BIH
  """Posavski kanton"""
  BA_02
  """Tuzlanska županija"""
  BA_03
  """Hercegovačko-neretvanski kanton"""
  BA_07
  """Unsko-sanski kanton"""
  BA_01
  """Bosansko-podrinjski kanton"""
  BA_05
  """Zapadnohercegovački kanton"""
  BA_08
  """Kanton br. 10 (Livanjski kanton)"""
  BA_10
  """Zeničko-dobojski kanton"""
  BA_04
  """Srednjobosanska županija"""
  BA_06
  """Sarajevska županija"""
  BA_09
  """Republika Srpska"""
  BA_SRP
  """Saint Lucy"""
  BB_07
  """Saint George"""
  BB_03
  """Saint John"""
  BB_05
  """Saint Andrew"""
  BB_02
  """Saint Philip"""
  BB_10
  """Saint Thomas"""
  BB_11
  """Saint Michael"""
  BB_08
  """Saint James"""
  BB_04
  """Saint Peter"""
  BB_09
  """Christ Church"""
  BB_01
  """Saint Joseph"""
  BB_06
  """Chittagong"""
  BD_B
  """Brahmanbaria"""
  BD_04
  """Noakhali"""
  BD_47
  """Chittagong"""
  BD_10
  """Cox's Bazar"""
  BD_11
  """Rangamati"""
  BD_56
  """Feni"""
  BD_16
  """Lakshmipur"""
  BD_31
  """Chandpur"""
  BD_09
  """Comilla"""
  BD_08
  """Khagrachari"""
  BD_29
  """Bandarban"""
  BD_01
  """Dhaka"""
  BD_C
  """Madaripur"""
  BD_36
  """Shariatpur"""
  BD_62
  """Tangail"""
  BD_63
  """Mymensingh"""
  BD_34
  """Sherpur"""
  BD_57
  """Kishoreganj"""
  BD_26
  """Jamalpur"""
  BD_21
  """Netrakona"""
  BD_41
  """Narsingdi"""
  BD_42
  """Dhaka"""
  BD_13
  """Faridpur"""
  BD_15
  """Gopalganj"""
  BD_17
  """Rajbari"""
  BD_53
  """Gazipur"""
  BD_18
  """Manikganj"""
  BD_33
  """Munshiganj"""
  BD_35
  """Narayanganj"""
  BD_40
  """Barisal"""
  BD_A
  """Barguna"""
  BD_02
  """Jhalakati"""
  BD_25
  """Pirojpur"""
  BD_50
  """Barisal"""
  BD_06
  """Bhola"""
  BD_07
  """Patuakhali"""
  BD_51
  """Khulna"""
  BD_D
  """Narail"""
  BD_43
  """Kushtia"""
  BD_30
  """Meherpur"""
  BD_39
  """Chuadanga"""
  BD_12
  """Jessore"""
  BD_22
  """Satkhira"""
  BD_58
  """Magura"""
  BD_37
  """Bagerhat"""
  BD_05
  """Jhenaidah"""
  BD_23
  """Khulna"""
  BD_27
  """Rajshahi"""
  BD_E
  """Natore"""
  BD_44
  """Nawabganj"""
  BD_45
  """Naogaon"""
  BD_48
  """Rangpur"""
  BD_55
  """Pabna"""
  BD_49
  """Rajshahi"""
  BD_54
  """Jaipurhat"""
  BD_24
  """Sirajganj"""
  BD_59
  """Bogra"""
  BD_03
  """Sylhet"""
  BD_G
  """Habiganj"""
  BD_20
  """Moulvibazar"""
  BD_38
  """Sylhet"""
  BD_60
  """Sunamganj"""
  BD_61
  """Rangpur"""
  BD_F
  """Gaibandha"""
  BD_19
  """Thakurgaon"""
  BD_64
  """Kurigram"""
  BD_28
  """Panchagarh"""
  BD_52
  """Dinajpur"""
  BD_14
  """Lalmonirhat"""
  BD_32
  """Nilphamari"""
  BD_46
  """wallonne, Région"""
  BE_WAL
  """Brabant wallon"""
  BE_WBR
  """Liège"""
  BE_WLG
  """Brussels Hoofdstedelijk Gewest"""
  BE_BRU
  """Vlaams Gewest"""
  BE_VLG
  """Vlaams-Brabant"""
  BE_VBR
  """West-Vlaanderen"""
  BE_VWV
  """Luxembourg"""
  BE_WLX
  """Antwerpen"""
  BE_VAN
  """Limburg"""
  BE_VLI
  """Oost-Vlaanderen"""
  BE_VOV
  """Namur"""
  BE_WNA
  """Hainaut"""
  BE_WHT
  """Centre-Nord"""
  BF_05
  """Bam"""
  BF_BAM
  """Sanmatenga"""
  BF_SMT
  """Namentenga"""
  BF_NAM
  """Boucle du Mouhoun"""
  BF_01
  """Banwa"""
  BF_BAN
  """Mouhoun"""
  BF_MOU
  """Nayala"""
  BF_NAY
  """Sourou"""
  BF_SOR
  """Balé"""
  BF_BAL
  """Kossi"""
  BF_KOS
  """Nord"""
  BF_10
  """Yatenga"""
  BF_YAT
  """Loroum"""
  BF_LOR
  """Passoré"""
  BF_PAS
  """Zondoma"""
  BF_ZON
  """Cascades"""
  BF_02
  """Comoé"""
  BF_COM
  """Léraba"""
  BF_LER
  """Centre"""
  BF_03
  """Kadiogo"""
  BF_KAD
  """Centre-Est"""
  BF_04
  """Boulgou"""
  BF_BLG
  """Kouritenga"""
  BF_KOT
  """Koulpélogo"""
  BF_KOP
  """Centre-Ouest"""
  BF_06
  """Sanguié"""
  BF_SNG
  """Sissili"""
  BF_SIS
  """Ziro"""
  BF_ZIR
  """Boulkiemdé"""
  BF_BLK
  """Centre-Sud"""
  BF_07
  """Zoundwéogo"""
  BF_ZOU
  """Nahouri"""
  BF_NAO
  """Bazèga"""
  BF_BAZ
  """Est"""
  BF_08
  """Gourma"""
  BF_GOU
  """Gnagna"""
  BF_GNA
  """Komondjari"""
  BF_KMD
  """Kompienga"""
  BF_KMP
  """Tapoa"""
  BF_TAP
  """Hauts-Bassins"""
  BF_09
  """Houet"""
  BF_HOU
  """Tui"""
  BF_TUI
  """Kénédougou"""
  BF_KEN
  """Plateau-Central"""
  BF_11
  """Ganzourgou"""
  BF_GAN
  """Kourwéogo"""
  BF_KOW
  """Oubritenga"""
  BF_OUB
  """Sahel"""
  BF_12
  """Séno"""
  BF_SEN
  """Oudalan"""
  BF_OUD
  """Soum"""
  BF_SOM
  """Yagha"""
  BF_YAG
  """Sud-Ouest"""
  BF_13
  """Poni"""
  BF_PON
  """Bougouriba"""
  BF_BGR
  """Noumbiel"""
  BF_NOU
  """Ioba"""
  BF_IOB
  """Vidin"""
  BG_05
  """Vratsa"""
  BG_06
  """Gabrovo"""
  BG_07
  """Dobrich"""
  BG_08
  """Haskovo"""
  BG_26
  """Veliko Tarnovo"""
  BG_04
  """Kardzhali"""
  BG_09
  """Pleven"""
  BG_15
  """Plovdiv"""
  BG_16
  """Yambol"""
  BG_28
  """Pazardzhik"""
  BG_13
  """Ruse"""
  BG_18
  """Smolyan"""
  BG_21
  """Sofia (stolitsa)"""
  BG_22
  """Shumen"""
  BG_27
  """Burgas"""
  BG_02
  """Pernik"""
  BG_14
  """Silistra"""
  BG_19
  """Targovishte"""
  BG_25
  """Varna"""
  BG_03
  """Stara Zagora"""
  BG_24
  """Blagoevgrad"""
  BG_01
  """Kyustendil"""
  BG_10
  """Montana"""
  BG_12
  """Sliven"""
  BG_20
  """Sofia"""
  BG_23
  """Lovech"""
  BG_11
  """Razgrad"""
  BG_17
  """Al Muḩarraq"""
  BH_15
  """Ash Shamālīyah"""
  BH_17
  """Al Janūbīyah"""
  BH_14
  """Al Wusţá"""
  BH_16
  """Al Manāmah"""
  BH_13
  """Bubanza"""
  BI_BB
  """Bujumbura Mairie"""
  BI_BM
  """Karuzi"""
  BI_KR
  """Muyinga"""
  BI_MY
  """Kirundo"""
  BI_KI
  """Bururi"""
  BI_BR
  """Cibitoke"""
  BI_CI
  """Gitega"""
  BI_GI
  """Makamba"""
  BI_MA
  """Muramvya"""
  BI_MU
  """Ngozi"""
  BI_NG
  """Ruyigi"""
  BI_RY
  """Kayanza"""
  BI_KY
  """Mwaro"""
  BI_MW
  """Cankuzo"""
  BI_CA
  """Bujumbura Rural"""
  BI_BL
  """Rutana"""
  BI_RT
  """Alibori"""
  BJ_AL
  """Donga"""
  BJ_DO
  """Kouffo"""
  BJ_KO
  """Plateau"""
  BJ_PL
  """Zou"""
  BJ_ZO
  """Atakora"""
  BJ_AK
  """Collines"""
  BJ_CO
  """Borgou"""
  BJ_BO
  """Ouémé"""
  BJ_OU
  """Littoral"""
  BJ_LI
  """Atlantique"""
  BJ_AQ
  """Mono"""
  BJ_MO
  """Tutong"""
  BN_TU
  """Brunei-Muara"""
  BN_BM
  """Belait"""
  BN_BE
  """Temburong"""
  BN_TE
  """Cochabamba"""
  BO_C
  """La Paz"""
  BO_L
  """El Beni"""
  BO_B
  """Oruro"""
  BO_O
  """Santa Cruz"""
  BO_S
  """Potosí"""
  BO_P
  """Tarija"""
  BO_T
  """Chuquisaca"""
  BO_H
  """Pando"""
  BO_N
  """Bonaire"""
  BQ_BO
  """Saba"""
  BQ_SA
  """Sint Eustatius"""
  BQ_SE
  """Acre"""
  BR_AC
  """Amazonas"""
  BR_AM
  """Ceará"""
  BR_CE
  """Roraima"""
  BR_RR
  """Goiás"""
  BR_GO
  """Minas Gerais"""
  BR_MG
  """Tocantins"""
  BR_TO
  """Espírito Santo"""
  BR_ES
  """Amapá"""
  BR_AP
  """Bahia"""
  BR_BA
  """Mato Grosso do Sul"""
  BR_MS
  """Paraná"""
  BR_PR
  """Rio Grande do Norte"""
  BR_RN
  """Mato Grosso"""
  BR_MT
  """Paraíba"""
  BR_PB
  """Pernambuco"""
  BR_PE
  """Rio de Janeiro"""
  BR_RJ
  """Rondônia"""
  BR_RO
  """Santa Catarina"""
  BR_SC
  """São Paulo"""
  BR_SP
  """Alagoas"""
  BR_AL
  """Distrito Federal"""
  BR_DF
  """Maranhão"""
  BR_MA
  """Pará"""
  BR_PA
  """Piauí"""
  BR_PI
  """Rio Grande do Sul"""
  BR_RS
  """Sergipe"""
  BR_SE
  """Crooked Island and Long Cay"""
  BS_CK
  """Hope Town"""
  BS_HT
  """Ragged Island"""
  BS_RI
  """Central Abaco"""
  BS_CO
  """East Grand Bahama"""
  BS_EG
  """Harbour Island"""
  BS_HI
  """Moore's Island"""
  BS_MI
  """San Salvador"""
  BS_SS
  """Spanish Wells"""
  BS_SW
  """Acklins"""
  BS_AK
  """Long Island"""
  BS_LI
  """Berry Islands"""
  BS_BY
  """City of Freeport"""
  BS_FP
  """North Andros"""
  BS_NS
  """Rum Cay"""
  BS_RC
  """South Abaco"""
  BS_SO
  """Central Eleuthera"""
  BS_CE
  """Cat Island"""
  BS_CI
  """Central Andros"""
  BS_CS
  """Exuma"""
  BS_EX
  """Inagua"""
  BS_IN
  """Mangrove Cay"""
  BS_MC
  """South Andros"""
  BS_SA
  """Grand Cay"""
  BS_GC
  """Mayaguana"""
  BS_MG
  """West Grand Bahama"""
  BS_WG
  """Bimini"""
  BS_BI
  """Black Point"""
  BS_BP
  """North Eleuthera"""
  BS_NE
  """North Abaco"""
  BS_NO
  """South Eleuthera"""
  BS_SE
  """Paro"""
  BT_11
  """Monggar"""
  BT_42
  """Samdrup Jongkha"""
  BT_45
  """Chhukha"""
  BT_12
  """Punakha"""
  BT_23
  """Wangdue Phodrang"""
  BT_24
  """Tsirang"""
  BT_21
  """Bumthang"""
  BT_33
  """Zhemgang"""
  BT_34
  """Sarpang"""
  BT_31
  """Samtse"""
  BT_14
  """Thimphu"""
  BT_15
  """Lhuentse"""
  BT_44
  """Trashi Yangtse"""
  BT_TY
  """Ha"""
  BT_13
  """Trashigang"""
  BT_41
  """Gasa"""
  BT_GA
  """Dagana"""
  BT_22
  """Trongsa"""
  BT_32
  """Pemagatshel"""
  BT_43
  """North East"""
  BW_NE
  """Kgatleng"""
  BW_KL
  """Ghanzi"""
  BW_GH
  """North West"""
  BW_NW
  """Southern"""
  BW_SO
  """Kweneng"""
  BW_KW
  """Chobe"""
  BW_CH
  """Lobatse"""
  BW_LO
  """Selibe Phikwe"""
  BW_SP
  """Jwaneng"""
  BW_JW
  """Sowa Town"""
  BW_ST
  """Francistown"""
  BW_FR
  """Gaborone"""
  BW_GA
  """Kgalagadi"""
  BW_KG
  """Central"""
  BW_CE
  """South East"""
  BW_SE
  """Mogilevskaya oblast'"""
  BY_MA
  """Vitsyebskaya voblasts'"""
  BY_VI
  """Brestskaja oblast'"""
  BY_BR
  """Horad Minsk"""
  BY_HM
  """Gomel'skaya oblast'"""
  BY_HO
  """Grodnenskaya oblast'"""
  BY_HR
  """Minskaya voblasts'"""
  BY_MI
  """Belize"""
  BZ_BZ
  """Cayo"""
  BZ_CY
  """Orange Walk"""
  BZ_OW
  """Corozal"""
  BZ_CZL
  """Stann Creek"""
  BZ_SC
  """Toledo"""
  BZ_TOL
  """British Columbia"""
  CA_BC
  """Manitoba"""
  CA_MB
  """New Brunswick"""
  CA_NB
  """Saskatchewan"""
  CA_SK
  """Alberta"""
  CA_AB
  """Ontario"""
  CA_ON
  """Yukon"""
  CA_YT
  """Northwest Territories"""
  CA_NT
  """Nunavut"""
  CA_NU
  """Newfoundland and Labrador"""
  CA_NL
  """Prince Edward Island"""
  CA_PE
  """Nova Scotia"""
  CA_NS
  """Quebec"""
  CA_QC
  """Maniema"""
  CD_MA
  """Équateur"""
  CD_EQ
  """Bas-Congo"""
  CD_BC
  """Orientale"""
  CD_OR
  """Sud-Kivu"""
  CD_SK
  """Bandundu"""
  CD_BN
  """Kasai-Occidental"""
  CD_KW
  """Katanga"""
  CD_KA
  """Nord-Kivu"""
  CD_NK
  """Kasai-Oriental"""
  CD_KE
  """Kinshasa"""
  CD_KN
  """Basse-Kotto"""
  CF_BK
  """Tö-Mbömü"""
  CF_HM
  """Tö-Sangä / Mbaere-Kadeï"""
  CF_HS
  """Lobaye"""
  CF_LB
  """Ouham"""
  CF_AC
  """Gribingui"""
  CF_KB
  """Bamïngï-Bangoran"""
  CF_BB
  """Ömbëlä-Pökö"""
  CF_MP
  """Tö-Kötö"""
  CF_HK
  """Kemö-Gïrïbïngï"""
  CF_KG
  """Mbömü"""
  CF_MB
  """Nana-Mambéré"""
  CF_NM
  """Sangha"""
  CF_SE
  """Vakaga"""
  CF_VK
  """Bangî"""
  CF_BGF
  """Wâmo-Pendë"""
  CF_OP
  """Wäkä"""
  CF_UK
  """Plateaux"""
  CG_14
  """Lékoumou"""
  CG_2
  """Cuvette"""
  CG_8
  """Niari"""
  CG_9
  """Pointe-Noire"""
  CG_16
  """Cuvette-Ouest"""
  CG_15
  """Kouilou"""
  CG_5
  """Bouenza"""
  CG_11
  """Brazzaville"""
  CG_BZV
  """Pool"""
  CG_12
  """Sangha"""
  CG_13
  """Likouala"""
  CG_7
  """Basel-Landschaft"""
  CH_BL
  """Uri"""
  CH_UR
  """Jura"""
  CH_JU
  """Luzern"""
  CH_LU
  """Solothurn"""
  CH_SO
  """Thurgau"""
  CH_TG
  """Basel-Stadt"""
  CH_BS
  """Schwyz"""
  CH_SZ
  """Zug"""
  CH_ZG
  """Aargau"""
  CH_AG
  """Bern"""
  CH_BE
  """Freiburg"""
  CH_FR
  """Neuchâtel"""
  CH_NE
  """Obwalden"""
  CH_OW
  """Ticino"""
  CH_TI
  """Vaud"""
  CH_VD
  """Appenzell Ausserrhoden"""
  CH_AR
  """Genève"""
  CH_GE
  """Glarus"""
  CH_GL
  """Sankt Gallen"""
  CH_SG
  """Grigioni"""
  CH_GR
  """Nidwalden"""
  CH_NW
  """Schaffhausen"""
  CH_SH
  """Zürich"""
  CH_ZH
  """Appenzell Innerrhoden"""
  CH_AI
  """Valais"""
  CH_VS
  """Fromager (Région du)"""
  CI_18
  """Zanzan (Région du)"""
  CI_08
  """Worodougou (Région du)"""
  CI_14
  """Lagunes (Région des)"""
  CI_01
  """18 Montagnes (Région des)"""
  CI_06
  """Denguélé (Région du)"""
  CI_10
  """Sud-Bandama (Région du)"""
  CI_15
  """Nzi-Comoé (Région)"""
  CI_11
  """Marahoué (Région de la)"""
  CI_12
  """Agnébi (Région de l')"""
  CI_16
  """Moyen-Cavally (Région du)"""
  CI_19
  """Savanes (Région des)"""
  CI_03
  """Vallée du Bandama (Région de la)"""
  CI_04
  """Moyen-Comoé (Région du)"""
  CI_05
  """Lacs (Région des)"""
  CI_07
  """Bas-Sassandra (Région du)"""
  CI_09
  """Sud-Comoé (Région du)"""
  CI_13
  """Bafing (Région du)"""
  CI_17
  """Haut-Sassandra (Région du)"""
  CI_02
  """Magallanes"""
  CL_MA
  """Antofagasta"""
  CL_AN
  """Región Metropolitana de Santiago"""
  CL_RM
  """Tarapacá"""
  CL_TA
  """Biobío"""
  CL_BI
  """Arica y Parinacota"""
  CL_AP
  """Atacama"""
  CL_AT
  """Los Lagos"""
  CL_LL
  """Los Ríos"""
  CL_LR
  """Maule"""
  CL_ML
  """Araucanía"""
  CL_AR
  """Libertador General Bernardo O'Higgins"""
  CL_LI
  """Aysén"""
  CL_AI
  """Valparaíso"""
  CL_VS
  """Coquimbo"""
  CL_CO
  """South"""
  CM_SU
  """South-West"""
  CM_SW
  """North-West"""
  CM_NW
  """West"""
  CM_OU
  """Adamaoua"""
  CM_AD
  """Littoral"""
  CM_LT
  """North"""
  CM_NO
  """Centre"""
  CM_CE
  """Far North"""
  CM_EN
  """East"""
  CM_ES
  """Jiangxi"""
  CN_36
  """Hunan"""
  CN_43
  """Yunnan"""
  CN_53
  """Shanghai"""
  CN_31
  """Jiangsu"""
  CN_32
  """Shandong"""
  CN_37
  """Tianjin"""
  CN_12
  """Nei Mongol"""
  CN_15
  """Heilongjiang"""
  CN_23
  """Henan"""
  CN_41
  """Macao"""
  CN_92
  """Chongqing"""
  CN_50
  """Gansu"""
  CN_62
  """Qinghai"""
  CN_63
  """Beijing"""
  CN_11
  """Shanxi"""
  CN_14
  """Jilin"""
  CN_22
  """Hubei"""
  CN_42
  """Guangdong"""
  CN_44
  """Taiwan """
  CN_71
  """Hong Kong"""
  CN_91
  """Sichuan"""
  CN_51
  """Ningxia"""
  CN_64
  """Xinjiang"""
  CN_65
  """Hebei"""
  CN_13
  """Liaoning"""
  CN_21
  """Anhui"""
  CN_34
  """Hainan"""
  CN_46
  """Shaanxi"""
  CN_61
  """Zhejiang"""
  CN_33
  """Fujian"""
  CN_35
  """Guangxi"""
  CN_45
  """Guizhou"""
  CN_52
  """Xizang"""
  CN_54
  """Boyacá"""
  CO_BOY
  """Caquetá"""
  CO_CAQ
  """Cundinamarca"""
  CO_CUN
  """Nariño"""
  CO_NAR
  """Bolívar"""
  CO_BOL
  """Magdalena"""
  CO_MAG
  """Meta"""
  CO_MET
  """Putumayo"""
  CO_PUT
  """Vichada"""
  CO_VID
  """Amazonas"""
  CO_AMA
  """Caldas"""
  CO_CAL
  """Cauca"""
  CO_CAU
  """Cesar"""
  CO_CES
  """Distrito Capital de Bogotá"""
  CO_DC
  """La Guajira"""
  CO_LAG
  """Arauca"""
  CO_ARA
  """Norte de Santander"""
  CO_NSA
  """Tolima"""
  CO_TOL
  """Valle del Cauca"""
  CO_VAC
  """Guaviare"""
  CO_GUV
  """Huila"""
  CO_HUI
  """Sucre"""
  CO_SUC
  """Casanare"""
  CO_CAS
  """Chocó"""
  CO_CHO
  """Guainía"""
  CO_GUA
  """Quindío"""
  CO_QUI
  """Risaralda"""
  CO_RIS
  """Santander"""
  CO_SAN
  """Vaupés"""
  CO_VAU
  """Antioquia"""
  CO_ANT
  """Atlántico"""
  CO_ATL
  """Córdoba"""
  CO_COR
  """San Andrés, Providencia y Santa Catalina"""
  CO_SAP
  """Heredia"""
  CR_H
  """Limón"""
  CR_L
  """Guanacaste"""
  CR_G
  """Puntarenas"""
  CR_P
  """Alajuela"""
  CR_A
  """Cartago"""
  CR_C
  """San José"""
  CR_SJ
  """Matanzas"""
  CU_04
  """Cienfuegos"""
  CU_06
  """La Habana"""
  CU_03
  """Sancti Spíritus"""
  CU_07
  """Granma"""
  CU_12
  """Villa Clara"""
  CU_05
  """Holguín"""
  CU_11
  """Ciego de Ávila"""
  CU_08
  """Camagüey"""
  CU_09
  """Las Tunas"""
  CU_10
  """Santiago de Cuba"""
  CU_13
  """Artemisa"""
  CU_15
  """Mayabeque"""
  CU_16
  """Pinar del Río"""
  CU_01
  """Guantánamo"""
  CU_14
  """Isla de la Juventud"""
  CU_99
  """Ilhas de Barlavento"""
  CV_B
  """Porto Novo"""
  CV_PN
  """Ribeira Grande"""
  CV_RG
  """São Vicente"""
  CV_SV
  """Boa Vista"""
  CV_BV
  """Sal"""
  CV_SL
  """Tarrafal de São Nicolau"""
  CV_TS
  """Paul"""
  CV_PA
  """Ribeira Brava"""
  CV_RB
  """Ilhas de Sotavento"""
  CV_S
  """Santa Catarina do Fogo"""
  CV_CF
  """Brava"""
  CV_BR
  """Maio"""
  CV_MA
  """Praia"""
  CV_PR
  """Ribeira Grande de Santiago"""
  CV_RS
  """São Salvador do Mundo"""
  CV_SS
  """Tarrafal"""
  CV_TA
  """Santa Cruz"""
  CV_CR
  """São Domingos"""
  CV_SD
  """São Filipe"""
  CV_SF
  """Santa Catarina"""
  CV_CA
  """Mosteiros"""
  CV_MO
  """São Miguel"""
  CV_SM
  """São Lourenço dos Órgãos"""
  CV_SO
  """Larnaka"""
  CY_03
  """Keryneia"""
  CY_06
  """Lefkosia"""
  CY_01
  """Gazimaǧusa"""
  CY_04
  """Pafos"""
  CY_05
  """Leymosun"""
  CY_02
  """Středočeský kraj"""
  CZ_ST
  """Nymburk"""
  CZ_208
  """Kutná Hora"""
  CZ_205
  """Rakovník"""
  CZ_20C
  """Kladno"""
  CZ_203
  """Mladá Boleslav"""
  CZ_207
  """Mělník"""
  CZ_206
  """Praha-západ"""
  CZ_20A
  """Příbram"""
  CZ_20B
  """Benešov"""
  CZ_201
  """Beroun"""
  CZ_202
  """Kolín"""
  CZ_204
  """Praha-východ"""
  CZ_209
  """Vysočina"""
  CZ_VY
  """Havlíčkův Brod"""
  CZ_611
  """Jihlava"""
  CZ_612
  """Třebíč"""
  CZ_614
  """Pelhřimov"""
  CZ_613
  """Žd'ár nad Sázavou"""
  CZ_615
  """Pardubický kraj"""
  CZ_PA
  """Chrudim"""
  CZ_531
  """Pardubice"""
  CZ_532
  """Ústí nad Orlicí"""
  CZ_534
  """Svitavy"""
  CZ_533
  """Moravskoslezský kraj"""
  CZ_MO
  """Bruntál"""
  CZ_801
  """Frýdek Místek"""
  CZ_802
  """Karviná"""
  CZ_803
  """Ostrava město"""
  CZ_806
  """Nový Jičín"""
  CZ_804
  """Opava"""
  CZ_805
  """Jihočeský kraj"""
  CZ_JC
  """České Budějovice"""
  CZ_311
  """Písek"""
  CZ_314
  """Prachatice"""
  CZ_315
  """Český Krumlov"""
  CZ_312
  """Strakonice"""
  CZ_316
  """Tábor"""
  CZ_317
  """Jindřichův Hradec"""
  CZ_313
  """Olomoucký kraj"""
  CZ_OL
  """Prostĕjov"""
  CZ_713
  """Přerov"""
  CZ_714
  """Olomouc"""
  CZ_712
  """Jeseník"""
  CZ_711
  """Šumperk"""
  CZ_715
  """Jihomoravský kraj"""
  CZ_JM
  """Znojmo"""
  CZ_627
  """Brno-venkov"""
  CZ_623
  """Břeclav"""
  CZ_624
  """Vyškov"""
  CZ_626
  """Blansko"""
  CZ_621
  """Brno-město"""
  CZ_622
  """Hodonín"""
  CZ_625
  """Zlínský kraj"""
  CZ_ZL
  """Zlín"""
  CZ_724
  """Kromĕříž"""
  CZ_721
  """Uherské Hradištĕ"""
  CZ_722
  """Vsetín"""
  CZ_723
  """Ústecký kraj"""
  CZ_US
  """Most"""
  CZ_425
  """Litoměřice"""
  CZ_423
  """Děčín"""
  CZ_421
  """Chomutov"""
  CZ_422
  """Louny"""
  CZ_424
  """Teplice"""
  CZ_426
  """Ústí nad Labem"""
  CZ_427
  """Karlovarský kraj"""
  CZ_KA
  """Cheb"""
  CZ_411
  """Karlovy Vary"""
  CZ_412
  """Sokolov"""
  CZ_413
  """Královéhradecký kraj"""
  CZ_KR
  """Náchod"""
  CZ_523
  """Hradec Králové"""
  CZ_521
  """Rychnov nad Kněžnou"""
  CZ_524
  """Jičín"""
  CZ_522
  """Trutnov"""
  CZ_525
  """Liberecký kraj"""
  CZ_LI
  """Česká Lípa"""
  CZ_511
  """Semily"""
  CZ_514
  """Jablonec nad Nisou"""
  CZ_512
  """Liberec"""
  CZ_513
  """Plzeňský kraj"""
  CZ_PL
  """Klatovy"""
  CZ_322
  """Domažlice"""
  CZ_321
  """Tachov"""
  CZ_327
  """Plzeň-sever"""
  CZ_325
  """Plzeň-jih"""
  CZ_324
  """Plzeň-město"""
  CZ_323
  """Rokycany"""
  CZ_326
  """Praha, hlavní mešto"""
  CZ_PR
  """Praha 1"""
  CZ_101
  """Praha 4"""
  CZ_104
  """Praha 8"""
  CZ_108
  """Praha 9"""
  CZ_109
  """Praha 15"""
  CZ_10F
  """Praha 3"""
  CZ_103
  """Praha 6"""
  CZ_106
  """Praha 14"""
  CZ_10E
  """Praha 11"""
  CZ_10B
  """Praha 5"""
  CZ_105
  """Praha 7"""
  CZ_107
  """Praha 10"""
  CZ_10A
  """Praha 12"""
  CZ_10C
  """Praha 2"""
  CZ_102
  """Praha 13"""
  CZ_10D
  """Rheinland-Pfalz"""
  DE_RP
  """Sachsen"""
  DE_SN
  """Baden-Württemberg"""
  DE_BW
  """Mecklenburg-Vorpommern"""
  DE_MV
  """Nordrhein-Westfalen"""
  DE_NW
  """Saarland"""
  DE_SL
  """Thüringen"""
  DE_TH
  """Sachsen-Anhalt"""
  DE_ST
  """Hamburg"""
  DE_HH
  """Brandenburg"""
  DE_BB
  """Berlin"""
  DE_BE
  """Bayern"""
  DE_BY
  """Bremen"""
  DE_HB
  """Hessen"""
  DE_HE
  """Niedersachsen"""
  DE_NI
  """Schleswig-Holstein"""
  DE_SH
  """Tadjourah"""
  DJ_TA
  """Ūbūk"""
  DJ_OB
  """Arta"""
  DJ_AR
  """Dikhīl"""
  DJ_DI
  """Jībūtī"""
  DJ_DJ
  """‘Alī Ṣabīḥ"""
  DJ_AS
  """Syddanmark"""
  DK_83
  """Midtjylland"""
  DK_82
  """Sjælland"""
  DK_85
  """Nordjylland"""
  DK_81
  """Hovedstaden"""
  DK_84
  """Saint John"""
  DM_05
  """Saint Luke"""
  DM_07
  """Saint Joseph"""
  DM_06
  """Saint Mark"""
  DM_08
  """Saint Patrick"""
  DM_09
  """Saint David"""
  DM_03
  """Saint Andrew"""
  DM_02
  """Saint Peter"""
  DM_11
  """Saint George"""
  DM_04
  """Saint Paul"""
  DM_10
  """Cibao Nordeste"""
  DO_33
  """Hermanas Mirabal"""
  DO_19
  """Samaná"""
  DO_20
  """María Trinidad Sánchez"""
  DO_14
  """Duarte"""
  DO_06
  """Cibao Noroeste"""
  DO_34
  """Santiago Rodríguez"""
  DO_26
  """Valverde"""
  DO_27
  """Dajabón"""
  DO_05
  """Monte Cristi"""
  DO_15
  """Cibao Norte"""
  DO_35
  """Espaillat"""
  DO_09
  """Puerto Plata"""
  DO_18
  """Santiago"""
  DO_25
  """Cibao Sur"""
  DO_36
  """Sánchez Ramírez"""
  DO_24
  """La Vega"""
  DO_13
  """Monseñor Nouel"""
  DO_28
  """El Valle"""
  DO_37
  """La Estrelleta"""
  DO_07
  """San Juan"""
  DO_22
  """Enriquillo"""
  DO_38
  """Baoruco"""
  DO_03
  """Pedernales"""
  DO_16
  """Barahona"""
  DO_04
  """Independencia"""
  DO_10
  """Higuamo"""
  DO_39
  """San Pedro de Macorís"""
  DO_23
  """Hato Mayor"""
  DO_30
  """Monte Plata"""
  DO_29
  """Ozama"""
  DO_40
  """Santo Domingo"""
  DO_32
  """Distrito Nacional (Santo Domingo)"""
  DO_01
  """Valdesia"""
  DO_41
  """Peravia"""
  DO_17
  """San Cristóbal"""
  DO_21
  """San José de Ocoa"""
  DO_31
  """Azua"""
  DO_02
  """Yuma"""
  DO_42
  """La Altagracia"""
  DO_11
  """El Seibo"""
  DO_08
  """La Romana"""
  DO_12
  """Tébessa"""
  DZ_12
  """Médéa"""
  DZ_26
  """Mascara"""
  DZ_29
  """Bordj Bou Arréridj"""
  DZ_34
  """Tindouf"""
  DZ_37
  """Béjaïa"""
  DZ_06
  """Tamanrasset"""
  DZ_11
  """Tlemcen"""
  DZ_13
  """Mostaganem"""
  DZ_27
  """Khenchela"""
  DZ_40
  """Laghouat"""
  DZ_03
  """Blida"""
  DZ_09
  """Tiaret"""
  DZ_14
  """Tizi Ouzou"""
  DZ_15
  """Sétif"""
  DZ_19
  """Saïda"""
  DZ_20
  """Boumerdès"""
  DZ_35
  """Souk Ahras"""
  DZ_41
  """Tipaza"""
  DZ_42
  """Aïn Defla"""
  DZ_44
  """Chlef"""
  DZ_02
  """Oum el Bouaghi"""
  DZ_04
  """Batna"""
  DZ_05
  """Annaba"""
  DZ_23
  """El Oued"""
  DZ_39
  """Adrar"""
  DZ_01
  """Béchar"""
  DZ_08
  """Alger"""
  DZ_16
  """Msila"""
  DZ_28
  """Oran"""
  DZ_31
  """Biskra"""
  DZ_07
  """Guelma"""
  DZ_24
  """Illizi"""
  DZ_33
  """El Tarf"""
  DZ_36
  """Tissemsilt"""
  DZ_38
  """Naama"""
  DZ_45
  """Bouira"""
  DZ_10
  """Skikda"""
  DZ_21
  """Constantine"""
  DZ_25
  """El Bayadh"""
  DZ_32
  """Mila"""
  DZ_43
  """Aïn Témouchent"""
  DZ_46
  """Relizane"""
  DZ_48
  """Djelfa"""
  DZ_17
  """Jijel"""
  DZ_18
  """Sidi Bel Abbès"""
  DZ_22
  """Ouargla"""
  DZ_30
  """Ghardaïa"""
  DZ_47
  """Bolívar"""
  EC_B
  """Los Ríos"""
  EC_R
  """Esmeraldas"""
  EC_E
  """Guayas"""
  EC_G
  """Cotopaxi"""
  EC_X
  """Pastaza"""
  EC_Y
  """Azuay"""
  EC_A
  """Orellana"""
  EC_D
  """Loja"""
  EC_L
  """El Oro"""
  EC_O
  """Santa Elena"""
  EC_SE
  """Zamora-Chinchipe"""
  EC_Z
  """Chimborazo"""
  EC_H
  """Santo Domingo de los Tsáchilas"""
  EC_SD
  """Imbabura"""
  EC_I
  """Manabí"""
  EC_M
  """Pichincha"""
  EC_P
  """Galápagos"""
  EC_W
  """Carchi"""
  EC_C
  """Cañar"""
  EC_F
  """Morona-Santiago"""
  EC_S
  """Sucumbíos"""
  EC_U
  """Napo"""
  EC_N
  """Tungurahua"""
  EC_T
  """Põlvamaa"""
  EE_65
  """Hiiumaa"""
  EE_39
  """Tartumaa"""
  EE_78
  """Jõgevamaa"""
  EE_49
  """Järvamaa"""
  EE_51
  """Raplamaa"""
  EE_70
  """Viljandimaa"""
  EE_84
  """Harjumaa"""
  EE_37
  """Ida-Virumaa"""
  EE_44
  """Läänemaa"""
  EE_57
  """Lääne-Virumaa"""
  EE_59
  """Pärnumaa"""
  EE_67
  """Saaremaa"""
  EE_74
  """Valgamaa"""
  EE_82
  """Võrumaa"""
  EE_86
  """Al Iskandarīyah"""
  EG_ALX
  """Aswān"""
  EG_ASN
  """Janūb Sīnā'"""
  EG_JS
  """Kafr ash Shaykh"""
  EG_KFS
  """Al Minyā"""
  EG_MN
  """Asyūţ"""
  EG_AST
  """Banī Suwayf"""
  EG_BNS
  """Al Qāhirah"""
  EG_C
  """Al Fayyūm"""
  EG_FYM
  """Būr Sa‘īd"""
  EG_PTS
  """Dumyāţ"""
  EG_DT
  """Al Jīzah"""
  EG_GZ
  """Al Ismā'īlīyah"""
  EG_IS
  """Sūhāj"""
  EG_SHG
  """Al Baḩr al Aḩmar"""
  EG_BA
  """Al Qalyūbīyah"""
  EG_KB
  """Ash Sharqīyah"""
  EG_SHR
  """Ad Daqahlīyah"""
  EG_DK
  """Al Uqşur"""
  EG_LX
  """Shamāl Sīnā'"""
  EG_SIN
  """Al Wādī al Jadīd"""
  EG_WAD
  """Al Gharbīyah"""
  EG_GH
  """Qinā"""
  EG_KN
  """Al Minūfīyah"""
  EG_MNF
  """As Suways"""
  EG_SUZ
  """Al Buḩayrah"""
  EG_BH
  """Maţrūḩ"""
  EG_MT
  """Gash-Barka"""
  ER_GB
  """Al Awsaţ"""
  ER_MA
  """Semienawi K’eyyĭḥ Baḥri"""
  ER_SK
  """Janūbī al Baḩrī al Aḩmar"""
  ER_DK
  """Debub"""
  ER_DU
  """‘Anseba"""
  ER_AN
  """Andalucía"""
  ES_AN
  """Almería"""
  ES_AL
  """Jaén"""
  ES_J
  """Sevilla"""
  ES_SE
  """Cádiz"""
  ES_CA
  """Granada"""
  ES_GR
  """Huelva"""
  ES_H
  """Málaga"""
  ES_MA
  """Córdoba"""
  ES_CO
  """Euskal Herria"""
  ES_PV
  """Bizkaia*"""
  ES_BI
  """Gipuzkoa*"""
  ES_SS
  """Araba*"""
  ES_VI
  """Cantabria"""
  ES_CB
  """Cantabria"""
  ES_S
  """Murcia, Región de"""
  ES_MC
  """Murcia"""
  ES_MU
  """Aragón"""
  ES_AR
  """Zaragoza"""
  ES_Z
  """Huesca"""
  ES_HU
  """Teruel"""
  ES_TE
  """Asturias, Principado de"""
  ES_AS
  """Asturias"""
  ES_O
  """Ceuta"""
  ES_CE
  """Galicia """
  ES_GA
  """Pontevedra """
  ES_PO
  """A Coruña """
  ES_C
  """Lugo """
  ES_LU
  """Ourense """
  ES_OR
  """La Rioja"""
  ES_RI
  """La Rioja"""
  ES_LO
  """Valenciana, Comunitat*"""
  ES_VC
  """València*"""
  ES_V
  """Castellón"""
  ES_CS
  """Alacant*"""
  ES_A
  """Catalunya """
  ES_CT
  """Tarragona """
  ES_T
  """Girona """
  ES_GI
  """Barcelona """
  ES_B
  """Lleida """
  ES_L
  """Illes Balears """
  ES_IB
  """Balears """
  ES_PM
  """Castilla-La Mancha"""
  ES_CM
  """Ciudad Real"""
  ES_CR
  """Guadalajara"""
  ES_GU
  """Albacete"""
  ES_AB
  """Cuenca"""
  ES_CU
  """Toledo"""
  ES_TO
  """Extremadura"""
  ES_EX
  """Cáceres"""
  ES_CC
  """Badajoz"""
  ES_BA
  """Madrid, Comunidad de"""
  ES_MD
  """Madrid"""
  ES_M
  """Melilla"""
  ES_ML
  """Castilla y León"""
  ES_CL
  """Salamanca"""
  ES_SA
  """Ávila"""
  ES_AV
  """Soria"""
  ES_SO
  """Palencia"""
  ES_P
  """Valladolid"""
  ES_VA
  """Burgos"""
  ES_BU
  """Segovia"""
  ES_SG
  """Zamora"""
  ES_ZA
  """León"""
  ES_LE
  """Canarias"""
  ES_CN
  """Santa Cruz de Tenerife"""
  ES_TF
  """Las Palmas"""
  ES_GC
  """Nafarroako Foru Komunitatea*"""
  ES_NC
  """Navarra"""
  ES_NA
  """Benshangul-Gumaz"""
  ET_BE
  """Harari People"""
  ET_HA
  """Somali"""
  ET_SO
  """Dire Dawa"""
  ET_DD
  """Gambela Peoples"""
  ET_GA
  """Amara"""
  ET_AM
  """Addis Ababa"""
  ET_AA
  """Afar"""
  ET_AF
  """Oromia"""
  ET_OR
  """Tigrai"""
  ET_TI
  """Southern Nations, Nationalities and Peoples"""
  ET_SN
  """Södra Karelen"""
  FI_02
  """Päijänne-Tavastland"""
  FI_16
  """Egentliga Tavastland"""
  FI_06
  """Mellersta Finland"""
  FI_08
  """Pohjois-Karjala"""
  FI_13
  """Nyland"""
  FI_18
  """Ahvenanmaan maakunta"""
  FI_01
  """Norra Savolax"""
  FI_15
  """Norra Österbotten"""
  FI_14
  """Etelä-Savo"""
  FI_04
  """Mellersta Österbotten"""
  FI_07
  """Kymmenedalen"""
  FI_09
  """Pirkanmaa"""
  FI_11
  """Pohjanmaa"""
  FI_12
  """Varsinais-Suomi"""
  FI_19
  """Satakunda"""
  FI_17
  """Södra Österbotten"""
  FI_03
  """Kainuu"""
  FI_05
  """Lappi"""
  FI_10
  """Central"""
  FJ_C
  """Rotuma"""
  FJ_R
  """Western"""
  FJ_W
  """Northern"""
  FJ_N
  """Bua"""
  FJ_02
  """Ba"""
  FJ_01
  """Cakaudrove"""
  FJ_03
  """Kadavu"""
  FJ_04
  """Lau"""
  FJ_05
  """Lomaiviti"""
  FJ_06
  """Macuata"""
  FJ_07
  """Nadroga and Navosa"""
  FJ_08
  """Ra"""
  FJ_11
  """Naitasiri"""
  FJ_09
  """Namosi"""
  FJ_10
  """Rewa"""
  FJ_12
  """Serua"""
  FJ_13
  """Tailevu"""
  FJ_14
  """Eastern"""
  FJ_E
  """Chuuk"""
  FM_TRK
  """Pohnpei"""
  FM_PNI
  """Kosrae"""
  FM_KSA
  """Yap"""
  FM_YAP
  """Saint-Barthélemy """
  FR_BL
  """Champagne-Ardenne"""
  FR_G
  """Ardennes"""
  FR_08
  """Marne"""
  FR_51
  """Aube"""
  FR_10
  """Haute-Marne"""
  FR_52
  """Polynésie française """
  FR_PF
  """La Réunion """
  FR_RE
  """Alsace"""
  FR_A
  """Bas-Rhin"""
  FR_67
  """Haut-Rhin"""
  FR_68
  """Clipperton"""
  FR_CP
  """Corse"""
  FR_H
  """Corse-du-Sud"""
  FR_2A
  """Haute-Corse"""
  FR_2B
  """Lorraine"""
  FR_M
  """Vosges"""
  FR_88
  """Meuse"""
  FR_55
  """Moselle"""
  FR_57
  """Meurthe-et-Moselle"""
  FR_54
  """Saint-Martin """
  FR_MF
  """Midi-Pyrénées"""
  FR_N
  """Aveyron"""
  FR_12
  """Haute-Garonne"""
  FR_31
  """Gers"""
  FR_32
  """Ariège"""
  FR_09
  """Hautes-Pyrénées"""
  FR_65
  """Lot"""
  FR_46
  """Tarn-et-Garonne"""
  FR_82
  """Tarn"""
  FR_81
  """Haute-Normandie"""
  FR_Q
  """Seine-Maritime"""
  FR_76
  """Eure"""
  FR_27
  """Pays-de-la-Loire"""
  FR_R
  """Loire-Atlantique"""
  FR_44
  """Vendée"""
  FR_85
  """Mayenne"""
  FR_53
  """Maine-et-Loire"""
  FR_49
  """Sarthe"""
  FR_72
  """Provence-Alpes-Côte-d'Azur"""
  FR_U
  """Bouches-du-Rhône"""
  FR_13
  """Alpes-de-Haute-Provence"""
  FR_04
  """Hautes-Alpes"""
  FR_05
  """Var"""
  FR_83
  """Alpes-Maritimes"""
  FR_06
  """Vaucluse"""
  FR_84
  """Centre"""
  FR_F
  """Cher"""
  FR_18
  """Loir-et-Cher"""
  FR_41
  """Loiret"""
  FR_45
  """Indre-et-Loire"""
  FR_37
  """Indre"""
  FR_36
  """Eure-et-Loir"""
  FR_28
  """Guadeloupe """
  FR_GP
  """Île-de-France"""
  FR_J
  """Seine-Saint-Denis"""
  FR_93
  """Seine-et-Marne"""
  FR_77
  """Yvelines"""
  FR_78
  """Val-d'Oise"""
  FR_95
  """Hauts-de-Seine"""
  FR_92
  """Paris"""
  FR_75
  """Essonne"""
  FR_91
  """Val-de-Marne"""
  FR_94
  """Nord-Pas-de-Calais"""
  FR_O
  """Nord"""
  FR_59
  """Pas-de-Calais"""
  FR_62
  """Limousin"""
  FR_L
  """Creuse"""
  FR_23
  """Corrèze"""
  FR_19
  """Haute-Vienne"""
  FR_87
  """Martinique """
  FR_MQ
  """Rhône-Alpes"""
  FR_V
  """Loire"""
  FR_42
  """Drôme"""
  FR_26
  """Ardèche"""
  FR_07
  """Ain"""
  FR_01
  """Isère"""
  FR_38
  """Haute-Savoie"""
  FR_74
  """Rhône"""
  FR_69
  """Savoie"""
  FR_73
  """Auvergne"""
  FR_C
  """Puy-de-Dôme"""
  FR_63
  """Allier"""
  FR_03
  """Cantal"""
  FR_15
  """Haute-Loire"""
  FR_43
  """Guyane """
  FR_GF
  """Nouvelle-Calédonie """
  FR_NC
  """Saint-Pierre-et-Miquelon """
  FR_PM
  """Picardie"""
  FR_S
  """Oise"""
  FR_60
  """Aisne"""
  FR_02
  """Somme"""
  FR_80
  """Poitou-Charentes"""
  FR_T
  """Charente"""
  FR_16
  """Deux-Sèvres"""
  FR_79
  """Charente-Maritime"""
  FR_17
  """Vienne"""
  FR_86
  """Terres australes françaises """
  FR_TF
  """Wallis-et-Futuna """
  FR_WF
  """Aquitaine"""
  FR_B
  """Pyrénées-Atlantiques"""
  FR_64
  """Landes"""
  FR_40
  """Dordogne"""
  FR_24
  """Lot-et-Garonne"""
  FR_47
  """Gironde"""
  FR_33
  """Basse-Normandie"""
  FR_P
  """Orne"""
  FR_61
  """Calvados"""
  FR_14
  """Manche"""
  FR_50
  """Bourgogne"""
  FR_D
  """Saône-et-Loire"""
  FR_71
  """Côte-d'Or"""
  FR_21
  """Yonne"""
  FR_89
  """Nièvre"""
  FR_58
  """Bretagne"""
  FR_E
  """Côtes-d'Armor"""
  FR_22
  """Finistère"""
  FR_29
  """Morbihan"""
  FR_56
  """Ille-et-Vilaine"""
  FR_35
  """Franche-Comté"""
  FR_I
  """Doubs"""
  FR_25
  """Haute-Saône"""
  FR_70
  """Territoire de Belfort"""
  FR_90
  """Jura"""
  FR_39
  """Languedoc-Roussillon"""
  FR_K
  """Gard"""
  FR_30
  """Aude"""
  FR_11
  """Lozère"""
  FR_48
  """Hérault"""
  FR_34
  """Pyrénées-Orientales"""
  FR_66
  """Mayotte """
  FR_YT
  """Moyen-Ogooué"""
  GA_3
  """Nyanga"""
  GA_5
  """Estuaire"""
  GA_1
  """Ogooué-Ivindo"""
  GA_6
  """Ogooué-Lolo"""
  GA_7
  """Ogooué-Maritime"""
  GA_8
  """Haut-Ogooué"""
  GA_2
  """Ngounié"""
  GA_4
  """Woleu-Ntem"""
  GA_9
  """United Kingdom"""
  GB_UKM
  """Great Britain"""
  GB_GBN
  """Scotland"""
  GB_SCT
  """North Lanarkshire"""
  GB_NLK
  """Renfrewshire"""
  GB_RFW
  """Perth and Kinross"""
  GB_PKN
  """Angus"""
  GB_ANS
  """Falkirk"""
  GB_FAL
  """Glasgow City"""
  GB_GLG
  """Moray"""
  GB_MRY
  """Dumfries and Galloway"""
  GB_DGY
  """East Lothian"""
  GB_ELN
  """South Ayrshire"""
  GB_SAY
  """Aberdeenshire"""
  GB_ABD
  """Eilean Siar"""
  GB_ELS
  """North Ayrshire"""
  GB_NAY
  """West Lothian"""
  GB_WLN
  """Argyll and Bute"""
  GB_AGB
  """Clackmannanshire"""
  GB_CLK
  """East Dunbartonshire"""
  GB_EDU
  """Fife"""
  GB_FIF
  """Midlothian"""
  GB_MLN
  """Orkney Islands"""
  GB_ORK
  """Scottish Borders, The"""
  GB_SCB
  """South Lanarkshire"""
  GB_SLK
  """Stirling"""
  GB_STG
  """Shetland Islands"""
  GB_ZET
  """West Dunbartonshire"""
  GB_WDU
  """Aberdeen City"""
  GB_ABE
  """Dundee City"""
  GB_DND
  """East Ayrshire"""
  GB_EAY
  """East Renfrewshire"""
  GB_ERW
  """Highland"""
  GB_HLD
  """Inverclyde"""
  GB_IVC
  """Edinburgh, City of"""
  GB_EDH
  """England and Wales"""
  GB_EAW
  """England"""
  GB_ENG
  """Greenwich"""
  GB_GRE
  """Halton"""
  GB_HAL
  """Haringey"""
  GB_HRY
  """Kingston upon Hull"""
  GB_KHL
  """North East Lincolnshire"""
  GB_NEL
  """Norfolk"""
  GB_NFK
  """Portsmouth"""
  GB_POR
  """South Gloucestershire"""
  GB_SGC
  """West Berkshire"""
  GB_WBK
  """Wandsworth"""
  GB_WND
  """Warrington"""
  GB_WRT
  """Isles of Scilly"""
  GB_IOS
  """Bedford"""
  GB_BDF
  """Barking and Dagenham"""
  GB_BDG
  """Buckinghamshire"""
  GB_BKM
  """Bristol, City of"""
  GB_BST
  """Cambridgeshire"""
  GB_CAM
  """Doncaster"""
  GB_DNC
  """Kirklees"""
  GB_KIR
  """London, City of"""
  GB_LND
  """Luton"""
  GB_LUT
  """Manchester"""
  GB_MAN
  """Milton Keynes"""
  GB_MIK
  """North Lincolnshire"""
  GB_NLN
  """North Somerset"""
  GB_NSM
  """North Tyneside"""
  GB_NTY
  """Plymouth"""
  GB_PLY
  """Reading"""
  GB_RDG
  """Shropshire"""
  GB_SHR
  """Sunderland"""
  GB_SND
  """South Tyneside"""
  GB_STY
  """Southwark"""
  GB_SWK
  """Wirral"""
  GB_WRL
  """Westminster"""
  GB_WSM
  """Bath and North East Somerset"""
  GB_BAS
  """Birmingham"""
  GB_BIR
  """Blackpool"""
  GB_BPL
  """Cheshire West and Chester"""
  GB_CHW
  """Hounslow"""
  GB_HNS
  """Hertfordshire"""
  GB_HRT
  """Kingston upon Thames"""
  GB_KTT
  """Leicestershire"""
  GB_LEC
  """Rochdale"""
  GB_RCH
  """Rotherham"""
  GB_ROT
  """Suffolk"""
  GB_SFK
  """Surrey"""
  GB_SRY
  """Southampton"""
  GB_STH
  """Stockton-on-Tees"""
  GB_STT
  """Swindon"""
  GB_SWD
  """Telford and Wrekin"""
  GB_TFW
  """Windsor and Maidenhead"""
  GB_WNM
  """Worcestershire"""
  GB_WOR
  """West Sussex"""
  GB_WSX
  """Bexley"""
  GB_BEX
  """Bournemouth"""
  GB_BMH
  """Bradford"""
  GB_BRD
  """Bury"""
  GB_BUR
  """Cheshire East"""
  GB_CHE
  """Cornwall"""
  GB_CON
  """Hampshire"""
  GB_HAM
  """Liverpool"""
  GB_LIV
  """North Yorkshire"""
  GB_NYK
  """Oxfordshire"""
  GB_OXF
  """Richmond upon Thames"""
  GB_RIC
  """Rutland"""
  GB_RUT
  """Sandwell"""
  GB_SAW
  """Sheffield"""
  GB_SHF
  """Slough"""
  GB_SLG
  """Thurrock"""
  GB_THR
  """Torbay"""
  GB_TOB
  """Waltham Forest"""
  GB_WFT
  """Wiltshire"""
  GB_WIL
  """Wakefield"""
  GB_WKF
  """York"""
  GB_YOR
  """Calderdale"""
  GB_CLD
  """Coventry"""
  GB_COV
  """Derby"""
  GB_DER
  """Devon"""
  GB_DEV
  """Dudley"""
  GB_DUD
  """Gloucestershire"""
  GB_GLS
  """Hackney"""
  GB_HCK
  """Harrow"""
  GB_HRW
  """Isle of Wight"""
  GB_IOW
  """Islington"""
  GB_ISL
  """Kensington and Chelsea"""
  GB_KEC
  """Lambeth"""
  GB_LBH
  """Leeds"""
  GB_LDS
  """Newcastle upon Tyne"""
  GB_NET
  """Nottingham"""
  GB_NGM
  """Salford"""
  GB_SLF
  """Solihull"""
  GB_SOL
  """Stoke-on-Trent"""
  GB_STE
  """Wolverhampton"""
  GB_WLV
  """Wokingham"""
  GB_WOK
  """Barnet"""
  GB_BNE
  """Brighton and Hove"""
  GB_BNH
  """Barnsley"""
  GB_BNS
  """Darlington"""
  GB_DAL
  """East Riding of Yorkshire"""
  GB_ERY
  """Essex"""
  GB_ESS
  """Havering"""
  GB_HAV
  """Hillingdon"""
  GB_HIL
  """Hartlepool"""
  GB_HPL
  """Kent"""
  GB_KEN
  """Leicester"""
  GB_LCE
  """Middlesbrough"""
  GB_MDB
  """Merton"""
  GB_MRT
  """Redbridge"""
  GB_RDB
  """Sefton"""
  GB_SFT
  """St. Helens"""
  GB_SHN
  """Trafford"""
  GB_TRF
  """Tower Hamlets"""
  GB_TWH
  """Warwickshire"""
  GB_WAR
  """Walsall"""
  GB_WLL
  """Derbyshire"""
  GB_DBY
  """Dorset"""
  GB_DOR
  """Enfield"""
  GB_ENF
  """Gateshead"""
  GB_GAT
  """Hammersmith and Fulham"""
  GB_HMF
  """Knowsley"""
  GB_KWL
  """Lancashire"""
  GB_LAN
  """Lewisham"""
  GB_LEW
  """Lincolnshire"""
  GB_LIN
  """Northumberland"""
  GB_NBL
  """Poole"""
  GB_POL
  """Redcar and Cleveland"""
  GB_RCC
  """Staffordshire"""
  GB_STS
  """Tameside"""
  GB_TAM
  """Wigan"""
  GB_WGN
  """Blackburn with Darwen"""
  GB_BBD
  """Brent"""
  GB_BEN
  """Bolton"""
  GB_BOL
  """Bracknell Forest"""
  GB_BRC
  """Central Bedfordshire"""
  GB_CBF
  """Cumbria"""
  GB_CMA
  """Camden"""
  GB_CMD
  """Croydon"""
  GB_CRY
  """County Durham"""
  GB_DUR
  """East Sussex"""
  GB_ESX
  """Herefordshire"""
  GB_HEF
  """Medway"""
  GB_MDW
  """Northamptonshire"""
  GB_NTH
  """Nottinghamshire"""
  GB_NTT
  """Newham"""
  GB_NWM
  """Oldham"""
  GB_OLD
  """Peterborough"""
  GB_PTE
  """Stockport"""
  GB_SKP
  """Somerset"""
  GB_SOM
  """Southend-on-Sea"""
  GB_SOS
  """Sutton"""
  GB_STN
  """Bromley"""
  GB_BRY
  """Ealing"""
  GB_EAL
  """Wales """
  GB_WLS
  """Neath Port Talbot """
  GB_NTL
  """Rhondda, Cynon, Taff """
  GB_RCT
  """Bridgend """
  GB_BGE
  """Newport """
  GB_NWP
  """Blaenau Gwent"""
  GB_BGW
  """Carmarthenshire """
  GB_CMN
  """Denbighshire """
  GB_DEN
  """Flintshire """
  GB_FLN
  """Merthyr Tydfil """
  GB_MTY
  """Powys"""
  GB_POW
  """Vale of Glamorgan, The """
  GB_VGL
  """Isle of Anglesey """
  GB_AGY
  """Caerphilly """
  GB_CAY
  """Gwynedd"""
  GB_GWN
  """Wrexham """
  GB_WRX
  """Ceredigion """
  GB_CGN
  """Monmouthshire """
  GB_MON
  """Pembrokeshire """
  GB_PEM
  """Torfaen """
  GB_TOF
  """Cardiff """
  GB_CRF
  """Swansea """
  GB_SWA
  """Conwy"""
  GB_CWY
  """Northern Ireland"""
  GB_NIR
  """North Down"""
  GB_NDN
  """Newry and Mourne"""
  GB_NYM
  """Antrim"""
  GB_ANT
  """Down"""
  GB_DOW
  """Derry"""
  GB_DRY
  """Fermanagh"""
  GB_FER
  """Newtownabbey"""
  GB_NTA
  """Ards"""
  GB_ARD
  """Craigavon"""
  GB_CGV
  """Lisburn"""
  GB_LSB
  """Banbridge"""
  GB_BNB
  """Castlereagh"""
  GB_CSR
  """Moyle"""
  GB_MYL
  """Omagh"""
  GB_OMH
  """Carrickfergus"""
  GB_CKF
  """Magherafelt"""
  GB_MFT
  """Armagh"""
  GB_ARM
  """Ballymena"""
  GB_BLA
  """Limavady"""
  GB_LMV
  """Strabane"""
  GB_STB
  """Cookstown"""
  GB_CKT
  """Dungannon and South Tyrone"""
  GB_DGN
  """Larne"""
  GB_LRN
  """Belfast"""
  GB_BFS
  """Ballymoney"""
  GB_BLY
  """Coleraine"""
  GB_CLR
  """Saint John"""
  GD_04
  """Southern Grenadine Islands"""
  GD_10
  """Saint David"""
  GD_02
  """Saint Mark"""
  GD_05
  """Saint Andrew"""
  GD_01
  """Saint George"""
  GD_03
  """Saint Patrick"""
  GD_06
  """Abkhazia"""
  GE_AB
  """Ajaria"""
  GE_AJ
  """Mtskheta-Mtianeti"""
  GE_MM
  """Samegrelo-Zemo Svaneti"""
  GE_SZ
  """Samtskhe-Javakheti"""
  GE_SJ
  """Shida Kartli"""
  GE_SK
  """Imereti"""
  GE_IM
  """Guria"""
  GE_GU
  """Rach'a-Lechkhumi-Kvemo Svaneti"""
  GE_RL
  """Tbilisi"""
  GE_TB
  """K'akheti"""
  GE_KA
  """Kvemo Kartli"""
  GE_KK
  """Western"""
  GH_WP
  """Eastern"""
  GH_EP
  """Brong-Ahafo"""
  GH_BA
  """Volta"""
  GH_TV
  """Upper West"""
  GH_UW
  """Central"""
  GH_CP
  """Northern"""
  GH_NP
  """Ashanti"""
  GH_AH
  """Greater Accra"""
  GH_AA
  """Upper East"""
  GH_UE
  """Qeqqata Kommunia"""
  GL_QE
  """Qaasuitsup Kommunia"""
  GL_QA
  """Kommune Kujalleq"""
  GL_KU
  """Kommuneqarfik Sermersooq"""
  GL_SM
  """Central River"""
  GM_M
  """Upper River"""
  GM_U
  """Western"""
  GM_W
  """Lower River"""
  GM_L
  """Banjul"""
  GM_B
  """North Bank"""
  GM_N
  """Mamou"""
  GN_M
  """Dalaba"""
  GN_DL
  """Pita"""
  GN_PI
  """Mamou"""
  GN_MM
  """Boké"""
  GN_B
  """Boké"""
  GN_BK
  """Boffa"""
  GN_BF
  """Gaoual"""
  GN_GA
  """Fria"""
  GN_FR
  """Koundara"""
  GN_KN
  """Faranah"""
  GN_F
  """Faranah"""
  GN_FA
  """Dabola"""
  GN_DB
  """Kissidougou"""
  GN_KS
  """Dinguiraye"""
  GN_DI
  """Conakry"""
  GN_C
  """Kankan"""
  GN_K
  """Siguiri"""
  GN_SI
  """Mandiana"""
  GN_MD
  """Kankan"""
  GN_KA
  """Kérouané"""
  GN_KE
  """Kouroussa"""
  GN_KO
  """Labé"""
  GN_L
  """Koubia"""
  GN_KB
  """Labé"""
  GN_LA
  """Mali"""
  GN_ML
  """Tougué"""
  GN_TO
  """Lélouma"""
  GN_LE
  """Kindia"""
  GN_D
  """Kindia"""
  GN_KD
  """Dubréka"""
  GN_DU
  """Coyah"""
  GN_CO
  """Forécariah"""
  GN_FO
  """Télimélé"""
  GN_TE
  """Nzérékoré"""
  GN_N
  """Macenta"""
  GN_MC
  """Lola"""
  GN_LO
  """Yomou"""
  GN_YO
  """Beyla"""
  GN_BE
  """Guékédou"""
  GN_GU
  """Nzérékoré"""
  GN_NZ
  """Región Continental"""
  GQ_C
  """Kié-Ntem"""
  GQ_KN
  """Centro Sul"""
  GQ_CS
  """Littoral"""
  GQ_LI
  """Wele-Nzas"""
  GQ_WN
  """Région Insulaire"""
  GQ_I
  """Bioko Sud"""
  GQ_BS
  """Annobón"""
  GQ_AN
  """Bioko Norte"""
  GQ_BN
  """Dytikí Makedonía"""
  GR_C
  """Kastoriá"""
  GR_56
  """Kozáni"""
  GR_58
  """Grevená"""
  GR_51
  """Flórina"""
  GR_63
  """Stereá Elláda"""
  GR_H
  """Fokída"""
  GR_07
  """Voiotía"""
  GR_03
  """Evrytanía"""
  GR_05
  """Fthiótida"""
  GR_06
  """Évvoia"""
  GR_04
  """Attikí"""
  GR_I
  """Attikí"""
  GR_A1
  """Notío Aigaío"""
  GR_L
  """Kykládes"""
  GR_82
  """Dodekánisa"""
  GR_81
  """Anatolikí Makedonía kai Thráki"""
  GR_A
  """Évros"""
  GR_71
  """Kavála"""
  GR_55
  """Xánthi"""
  GR_72
  """Rodópi"""
  GR_73
  """Dráma"""
  GR_52
  """Kentrikí Makedonía"""
  GR_B
  """Imathía"""
  GR_53
  """Pélla"""
  GR_59
  """Piería"""
  GR_61
  """Chalkidikí"""
  GR_64
  """Thessaloníki"""
  GR_54
  """Sérres"""
  GR_62
  """Kilkís"""
  GR_57
  """Ionía Nísia"""
  GR_F
  """Lefkáda"""
  GR_24
  """Kérkyra"""
  GR_22
  """Kefallinía"""
  GR_23
  """Zákynthos"""
  GR_21
  """Ágion Óros"""
  GR_69
  """Thessalía"""
  GR_E
  """Kardítsa"""
  GR_41
  """Magnisía"""
  GR_43
  """Tríkala"""
  GR_44
  """Lárisa"""
  GR_42
  """Voreío Aigaío"""
  GR_K
  """Sámos"""
  GR_84
  """Lésvos"""
  GR_83
  """Chíos"""
  GR_85
  """Ípeiros"""
  GR_D
  """Préveza"""
  GR_34
  """Thesprotía"""
  GR_32
  """Ioánnina"""
  GR_33
  """Árta"""
  GR_31
  """Dytikí Elláda"""
  GR_G
  """Achaḯa"""
  GR_13
  """Aitoloakarnanía"""
  GR_01
  """Ileía"""
  GR_14
  """Peloponnísos"""
  GR_J
  """Lakonía"""
  GR_16
  """Messinía"""
  GR_17
  """Argolída"""
  GR_11
  """Korinthía"""
  GR_15
  """Arkadía"""
  GR_12
  """Krítí"""
  GR_M
  """Lasíthi"""
  GR_92
  """Rethýmnis"""
  GR_93
  """Chaniá"""
  GR_94
  """Irakleío"""
  GR_91
  """Chimaltenango"""
  GT_CM
  """Escuintla"""
  GT_ES
  """Izabal"""
  GT_IZ
  """Petén"""
  GT_PE
  """Totonicapán"""
  GT_TO
  """Guatemala"""
  GT_GU
  """Zacapa"""
  GT_ZA
  """Jalapa"""
  GT_JA
  """Jutiapa"""
  GT_JU
  """Sacatepéquez"""
  GT_SA
  """San Marcos"""
  GT_SM
  """Quetzaltenango"""
  GT_QZ
  """Retalhuleu"""
  GT_RE
  """Huehuetenango"""
  GT_HU
  """Sololá"""
  GT_SO
  """Santa Rosa"""
  GT_SR
  """Suchitepéquez"""
  GT_SU
  """El Progreso"""
  GT_PR
  """Chiquimula"""
  GT_CQ
  """Quiché"""
  GT_QC
  """Alta Verapaz"""
  GT_AV
  """Baja Verapaz"""
  GT_BV
  """Leste"""
  GW_L
  """Gabú"""
  GW_GA
  """Bafatá"""
  GW_BA
  """Bissau"""
  GW_BS
  """Norte"""
  GW_N
  """Biombo"""
  GW_BM
  """Oio"""
  GW_OI
  """Cacheu"""
  GW_CA
  """Sul"""
  GW_S
  """Tombali"""
  GW_TO
  """Bolama"""
  GW_BL
  """Quinara"""
  GW_QU
  """East Berbice-Corentyne"""
  GY_EB
  """Upper Demerara-Berbice"""
  GY_UD
  """Barima-Waini"""
  GY_BA
  """Cuyuni-Mazaruni"""
  GY_CU
  """Demerara-Mahaica"""
  GY_DE
  """Potaro-Siparuni"""
  GY_PT
  """Pomeroon-Supenaam"""
  GY_PM
  """Upper Takutu-Upper Essequibo"""
  GY_UT
  """Essequibo Islands-West Demerara"""
  GY_ES
  """Mahaica-Berbice"""
  GY_MA
  """Copán"""
  HN_CP
  """La Paz"""
  HN_LP
  """Santa Bárbara"""
  HN_SB
  """Colón"""
  HN_CL
  """Yoro"""
  HN_YO
  """Choluteca"""
  HN_CH
  """Gracias a Dios"""
  HN_GD
  """Islas de la Bahía"""
  HN_IB
  """Olancho"""
  HN_OL
  """Valle"""
  HN_VA
  """Comayagua"""
  HN_CM
  """Lempira"""
  HN_LE
  """El Paraíso"""
  HN_EP
  """Atlántida"""
  HN_AT
  """Cortés"""
  HN_CR
  """Francisco Morazán"""
  HN_FM
  """Intibucá"""
  HN_IN
  """Ocotepeque"""
  HN_OC
  """Zadarska županija"""
  HR_13
  """Zagrebačka županija"""
  HR_01
  """Koprivničko-križevačka županija"""
  HR_06
  """Splitsko-dalmatinska županija"""
  HR_17
  """Grad Zagreb"""
  HR_21
  """Sisačko-moslavačka županija"""
  HR_03
  """Varaždinska županija"""
  HR_05
  """Primorsko-goranska županija"""
  HR_08
  """Šibensko-kninska županija"""
  HR_15
  """Karlovačka županija"""
  HR_04
  """Dubrovačko-neretvanska županija"""
  HR_19
  """Virovitičko-podravska županija"""
  HR_10
  """Osječko-baranjska županija"""
  HR_14
  """Vukovarsko-srijemska županija"""
  HR_16
  """Krapinsko-zagorska županija"""
  HR_02
  """Ličko-senjska županija"""
  HR_09
  """Brodsko-posavska županija"""
  HR_12
  """Istarska županija"""
  HR_18
  """Bjelovarsko-bilogorska županija"""
  HR_07
  """Međimurska županija"""
  HR_20
  """Požeško-slavonska županija"""
  HR_11
  """Nord-Ouest"""
  HT_NO
  """Nip"""
  HT_NI
  """Nòdès"""
  HT_NE
  """Lwès"""
  HT_OU
  """Grandans"""
  HT_GA
  """Nò"""
  HT_ND
  """Sid"""
  HT_SD
  """Sud-Est"""
  HT_SE
  """Artibonite"""
  HT_AR
  """Sant"""
  HT_CE
  """Nyíregyháza"""
  HU_NY
  """Tatabánya"""
  HU_TB
  """Fejér"""
  HU_FE
  """Győr-Moson-Sopron"""
  HU_GS
  """Miskolc"""
  HU_MI
  """Pécs"""
  HU_PS
  """Salgótarján"""
  HU_ST
  """Vas"""
  HU_VA
  """Borsod-Abaúj-Zemplén"""
  HU_BZ
  """Érd"""
  HU_ER
  """Nagykanizsa"""
  HU_NK
  """Nógrád"""
  HU_NO
  """Baranya"""
  HU_BA
  """Békéscsaba"""
  HU_BC
  """Csongrád"""
  HU_CS
  """Debrecen"""
  HU_DE
  """Hajdú-Bihar"""
  HU_HB
  """Pest"""
  HU_PE
  """Sopron"""
  HU_SN
  """Somogy"""
  HU_SO
  """Békés"""
  HU_BE
  """Jász-Nagykun-Szolnok"""
  HU_JN
  """Szeged"""
  HU_SD
  """Veszprém"""
  HU_VE
  """Zala"""
  HU_ZA
  """Zalaegerszeg"""
  HU_ZE
  """Dunaújváros"""
  HU_DU
  """Komárom-Esztergom"""
  HU_KE
  """Székesfehérvár"""
  HU_SF
  """Szekszárd"""
  HU_SS
  """Bács-Kiskun"""
  HU_BK
  """Eger"""
  HU_EG
  """Győr"""
  HU_GY
  """Heves"""
  HU_HE
  """Kecskemét"""
  HU_KM
  """Szabolcs-Szatmár-Bereg"""
  HU_SZ
  """Tolna"""
  HU_TO
  """Budapest"""
  HU_BU
  """Hódmezővásárhely"""
  HU_HV
  """Kaposvár"""
  HU_KV
  """Szombathely"""
  HU_SH
  """Szolnok"""
  HU_SK
  """Veszprém"""
  HU_VM
  """Kalimantan"""
  ID_KA
  """Kalimantan Utara"""
  ID_KU
  """Kalimantan Tengah"""
  ID_KT
  """Kalimantan Barat"""
  ID_KB
  """Kalimantan Selatan"""
  ID_KS
  """Kalimantan Timur"""
  ID_KI
  """Jawa"""
  ID_JW
  """Jawa Barat"""
  ID_JB
  """Jawa Tengah"""
  ID_JT
  """Jakarta Raya"""
  ID_JK
  """Jawa Timur"""
  ID_JI
  """Banten"""
  ID_BT
  """Yogyakarta"""
  ID_YO
  """Nusa Tenggara"""
  ID_NU
  """Bali"""
  ID_BA
  """Nusa Tenggara Timur"""
  ID_NT
  """Nusa Tenggara Barat"""
  ID_NB
  """Sumatera"""
  ID_SM
  """Bangka Belitung"""
  ID_BB
  """Jambi"""
  ID_JA
  """Aceh"""
  ID_AC
  """Riau"""
  ID_RI
  """Sumatera Selatan"""
  ID_SS
  """Bengkulu"""
  ID_BE
  """Sumatera Barat"""
  ID_SB
  """Sumatera Utara"""
  ID_SU
  """Lampung"""
  ID_LA
  """Kepulauan Riau"""
  ID_KR
  """Papua"""
  ID_PP
  """Papua"""
  ID_PA
  """Papua Barat"""
  ID_PB
  """Maluku"""
  ID_ML
  """Maluku"""
  ID_MA
  """Maluku Utara"""
  ID_MU
  """Sulawesi"""
  ID_SL
  """Gorontalo"""
  ID_GO
  """Sulawesi Utara"""
  ID_SA
  """Sulawesi Barat"""
  ID_SR
  """Sulawesi Tengah"""
  ID_ST
  """Sulawesi Tenggara"""
  ID_SG
  """Sulawesi Selatan"""
  ID_SN
  """Connaught"""
  IE_C
  """Galway"""
  IE_G
  """Roscommon"""
  IE_RN
  """Sligo"""
  IE_SO
  """Leitrim"""
  IE_LM
  """Mayo"""
  IE_MO
  """Leinster"""
  IE_L
  """Dublin"""
  IE_D
  """Offaly"""
  IE_OY
  """Kildare"""
  IE_KE
  """Longford"""
  IE_LD
  """Carlow"""
  IE_CW
  """Kilkenny"""
  IE_KK
  """Laois"""
  IE_LS
  """Meath"""
  IE_MH
  """Wicklow"""
  IE_WW
  """Wexford"""
  IE_WX
  """Louth"""
  IE_LH
  """Westmeath"""
  IE_WH
  """Ulster"""
  IE_U
  """Monaghan"""
  IE_MN
  """Cavan"""
  IE_CN
  """Donegal"""
  IE_DL
  """Munster"""
  IE_M
  """Clare"""
  IE_CE
  """Cork"""
  IE_CO
  """Tipperary"""
  IE_TA
  """Waterford"""
  IE_WD
  """Limerick"""
  IE_LK
  """Kerry"""
  IE_KY
  """HaMerkaz"""
  IL_M
  """HaTsafon"""
  IL_Z
  """HaDarom"""
  IL_D
  """H̱efa"""
  IL_HA
  """Yerushalayim"""
  IL_JM
  """Tel-Aviv"""
  IL_TA
  """Andaman and Nicobar Islands"""
  IN_AN
  """Andhra Pradesh"""
  IN_AP
  """Arunachal Pradesh"""
  IN_AR
  """Karnataka"""
  IN_KA
  """Kerala"""
  IN_KL
  """Lakshadweep"""
  IN_LD
  """Maharashtra"""
  IN_MH
  """Odisha"""
  IN_OR
  """Bihar"""
  IN_BR
  """Tripura"""
  IN_TR
  """West Bengal"""
  IN_WB
  """Gujarat"""
  IN_GJ
  """Meghalaya"""
  IN_ML
  """Madhya Pradesh"""
  IN_MP
  """Chhattisgarh"""
  IN_CT
  """Haryana"""
  IN_HR
  """Uttar Pradesh"""
  IN_UP
  """Daman and Diu"""
  IN_DD
  """Himachal Pradesh"""
  IN_HP
  """Jharkhand"""
  IN_JH
  """Jammu and Kashmir"""
  IN_JK
  """Nagaland"""
  IN_NL
  """Chandigarh"""
  IN_CH
  """Goa"""
  IN_GA
  """Mizoram"""
  IN_MZ
  """Puducherry"""
  IN_PY
  """Sikkim"""
  IN_SK
  """Uttarakhand"""
  IN_UT
  """Telangana"""
  IN_TG
  """Delhi"""
  IN_DL
  """Assam"""
  IN_AS
  """Dadra and Nagar Haveli"""
  IN_DN
  """Manipur"""
  IN_MN
  """Punjab"""
  IN_PB
  """Rajasthan"""
  IN_RJ
  """Tamil Nadu"""
  IN_TN
  """Bābil"""
  IQ_BB
  """Al Muthanná"""
  IQ_MU
  """Wāsiţ"""
  IQ_WA
  """Arbīl"""
  IQ_AR
  """Al Başrah"""
  IQ_BA
  """Dahūk"""
  IQ_DA
  """Al Qādisīyah"""
  IQ_QA
  """As Sulaymānīyah"""
  IQ_SU
  """Şalāḩ ad Dīn"""
  IQ_SD
  """Diyālá"""
  IQ_DI
  """Al Anbār"""
  IQ_AN
  """Dhī Qār"""
  IQ_DQ
  """Karbalā'"""
  IQ_KA
  """An Najaf"""
  IQ_NA
  """Kirkūk"""
  IQ_KI
  """Nīnawá"""
  IQ_NI
  """Baghdād"""
  IQ_BG
  """Maysān"""
  IQ_MA
  """Khūzestān"""
  IR_10
  """Kordestān"""
  IR_16
  """Gīlān"""
  IR_19
  """Yazd"""
  IR_25
  """Āz̄arbāyjān-e Sharqī"""
  IR_01
  """Sīstān va Balūchestān"""
  IR_13
  """Lorestān"""
  IR_20
  """Māzandarān"""
  IR_21
  """Qom"""
  IR_26
  """Āz̄arbāyjān-e Gharbī"""
  IR_02
  """Eşfahān"""
  IR_04
  """Tehrān"""
  IR_07
  """Zanjān"""
  IR_11
  """Kermān"""
  IR_15
  """Īlām"""
  IR_05
  """Kermānshāh"""
  IR_17
  """Kohgīlūyeh va Būyer Aḩmad"""
  IR_18
  """Qazvīn"""
  IR_28
  """Semnān"""
  IR_12
  """Fārs"""
  IR_14
  """Markazī"""
  IR_22
  """Hamadān"""
  IR_24
  """Būshehr"""
  IR_06
  """Golestān"""
  IR_27
  """Khorāsān-e Razavī"""
  IR_30
  """Alborz"""
  IR_32
  """Hormozgān"""
  IR_23
  """Khorāsān-e Janūbī"""
  IR_29
  """Khorāsān-e Shemālī"""
  IR_31
  """Ardabīl"""
  IR_03
  """Chahār Maḩāll va Bakhtīārī"""
  IR_08
  """Vestfirðir"""
  IS_4
  """Vesturland"""
  IS_3
  """Suðurnes"""
  IS_2
  """Austurland"""
  IS_7
  """Reykjavík"""
  IS_0
  """Höfuðborgarsvæði utan Reykjavíkur"""
  IS_1
  """Norðurland vestra"""
  IS_5
  """Norðurland eystra"""
  IS_6
  """Suðurland"""
  IS_8
  """Molise"""
  IT_67
  """Isernia"""
  IT_IS
  """Campobasso"""
  IT_CB
  """Valle d'Aosta"""
  IT_23
  """Aosta"""
  IT_AO
  """Lombardia"""
  IT_25
  """Cremona"""
  IT_CR
  """Lecco"""
  IT_LC
  """Pavia"""
  IT_PV
  """Monza e Brianza"""
  IT_MB
  """Brescia"""
  IT_BS
  """Sondrio"""
  IT_SO
  """Mantova"""
  IT_MN
  """Bergamo"""
  IT_BG
  """Varese"""
  IT_VA
  """Como"""
  IT_CO
  """Lodi"""
  IT_LO
  """Milano"""
  IT_MI
  """Friuli-Venezia Giulia"""
  IT_36
  """Trieste"""
  IT_TS
  """Udine"""
  IT_UD
  """Pordenone"""
  IT_PN
  """Gorizia"""
  IT_GO
  """Trentino-Südtirol"""
  IT_32
  """Trento"""
  IT_TN
  """Bolzano"""
  IT_BZ
  """Lazio"""
  IT_62
  """Frosinone"""
  IT_FR
  """Roma"""
  IT_RM
  """Viterbo"""
  IT_VT
  """Latina"""
  IT_LT
  """Rieti"""
  IT_RI
  """Veneto"""
  IT_34
  """Venezia"""
  IT_VE
  """Vicenza"""
  IT_VI
  """Padova"""
  IT_PD
  """Rovigo"""
  IT_RO
  """Belluno"""
  IT_BL
  """Treviso"""
  IT_TV
  """Verona"""
  IT_VR
  """Liguria"""
  IT_42
  """Imperia"""
  IT_IM
  """La Spezia"""
  IT_SP
  """Savona"""
  IT_SV
  """Genova"""
  IT_GE
  """Emilia-Romagna"""
  IT_45
  """Forlì-Cesena"""
  IT_FC
  """Ferrara"""
  IT_FE
  """Piacenza"""
  IT_PC
  """Ravenna"""
  IT_RA
  """Rimini"""
  IT_RN
  """Parma"""
  IT_PR
  """Reggio Emilia"""
  IT_RE
  """Bologna"""
  IT_BO
  """Modena"""
  IT_MO
  """Basilicata"""
  IT_77
  """Matera"""
  IT_MT
  """Potenza"""
  IT_PZ
  """Sicilia"""
  IT_82
  """Agrigento"""
  IT_AG
  """Palermo"""
  IT_PA
  """Trapani"""
  IT_TP
  """Caltanissetta"""
  IT_CL
  """Ragusa"""
  IT_RG
  """Siracusa"""
  IT_SR
  """Enna"""
  IT_EN
  """Messina"""
  IT_ME
  """Catania"""
  IT_CT
  """Sardegna"""
  IT_88
  """Cagliari"""
  IT_CA
  """Carbonia-Iglesias"""
  IT_CI
  """Ogliastra"""
  IT_OG
  """Oristano"""
  IT_OR
  """Olbia-Tempio"""
  IT_OT
  """Medio Campidano"""
  IT_VS
  """Sassari"""
  IT_SS
  """Nuoro"""
  IT_NU
  """Umbria"""
  IT_55
  """Perugia"""
  IT_PG
  """Terni"""
  IT_TR
  """Campania"""
  IT_72
  """Napoli"""
  IT_NA
  """Avellino"""
  IT_AV
  """Benevento"""
  IT_BN
  """Salerno"""
  IT_SA
  """Caserta"""
  IT_CE
  """Toscana"""
  IT_52
  """Grosseto"""
  IT_GR
  """Prato"""
  IT_PO
  """Pistoia"""
  IT_PT
  """Lucca"""
  IT_LU
  """Siena"""
  IT_SI
  """Massa-Carrara"""
  IT_MS
  """Pisa"""
  IT_PI
  """Firenze"""
  IT_FI
  """Arezzo"""
  IT_AR
  """Livorno"""
  IT_LI
  """Puglia"""
  IT_75
  """Barletta-Andria-Trani"""
  IT_BT
  """Foggia"""
  IT_FG
  """Taranto"""
  IT_TA
  """Lecce"""
  IT_LE
  """Bari"""
  IT_BA
  """Brindisi"""
  IT_BR
  """Calabria"""
  IT_78
  """Crotone"""
  IT_KR
  """Reggio Calabria"""
  IT_RC
  """Vibo Valentia"""
  IT_VV
  """Cosenza"""
  IT_CS
  """Catanzaro"""
  IT_CZ
  """Piemonte"""
  IT_21
  """Vercelli"""
  IT_VC
  """Biella"""
  IT_BI
  """Novara"""
  IT_NO
  """Verbano-Cusio-Ossola"""
  IT_VB
  """Torino"""
  IT_TO
  """Alessandria"""
  IT_AL
  """Asti"""
  IT_AT
  """Cuneo"""
  IT_CN
  """Marche"""
  IT_57
  """Fermo"""
  IT_FM
  """Ascoli Piceno"""
  IT_AP
  """Ancona"""
  IT_AN
  """Macerata"""
  IT_MC
  """Pesaro e Urbino"""
  IT_PU
  """Abruzzo"""
  IT_65
  """Pescara"""
  IT_PE
  """L'Aquila"""
  IT_AQ
  """Chieti"""
  IT_CH
  """Teramo"""
  IT_TE
  """Saint Ann"""
  JM_06
  """Clarendon"""
  JM_13
  """Saint Andrew"""
  JM_02
  """Saint Thomas"""
  JM_03
  """Saint James"""
  JM_08
  """Kingston"""
  JM_01
  """Manchester"""
  JM_12
  """Saint Catherine"""
  JM_14
  """Westmoreland"""
  JM_10
  """Saint Elizabeth"""
  JM_11
  """Trelawny"""
  JM_07
  """Hanover"""
  JM_09
  """Portland"""
  JM_04
  """Saint Mary"""
  JM_05
  """Al ʽAqabah"""
  JO_AQ
  """Az Zarqā'"""
  JO_AZ
  """Irbid"""
  JO_IR
  """Ma'ān"""
  JO_MN
  """Aţ Ţafīlah"""
  JO_AT
  """Jarash"""
  JO_JA
  """Al Karak"""
  JO_KA
  """ʽAjlūn"""
  JO_AJ
  """Al Mafraq"""
  JO_MA
  """‘Ammān"""
  JO_AM
  """Al Balqā'"""
  JO_BA
  """Mādabā"""
  JO_MD
  """Saitama"""
  JP_11
  """Toyama"""
  JP_16
  """Ishikawa"""
  JP_17
  """Yamanashi"""
  JP_19
  """Shizuoka"""
  JP_22
  """Mie"""
  JP_24
  """Kyoto"""
  JP_26
  """Shimane"""
  JP_32
  """Tokushima"""
  JP_36
  """Oita"""
  JP_44
  """Iwate"""
  JP_03
  """Shiga"""
  JP_25
  """Hyogo"""
  JP_28
  """Saga"""
  JP_41
  """Hokkaido"""
  JP_01
  """Akita"""
  JP_05
  """Tokyo"""
  JP_13
  """Aichi"""
  JP_23
  """Nara"""
  JP_29
  """Wakayama"""
  JP_30
  """Okayama"""
  JP_33
  """Kagawa"""
  JP_37
  """Gunma"""
  JP_10
  """Chiba"""
  JP_12
  """Kanagawa"""
  JP_14
  """Kochi"""
  JP_39
  """Miyazaki"""
  JP_45
  """Nagano"""
  JP_20
  """Tottori"""
  JP_31
  """Ehime"""
  JP_38
  """Fukuoka"""
  JP_40
  """Nagasaki"""
  JP_42
  """Aomori"""
  JP_02
  """Fukushima"""
  JP_07
  """Tochigi"""
  JP_09
  """Fukui"""
  JP_18
  """Gifu"""
  JP_21
  """Hiroshima"""
  JP_34
  """Yamaguchi"""
  JP_35
  """Kumamoto"""
  JP_43
  """Kagoshima"""
  JP_46
  """Okinawa"""
  JP_47
  """Miyagi"""
  JP_04
  """Yamagata"""
  JP_06
  """Ibaraki"""
  JP_08
  """Niigata"""
  JP_15
  """Osaka"""
  JP_27
  """Baringo"""
  KE_01
  """Bomet"""
  KE_02
  """Bungoma"""
  KE_03
  """Busia"""
  KE_04
  """Elgeyo/Marakwet"""
  KE_05
  """Embu"""
  KE_06
  """Garissa"""
  KE_07
  """Homa Bay"""
  KE_08
  """Isiolo"""
  KE_09
  """Kajiado"""
  KE_10
  """Kakamega"""
  KE_11
  """Kericho"""
  KE_12
  """Kiambu"""
  KE_13
  """Kilifi"""
  KE_14
  """Kirinyaga"""
  KE_15
  """Kisii"""
  KE_16
  """Kisumu"""
  KE_17
  """Kitui"""
  KE_18
  """Kwale"""
  KE_19
  """Laikipia"""
  KE_20
  """Lamu"""
  KE_21
  """Machakos"""
  KE_22
  """Makueni"""
  KE_23
  """Mandera"""
  KE_24
  """Marsabit"""
  KE_25
  """Meru"""
  KE_26
  """Migori"""
  KE_27
  """Mombasa"""
  KE_28
  """Murang'a"""
  KE_29
  """Nairobi City"""
  KE_30
  """Nakuru"""
  KE_31
  """Nandi"""
  KE_32
  """Narok"""
  KE_33
  """Nyamira"""
  KE_34
  """Nyandarua"""
  KE_35
  """Nyeri"""
  KE_36
  """Samburu"""
  KE_37
  """Siaya"""
  KE_38
  """Taita/Taveta"""
  KE_39
  """Tana River"""
  KE_40
  """Tharaka-Nithi"""
  KE_41
  """Trans Nzoia"""
  KE_42
  """Turkana"""
  KE_43
  """Uasin Gishu"""
  KE_44
  """Vihiga"""
  KE_45
  """Wajir"""
  KE_46
  """West Pokot"""
  KE_47
  """Narynskaya oblast'"""
  KG_N
  """Gorod Bishkek"""
  KG_GB
  """Dzhalal-Abadskaya oblast'"""
  KG_J
  """Issyk-Kul'skaja oblast'"""
  KG_Y
  """Oshskaya oblast'"""
  KG_O
  """Talasskaya oblast'"""
  KG_T
  """Batkenskaja oblast'"""
  KG_B
  """Osh"""
  KG_GO
  """Chuyskaya oblast'"""
  KG_C
  """Banteay Mean Chey"""
  KH_1
  """Takêv"""
  KH_21
  """Rôtânôkiri"""
  KH_16
  """Siĕmréab"""
  KH_17
  """Krong Preah Sihanouk"""
  KH_18
  """Svaay Rieng"""
  KH_20
  """Pousaat"""
  KH_15
  """Kâmpóng Cham"""
  KH_3
  """Kândal"""
  KH_8
  """Mondol Kiri"""
  KH_11
  """Krŏng Kêb"""
  KH_23
  """Kâmpóng Chhnăng"""
  KH_4
  """Kampong Thum"""
  KH_6
  """Bătdâmbâng"""
  KH_2
  """Kâmpóng Spœ"""
  KH_5
  """Kaôh Kŏng"""
  KH_9
  """Krong Pailin"""
  KH_24
  """Stueng Traeng"""
  KH_19
  """Otdar Mean Chey"""
  KH_22
  """Kâmpôt"""
  KH_7
  """Kracheh"""
  KH_10
  """Phnom Penh"""
  KH_12
  """Preah Vihear"""
  KH_13
  """Prey Veaeng"""
  KH_14
  """Line Islands"""
  KI_L
  """Phoenix Islands"""
  KI_P
  """Gilbert Islands"""
  KI_G
  """Grande Comore"""
  KM_G
  """Mohéli"""
  KM_M
  """Anjouan"""
  KM_A
  """Nevis"""
  KN_N
  """Saint James Windward"""
  KN_05
  """Saint John Figtree"""
  KN_07
  """Saint Thomas Lowland"""
  KN_12
  """Saint Paul Charlestown"""
  KN_10
  """Saint George Gingerland"""
  KN_04
  """Saint Kitts"""
  KN_K
  """Saint Mary Cayon"""
  KN_08
  """Saint Anne Sandy Point"""
  KN_02
  """Saint Peter Basseterre"""
  KN_11
  """Christ Church Nichola Town"""
  KN_01
  """Trinity Palmetto Point"""
  KN_15
  """Saint John Capisterre"""
  KN_06
  """Saint Paul Capisterre"""
  KN_09
  """Saint Thomas Middle Island"""
  KN_13
  """Saint George Basseterre"""
  KN_03
  """Hwanghainamto"""
  KP_05
  """Hwanghaipukto"""
  KP_06
  """Yanggang-do"""
  KP_10
  """P'yǒngan-namdo"""
  KP_02
  """Phyeongyang"""
  KP_01
  """Phyeonganpukto"""
  KP_03
  """Jakangto"""
  KP_04
  """Hamgyǒng-bukto"""
  KP_09
  """Nasǒn"""
  KP_13
  """Kangwǒn-do"""
  KP_07
  """Hamkyeongnamto"""
  KP_08
  """Jeollabuk-do """
  KR_45
  """Gyeongsangnam-do """
  KR_48
  """Seoul-T'ǔkpyǒlshi"""
  KR_11
  """Busan-gwangyeoksi """
  KR_26
  """Daegu-gwangyeoksi """
  KR_27
  """Gwangju-gwangyeoksi """
  KR_29
  """Chungcheongnam-do """
  KR_44
  """Incheon-gwangyeoksi """
  KR_28
  """Daejeon-gwangyeoksi """
  KR_30
  """Gangwon-do """
  KR_42
  """Chungcheongbuk-do """
  KR_43
  """Gyeongsangbuk-do """
  KR_47
  """Jejudo"""
  KR_49
  """Sejong"""
  KR_50
  """Ulsan-gwangyeoksi """
  KR_31
  """Jeollanam-do """
  KR_46
  """Gyeonggi-do """
  KR_41
  """Al Jahrā’"""
  KW_JA
  """Al Kuwayt"""
  KW_KU
  """Mubārak al Kabīr"""
  KW_MU
  """Al Farwānīyah"""
  KW_FA
  """Ḩawallī"""
  KW_HA
  """Al Aḩmadī"""
  KW_AH
  """Aqmola oblysy"""
  KZ_AKM
  """Kyzylordinskaya oblast'"""
  KZ_KZY
  """Vostochno-Kazakhstanskaya oblast'"""
  KZ_VOS
  """Almaty oblysy"""
  KZ_ALM
  """Severo-Kazahstanskaja oblast'"""
  KZ_SEV
  """Ongtüstik Qazaqstan oblysy"""
  KZ_YUZ
  """Zapadno-Kazakhstanskaya oblast'"""
  KZ_ZAP
  """Qaraghandy oblysy"""
  KZ_KAR
  """Pavlodarskaya oblast'"""
  KZ_PAV
  """Almaty"""
  KZ_ALA
  """Kostanajskaja oblast'"""
  KZ_KUS
  """Astana"""
  KZ_AST
  """Aktyubinskaya oblast'"""
  KZ_AKT
  """Atyrauskaya oblast'"""
  KZ_ATY
  """Mangystauskaja oblast'"""
  KZ_MAN
  """Zhambylskaya oblast'"""
  KZ_ZHA
  """Borikhane"""
  LA_BL
  """Sékong"""
  LA_XE
  """Bokèo"""
  LA_BK
  """Champassak"""
  LA_CH
  """Savannakhét"""
  LA_SV
  """Xieng Khouang"""
  LA_XI
  """Attopeu"""
  LA_AT
  """Phong Saly"""
  LA_PH
  """Houaphan"""
  LA_HO
  """Khammouan"""
  LA_KH
  """Saravane"""
  LA_SL
  """Vientiane"""
  LA_VI
  """Sayaboury"""
  LA_XA
  """Xaisômboun"""
  LA_XN
  """Louang Namtha"""
  LA_LM
  """Louang Prabang"""
  LA_LP
  """Oudomsai"""
  LA_OU
  """Vientiane"""
  LA_VT
  """An Nabaţīyah"""
  LB_NA
  """Liban-Nord"""
  LB_AS
  """Baalbek-Hermel"""
  LB_BH
  """Liban-Sud"""
  LB_JA
  """Jabal Lubnān"""
  LB_JL
  """Beyrouth"""
  LB_BA
  """Al Biqā‘"""
  LB_BI
  """‘Akkār"""
  LB_AK
  """Anse la Raye"""
  LC_01
  """Gros Islet"""
  LC_06
  """Laborie"""
  LC_07
  """Choiseul"""
  LC_03
  """Castries"""
  LC_02
  """Dennery"""
  LC_05
  """Micoud"""
  LC_08
  """Canaries"""
  LC_12
  """Soufrière"""
  LC_10
  """Vieux Fort"""
  LC_11
  """Eschen"""
  LI_02
  """Schellenberg"""
  LI_08
  """Vaduz"""
  LI_11
  """Mauren"""
  LI_04
  """Schaan"""
  LI_07
  """Gamprin"""
  LI_03
  """Planken"""
  LI_05
  """Ruggell"""
  LI_06
  """Balzers"""
  LI_01
  """Triesen"""
  LI_09
  """Triesenberg"""
  LI_10
  """Central Province"""
  LK_2
  """Galle"""
  LK_31
  """Colombo"""
  LK_11
  """Batticaloa"""
  LK_51
  """Southern Province"""
  LK_3
  """Hambantota"""
  LK_33
  """Jaffna"""
  LK_41
  """Gampaha"""
  LK_12
  """Uva Province"""
  LK_8
  """Puttalam"""
  LK_62
  """Ratnapura"""
  LK_91
  """Western Province"""
  LK_1
  """Ampara"""
  LK_52
  """Badulla"""
  LK_81
  """Anuradhapura"""
  LK_71
  """Northern Province"""
  LK_4
  """Kurunegala"""
  LK_61
  """Kilinochchi"""
  LK_42
  """Kegalla"""
  LK_92
  """Kalutara"""
  LK_13
  """Kandy"""
  LK_21
  """Sabaragamuwa Province"""
  LK_9
  """Trincomalee"""
  LK_53
  """Vavuniya"""
  LK_44
  """North Western Province"""
  LK_6
  """Mullaittivu"""
  LK_45
  """Monaragala"""
  LK_82
  """North Central Province"""
  LK_7
  """Nuwara Eliya"""
  LK_23
  """Polonnaruwa"""
  LK_72
  """Eastern Province"""
  LK_5
  """Matale"""
  LK_22
  """Mannar"""
  LK_43
  """Matara"""
  LK_32
  """Bomi"""
  LR_BM
  """Grand Bassa"""
  LR_GB
  """Grand Gedeh"""
  LR_GG
  """Lofa"""
  LR_LO
  """Rivercess"""
  LR_RI
  """Grand Cape Mount"""
  LR_CM
  """Gbarpolu"""
  LR_GP
  """Margibi"""
  LR_MG
  """Montserrado"""
  LR_MO
  """Bong"""
  LR_BG
  """Maryland"""
  LR_MY
  """Nimba"""
  LR_NI
  """Sinoe"""
  LR_SI
  """River Gee"""
  LR_RG
  """Grand Kru"""
  LR_GK
  """Quthing"""
  LS_G
  """Berea"""
  LS_D
  """Mafeteng"""
  LS_E
  """Mokhotlong"""
  LS_J
  """Thaba-Tseka"""
  LS_K
  """Maseru"""
  LS_A
  """Mohale's Hoek"""
  LS_F
  """Leribe"""
  LS_C
  """Qacha's Nek"""
  LS_H
  """Butha-Buthe"""
  LS_B
  """Marijampolės apskritis"""
  LT_MR
  """Panevėžio apskritis"""
  LT_PN
  """Šiaulių apskritis"""
  LT_SA
  """Šilalė"""
  LT_45
  """Šilutė"""
  LT_46
  """Širvintos"""
  LT_47
  """Skuodas"""
  LT_48
  """Švenčionys"""
  LT_49
  """Tauragė"""
  LT_50
  """Telšiai"""
  LT_51
  """Trakai"""
  LT_52
  """Ukmergė"""
  LT_53
  """Utena"""
  LT_54
  """Varėna"""
  LT_55
  """Vilkaviškis"""
  LT_56
  """Vilnius"""
  LT_58
  """Zarasai"""
  LT_60
  """Birštono"""
  LT_05
  """Druskininkai"""
  LT_07
  """Elektrénai"""
  LT_08
  """Kalvarijos"""
  LT_14
  """Kazlų Rūdos"""
  LT_17
  """Neringa"""
  LT_28
  """Pagégiai"""
  LT_29
  """Rietavo"""
  LT_39
  """Visaginas"""
  LT_59
  """Telšių apskritis"""
  LT_TE
  """Alytaus apskritis"""
  LT_AL
  """Kauno apskritis"""
  LT_KU
  """Utenos apskritis"""
  LT_UT
  """Alytaus miestas"""
  LT_02
  """Kauno miestas"""
  LT_15
  """Klaipėdos miestas"""
  LT_20
  """Palangos miestas"""
  LT_31
  """Šiaulių miestas"""
  LT_43
  """Alytus"""
  LT_03
  """Vilniaus miestas"""
  LT_57
  """Panevėžio miestas"""
  LT_32
  """Akmenė"""
  LT_01
  """Anykščiai"""
  LT_04
  """Biržai"""
  LT_06
  """Ignalina"""
  LT_09
  """Jonava"""
  LT_10
  """Joniškis"""
  LT_11
  """Jurbarkas"""
  LT_12
  """Kaišiadorys"""
  LT_13
  """Kaunas"""
  LT_16
  """Kėdainiai"""
  LT_18
  """Kelmė"""
  LT_19
  """Klaipėda"""
  LT_21
  """Kretinga"""
  LT_22
  """Kupiškis"""
  LT_23
  """Lazdijai"""
  LT_24
  """Marijampolė"""
  LT_25
  """Mažeikiai"""
  LT_26
  """Molėtai"""
  LT_27
  """Pakruojis"""
  LT_30
  """Panevėžys"""
  LT_33
  """Pasvalys"""
  LT_34
  """Plungė"""
  LT_35
  """Prienai"""
  LT_36
  """Radviliškis"""
  LT_37
  """Raseiniai"""
  LT_38
  """Rokiškis"""
  LT_40
  """Šakiai"""
  LT_41
  """Šalčininkai"""
  LT_42
  """Šiauliai"""
  LT_44
  """Klaipėdos apskritis"""
  LT_KL
  """Tauragės apskritis"""
  LT_TA
  """Vilniaus apskritis"""
  LT_VL
  """Diekirch"""
  LU_D
  """Luxemburg"""
  LU_L
  """Grevenmacher"""
  LU_G
  """Aglonas novads"""
  LV_001
  """Grobiņas novads"""
  LV_032
  """Gulbenes novads"""
  LV_033
  """Kokneses novads"""
  LV_046
  """Krustpils novads"""
  LV_049
  """Lielvārdes novads"""
  LV_053
  """Mālpils novads"""
  LV_061
  """Pāvilostas novads"""
  LV_071
  """Preiļu novads"""
  LV_073
  """Rucavas novads"""
  LV_081
  """Sējas novads"""
  LV_090
  """Tērvetes novads"""
  LV_098
  """Jēkabpils"""
  LV_JKB
  """Ventspils"""
  LV_VEN
  """Auces novads"""
  LV_010
  """Beverīnas novads"""
  LV_017
  """Ikšķiles novads"""
  LV_035
  """Olaines novads"""
  LV_068
  """Priekuļu novads"""
  LV_075
  """Raunas novads"""
  LV_076
  """Saldus novads"""
  LV_088
  """Talsu novads"""
  LV_097
  """Viesītes novads"""
  LV_107
  """Jelgava"""
  LV_JEL
  """Valmiera"""
  LV_VMR
  """Babītes novads"""
  LV_012
  """Baltinavas novads"""
  LV_014
  """Burtnieku novads"""
  LV_019
  """Carnikavas novads"""
  LV_020
  """Cēsu novads"""
  LV_022
  """Garkalnes novads"""
  LV_031
  """Ķeguma novads"""
  LV_051
  """Ludzas novads"""
  LV_058
  """Mērsraga novads"""
  LV_063
  """Nīcas novads"""
  LV_066
  """Ogres novads"""
  LV_067
  """Pārgaujas novads"""
  LV_070
  """Skrundas novads"""
  LV_093
  """Stopiņu novads"""
  LV_095
  """Strenču novads"""
  LV_096
  """Tukuma novads"""
  LV_099
  """Varakļānu novads"""
  LV_102
  """Alsungas novads"""
  LV_006
  """Ērgļu novads"""
  LV_030
  """Inčukalna novads"""
  LV_037
  """Jaunpiebalgas novads"""
  LV_039
  """Kandavas novads"""
  LV_043
  """Kuldīgas novads"""
  LV_050
  """Līgatnes novads"""
  LV_055
  """Neretas novads"""
  LV_065
  """Pļaviņu novads"""
  LV_072
  """Rēzeknes novads"""
  LV_077
  """Rojas novads"""
  LV_079
  """Salaspils novads"""
  LV_087
  """Saulkrastu novads"""
  LV_089
  """Siguldas novads"""
  LV_091
  """Smiltenes novads"""
  LV_094
  """Vaiņodes novads"""
  LV_100
  """Vecpiebalgas novads"""
  LV_104
  """Rēzekne"""
  LV_REZ
  """Baldones novads"""
  LV_013
  """Ciblas novads"""
  LV_023
  """Daugavpils novads"""
  LV_025
  """Dobeles novads"""
  LV_026
  """Engures novads"""
  LV_029
  """Kocēnu novads"""
  LV_045
  """Madonas novads"""
  LV_059
  """Ozolnieku novads"""
  LV_069
  """Rugāju novads"""
  LV_082
  """Salas novads"""
  LV_085
  """Skrīveru novads"""
  LV_092
  """Vārkavas novads"""
  LV_103
  """Jūrmala"""
  LV_JUR
  """Aknīstes novads"""
  LV_004
  """Ādažu novads"""
  LV_011
  """Brocēnu novads"""
  LV_018
  """Durbes novads"""
  LV_028
  """Naukšēnu novads"""
  LV_064
  """Valkas novads"""
  LV_101
  """Vecumnieku novads"""
  LV_105
  """Viļakas novads"""
  LV_108
  """Daugavpils"""
  LV_DGV
  """Liepāja"""
  LV_LPX
  """Rīga"""
  LV_RIX
  """Aizkraukles novads"""
  LV_002
  """Alojas novads"""
  LV_005
  """Alūksnes novads"""
  LV_007
  """Amatas novads"""
  LV_008
  """Balvu novads"""
  LV_015
  """Dagdas novads"""
  LV_024
  """Dundagas novads"""
  LV_027
  """Ilūkstes novads"""
  LV_036
  """Krāslavas novads"""
  LV_047
  """Krimuldas novads"""
  LV_048
  """Limbažu novads"""
  LV_054
  """Līvānu novads"""
  LV_056
  """Mazsalacas novads"""
  LV_060
  """Riebiņu novads"""
  LV_078
  """Ropažu novads"""
  LV_080
  """Rundāles novads"""
  LV_083
  """Salacgrīvas novads"""
  LV_086
  """Zilupes novads"""
  LV_110
  """Aizputes novads"""
  LV_003
  """Apes novads"""
  LV_009
  """Bauskas novads"""
  LV_016
  """Cesvaines novads"""
  LV_021
  """Iecavas novads"""
  LV_034
  """Jaunjelgavas novads"""
  LV_038
  """Jaunpils novads"""
  LV_040
  """Jelgavas novads"""
  LV_041
  """Jēkabpils novads"""
  LV_042
  """Kārsavas novads"""
  LV_044
  """Ķekavas novads"""
  LV_052
  """Lubānas novads"""
  LV_057
  """Mārupes novads"""
  LV_062
  """Priekules novads"""
  LV_074
  """Rūjienas novads"""
  LV_084
  """Ventspils novads"""
  LV_106
  """Viļānu novads"""
  LV_109
  """Banghāzī"""
  LY_BA
  """Al Buţnān"""
  LY_BU
  """Darnah"""
  LY_DR
  """Al Jabal al Akhḑar"""
  LY_JA
  """Al Kufrah"""
  LY_KF
  """Murzuq"""
  LY_MQ
  """Al Jifārah"""
  LY_JI
  """Mişrātah"""
  LY_MI
  """Nālūt"""
  LY_NL
  """An Nuqāţ al Khams"""
  LY_NQ
  """Surt"""
  LY_SR
  """Az Zāwiyah"""
  LY_ZA
  """Al Jufrah"""
  LY_JU
  """Al Marqab"""
  LY_MB
  """Wādī al Ḩayāt"""
  LY_WD
  """Ghāt"""
  LY_GT
  """Ţarābulus"""
  LY_TB
  """Al Jabal al Gharbī"""
  LY_JG
  """Wādī ash Shāţi’"""
  LY_WS
  """Al Marj"""
  LY_MJ
  """Sabhā"""
  LY_SB
  """Al Wāḩāt"""
  LY_WA
  """Oued ed Dahab-Lagouira (EH)"""
  MA_16
  """Aousserd (EH)"""
  MA_AOU
  """Oued ed Dahab (EH)"""
  MA_OUD
  """Fès-Boulemane"""
  MA_05
  """Moulay Yacoub"""
  MA_MOU
  """Fès-Dar-Dbibegh"""
  MA_FES
  """Sefrou"""
  MA_SEF
  """Boulemane"""
  MA_BOM
  """Taza-Al Hoceima-Taounate"""
  MA_03
  """Al Hoceïma"""
  MA_HOC
  """Taounate"""
  MA_TAO
  """Taza"""
  MA_TAZ
  """Grand Casablanca"""
  MA_08
  """Casablanca"""
  MA_CAS
  """Médiouna"""
  MA_MED
  """Mohammadia"""
  MA_MOH
  """Nouaceur"""
  MA_NOU
  """Tadla-Azilal"""
  MA_12
  """Beni Mellal"""
  MA_BEM
  """Azilal"""
  MA_AZI
  """Sous-Massa-Draa"""
  MA_13
  """Inezgane-Ait Melloul"""
  MA_INE
  """Ouarzazate"""
  MA_OUA
  """Agadir-Ida-Outanane"""
  MA_AGD
  """Zagora"""
  MA_ZAG
  """Taroudant"""
  MA_TAR
  """Tiznit"""
  MA_TIZ
  """Chtouka-Ait Baha"""
  MA_CHT
  """Marrakech-Tensift-Al Haouz"""
  MA_11
  """Chichaoua"""
  MA_CHI
  """Kelaat es Sraghna"""
  MA_KES
  """Marrakech-Medina"""
  MA_MMD
  """Al Haouz"""
  MA_HAO
  """Essaouira"""
  MA_ESI
  """Sidi Youssef Ben Ali"""
  MA_SYB
  """Marrakech-Menara"""
  MA_MMN
  """Laâyoune-Boujdour-Sakia el Hamra"""
  MA_15
  """Laâyoune"""
  MA_LAA
  """Boujdour (EH)"""
  MA_BOD
  """Tanger-Tétouan"""
  MA_01
  """Chefchaouen"""
  MA_CHE
  """Fahs-Beni Makada"""
  MA_FAH
  """Tanger-Assilah"""
  MA_TNG
  """Tétouan"""
  MA_TET
  """Larache"""
  MA_LAR
  """Chaouia-Ouardigha"""
  MA_09
  """Ben Slimane"""
  MA_BES
  """Khouribga"""
  MA_KHO
  """Settat"""
  MA_SET
  """Gharb-Chrarda-Beni Hssen"""
  MA_02
  """Sidi Kacem"""
  MA_SIK
  """Kénitra"""
  MA_KEN
  """Meknès-Tafilalet"""
  MA_06
  """Errachidia"""
  MA_ERR
  """Khenifra"""
  MA_KHN
  """Ifrane"""
  MA_IFR
  """El Hajeb"""
  MA_HAJ
  """Meknès"""
  MA_MEK
  """Doukkala-Abda"""
  MA_10
  """Safi"""
  MA_SAF
  """El Jadida"""
  MA_JDI
  """Guelmim-Es Semara"""
  MA_14
  """Es Smara (EH)"""
  MA_ESM
  """Assa-Zag"""
  MA_ASZ
  """Tan-Tan"""
  MA_TNT
  """Guelmim"""
  MA_GUE
  """Tata"""
  MA_TAT
  """L'Oriental"""
  MA_04
  """Nador"""
  MA_NAD
  """Taourirt"""
  MA_TAI
  """Berkane"""
  MA_BER
  """Oujda-Angad"""
  MA_OUJ
  """Jrada"""
  MA_JRA
  """Figuig"""
  MA_FIG
  """Rabat-Salé-Zemmour-Zaer"""
  MA_07
  """Rabat"""
  MA_RAB
  """Skhirate-Témara"""
  MA_SKH
  """Salé"""
  MA_SAL
  """Khemisset"""
  MA_KHE
  """Monaco-Ville"""
  MC_MO
  """Port-Hercule"""
  MC_PH
  """Saint-Roman"""
  MC_SR
  """Vallon de la Rousse"""
  MC_VR
  """Larvotto"""
  MC_LA
  """Sainte-Dévote"""
  MC_SD
  """La Source"""
  MC_SO
  """La Colle"""
  MC_CL
  """La Gare"""
  MC_GA
  """Jardin Exotique"""
  MC_JE
  """Malbousquet"""
  MC_MA
  """Spélugues"""
  MC_SP
  """Monte-Carlo"""
  MC_MC
  """Moneghetti"""
  MC_MG
  """La Condamine"""
  MC_CO
  """Fontvieille"""
  MC_FO
  """Moulins"""
  MC_MU
  """Edineţ"""
  MD_ED
  """Hînceşti"""
  MD_HI
  """Nisporeni"""
  MD_NI
  """Rezina"""
  MD_RE
  """Stînga Nistrului, unitatea teritorială din"""
  MD_SN
  """Ştefan Vodă"""
  MD_SV
  """Briceni"""
  MD_BR
  """Făleşti"""
  MD_FA
  """Bălţi"""
  MD_BA
  """Basarabeasca"""
  MD_BS
  """Cahul"""
  MD_CA
  """Şoldăneşti"""
  MD_SD
  """Sîngerei"""
  MD_SI
  """Cimişlia"""
  MD_CM
  """Floreşti"""
  MD_FL
  """Leova"""
  MD_LE
  """Orhei"""
  MD_OR
  """Anenii Noi"""
  MD_AN
  """Criuleni"""
  MD_CR
  """Cantemir"""
  MD_CT
  """Glodeni"""
  MD_GL
  """Rîşcani"""
  MD_RI
  """Străşeni"""
  MD_ST
  """Călăraşi"""
  MD_CL
  """Drochia"""
  MD_DR
  """Găgăuzia, Unitatea teritorială autonomă (UTAG)"""
  MD_GA
  """Ocniţa"""
  MD_OC
  """Soroca"""
  MD_SO
  """Taraclia"""
  MD_TA
  """Teleneşti"""
  MD_TE
  """Bender """
  MD_BD
  """Căuşeni"""
  MD_CS
  """Chişinău"""
  MD_CU
  """Donduşeni"""
  MD_DO
  """Dubăsari"""
  MD_DU
  """Ialoveni"""
  MD_IA
  """Ungheni"""
  MD_UN
  """Andrijevica"""
  ME_01
  """Danilovgrad"""
  ME_07
  """Kotor"""
  ME_10
  """Rožaje"""
  ME_17
  """Gusinje"""
  ME_22
  """Petnjica"""
  ME_23
  """Budva"""
  ME_05
  """Plužine"""
  ME_15
  """Tivat"""
  ME_19
  """Cetinje"""
  ME_06
  """Kolašin"""
  ME_09
  """Pljevlja"""
  ME_14
  """Šavnik"""
  ME_18
  """Žabljak"""
  ME_21
  """Bar"""
  ME_02
  """Bijelo Polje"""
  ME_04
  """Herceg-Novi"""
  ME_08
  """Mojkovac"""
  ME_11
  """Berane"""
  ME_03
  """Podgorica"""
  ME_16
  """Ulcinj"""
  ME_20
  """Plav"""
  ME_13
  """Nikšić"""
  ME_12
  """Toliara"""
  MG_U
  """Antananarivo"""
  MG_T
  """Toamasina"""
  MG_A
  """Fianarantsoa"""
  MG_F
  """Mahajanga"""
  MG_M
  """Antsiranana"""
  MG_D
  """Ratak chain"""
  MH_T
  """Utrik"""
  MH_UTI
  """Likiep"""
  MH_LIK
  """Majuro"""
  MH_MAJ
  """Arno"""
  MH_ARN
  """Aur"""
  MH_AUR
  """Maloelap"""
  MH_MAL
  """Mejit"""
  MH_MEJ
  """Mili"""
  MH_MIL
  """Wotje"""
  MH_WTJ
  """Ailuk"""
  MH_ALK
  """Ralik chain"""
  MH_L
  """Namdrik"""
  MH_NMK
  """Rongelap"""
  MH_RON
  """Ebon"""
  MH_EBO
  """Enewetak and Ujelang"""
  MH_ENI
  """Wotho"""
  MH_WTH
  """Kwajalein"""
  MH_KWA
  """Ailinglaplap"""
  MH_ALL
  """Bikini and Kili"""
  MH_KIL
  """Lae"""
  MH_LAE
  """Namu"""
  MH_NMU
  """Jabat"""
  MH_JAB
  """Jaluit"""
  MH_JAL
  """Lib"""
  MH_LIB
  """Ujae"""
  MH_UJA
  """Bogdanci"""
  MK_05
  """Brvenica"""
  MK_08
  """Vinica"""
  MK_14
  """Debar"""
  MK_21
  """Delčevo"""
  MK_23
  """Dolneni"""
  MK_27
  """Zelenikovo"""
  MK_32
  """Karbinci"""
  MK_37
  """Novaci"""
  MK_55
  """Radoviš"""
  MK_64
  """Staro Nagoričane"""
  MK_71
  """Centar †"""
  MK_77
  """Aerodrom †"""
  MK_01
  """Aračinovo"""
  MK_02
  """Bitola"""
  MK_04
  """Bosilovo"""
  MK_07
  """Gostivar"""
  MK_19
  """Drugovo"""
  MK_28
  """Želino"""
  MK_30
  """Kičevo"""
  MK_40
  """Makedonska Kamenica"""
  MK_51
  """Mogila"""
  MK_53
  """Resen"""
  MK_66
  """Rosoman"""
  MK_67
  """Tearce"""
  MK_75
  """Šuto Orizari †"""
  MK_84
  """Berovo"""
  MK_03
  """Valandovo"""
  MK_10
  """Vasilevo"""
  MK_11
  """Dojran"""
  MK_26
  """Kriva Palanka"""
  MK_44
  """Negotino"""
  MK_54
  """Novo Selo"""
  MK_56
  """Pehčevo"""
  MK_60
  """Centar Župa"""
  MK_78
  """Čaška"""
  MK_80
  """Češinovo-Obleševo"""
  MK_81
  """Bogovinje"""
  MK_06
  """Vrapčište"""
  MK_16
  """Demir Hisar"""
  MK_25
  """Zajas"""
  MK_31
  """Jegunovce"""
  MK_35
  """Karpoš †"""
  MK_38
  """Konče"""
  MK_41
  """Ohrid"""
  MK_58
  """Prilep"""
  MK_62
  """Saraj †"""
  MK_68
  """Strumica"""
  MK_73
  """Čair †"""
  MK_79
  """Gevgelija"""
  MK_18
  """Debarca"""
  MK_22
  """Demir Kapija"""
  MK_24
  """Kavadarci"""
  MK_36
  """Kisela Voda †"""
  MK_39
  """Kratovo"""
  MK_43
  """Mavrovo i Rostuša"""
  MK_50
  """Oslomej"""
  MK_57
  """Plasnica"""
  MK_61
  """Sveti Nikole"""
  MK_69
  """Ilinden"""
  MK_34
  """Kočani"""
  MK_42
  """Krivogaštani"""
  MK_45
  """Kruševo"""
  MK_46
  """Lipkovo"""
  MK_48
  """Probištip"""
  MK_63
  """Studeničani"""
  MK_74
  """Tetovo"""
  MK_76
  """Vevčani"""
  MK_12
  """Gazi Baba †"""
  MK_17
  """Gradsko"""
  MK_20
  """Kumanovo"""
  MK_47
  """Rankovce"""
  MK_65
  """Struga"""
  MK_72
  """Štip"""
  MK_83
  """Butel †"""
  MK_09
  """Veles"""
  MK_13
  """Vraneštica"""
  MK_15
  """Gjorče Petrov †"""
  MK_29
  """Zrnovci"""
  MK_33
  """Lozovo"""
  MK_49
  """Makedonski Brod"""
  MK_52
  """Petrovec"""
  MK_59
  """Sopište"""
  MK_70
  """Čučer Sandevo"""
  MK_82
  """Ségou"""
  ML_4
  """Koulikoro"""
  ML_2
  """Mopti"""
  ML_5
  """Bamako"""
  ML_BKO
  """Tombouctou"""
  ML_6
  """Sikasso"""
  ML_3
  """Kidal"""
  ML_8
  """Kayes"""
  ML_1
  """Gao"""
  ML_7
  """Rakhine"""
  MM_16
  """Nay Pyi Taw"""
  MM_18
  """Bago"""
  MM_02
  """Kayah"""
  MM_12
  """Taninthayi"""
  MM_05
  """Kachin"""
  MM_11
  """Kayin"""
  MM_13
  """Mon"""
  MM_15
  """Sagaing"""
  MM_01
  """Mandalay"""
  MM_04
  """Yangon"""
  MM_06
  """Shan"""
  MM_17
  """Magway"""
  MM_03
  """Chin"""
  MM_14
  """Ayeyawady"""
  MM_07
  """Uvs"""
  MN_046
  """Govĭ-Altay"""
  MN_065
  """Hovd"""
  MN_043
  """Bayan-Ölgiy"""
  MN_071
  """Hövsgöl"""
  MN_041
  """Ömnögovĭ"""
  MN_053
  """Dornod"""
  MN_061
  """Bulgan"""
  MN_067
  """Övörhangay"""
  MN_055
  """Bayanhongor"""
  MN_069
  """Hentiy"""
  MN_039
  """Töv"""
  MN_047
  """Selenge"""
  MN_049
  """Dzavhan"""
  MN_057
  """Dundgovĭ"""
  MN_059
  """Orhon"""
  MN_035
  """Darhan uul"""
  MN_037
  """Govĭ-Sümber"""
  MN_064
  """Sühbaatar"""
  MN_051
  """Dornogovĭ"""
  MN_063
  """Arhangay"""
  MN_073
  """Ulaanbaatar"""
  MN_1
  """Hodh ech Chargui"""
  MR_01
  """Brakna"""
  MR_05
  """Inchiri"""
  MR_12
  """Hodh el Gharbi"""
  MR_02
  """Dakhlet Nouâdhibou"""
  MR_08
  """Assaba"""
  MR_03
  """Adrar"""
  MR_07
  """Nouakchott"""
  MR_NKC
  """Gorgol"""
  MR_04
  """Guidimaka"""
  MR_10
  """Trarza"""
  MR_06
  """Tagant"""
  MR_09
  """Tiris Zemmour"""
  MR_11
  """Mosta"""
  MT_32
  """Mqabba"""
  MT_33
  """Qormi"""
  MT_43
  """Saint Julian’s"""
  MT_48
  """Fgura"""
  MT_08
  """Msida"""
  MT_34
  """Mtarfa"""
  MT_35
  """Nadur"""
  MT_37
  """Rabat Malta"""
  MT_46
  """Birkirkara"""
  MT_04
  """Għarb"""
  MT_14
  """Għasri"""
  MT_16
  """Ħamrun"""
  MT_18
  """Kerċem"""
  MT_22
  """Marsa"""
  MT_26
  """Għajnsielem"""
  MT_13
  """Għargħur"""
  MT_15
  """Isla"""
  MT_20
  """Marsaskala"""
  MT_27
  """Munxar"""
  MT_36
  """Pembroke"""
  MT_40
  """Qrendi"""
  MT_44
  """Saint John"""
  MT_49
  """Saint Lawrence"""
  MT_50
  """Saint Paul’s Bay"""
  MT_51
  """Xagħra"""
  MT_61
  """Xgħajra"""
  MT_63
  """Żejtun"""
  MT_67
  """Birżebbuġa"""
  MT_05
  """Bormla"""
  MT_06
  """Gżira"""
  MT_12
  """Żabbar"""
  MT_64
  """Balzan"""
  MT_02
  """Birgu"""
  MT_03
  """Iklin"""
  MT_19
  """Lija"""
  MT_24
  """Luqa"""
  MT_25
  """Paola"""
  MT_39
  """Sannat"""
  MT_52
  """Siġġiewi"""
  MT_55
  """Sliema"""
  MT_56
  """Żebbuġ Malta"""
  MT_66
  """Żurrieq"""
  MT_68
  """Naxxar"""
  MT_38
  """Pietà"""
  MT_41
  """Santa Venera"""
  MT_54
  """Ta’ Xbiex"""
  MT_58
  """Valletta"""
  MT_60
  """Dingli"""
  MT_07
  """Gudja"""
  MT_11
  """Kalkara"""
  MT_21
  """Mġarr"""
  MT_31
  """Safi"""
  MT_47
  """Tarxien"""
  MT_59
  """Xewkija"""
  MT_62
  """Żebbuġ Gozo"""
  MT_65
  """Floriana"""
  MT_09
  """Mellieħa"""
  MT_30
  """Qala"""
  MT_42
  """Rabat Gozo"""
  MT_45
  """Saint Lucia’s"""
  MT_53
  """Swieqi"""
  MT_57
  """Attard"""
  MT_01
  """Fontana"""
  MT_10
  """Għaxaq"""
  MT_17
  """Kirkop"""
  MT_23
  """Marsaxlokk"""
  MT_28
  """Mdina"""
  MT_29
  """Agalega Islands"""
  MU_AG
  """Beau Bassin-Rose Hill"""
  MU_BR
  """Rodrigues Island"""
  MU_RO
  """Savanne"""
  MU_SA
  """Plaines Wilhems"""
  MU_PW
  """Cargados Carajos Shoals"""
  MU_CC
  """Grand Port"""
  MU_GP
  """Curepipe"""
  MU_CU
  """Pamplemousses"""
  MU_PA
  """Port Louis"""
  MU_PL
  """Black River"""
  MU_BL
  """Flacq"""
  MU_FL
  """Quatre Bornes"""
  MU_QB
  """Moka"""
  MU_MO
  """Port Louis"""
  MU_PU
  """Rivière du Rempart"""
  MU_RR
  """Vacoas-Phoenix"""
  MU_VP
  """Central"""
  MV_CE
  """Faafu"""
  MV_14
  """Meemu"""
  MV_12
  """Dhaalu"""
  MV_17
  """North Central"""
  MV_NC
  """Vaavu"""
  MV_04
  """Kaafu"""
  MV_26
  """Alifu Dhaalu"""
  MV_00
  """Alifu Alifu"""
  MV_02
  """South"""
  MV_SU
  """Gnaviyani"""
  MV_29
  """Seenu"""
  MV_01
  """South Central"""
  MV_SC
  """Gaafu Alifu"""
  MV_27
  """Gaafu Dhaalu"""
  MV_28
  """Male"""
  MV_MLE
  """North"""
  MV_NO
  """Raa"""
  MV_13
  """Lhaviyani"""
  MV_03
  """Baa"""
  MV_20
  """Noonu"""
  MV_25
  """Upper North"""
  MV_UN
  """Haa Dhaalu"""
  MV_23
  """Shaviyani"""
  MV_24
  """Haa Alifu"""
  MV_07
  """Upper South"""
  MV_US
  """Laamu"""
  MV_05
  """Thaa"""
  MV_08
  """Central Region"""
  MW_C
  """Lilongwe"""
  MW_LI
  """Kasungu"""
  MW_KS
  """Nkhotakota"""
  MW_NK
  """Mchinji"""
  MW_MC
  """Ntchisi"""
  MW_NI
  """Salima"""
  MW_SA
  """Dedza"""
  MW_DE
  """Dowa"""
  MW_DO
  """Ntcheu"""
  MW_NU
  """Northern Region"""
  MW_N
  """Rumphi"""
  MW_RU
  """Chitipa"""
  MW_CT
  """Karonga"""
  MW_KR
  """Likoma"""
  MW_LK
  """Nkhata Bay"""
  MW_NB
  """Mzimba"""
  MW_MZ
  """Southern Region"""
  MW_S
  """Chiradzulu"""
  MW_CR
  """Mulanje"""
  MW_MU
  """Nsanje"""
  MW_NS
  """Phalombe"""
  MW_PH
  """Zomba"""
  MW_ZO
  """Balaka"""
  MW_BA
  """Chikwawa"""
  MW_CK
  """Mangochi"""
  MW_MG
  """Mwanza"""
  MW_MW
  """Thyolo"""
  MW_TH
  """Blantyre"""
  MW_BL
  """Machinga"""
  MW_MH
  """Neno"""
  MW_NE
  """Aguascalientes"""
  MX_AGU
  """Baja California"""
  MX_BCN
  """Campeche"""
  MX_CAM
  """Distrito Federal"""
  MX_DIF
  """Guanajuato"""
  MX_GUA
  """Morelos"""
  MX_MOR
  """Baja California Sur"""
  MX_BCS
  """Guerrero"""
  MX_GRO
  """Hidalgo"""
  MX_HID
  """Sonora"""
  MX_SON
  """Zacatecas"""
  MX_ZAC
  """Coahuila"""
  MX_COA
  """Colima"""
  MX_COL
  """Durango"""
  MX_DUR
  """Querétaro"""
  MX_QUE
  """Sinaloa"""
  MX_SIN
  """Veracruz"""
  MX_VER
  """Chiapas"""
  MX_CHP
  """Jalisco"""
  MX_JAL
  """Puebla"""
  MX_PUE
  """Quintana Roo"""
  MX_ROO
  """Tlaxcala"""
  MX_TLA
  """México"""
  MX_MEX
  """Nayarit"""
  MX_NAY
  """Oaxaca"""
  MX_OAX
  """San Luis Potosí"""
  MX_SLP
  """Tabasco"""
  MX_TAB
  """Chihuahua"""
  MX_CHH
  """Nuevo León"""
  MX_NLE
  """Tamaulipas"""
  MX_TAM
  """Yucatán"""
  MX_YUC
  """Michoacán"""
  MX_MIC
  """Sabah"""
  MY_12
  """Sarawak"""
  MY_13
  """Negeri Sembilan"""
  MY_05
  """Perlis"""
  MY_09
  """Pulau Pinang"""
  MY_07
  """Johor"""
  MY_01
  """Perak"""
  MY_08
  """Selangor"""
  MY_10
  """Wilayah Persekutuan Kuala Lumpur"""
  MY_14
  """Wilayah Persekutuan Putrajaya"""
  MY_16
  """Kelantan"""
  MY_03
  """Melaka"""
  MY_04
  """Kedah"""
  MY_02
  """Terengganu"""
  MY_11
  """Pahang"""
  MY_06
  """Wilayah Persekutuan Labuan"""
  MY_15
  """Inhambane"""
  MZ_I
  """Maputo"""
  MZ_MPM
  """Niassa"""
  MZ_A
  """Maputo"""
  MZ_L
  """Zambézia"""
  MZ_Q
  """Sofala"""
  MZ_S
  """Manica"""
  MZ_B
  """Tete"""
  MZ_T
  """Cabo Delgado"""
  MZ_P
  """Nampula"""
  MZ_N
  """Gaza"""
  MZ_G
  """Oshana"""
  NA_ON
  """Kavango East"""
  NA_KE
  """Kavango West"""
  NA_KW
  """Hardap"""
  NA_HA
  """Khomas"""
  NA_KH
  """Zambezi"""
  NA_CA
  """Erongo"""
  NA_ER
  """Kunene"""
  NA_KU
  """Omusati"""
  NA_OS
  """Ohangwena"""
  NA_OW
  """Otjozondjupa"""
  NA_OD
  """Karas"""
  NA_KA
  """Omaheke"""
  NA_OH
  """Oshikoto"""
  NA_OT
  """Agadez"""
  NE_1
  """Tillabéri"""
  NE_6
  """Tahoua"""
  NE_5
  """Diffa"""
  NE_2
  """Zinder"""
  NE_7
  """Dosso"""
  NE_3
  """Maradi"""
  NE_4
  """Niamey"""
  NE_8
  """Bayelsa"""
  NG_BY
  """Kano"""
  NG_KN
  """Katsina"""
  NG_KT
  """Borno"""
  NG_BO
  """Ebonyi"""
  NG_EB
  """Abuja Federal Capital Territory"""
  NG_FC
  """Kebbi"""
  NG_KE
  """Nasarawa"""
  NG_NA
  """Niger"""
  NG_NI
  """Ondo"""
  NG_ON
  """Osun"""
  NG_OS
  """Oyo"""
  NG_OY
  """Delta"""
  NG_DE
  """Ekiti"""
  NG_EK
  """Kogi"""
  NG_KO
  """Lagos"""
  NG_LA
  """Taraba"""
  NG_TA
  """Kaduna"""
  NG_KD
  """Ogun"""
  NG_OG
  """Sokoto"""
  NG_SO
  """Yobe"""
  NG_YO
  """Zamfara"""
  NG_ZA
  """Akwa Ibom"""
  NG_AK
  """Enugu"""
  NG_EN
  """Imo"""
  NG_IM
  """Benue"""
  NG_BE
  """Cross River"""
  NG_CR
  """Jigawa"""
  NG_JI
  """Adamawa"""
  NG_AD
  """Anambra"""
  NG_AN
  """Abia"""
  NG_AB
  """Bauchi"""
  NG_BA
  """Edo"""
  NG_ED
  """Gombe"""
  NG_GO
  """Kwara"""
  NG_KW
  """Plateau"""
  NG_PL
  """Rivers"""
  NG_RI
  """Carazo"""
  NI_CA
  """Estelí"""
  NI_ES
  """Managua"""
  NI_MN
  """Masaya"""
  NI_MS
  """Atlántico Norte"""
  NI_AN
  """Rivas"""
  NI_RI
  """Río San Juan"""
  NI_SJ
  """Atlántico Sur"""
  NI_AS
  """Granada"""
  NI_GR
  """Madriz"""
  NI_MD
  """León"""
  NI_LE
  """Nueva Segovia"""
  NI_NS
  """Chinandega"""
  NI_CI
  """Jinotega"""
  NI_JI
  """Chontales"""
  NI_CO
  """Boaco"""
  NI_BO
  """Matagalpa"""
  NI_MT
  """Noord-Brabant"""
  NL_NB
  """Noord-Holland"""
  NL_NH
  """Zuid-Holland"""
  NL_ZH
  """Curaçao """
  NL_CW
  """Groningen"""
  NL_GR
  """Limburg"""
  NL_LI
  """Overijssel"""
  NL_OV
  """Aruba """
  NL_AW
  """Drenthe"""
  NL_DR
  """Sint Eustatius """
  NL_BQ3
  """Gelderland"""
  NL_GE
  """Utrecht"""
  NL_UT
  """Flevoland"""
  NL_FL
  """Fryslân"""
  NL_FR
  """Bonaire """
  NL_BQ1
  """Zeeland"""
  NL_ZE
  """Sint Maarten """
  NL_SX
  """Saba """
  NL_BQ2
  """Hedmark"""
  NO_04
  """Hordaland"""
  NO_12
  """Sogn og Fjordane"""
  NO_14
  """Jan Mayen """
  NO_22
  """Akershus"""
  NO_02
  """Oslo"""
  NO_03
  """Oppland"""
  NO_05
  """Vestfold"""
  NO_07
  """Finnmárku"""
  NO_20
  """Østfold"""
  NO_01
  """Vest-Agder"""
  NO_10
  """Romsa"""
  NO_19
  """Telemark"""
  NO_08
  """Buskerud"""
  NO_06
  """Aust-Agder"""
  NO_09
  """Sør-Trøndelag"""
  NO_16
  """Nord-Trøndelag"""
  NO_17
  """Svalbard """
  NO_21
  """Nordland"""
  NO_18
  """Rogaland"""
  NO_11
  """Møre og Romsdal"""
  NO_15
  """Mid Western"""
  NP_2
  """Rapti"""
  NP_RA
  """Bheri"""
  NP_BH
  """Karnali"""
  NP_KA
  """Western"""
  NP_3
  """Dhawalagiri"""
  NP_DH
  """Gandaki"""
  NP_GA
  """Lumbini"""
  NP_LU
  """Eastern"""
  NP_4
  """Mechi"""
  NP_ME
  """Kosi"""
  NP_KO
  """Sagarmatha"""
  NP_SA
  """Far Western"""
  NP_5
  """Seti"""
  NP_SE
  """Mahakali"""
  NP_MA
  """Central"""
  NP_1
  """Janakpur"""
  NP_JA
  """Bagmati"""
  NP_BA
  """Narayani"""
  NP_NA
  """Anabar"""
  NR_02
  """Anibare"""
  NR_04
  """Aiwo"""
  NR_01
  """Anetan"""
  NR_03
  """Denigomodu"""
  NR_08
  """Ijuw"""
  NR_10
  """Ewa"""
  NR_09
  """Nibok"""
  NR_12
  """Yaren"""
  NR_14
  """Buada"""
  NR_07
  """Uaboe"""
  NR_13
  """Baiti"""
  NR_05
  """Boe"""
  NR_06
  """Meneng"""
  NR_11
  """South Island"""
  NZ_S
  """Tasman District"""
  NZ_TAS
  """Marlborough District"""
  NZ_MBH
  """Southland"""
  NZ_STL
  """Otago"""
  NZ_OTA
  """Canterbury"""
  NZ_CAN
  """Nelson City"""
  NZ_NSN
  """West Coast"""
  NZ_WTC
  """North Island"""
  NZ_N
  """Auckland"""
  NZ_AUK
  """Waikato"""
  NZ_WKO
  """Northland"""
  NZ_NTL
  """Taranaki"""
  NZ_TKI
  """Hawke's Bay"""
  NZ_HKB
  """Gisborne District"""
  NZ_GIS
  """Manawatu-Wanganui"""
  NZ_MWT
  """Bay of Plenty"""
  NZ_BOP
  """Wellington"""
  NZ_WGN
  """Chatham Islands Territory"""
  NZ_CIT
  """Ash Sharqīyah"""
  OM_SH
  """Az̧ Z̧āhirah"""
  OM_ZA
  """Ad Dākhilīyah"""
  OM_DA
  """Masqaţ"""
  OM_MA
  """Z̧ufār"""
  OM_ZU
  """Al Bāţinah"""
  OM_BA
  """Al Buraymī"""
  OM_BU
  """Musandam"""
  OM_MU
  """Al Wusţá"""
  OM_WU
  """Panamá Oeste"""
  PA_10
  """Bocas del Toro"""
  PA_1
  """Coclé"""
  PA_2
  """Darién"""
  PA_5
  """Ngöbe-Buglé"""
  PA_NB
  """Chiriquí"""
  PA_4
  """Los Santos"""
  PA_7
  """Panamá"""
  PA_8
  """Herrera"""
  PA_6
  """Colón"""
  PA_3
  """Kuna Yala"""
  PA_KY
  """Emberá"""
  PA_EM
  """Veraguas"""
  PA_9
  """Ica"""
  PE_ICA
  """Lima"""
  PE_LIM
  """Mayutata"""
  PE_MDD
  """El Callao"""
  PE_CAL
  """Ayacucho"""
  PE_AYA
  """Huánuco"""
  PE_HUC
  """Anqash"""
  PE_ANC
  """Wankawelika"""
  PE_HUV
  """Lambayeque"""
  PE_LAM
  """Tacna"""
  PE_TAC
  """Apurimaq"""
  PE_APU
  """La Libertad"""
  PE_LAL
  """Pasqu"""
  PE_PAS
  """Piwra"""
  PE_PIU
  """Cusco"""
  PE_CUS
  """Moquegua"""
  PE_MOQ
  """Punu"""
  PE_PUN
  """San Martin"""
  PE_SAM
  """Amasunu"""
  PE_AMA
  """Ariqipa"""
  PE_ARE
  """Tumbes"""
  PE_TUM
  """Kashamarka"""
  PE_CAJ
  """Junín"""
  PE_JUN
  """Lima llaqta suyu"""
  PE_LMA
  """Luritu"""
  PE_LOR
  """Ucayali"""
  PE_UCA
  """Western Highlands"""
  PG_WHM
  """Hela"""
  PG_HLA
  """Jiwaka"""
  PG_JWK
  """National Capital District (Port Moresby)"""
  PG_NCD
  """Western"""
  PG_WPD
  """East Sepik"""
  PG_ESW
  """Gulf"""
  PG_GPK
  """Bougainville"""
  PG_NSB
  """East New Britain"""
  PG_EBR
  """New Ireland"""
  PG_NIK
  """West Sepik"""
  PG_SAN
  """Eastern Highlands"""
  PG_EHG
  """Enga"""
  PG_EPW
  """Manus"""
  PG_MRL
  """Northern"""
  PG_NPP
  """West New Britain"""
  PG_WBK
  """Milne Bay"""
  PG_MBA
  """Morobe"""
  PG_MPL
  """Southern Highlands"""
  PG_SHM
  """Chimbu"""
  PG_CPK
  """Central"""
  PG_CPM
  """Madang"""
  PG_MPM
  """Western Visayas (Region VI)"""
  PH_06
  """Aklan"""
  PH_AKL
  """Antique"""
  PH_ANT
  """Capiz"""
  PH_CAP
  """Guimaras"""
  PH_GUI
  """Iloilo"""
  PH_ILI
  """Negros Occidental"""
  PH_NEC
  """Davao (Region XI)"""
  PH_11
  """Compostela Valley"""
  PH_COM
  """Davao del Norte"""
  PH_DAV
  """South Cotabato"""
  PH_SCO
  """Sarangani"""
  PH_SAR
  """Davao Oriental"""
  PH_DAO
  """Davao del Sur"""
  PH_DAS
  """Caraga (Region XIII)"""
  PH_13
  """Surigao del Norte"""
  PH_SUN
  """Dinagat Islands"""
  PH_DIN
  """Surigao del Sur"""
  PH_SUR
  """Agusan del Sur"""
  PH_AGS
  """Agusan del Norte"""
  PH_AGN
  """Ilocos (Region I)"""
  PH_01
  """Ilocos Sur"""
  PH_ILS
  """Ilocos Norte"""
  PH_ILN
  """La Union"""
  PH_LUN
  """Pangasinan"""
  PH_PAN
  """Central Luzon (Region III)"""
  PH_03
  """Bataan"""
  PH_BAN
  """Aurora"""
  PH_AUR
  """Pampanga"""
  PH_PAM
  """Bulacan"""
  PH_BUL
  """Nueva Ecija"""
  PH_NUE
  """Tarlac"""
  PH_TAR
  """Zambales"""
  PH_ZMB
  """Eastern Visayas (Region VIII)"""
  PH_08
  """Leyte"""
  PH_LEY
  """Southern Leyte"""
  PH_SLE
  """Biliran"""
  PH_BIL
  """Eastern Samar"""
  PH_EAS
  """Northern Samar"""
  PH_NSA
  """Samar"""
  PH_WSA
  """Northern Mindanao (Region X)"""
  PH_10
  """Misamis Oriental"""
  PH_MSR
  """Misamis Occidental"""
  PH_MSC
  """Camiguin"""
  PH_CAM
  """Bukidnon"""
  PH_BUK
  """National Capital Region"""
  PH_00
  """Cagayan Valley (Region II)"""
  PH_02
  """Batanes"""
  PH_BTN
  """Cagayan"""
  PH_CAG
  """Nueva Vizcaya"""
  PH_NUV
  """Quirino"""
  PH_QUI
  """Isabela"""
  PH_ISA
  """Central Visayas (Region VII)"""
  PH_07
  """Bohol"""
  PH_BOH
  """Negros Oriental"""
  PH_NER
  """Siquijor"""
  PH_SIG
  """Cebu"""
  PH_CEB
  """Bicol (Region V)"""
  PH_05
  """Catanduanes"""
  PH_CAT
  """Masbate"""
  PH_MAS
  """Camarines Norte"""
  PH_CAN
  """Sorsogon"""
  PH_SOR
  """Albay"""
  PH_ALB
  """Camarines Sur"""
  PH_CAS
  """Zamboanga Peninsula (Region IX)"""
  PH_09
  """Basilan"""
  PH_BAS
  """Zamboanga del Sur"""
  PH_ZAS
  """Zamboanga del Norte"""
  PH_ZAN
  """Zamboanga Sibugay"""
  PH_ZSI
  """Soccsksargen (Region XII)"""
  PH_12
  """Lanao del Norte"""
  PH_LAN
  """Sultan Kudarat"""
  PH_SUK
  """Cotabato"""
  PH_NCO
  """Autonomous Region in Muslim Mindanao (ARMM)"""
  PH_14
  """Lanao del Sur"""
  PH_LAS
  """Maguindanao"""
  PH_MAG
  """Sulu"""
  PH_SLU
  """Tawi-Tawi"""
  PH_TAW
  """Cordillera Administrative Region (CAR)"""
  PH_15
  """Abra"""
  PH_ABR
  """Ifugao"""
  PH_IFU
  """Kalinga"""
  PH_KAL
  """Benguet"""
  PH_BEN
  """Mountain Province"""
  PH_MOU
  """Apayao"""
  PH_APA
  """Calabarzon (Region IV-A)"""
  PH_40
  """Laguna"""
  PH_LAG
  """Quezon"""
  PH_QUE
  """Rizal"""
  PH_RIZ
  """Batangas"""
  PH_BTG
  """Cavite"""
  PH_CAV
  """Mimaropa (Region IV-B)"""
  PH_41
  """Romblon"""
  PH_ROM
  """Marinduque"""
  PH_MAD
  """Mindoro Occidental"""
  PH_MDC
  """Mindoro Oriental"""
  PH_MDR
  """Palawan"""
  PH_PLW
  """Gilgit-Baltistan"""
  PK_GB
  """Sindh"""
  PK_SD
  """Khyber Pakhtunkhwa"""
  PK_KP
  """Federally Administered Tribal Areas"""
  PK_TA
  """Punjab"""
  PK_PB
  """Azad Kashmir"""
  PK_JK
  """Balochistan"""
  PK_BA
  """Islamabad"""
  PK_IS
  """Dolnośląskie"""
  PL_DS
  """Podlaskie"""
  PL_PD
  """Świętokrzyskie"""
  PL_SK
  """Śląskie"""
  PL_SL
  """Warmińsko-mazurskie"""
  PL_WN
  """Zachodniopomorskie"""
  PL_ZP
  """Lubelskie"""
  PL_LU
  """Małopolskie"""
  PL_MA
  """Mazowieckie"""
  PL_MZ
  """Lubuskie"""
  PL_LB
  """Podkarpackie"""
  PL_PK
  """Pomorskie"""
  PL_PM
  """Kujawsko-pomorskie"""
  PL_KP
  """Opolskie"""
  PL_OP
  """Wielkopolskie"""
  PL_WP
  """Łódzkie"""
  PL_LD
  """Deir El Balah"""
  PS_DEB
  """Qalqilya"""
  PS_QQA
  """Rafah"""
  PS_RFH
  """Hebron"""
  PS_HBN
  """Jenin"""
  PS_JEN
  """North Gaza"""
  PS_NGZ
  """Ramallah"""
  PS_RBH
  """Tubas"""
  PS_TBS
  """Gaza"""
  PS_GZA
  """Jericho – Al Aghwar"""
  PS_JRH
  """Nablus"""
  PS_NBS
  """Bethlehem"""
  PS_BTH
  """Jerusalem"""
  PS_JEM
  """Salfit"""
  PS_SLT
  """Tulkarm"""
  PS_TKM
  """Khan Yunis"""
  PS_KYS
  """Aveiro"""
  PT_01
  """Beja"""
  PT_02
  """Castelo Branco"""
  PT_05
  """Guarda"""
  PT_09
  """Portalegre"""
  PT_12
  """Bragança"""
  PT_04
  """Coimbra"""
  PT_06
  """Leiria"""
  PT_10
  """Lisboa"""
  PT_11
  """Setúbal"""
  PT_15
  """Viana do Castelo"""
  PT_16
  """Região Autónoma da Madeira"""
  PT_30
  """Braga"""
  PT_03
  """Vila Real"""
  PT_17
  """Évora"""
  PT_07
  """Porto"""
  PT_13
  """Santarém"""
  PT_14
  """Faro"""
  PT_08
  """Viseu"""
  PT_18
  """Região Autónoma dos Açores"""
  PT_20
  """Melekeok"""
  PW_212
  """Ngaraard"""
  PW_214
  """Ngatpang"""
  PW_224
  """Ngiwal"""
  PW_228
  """Ngarchelong"""
  PW_218
  """Airai"""
  PW_004
  """Ngeremlengui"""
  PW_227
  """Peleliu"""
  PW_350
  """Aimeliik"""
  PW_002
  """Angaur"""
  PW_010
  """Koror"""
  PW_150
  """Ngardmau"""
  PW_222
  """Ngchesar"""
  PW_226
  """Sonsorol"""
  PW_370
  """Hatobohei"""
  PW_050
  """Kayangel"""
  PW_100
  """Ñeembucú"""
  PY_12
  """Presidente Hayes"""
  PY_15
  """Cordillera"""
  PY_3
  """Misiones"""
  PY_8
  """Paraguarí"""
  PY_9
  """Boquerón"""
  PY_19
  """Caazapá"""
  PY_6
  """Itapúa"""
  PY_7
  """Asunción"""
  PY_ASU
  """Guairá"""
  PY_4
  """Concepción"""
  PY_1
  """Caaguazú"""
  PY_5
  """Amambay"""
  PY_13
  """Alto Paraguay"""
  PY_16
  """San Pedro"""
  PY_2
  """Alto Paraná"""
  PY_10
  """Central"""
  PY_11
  """Canindeyú"""
  PY_14
  """Umm Şalāl"""
  QA_US
  """Al Wakrah"""
  QA_WA
  """Az̧ Z̧a‘āyin"""
  QA_ZA
  """Ar Rayyān"""
  QA_RA
  """Ad Dawḩah"""
  QA_DA
  """Al Khawr wa adh Dhakhīrah"""
  QA_KH
  """Ash Shamāl"""
  QA_MS
  """Bihor"""
  RO_BH
  """Ilfov"""
  RO_IF
  """Iaşi"""
  RO_IS
  """Vaslui"""
  RO_VS
  """Bucureşti"""
  RO_B
  """Galaţi"""
  RO_GL
  """Satu Mare"""
  RO_SM
  """Suceava"""
  RO_SV
  """Teleorman"""
  RO_TR
  """Vâlcea"""
  RO_VL
  """Vrancea"""
  RO_VN
  """Brăila"""
  RO_BR
  """Constanţa"""
  RO_CT
  """Ialomiţa"""
  RO_IL
  """Mehedinţi"""
  RO_MH
  """Maramureş"""
  RO_MM
  """Olt"""
  RO_OT
  """Prahova"""
  RO_PH
  """Buzău"""
  RO_BZ
  """Dolj"""
  RO_DJ
  """Hunedoara"""
  RO_HD
  """Harghita"""
  RO_HR
  """Timiş"""
  RO_TM
  """Argeş"""
  RO_AG
  """Bacău"""
  RO_BC
  """Gorj"""
  RO_GJ
  """Sălaj"""
  RO_SJ
  """Braşov"""
  RO_BV
  """Giurgiu"""
  RO_GR
  """Neamţ"""
  RO_NT
  """Tulcea"""
  RO_TL
  """Bistriţa-Năsăud"""
  RO_BN
  """Călăraşi"""
  RO_CL
  """Caraş-Severin"""
  RO_CS
  """Covasna"""
  RO_CV
  """Dâmboviţa"""
  RO_DB
  """Mureş"""
  RO_MS
  """Alba"""
  RO_AB
  """Arad"""
  RO_AR
  """Botoşani"""
  RO_BT
  """Cluj"""
  RO_CJ
  """Sibiu"""
  RO_SB
  """Braničevski okrug"""
  RS_11
  """Pomoravski okrug"""
  RS_13
  """Zlatiborski okrug"""
  RS_16
  """Kosovo-Metohija"""
  RS_KM
  """Prizrenski okrug"""
  RS_27
  """Kosovski okrug"""
  RS_25
  """Pećki okrug"""
  RS_26
  """Kosovsko-Mitrovački okrug"""
  RS_28
  """Kosovsko-Pomoravski okrug"""
  RS_29
  """Vojvodina"""
  RS_VO
  """Severnobački okrug"""
  RS_01
  """Zapadnobački okrug"""
  RS_05
  """Severnobanatski okrug"""
  RS_03
  """Južnobanatski okrug"""
  RS_04
  """Srednjebanatski okrug"""
  RS_02
  """Sremski okrug"""
  RS_07
  """Južnobački okrug"""
  RS_06
  """Nišavski okrug"""
  RS_20
  """Toplički okrug"""
  RS_21
  """Pirotski okrug"""
  RS_22
  """Pčinjski okrug"""
  RS_24
  """Kolubarski okrug"""
  RS_09
  """Podunavski okrug"""
  RS_10
  """Rasinski okrug"""
  RS_19
  """Beograd"""
  RS_00
  """Šumadijski okrug"""
  RS_12
  """Borski okrug"""
  RS_14
  """Zaječarski okrug"""
  RS_15
  """Jablanički okrug"""
  RS_23
  """Mačvanski okrug"""
  RS_08
  """Raški okrug"""
  RS_18
  """Moravički okrug"""
  RS_17
  """Udmurtskaja Respublika"""
  RU_UD
  """Chuvashskaya Respublika"""
  RU_CU
  """Dagestan, Respublika"""
  RU_DA
  """Irkutskaja oblast'"""
  RU_IRK
  """Kamčatskij kraj"""
  RU_KAM
  """Habarovskij kraj"""
  RU_KHA
  """Magadanskaja oblast'"""
  RU_MAG
  """Novgorodskaya oblast'"""
  RU_NGR
  """Nizhegorodskaya oblast'"""
  RU_NIZ
  """Orenburgskaya oblast'"""
  RU_ORE
  """Orlovskaya oblast'"""
  RU_ORL
  """Pskovskaja oblast'"""
  RU_PSK
  """Sverdlovskaja oblast'"""
  RU_SVE
  """Yaroslavskaya oblast'"""
  RU_YAR
  """Zabajkal'skij kraj"""
  RU_ZAB
  """Tjumenskaja oblast'"""
  RU_TYU
  """Altayskiy kray"""
  RU_ALT
  """Ivanovskaja oblast'"""
  RU_IVA
  """Krasnodarskij kraj"""
  RU_KDA
  """Kemerovskaja oblast'"""
  RU_KEM
  """Hanty-Mansijskij avtonomnyj okrug"""
  RU_KHM
  """Khakasiya, Respublika"""
  RU_KK
  """Lipetskaya oblast'"""
  RU_LIP
  """Marij Èl, Respublika"""
  RU_ME
  """Mordovija, Respublika"""
  RU_MO
  """Penzenskaja oblast'"""
  RU_PNZ
  """Sakha, Respublika"""
  RU_SA
  """Smolenskaya oblast'"""
  RU_SMO
  """Vologodskaja oblast'"""
  RU_VLG
  """Astrahanskaja oblast'"""
  RU_AST
  """Burjatija, Respublika"""
  RU_BU
  """Čukotskij avtonomnyj okrug"""
  RU_CHU
  """Stavropol'skij kraj"""
  RU_STA
  """Yamalo-Nenetskiy avtonomnyy okrug"""
  RU_YAN
  """Evrejskaja avtonomnaja oblast'"""
  RU_YEV
  """Belgorodskaja oblast'"""
  RU_BEL
  """Ingushetiya, Respublika"""
  RU_IN
  """Karelija, Respublika"""
  RU_KR
  """Kurskaya oblast'"""
  RU_KRS
  """Moskva"""
  RU_MOW
  """Ryazanskaya oblast'"""
  RU_RYA
  """Sakhalinskaya oblast'"""
  RU_SAK
  """Tatarstan, Respublika"""
  RU_TA
  """Tomskaja oblast'"""
  RU_TOM
  """Tul'skaya oblast'"""
  RU_TUL
  """Ul'yanovskaya oblast'"""
  RU_ULY
  """Vladimirskaja oblast'"""
  RU_VLA
  """Voronezhskaya oblast'"""
  RU_VOR
  """Brjanskaja oblast'"""
  RU_BRY
  """Chelyabinskaya oblast'"""
  RU_CHE
  """Kurganskaya oblast'"""
  RU_KGN
  """Kirovskaya oblast'"""
  RU_KIR
  """Moskovskaja oblast'"""
  RU_MOS
  """Samarskaja oblast'"""
  RU_SAM
  """Tambovskaja oblast'"""
  RU_TAM
  """Amurskaja oblast'"""
  RU_AMU
  """Kalmykiya, Respublika"""
  RU_KL
  """Kostromskaja oblast'"""
  RU_KOS
  """Murmanskaja oblast'"""
  RU_MUR
  """Omskaja oblast'"""
  RU_OMS
  """Tyva, Respublika"""
  RU_TY
  """Adygeja, Respublika"""
  RU_AD
  """Bashkortostan, Respublika"""
  RU_BA
  """Karačaevo-Čerkesskaja Respublika"""
  RU_KC
  """Kaluzhskaya oblast'"""
  RU_KLU
  """Leningradskaya oblast'"""
  RU_LEN
  """Novosibirskaja oblast'"""
  RU_NVS
  """Permskij kraj"""
  RU_PER
  """Tverskaya oblast'"""
  RU_TVE
  """Volgogradskaya oblast'"""
  RU_VGG
  """Altay, Respublika"""
  RU_AL
  """Arhangel'skaja oblast'"""
  RU_ARK
  """Chechenskaya Respublika"""
  RU_CE
  """Kabardino-Balkarskaja Respublika"""
  RU_KB
  """Kaliningradskaja oblast'"""
  RU_KGD
  """Komi, Respublika"""
  RU_KO
  """Krasnoyarskiy kray"""
  RU_KYA
  """Neneckij avtonomnyj okrug"""
  RU_NEN
  """Primorskij kraj"""
  RU_PRI
  """Rostovskaja oblast'"""
  RU_ROS
  """Saratovskaja oblast'"""
  RU_SAR
  """Severnaja Osetija, Respublika"""
  RU_SE
  """Sankt-Peterburg"""
  RU_SPE
  """Nord"""
  RW_03
  """Ouest"""
  RW_04
  """Ville de Kigali"""
  RW_01
  """Est"""
  RW_02
  """Sud"""
  RW_05
  """Makkah al Mukarramah"""
  SA_02
  """Al Bāḩah"""
  SA_11
  """Al Jawf"""
  SA_12
  """'Asīr"""
  SA_14
  """Al Ḩudūd ash Shamālīyah"""
  SA_08
  """Al Madīnah al Munawwarah"""
  SA_03
  """Ash Sharqīyah"""
  SA_04
  """Najrān"""
  SA_10
  """Tabūk"""
  SA_07
  """Ar Riyāḑ"""
  SA_01
  """Al Qaşīm"""
  SA_05
  """Ḩā'il"""
  SA_06
  """Jāzān"""
  SA_09
  """Western"""
  SB_WE
  """Isabel"""
  SB_IS
  """Central"""
  SB_CE
  """Capital Territory (Honiara)"""
  SB_CT
  """Malaita"""
  SB_ML
  """Makira-Ulawa"""
  SB_MK
  """Rennell and Bellona"""
  SB_RB
  """Guadalcanal"""
  SB_GU
  """Temotu"""
  SB_TE
  """Choiseul"""
  SB_CH
  """Les Mamelles"""
  SC_24
  """Anse Royale"""
  SC_05
  """Baie Sainte Anne"""
  SC_07
  """Bel Ombre"""
  SC_10
  """Cascade"""
  SC_11
  """English River"""
  SC_16
  """Mont Fleuri"""
  SC_18
  """Roche Caiman"""
  SC_25
  """Beau Vallon"""
  SC_08
  """Plaisance"""
  SC_19
  """Glacis"""
  SC_12
  """Grand Anse Mahe"""
  SC_13
  """Au Cap"""
  SC_04
  """Mont Buxton"""
  SC_17
  """La Digue"""
  SC_15
  """Pointe Larue"""
  SC_20
  """Port Glaud"""
  SC_21
  """Takamaka"""
  SC_23
  """Anse aux Pins"""
  SC_01
  """Anse Boileau"""
  SC_02
  """Bel Air"""
  SC_09
  """Grand Anse Praslin"""
  SC_14
  """Saint Louis"""
  SC_22
  """Anse Etoile"""
  SC_03
  """Baie Lazare"""
  SC_06
  """Gedaref"""
  SD_GD
  """Red Sea"""
  SD_RS
  """East Darfur"""
  SD_DE
  """Khartoum"""
  SD_KH
  """Northern"""
  SD_NO
  """South Darfur"""
  SD_DS
  """Sennar"""
  SD_SI
  """North Darfur"""
  SD_DN
  """West Darfur"""
  SD_DW
  """Gezira"""
  SD_GZ
  """White Nile"""
  SD_NW
  """Central Darfur"""
  SD_DC
  """Kassala"""
  SD_KA
  """North Kordofan"""
  SD_KN
  """South Kordofan"""
  SD_KS
  """Blue Nile"""
  SD_NB
  """River Nile"""
  SD_NR
  """Gotlands län """
  SE_I
  """Hallands län """
  SE_N
  """Värmlands län """
  SE_S
  """Örebro län """
  SE_T
  """Västra Götalands län """
  SE_O
  """Gävleborgs län """
  SE_X
  """Blekinge län """
  SE_K
  """Västmanlands län """
  SE_U
  """Dalarnas län """
  SE_W
  """Västernorrlands län """
  SE_Y
  """Östergötlands län """
  SE_E
  """Stockholms län """
  SE_AB
  """Södermanlands län """
  SE_D
  """Kronobergs län """
  SE_G
  """Jämtlands län """
  SE_Z
  """Norrbottens län """
  SE_BD
  """Jönköpings län """
  SE_F
  """Västerbottens län """
  SE_AC
  """Uppsala län """
  SE_C
  """Kalmar län """
  SE_H
  """Skåne län """
  SE_M
  """North East"""
  SG_02
  """North West"""
  SG_03
  """South East"""
  SG_04
  """Central Singapore"""
  SG_01
  """South West"""
  SG_05
  """Saint Helena"""
  SH_HL
  """Tristan da Cunha"""
  SH_TA
  """Ascension"""
  SH_AC
  """Bled"""
  SI_003
  """Borovnica"""
  SI_005
  """Brezovica"""
  SI_008
  """Destrnik"""
  SI_018
  """Dornava"""
  SI_024
  """Šalovci"""
  SI_033
  """Ig"""
  SI_037
  """Juršinci"""
  SI_042
  """Kanal"""
  SI_044
  """Laško"""
  SI_057
  """Maribor"""
  SI_070
  """Miren-Kostanjevica"""
  SI_075
  """Muta"""
  SI_081
  """Postojna"""
  SI_094
  """Preddvor"""
  SI_095
  """Sežana"""
  SI_111
  """Slovenska Bistrica"""
  SI_113
  """Slovenske Konjice"""
  SI_114
  """Velike Lašče"""
  SI_134
  """Zavrč"""
  SI_143
  """Žiri"""
  SI_147
  """Braslovče"""
  SI_151
  """Hoče-Slivnica"""
  SI_160
  """Markovci"""
  SI_168
  """Prevalje"""
  SI_175
  """Velika Polana"""
  SI_187
  """Apače"""
  SI_195
  """Sveti Jurij v Slovenskih Goricah"""
  SI_210
  """Mirna"""
  SI_212
  """Brda"""
  SI_007
  """Črna na Koroškem"""
  SI_016
  """Dol pri Ljubljani"""
  SI_022
  """Gorišnica"""
  SI_028
  """Kidričevo"""
  SI_045
  """Kozje"""
  SI_051
  """Loška Dolina"""
  SI_065
  """Luče"""
  SI_067
  """Lukovica"""
  SI_068
  """Mežica"""
  SI_074
  """Mozirje"""
  SI_079
  """Murska Sobota"""
  SI_080
  """Naklo"""
  SI_082
  """Novo Mesto"""
  SI_085
  """Osilnica"""
  SI_088
  """Semič"""
  SI_109
  """Sveti Jurij"""
  SI_116
  """Šmartno ob Paki"""
  SI_125
  """Šoštanj"""
  SI_126
  """Zagorje ob Savi"""
  SI_142
  """Benedikt"""
  SI_148
  """Cerkvenjak"""
  SI_153
  """Hajdina"""
  SI_159
  """Horjul"""
  SI_162
  """Križevci"""
  SI_166
  """Prebold"""
  SI_174
  """Solčava"""
  SI_180
  """Mokronog-Trebelno"""
  SI_199
  """Idrija"""
  SI_036
  """Kobilje"""
  SI_047
  """Ljubljana"""
  SI_061
  """Odranci"""
  SI_086
  """Podčetrtek"""
  SI_092
  """Podvelka"""
  SI_093
  """Radovljica"""
  SI_102
  """Rogatec"""
  SI_107
  """Trbovlje"""
  SI_129
  """Vitanje"""
  SI_137
  """Bistrica ob Sotli"""
  SI_149
  """Bloke"""
  SI_150
  """Cankova"""
  SI_152
  """Dobje"""
  SI_154
  """Jezersko"""
  SI_163
  """Podlehnik"""
  SI_172
  """Selnica ob Dravi"""
  SI_178
  """Renče-Vogrsko"""
  SI_201
  """Ajdovščina"""
  SI_001
  """Divača"""
  SI_019
  """Dravograd"""
  SI_025
  """Gorenja vas-Poljane"""
  SI_027
  """Grosuplje"""
  SI_032
  """Hrastnik"""
  SI_034
  """Ivančna Gorica"""
  SI_039
  """Izola"""
  SI_040
  """Kranjska Gora"""
  SI_053
  """Lenart"""
  SI_058
  """Litija"""
  SI_060
  """Nova Gorica"""
  SI_084
  """Pivka"""
  SI_091
  """Radeče"""
  SI_099
  """Ribnica"""
  SI_104
  """Škocjan"""
  SI_121
  """Videm"""
  SI_135
  """Dolenjske Toplice"""
  SI_157
  """Mirna Peč"""
  SI_170
  """Oplotnica"""
  SI_171
  """Ribnica na Pohorju"""
  SI_177
  """Sodražica"""
  SI_179
  """Sveta Ana"""
  SI_181
  """Tabor"""
  SI_184
  """Trzin"""
  SI_186
  """Makole"""
  SI_198
  """Poljčane"""
  SI_200
  """Straža"""
  SI_203
  """Šentrupert"""
  SI_211
  """Bohinj"""
  SI_004
  """Bovec"""
  SI_006
  """Brežice"""
  SI_009
  """Črenšovci"""
  SI_015
  """Gornji Petrovci"""
  SI_031
  """Jesenice"""
  SI_041
  """Kobarid"""
  SI_046
  """Kočevje"""
  SI_048
  """Loški Potok"""
  SI_066
  """Majšperk"""
  SI_069
  """Medvode"""
  SI_071
  """Mengeš"""
  SI_072
  """Mislinja"""
  SI_076
  """Moravske Toplice"""
  SI_078
  """Piran"""
  SI_090
  """Puconci"""
  SI_097
  """Radenci"""
  SI_100
  """Ravne na Koroškem"""
  SI_103
  """Šentjur"""
  SI_120
  """Vipava"""
  SI_136
  """Dobrovnik"""
  SI_156
  """Hodoš"""
  SI_161
  """Polzela"""
  SI_173
  """Sveti Andraž v Slovenskih Goricah"""
  SI_182
  """Žalec"""
  SI_190
  """Žirovnica"""
  SI_192
  """Tišina"""
  SI_010
  """Celje"""
  SI_011
  """Cerknica"""
  SI_013
  """Dobrepolje"""
  SI_020
  """Dobrova-Polhov Gradec"""
  SI_021
  """Domžale"""
  SI_023
  """Gornja Radgona"""
  SI_029
  """Ilirska Bistrica"""
  SI_038
  """Komen"""
  SI_049
  """Kranj"""
  SI_052
  """Ljutomer"""
  SI_063
  """Metlika"""
  SI_073
  """Moravče"""
  SI_077
  """Nazarje"""
  SI_083
  """Pesnica"""
  SI_089
  """Ptuj"""
  SI_096
  """Sevnica"""
  SI_110
  """Starše"""
  SI_115
  """Šentilj"""
  SI_118
  """Škofljica"""
  SI_123
  """Šmarje pri Jelšah"""
  SI_124
  """Trebnje"""
  SI_130
  """Tržič"""
  SI_131
  """Turnišče"""
  SI_132
  """Velenje"""
  SI_133
  """Železniki"""
  SI_146
  """Kostel"""
  SI_165
  """Razkrižje"""
  SI_176
  """Trnovska Vas"""
  SI_185
  """Veržej"""
  SI_188
  """Vransko"""
  SI_189
  """Žetale"""
  SI_191
  """Šmartno pri Litiji"""
  SI_194
  """Cirkulane"""
  SI_196
  """Sveta Trojica v Slovenskih Goricah"""
  SI_204
  """Sveti Tomaž"""
  SI_205
  """Log-Dragomer"""
  SI_208
  """Cerklje na Gorenjskem"""
  SI_012
  """Cerkno"""
  SI_014
  """Črnomelj"""
  SI_017
  """Gornji Grad"""
  SI_030
  """Lendava"""
  SI_059
  """Ormož"""
  SI_087
  """Rače-Fram"""
  SI_098
  """Radlje ob Dravi"""
  SI_101
  """Rogaška Slatina"""
  SI_106
  """Ruše"""
  SI_108
  """Šenčur"""
  SI_117
  """Šentjernej"""
  SI_119
  """Štore"""
  SI_127
  """Vodice"""
  SI_138
  """Vojnik"""
  SI_139
  """Vrhnika"""
  SI_140
  """Dobrna"""
  SI_155
  """Grad"""
  SI_158
  """Komenda"""
  SI_164
  """Šempeter-Vrtojba"""
  SI_183
  """Kosanjevica na Krki"""
  SI_197
  """Šmarješke Toplice"""
  SI_206
  """Gorje"""
  SI_207
  """Rečica ob Savinji"""
  SI_209
  """Beltinci"""
  SI_002
  """Duplek"""
  SI_026
  """Hrpelje-Kozina"""
  SI_035
  """Kamnik"""
  SI_043
  """Koper"""
  SI_050
  """Krško"""
  SI_054
  """Kungota"""
  SI_055
  """Kuzma"""
  SI_056
  """Ljubno"""
  SI_062
  """Logatec"""
  SI_064
  """Rogašovci"""
  SI_105
  """Slovenj Gradec"""
  SI_112
  """Škofja Loka"""
  SI_122
  """Tolmin"""
  SI_128
  """Vuzenica"""
  SI_141
  """Zreče"""
  SI_144
  """Lovrenc na Pohorju"""
  SI_167
  """Miklavž na Dravskem Polju"""
  SI_169
  """Žužemberk"""
  SI_193
  """Središče ob Dravi"""
  SI_202
  """Žilinský kraj"""
  SK_ZI
  """Prešovský kraj"""
  SK_PV
  """Trnavský kraj"""
  SK_TA
  """Košický kraj"""
  SK_KI
  """Banskobystrický kraj"""
  SK_BC
  """Nitriansky kraj"""
  SK_NI
  """Bratislavský kraj"""
  SK_BL
  """Trenčiansky kraj"""
  SK_TC
  """Southern"""
  SL_S
  """Northern"""
  SL_N
  """Eastern"""
  SL_E
  """Western Area (Freetown)"""
  SL_W
  """Acquaviva"""
  SM_01
  """Fiorentino"""
  SM_05
  """Domagnano"""
  SM_03
  """Borgo Maggiore"""
  SM_06
  """Montegiardino"""
  SM_08
  """Chiesanuova"""
  SM_02
  """Faetano"""
  SM_04
  """Serravalle"""
  SM_09
  """San Marino"""
  SM_07
  """Thiès"""
  SN_TH
  """Kaolack"""
  SN_KL
  """Sédhiou"""
  SN_SE
  """Dakar"""
  SN_DK
  """Kolda"""
  SN_KD
  """Saint-Louis"""
  SN_SL
  """Fatick"""
  SN_FK
  """Kaffrine"""
  SN_KA
  """Ziguinchor"""
  SN_ZG
  """Kédougou"""
  SN_KE
  """Louga"""
  SN_LG
  """Diourbel"""
  SN_DB
  """Matam"""
  SN_MT
  """Tambacounda"""
  SN_TC
  """Galguduud"""
  SO_GA
  """Hiiraan"""
  SO_HI
  """Shabeellaha Hoose"""
  SO_SH
  """Bay"""
  SO_BY
  """Jubbada Dhexe"""
  SO_JD
  """Mudug"""
  SO_MU
  """Sanaag"""
  SO_SA
  """Shabeellaha Dhexe"""
  SO_SD
  """Sool"""
  SO_SO
  """Woqooyi Galbeed"""
  SO_WO
  """Bakool"""
  SO_BK
  """Bari"""
  SO_BR
  """Banaadir"""
  SO_BN
  """Awdal"""
  SO_AW
  """Gedo"""
  SO_GE
  """Jubbada Hoose"""
  SO_JH
  """Nugaal"""
  SO_NU
  """Togdheer"""
  SO_TO
  """Wanica"""
  SR_WA
  """Commewijne"""
  SR_CM
  """Marowijne"""
  SR_MA
  """Saramacca"""
  SR_SA
  """Coronie"""
  SR_CR
  """Paramaribo"""
  SR_PM
  """Brokopondo"""
  SR_BR
  """Nickerie"""
  SR_NI
  """Para"""
  SR_PR
  """Sipaliwini"""
  SR_SI
  """Eastern Equatoria"""
  SS_EE
  """Western Bahr el  Ghazal"""
  SS_BW
  """Upper Nile"""
  SS_NU
  """Unity"""
  SS_UY
  """Northern Bahr el Ghazal"""
  SS_BN
  """Warrap"""
  SS_WR
  """Central Equatoria"""
  SS_EC
  """Western Equatoria"""
  SS_EW
  """Jonglei"""
  SS_JG
  """Lakes"""
  SS_LK
  """São Tomé"""
  ST_S
  """Príncipe"""
  ST_P
  """Cuscatlán"""
  SV_CU
  """San Salvador"""
  SV_SS
  """Chalatenango"""
  SV_CH
  """Ahuachapán"""
  SV_AH
  """Santa Ana"""
  SV_SA
  """Sonsonate"""
  SV_SO
  """La Paz"""
  SV_PA
  """San Miguel"""
  SV_SM
  """Cabañas"""
  SV_CA
  """La Unión"""
  SV_UN
  """La Libertad"""
  SV_LI
  """San Vicente"""
  SV_SV
  """Morazán"""
  SV_MO
  """Usulután"""
  SV_US
  """Dimashq"""
  SY_DI
  """Idlib"""
  SY_ID
  """Rīf Dimashq"""
  SY_RD
  """Ţarţūs"""
  SY_TA
  """Dayr az Zawr"""
  SY_DY
  """Al Lādhiqīyah"""
  SY_LA
  """Ar Raqqah"""
  SY_RA
  """Al Qunayţirah"""
  SY_QU
  """As Suwaydā'"""
  SY_SU
  """Dar'ā"""
  SY_DR
  """Ḩimş"""
  SY_HI
  """Al Ḩasakah"""
  SY_HA
  """Ḩalab"""
  SY_HL
  """Ḩamāh"""
  SY_HM
  """Shiselweni"""
  SZ_SH
  """Manzini"""
  SZ_MA
  """Lubombo"""
  SZ_LU
  """Hhohho"""
  SZ_HH
  """Lac"""
  TD_LC
  """Māyū Kībbī ash Sharqī"""
  TD_ME
  """Wadi Fira"""
  TD_WF
  """Ennedi-Est"""
  TD_EE
  """Ennedi-Ouest"""
  TD_EO
  """Kānim"""
  TD_KA
  """Lūqūn ash Sharqī"""
  TD_LR
  """Sila"""
  TD_SI
  """Būrkū"""
  TD_BO
  """Guéra"""
  TD_GR
  """Tānjilī"""
  TD_TA
  """Tibastī"""
  TD_TI
  """Baḩr al Ghazāl"""
  TD_BG
  """Shārī Bāqirmī"""
  TD_CB
  """Logone-Occidental"""
  TD_LO
  """Mandoul"""
  TD_MA
  """Batha"""
  TD_BA
  """Ḩajjar Lamīs"""
  TD_HL
  """Māyū Kībbī al Gharbī"""
  TD_MO
  """Shārī al Awsaţ"""
  TD_MC
  """Madīnat Injamīnā"""
  TD_ND
  """Waddāy"""
  TD_OD
  """Salamat"""
  TD_SA
  """Kara"""
  TG_K
  """Centre"""
  TG_C
  """Plateaux"""
  TG_P
  """Savannes"""
  TG_S
  """Maritime (Région)"""
  TG_M
  """Krung Thep Maha Nakhon"""
  TH_10
  """Nong Khai"""
  TH_43
  """Lamphun"""
  TH_51
  """Chiang Rai"""
  TH_57
  """Tak"""
  TH_63
  """Ratchaburi"""
  TH_70
  """Prachuap Khiri Khan"""
  TH_77
  """Phangnga"""
  TH_82
  """Trang"""
  TH_92
  """Phatthalung"""
  TH_93
  """Rayong"""
  TH_21
  """Chanthaburi"""
  TH_22
  """Nan"""
  TH_55
  """Phayao"""
  TH_56
  """Nakhon Sawan"""
  TH_60
  """Phitsanulok"""
  TH_65
  """Phetchabun"""
  TH_67
  """Pattani"""
  TH_94
  """Yala"""
  TH_95
  """Lop Buri"""
  TH_16
  """Chachoengsao"""
  TH_24
  """Yasothon"""
  TH_35
  """Nong Bua Lam Phu"""
  TH_39
  """Kalasin"""
  TH_46
  """Nakhon Phanom"""
  TH_48
  """Phrae"""
  TH_54
  """Phichit"""
  TH_66
  """Nakhon Si Thammarat"""
  TH_80
  """Phatthaya"""
  TH_S
  """Phra Nakhon Si Ayutthaya"""
  TH_14
  """Chon Buri"""
  TH_20
  """Sakon Nakhon"""
  TH_47
  """Mukdahan"""
  TH_49
  """Lampang"""
  TH_52
  """Mae Hong Son"""
  TH_58
  """Uthai Thani"""
  TH_61
  """Ranong"""
  TH_85
  """Trat"""
  TH_23
  """Sa Kaeo"""
  TH_27
  """Amnat Charoen"""
  TH_37
  """Loei"""
  TH_42
  """Roi Et"""
  TH_45
  """Suphan Buri"""
  TH_72
  """Samut Sakhon"""
  TH_74
  """Surat Thani"""
  TH_84
  """Pathum Thani"""
  TH_13
  """Ang Thong"""
  TH_15
  """Chai Nat"""
  TH_18
  """Nakhon Ratchasima"""
  TH_30
  """Surin"""
  TH_32
  """Kanchanaburi"""
  TH_71
  """Nakhon Pathom"""
  TH_73
  """Phuket"""
  TH_83
  """Chumphon"""
  TH_86
  """Satun"""
  TH_91
  """Bueng Kan"""
  TH_38
  """Samut Prakan"""
  TH_11
  """Sing Buri"""
  TH_17
  """Saraburi"""
  TH_19
  """Ubon Ratchathani"""
  TH_34
  """Chaiyaphum"""
  TH_36
  """Udon Thani"""
  TH_41
  """Maha Sarakham"""
  TH_44
  """Samut Songkhram"""
  TH_75
  """Songkhla"""
  TH_90
  """Narathiwat"""
  TH_96
  """Nonthaburi"""
  TH_12
  """Prachin Buri"""
  TH_25
  """Nakhon Nayok"""
  TH_26
  """Buri Ram"""
  TH_31
  """Si Sa Ket"""
  TH_33
  """Khon Kaen"""
  TH_40
  """Chiang Mai"""
  TH_50
  """Uttaradit"""
  TH_53
  """Kamphaeng Phet"""
  TH_62
  """Sukhothai"""
  TH_64
  """Phetchaburi"""
  TH_76
  """Krabi"""
  TH_81
  """Dushanbe"""
  TJ_DU
  """Khatlon"""
  TJ_KT
  """Sughd"""
  TJ_SU
  """Kŭhistoni Badakhshon"""
  TJ_GB
  """Aileu"""
  TL_AL
  """Oekusi-Ambenu"""
  TL_OE
  """Viqueque"""
  TL_VI
  """Ermera"""
  TL_ER
  """Bobonaru"""
  TL_BO
  """Cova Lima"""
  TL_CO
  """Manufahi"""
  TL_MF
  """Ainaru"""
  TL_AN
  """Baucau"""
  TL_BA
  """Lautém"""
  TL_LA
  """Díli"""
  TL_DI
  """Likisá"""
  TL_LI
  """Manatutu"""
  TL_MT
  """Balkan"""
  TM_B
  """Ahal"""
  TM_A
  """Aşgabat"""
  TM_S
  """Daşoguz"""
  TM_D
  """Lebap"""
  TM_L
  """Mary"""
  TM_M
  """Ben Arous"""
  TN_13
  """Kasserine"""
  TN_42
  """Sidi Bouzid"""
  TN_43
  """Mahdia"""
  TN_53
  """Kebili"""
  TN_73
  """Ariana"""
  TN_12
  """Nabeul"""
  TN_21
  """Tozeur"""
  TN_72
  """Siliana"""
  TN_34
  """Kairouan"""
  TN_41
  """Monastir"""
  TN_52
  """Tataouine"""
  TN_83
  """Bizerte"""
  TN_23
  """Sousse"""
  TN_51
  """Gafsa"""
  TN_71
  """Le Kef"""
  TN_33
  """Tunis"""
  TN_11
  """La Manouba"""
  TN_14
  """Béja"""
  TN_31
  """Sfax"""
  TN_61
  """Gabès"""
  TN_81
  """Medenine"""
  TN_82
  """Zaghouan"""
  TN_22
  """Jendouba"""
  TN_32
  """Ha'apai"""
  TO_02
  """Niuas"""
  TO_03
  """Tongatapu"""
  TO_04
  """'Eua"""
  TO_01
  """Vava'u"""
  TO_05
  """Bolu"""
  TR_14
  """Kayseri"""
  TR_38
  """Kocaeli"""
  TR_41
  """Malatya"""
  TR_44
  """Sivas"""
  TR_58
  """Aksaray"""
  TR_68
  """Kırıkkale"""
  TR_71
  """Şırnak"""
  TR_73
  """Adana"""
  TR_01
  """Bursa"""
  TR_16
  """Çorum"""
  TR_19
  """Denizli"""
  TR_20
  """İstanbul"""
  TR_34
  """Mardin"""
  TR_47
  """Muş"""
  TR_49
  """Sinop"""
  TR_57
  """Yozgat"""
  TR_66
  """Bayburt"""
  TR_69
  """Ardahan"""
  TR_75
  """Yalova"""
  TR_77
  """Karabük"""
  TR_78
  """Afyonkarahisar"""
  TR_03
  """Artvin"""
  TR_08
  """Burdur"""
  TR_15
  """Edirne"""
  TR_22
  """Erzurum"""
  TR_25
  """Gaziantep"""
  TR_27
  """Gümüşhane"""
  TR_29
  """Kırşehir"""
  TR_40
  """Manisa"""
  TR_45
  """Siirt"""
  TR_56
  """Zonguldak"""
  TR_67
  """Karaman"""
  TR_70
  """Adıyaman"""
  TR_02
  """Amasya"""
  TR_05
  """Bilecik"""
  TR_11
  """Bitlis"""
  TR_13
  """Çanakkale"""
  TR_17
  """Kütahya"""
  TR_43
  """Ordu"""
  TR_52
  """Tokat"""
  TR_60
  """Trabzon"""
  TR_61
  """Tunceli"""
  TR_62
  """Osmaniye"""
  TR_80
  """Balıkesir"""
  TR_10
  """Çankırı"""
  TR_18
  """Hakkâri"""
  TR_30
  """Hatay"""
  TR_31
  """Isparta"""
  TR_32
  """İzmir"""
  TR_35
  """Kastamonu"""
  TR_37
  """Bartın"""
  TR_74
  """Diyarbakır"""
  TR_21
  """Erzincan"""
  TR_24
  """Giresun"""
  TR_28
  """Mersin"""
  TR_33
  """Kahramanmaraş"""
  TR_46
  """Sakarya"""
  TR_54
  """Van"""
  TR_65
  """Batman"""
  TR_72
  """Kırklareli"""
  TR_39
  """Nevşehir"""
  TR_50
  """Rize"""
  TR_53
  """Samsun"""
  TR_55
  """Şanlıurfa"""
  TR_63
  """Uşak"""
  TR_64
  """Iğdır"""
  TR_76
  """Düzce"""
  TR_81
  """Ağrı"""
  TR_04
  """Ankara"""
  TR_06
  """Antalya"""
  TR_07
  """Aydın"""
  TR_09
  """Bingöl"""
  TR_12
  """Elazığ"""
  TR_23
  """Eskişehir"""
  TR_26
  """Kars"""
  TR_36
  """Konya"""
  TR_42
  """Muğla"""
  TR_48
  """Niğde"""
  TR_51
  """Tekirdağ"""
  TR_59
  """Kilis"""
  TR_79
  """Penal-Debe"""
  TT_PED
  """Siparia"""
  TT_SIP
  """Arima"""
  TT_ARI
  """Diego Martin"""
  TT_DMN
  """Point Fortin"""
  TT_PTF
  """Rio Claro-Mayaro"""
  TT_RCM
  """Tunapuna-Piarco"""
  TT_TUP
  """Couva-Tabaquite-Talparo"""
  TT_CTT
  """Princes Town"""
  TT_PRT
  """San Juan-Laventille"""
  TT_SJL
  """Chaguanas"""
  TT_CHA
  """Eastern Tobago"""
  TT_ETO
  """Sangre Grande"""
  TT_SGE
  """Port of Spain"""
  TT_POS
  """San Fernando"""
  TT_SFO
  """Western Tobago"""
  TT_WTO
  """Nukufetau"""
  TV_NKF
  """Nanumanga"""
  TV_NMG
  """Funafuti"""
  TV_FUN
  """Nanumea"""
  TV_NMA
  """Nui"""
  TV_NUI
  """Niutao"""
  TV_NIT
  """Vaitupu"""
  TV_VAI
  """Nukulaelae"""
  TV_NKL
  """Kaohsiung"""
  TW_KHH
  """Taitung"""
  TW_TTT
  """Chiayi"""
  TW_CYI
  """Chiayi"""
  TW_CYQ
  """Hualien"""
  TW_HUA
  """Hsinchu"""
  TW_HSZ
  """Penghu"""
  TW_PEN
  """Pingtung"""
  TW_PIF
  """Taipei"""
  TW_TPE
  """Taipei"""
  TW_TPQ
  """Changhua"""
  TW_CHA
  """Ilan"""
  TW_ILA
  """Tainan"""
  TW_TNN
  """Taichung"""
  TW_TXQ
  """Yunlin"""
  TW_YUN
  """Nantou"""
  TW_NAN
  """Taoyuan"""
  TW_TAO
  """Tainan"""
  TW_TNQ
  """Taichung"""
  TW_TXG
  """Hsinchu"""
  TW_HSQ
  """Miaoli"""
  TW_MIA
  """Keelung"""
  TW_KEE
  """Kaohsiung"""
  TW_KHQ
  """Dar es Salaam"""
  TZ_02
  """Iringa"""
  TZ_04
  """Kagera"""
  TZ_05
  """Zanzibar North"""
  TZ_07
  """Geita"""
  TZ_27
  """Katavi"""
  TZ_28
  """Njombe"""
  TZ_29
  """Simiyu"""
  TZ_30
  """Arusha"""
  TZ_01
  """Lindi"""
  TZ_12
  """Zanzibar West"""
  TZ_15
  """Singida"""
  TZ_23
  """Coast"""
  TZ_19
  """Tanga"""
  TZ_25
  """Pemba South"""
  TZ_10
  """Mtwara"""
  TZ_17
  """Zanzibar South"""
  TZ_11
  """Ruvuma"""
  TZ_21
  """Tabora"""
  TZ_24
  """Dodoma"""
  TZ_03
  """Kigoma"""
  TZ_08
  """Kilimanjaro"""
  TZ_09
  """Morogoro"""
  TZ_16
  """Mwanza"""
  TZ_18
  """Mara"""
  TZ_13
  """Shinyanga"""
  TZ_22
  """Pemba North"""
  TZ_06
  """Mbeya"""
  TZ_14
  """Rukwa"""
  TZ_20
  """Manyara"""
  TZ_26
  """Luhanska oblast"""
  UA_09
  """Zakarpatska oblast"""
  UA_21
  """Zaporizka oblast"""
  UA_23
  """Kyivska oblast"""
  UA_32
  """Kirovohradska oblast"""
  UA_35
  """Sumska oblast"""
  UA_59
  """Vinnytska oblast"""
  UA_05
  """Kharkivska oblast"""
  UA_63
  """Chernihivska oblast"""
  UA_74
  """Dnipropetrovska oblast"""
  UA_12
  """Mykolaivska oblast"""
  UA_48
  """Rivnenska oblast"""
  UA_56
  """Cherkaska oblast"""
  UA_71
  """Ivano-Frankivska oblast"""
  UA_26
  """Odeska oblast"""
  UA_51
  """Chernivetska oblast"""
  UA_77
  """Sevastopol"""
  UA_40
  """Poltavska oblast"""
  UA_53
  """Donetska oblast"""
  UA_14
  """Avtonomna Respublika Krym"""
  UA_43
  """Lvivska oblast"""
  UA_46
  """Zhytomyrska oblast"""
  UA_18
  """Kyiv"""
  UA_30
  """Khmelnytska oblast"""
  UA_68
  """Volynska oblast"""
  UA_07
  """Ternopilska oblast"""
  UA_61
  """Khersonska oblast"""
  UA_65
  """Western"""
  UG_W
  """Kiryandongo"""
  UG_420
  """Kyegegwa"""
  UG_421
  """Mitooma"""
  UG_422
  """Ntoroko"""
  UG_423
  """Rubirizi"""
  UG_424
  """Sheema"""
  UG_425
  """Bundibugyo"""
  UG_401
  """Hoima"""
  UG_403
  """Kyenjojo"""
  UG_415
  """Buliisa"""
  UG_419
  """Kabale"""
  UG_404
  """Ntungamo"""
  UG_411
  """Kamwenge"""
  UG_413
  """Ibanda"""
  UG_416
  """Kanungu"""
  UG_414
  """Isingiro"""
  UG_417
  """Kiruhura"""
  UG_418
  """Kabarole"""
  UG_405
  """Kibaale"""
  UG_407
  """Masindi"""
  UG_409
  """Rukungiri"""
  UG_412
  """Bushenyi"""
  UG_402
  """Kasese"""
  UG_406
  """Kisoro"""
  UG_408
  """Mbarara"""
  UG_410
  """Central"""
  UG_C
  """Buikwe"""
  UG_117
  """Bukomansibi"""
  UG_118
  """Butambala"""
  UG_119
  """Buvuma"""
  UG_120
  """Gomba"""
  UG_121
  """Kalungu"""
  UG_122
  """Kampala"""
  UG_102
  """Kyankwanzi"""
  UG_123
  """Lwengo"""
  UG_124
  """Luwero"""
  UG_104
  """Mubende"""
  UG_107
  """Lyantonde"""
  UG_116
  """Kiboga"""
  UG_103
  """Kalangala"""
  UG_101
  """Mpigi"""
  UG_106
  """Nakasongola"""
  UG_109
  """Rakai"""
  UG_110
  """Kayunga"""
  UG_112
  """Wakiso"""
  UG_113
  """Masaka"""
  UG_105
  """Nakaseke"""
  UG_115
  """Mukono"""
  UG_108
  """Sembabule"""
  UG_111
  """Mityana"""
  UG_114
  """Eastern"""
  UG_E
  """Bulambuli"""
  UG_225
  """Buyende"""
  UG_226
  """Kibuku"""
  UG_227
  """Kween"""
  UG_228
  """Luuka"""
  UG_229
  """Namayingo"""
  UG_230
  """Ngora"""
  UG_231
  """Serere"""
  UG_232
  """Pallisa"""
  UG_210
  """Bugiri"""
  UG_201
  """Soroti"""
  UG_211
  """Budaka"""
  UG_217
  """Bukedea"""
  UG_224
  """Jinja"""
  UG_204
  """Mbale"""
  UG_209
  """Tororo"""
  UG_212
  """Bududa"""
  UG_223
  """Busia"""
  UG_202
  """Katakwi"""
  UG_207
  """Kamuli"""
  UG_205
  """Kumi"""
  UG_208
  """Namutumba"""
  UG_222
  """Iganga"""
  UG_203
  """Kapchorwa"""
  UG_206
  """Kaberamaido"""
  UG_213
  """Mayuge"""
  UG_214
  """Sironko"""
  UG_215
  """Bukwa"""
  UG_218
  """Butaleja"""
  UG_219
  """Manafwa"""
  UG_221
  """Amuria"""
  UG_216
  """Kaliro"""
  UG_220
  """Northern"""
  UG_N
  """Agago"""
  UG_322
  """Alebtong"""
  UG_323
  """Amudat"""
  UG_324
  """Buhweju"""
  UG_325
  """Kole"""
  UG_326
  """Lamwo"""
  UG_327
  """Napak"""
  UG_328
  """Nwoya"""
  UG_329
  """Otuke"""
  UG_330
  """Zombo"""
  UG_331
  """Kotido"""
  UG_306
  """Moyo"""
  UG_309
  """Nebbi"""
  UG_310
  """Yumbe"""
  UG_313
  """Dokolo"""
  UG_318
  """Apac"""
  UG_302
  """Arua"""
  UG_303
  """Nakapiripirit"""
  UG_311
  """Gulu"""
  UG_304
  """Pader"""
  UG_312
  """Amuru"""
  UG_319
  """Adjumani"""
  UG_301
  """Moroto"""
  UG_308
  """Amolatar"""
  UG_314
  """Kaabong"""
  UG_315
  """Abim"""
  UG_317
  """Koboko"""
  UG_316
  """Maracha"""
  UG_320
  """Kitgum"""
  UG_305
  """Lira"""
  UG_307
  """Oyam"""
  UG_321
  """Midway Islands"""
  UM_71
  """Howland Island"""
  UM_84
  """Jarvis Island"""
  UM_86
  """Wake Island"""
  UM_79
  """Kingman Reef"""
  UM_89
  """Navassa Island"""
  UM_76
  """Johnston Atoll"""
  UM_67
  """Baker Island"""
  UM_81
  """Palmyra Atoll"""
  UM_95
  """American Samoa"""
  US_AS
  """Georgia"""
  US_GA
  """Kansas"""
  US_KS
  """Minnesota"""
  US_MN
  """Texas"""
  US_TX
  """United States Minor Outlying Islands"""
  US_UM
  """Alaska"""
  US_AK
  """Alabama"""
  US_AL
  """Colorado"""
  US_CO
  """Kentucky"""
  US_KY
  """Northern Mariana Islands"""
  US_MP
  """New York"""
  US_NY
  """Rhode Island"""
  US_RI
  """South Carolina"""
  US_SC
  """South Dakota"""
  US_SD
  """Washington"""
  US_WA
  """District of Columbia"""
  US_DC
  """Guam """
  US_GU
  """Iowa"""
  US_IA
  """Ohio"""
  US_OH
  """Oregon"""
  US_OR
  """California"""
  US_CA
  """Delaware"""
  US_DE
  """Hawaii"""
  US_HI
  """Massachusetts"""
  US_MA
  """Montana"""
  US_MT
  """North Carolina"""
  US_NC
  """Nebraska"""
  US_NE
  """New Jersey"""
  US_NJ
  """Virgin Islands, U.S."""
  US_VI
  """Connecticut"""
  US_CT
  """Florida"""
  US_FL
  """Indiana"""
  US_IN
  """Oklahoma"""
  US_OK
  """Utah"""
  US_UT
  """Wisconsin"""
  US_WI
  """West Virginia"""
  US_WV
  """Idaho"""
  US_ID
  """Illinois"""
  US_IL
  """Maryland"""
  US_MD
  """Maine"""
  US_ME
  """Missouri"""
  US_MO
  """Mississippi"""
  US_MS
  """New Mexico"""
  US_NM
  """Pennsylvania"""
  US_PA
  """Vermont"""
  US_VT
  """Wyoming"""
  US_WY
  """Arizona"""
  US_AZ
  """Louisiana"""
  US_LA
  """North Dakota"""
  US_ND
  """New Hampshire"""
  US_NH
  """Nevada"""
  US_NV
  """Virginia"""
  US_VA
  """Arkansas"""
  US_AR
  """Michigan"""
  US_MI
  """Puerto Rico """
  US_PR
  """Tennessee"""
  US_TN
  """Armed Forces of the Americas"""
  US_AA
  """Armed Forces of Europe"""
  US_AE
  """Armed Forces of the Pacific"""
  US_AP
  """Colonia"""
  UY_CO
  """Lavalleja"""
  UY_LA
  """Río Negro"""
  UY_RN
  """Salto"""
  UY_SA
  """Durazno"""
  UY_DU
  """Florida"""
  UY_FD
  """Flores"""
  UY_FS
  """Rivera"""
  UY_RV
  """Cerro Largo"""
  UY_CL
  """Maldonado"""
  UY_MA
  """Rocha"""
  UY_RO
  """Tacuarembó"""
  UY_TA
  """San José"""
  UY_SJ
  """Artigas"""
  UY_AR
  """Paysandú"""
  UY_PA
  """Soriano"""
  UY_SO
  """Canelones"""
  UY_CA
  """Montevideo"""
  UY_MO
  """Treinta y Tres"""
  UY_TT
  """Jizzax"""
  UZ_JI
  """Namangan"""
  UZ_NG
  """Farg‘ona"""
  UZ_FA
  """Qashqadaryo"""
  UZ_QA
  """Andijon"""
  UZ_AN
  """Qoraqalpog‘iston Respublikasi"""
  UZ_QR
  """Samarqand"""
  UZ_SA
  """Sirdaryo"""
  UZ_SI
  """Surxondaryo"""
  UZ_SU
  """Xorazm"""
  UZ_XO
  """Toshkent"""
  UZ_TK
  """Toshkent"""
  UZ_TO
  """Buxoro"""
  UZ_BU
  """Navoiy"""
  UZ_NW
  """Charlotte"""
  VC_01
  """Grenadines"""
  VC_06
  """Saint Andrew"""
  VC_02
  """Saint Patrick"""
  VC_05
  """Saint David"""
  VC_03
  """Saint George"""
  VC_04
  """Aragua"""
  VE_D
  """Portuguesa"""
  VE_P
  """Táchira"""
  VE_S
  """Bolívar"""
  VE_F
  """Cojedes"""
  VE_H
  """Falcón"""
  VE_I
  """Amazonas"""
  VE_Z
  """Guárico"""
  VE_J
  """Lara"""
  VE_K
  """Nueva Esparta"""
  VE_O
  """Yaracuy"""
  VE_U
  """Apure"""
  VE_C
  """Delta Amacuro"""
  VE_Y
  """Distrito Capital"""
  VE_A
  """Anzoátegui"""
  VE_B
  """Mérida"""
  VE_L
  """Monagas"""
  VE_N
  """Sucre"""
  VE_R
  """Trujillo"""
  VE_T
  """Dependencias Federales"""
  VE_W
  """Vargas"""
  VE_X
  """Barinas"""
  VE_E
  """Miranda"""
  VE_M
  """Carabobo"""
  VE_G
  """Zulia"""
  VE_V
  """Yên Bái"""
  VN_06
  """Ninh Bình"""
  VN_18
  """Nghệ An"""
  VN_22
  """Trà Vinh"""
  VN_51
  """Hà Nam"""
  VN_63
  """Thái Nguyên"""
  VN_69
  """Phú Yên"""
  VN_32
  """Ninh Thuận"""
  VN_36
  """Sóc Trăng"""
  VN_52
  """Bắc Giang"""
  VN_54
  """Bắc Ninh"""
  VN_56
  """Bình Phước"""
  VN_58
  """Hậu Giang"""
  VN_73
  """Lào Cai"""
  VN_02
  """Quảng Ninh"""
  VN_13
  """Thái Bình"""
  VN_20
  """Quảng Ngãi"""
  VN_29
  """Hưng Yên"""
  VN_66
  """Phú Thọ"""
  VN_68
  """Hà Tĩnh"""
  VN_23
  """Thừa Thiên-Huế"""
  VN_26
  """Đắk Lắk"""
  VN_33
  """Khánh Hòa"""
  VN_34
  """An Giang"""
  VN_44
  """Ðồng Tháp"""
  VN_45
  """Sơn La"""
  VN_05
  """Hòa Bình"""
  VN_14
  """Quảng Trị"""
  VN_25
  """Kiến Giang"""
  VN_47
  """Hải Dương"""
  VN_61
  """Nam Ðịnh"""
  VN_67
  """Hai Phong"""
  VN_HP
  """Ho Chi Minh"""
  VN_SG
  """Lạng Sơn"""
  VN_09
  """Thanh Hóa"""
  VN_21
  """Quảng Bình"""
  VN_24
  """Bình Thuận"""
  VN_40
  """Bà Rịa - Vũng Tàu"""
  VN_43
  """Tiền Giang"""
  VN_46
  """Bến Tre"""
  VN_50
  """Bạc Liêu"""
  VN_55
  """Cà Mau"""
  VN_59
  """Vĩnh Phúc"""
  VN_70
  """Tuyên Quang"""
  VN_07
  """Gia Lai"""
  VN_30
  """Lâm Ðồng"""
  VN_35
  """Tây Ninh"""
  VN_37
  """Ðồng Nai"""
  VN_39
  """Bình Dương"""
  VN_57
  """Đắk Nông"""
  VN_72
  """Can Tho"""
  VN_CT
  """Ha Noi"""
  VN_HN
  """Lai Châu"""
  VN_01
  """Hà Giang"""
  VN_03
  """Cao Bằng"""
  VN_04
  """Quảng Nam"""
  VN_27
  """Kon Tum"""
  VN_28
  """Bình Định"""
  VN_31
  """Long An"""
  VN_41
  """Vĩnh Long"""
  VN_49
  """Bắc Kạn"""
  VN_53
  """Điện Biên"""
  VN_71
  """Da Nang"""
  VN_DN
  """Shéfa"""
  VU_SEE
  """Malampa"""
  VU_MAP
  """Pénama"""
  VU_PAM
  """Sanma"""
  VU_SAM
  """Torba"""
  VU_TOB
  """Taféa"""
  VU_TAE
  """Satupa'itea"""
  WS_SA
  """A'ana"""
  WS_AA
  """Fa'asaleleaga"""
  WS_FA
  """Gaga'emauga"""
  WS_GE
  """Atua"""
  WS_AT
  """Palauli"""
  WS_PA
  """Tuamasaga"""
  WS_TU
  """Va'a-o-Fonoti"""
  WS_VF
  """Gagaifomauga"""
  WS_GI
  """Aiga-i-le-Tai"""
  WS_AL
  """Vaisigano"""
  WS_VS
  """Ḩaḑramawt"""
  YE_HD
  """Ḩajjah"""
  YE_HJ
  """Şanʻā'"""
  YE_SN
  """Ibb"""
  YE_IB
  """Al Mahrah"""
  YE_MR
  """'Adan"""
  YE_AD
  """Dhamār"""
  YE_DH
  """Amānat al ‘Āşimah """
  YE_SA
  """Ma'rib"""
  YE_MA
  """Aḑ Ḑāli'"""
  YE_DA
  """Shabwah"""
  YE_SH
  """'Amrān"""
  YE_AM
  """Al Bayḑā'"""
  YE_BA
  """Abyān"""
  YE_AB
  """Al Jawf"""
  YE_JA
  """Şāʻdah"""
  YE_SD
  """Al Ḩudaydah"""
  YE_HU
  """Laḩij"""
  YE_LA
  """Al Maḩwīt"""
  YE_MW
  """Raymah"""
  YE_RA
  """Tāʻizz"""
  YE_TA
  """Kwazulu-Natal"""
  ZA_NL
  """Western Cape"""
  ZA_WC
  """Northern Cape"""
  ZA_NC
  """Gauteng"""
  ZA_GT
  """Eastern Cape"""
  ZA_EC
  """Mpumalanga"""
  ZA_MP
  """Free State"""
  ZA_FS
  """Limpopo"""
  ZA_LP
  """North-West"""
  ZA_NW
  """Northern"""
  ZM_05
  """Western"""
  ZM_01
  """Muchinga"""
  ZM_10
  """Central"""
  ZM_02
  """North-Western"""
  ZM_06
  """Southern"""
  ZM_07
  """Luapula"""
  ZM_04
  """Eastern"""
  ZM_03
  """Copperbelt"""
  ZM_08
  """Lusaka"""
  ZM_09
  """Manicaland"""
  ZW_MA
  """Mashonaland Central"""
  ZW_MC
  """Matabeleland South"""
  ZW_MS
  """Bulawayo"""
  ZW_BU
  """Harare"""
  ZW_HA
  """Midlands"""
  ZW_MI
  """Mashonaland West"""
  ZW_MW
  """Mashonaland East"""
  ZW_ME
  """Matabeleland North"""
  ZW_MN
  """Masvingo"""
  ZW_MV
}

"""The system time zone."""
enum Timezone {
  """Africa/Abidjan"""
  AFRICAABIDJAN
  """Africa/Accra"""
  AFRICAACCRA
  """Africa/Addis_Ababa"""
  AFRICAADDISABABA
  """Africa/Algiers"""
  AFRICAALGIERS
  """Africa/Asmara"""
  AFRICAASMARA
  """Africa/Asmera"""
  AFRICAASMERA
  """Africa/Bamako"""
  AFRICABAMAKO
  """Africa/Bangui"""
  AFRICABANGUI
  """Africa/Banjul"""
  AFRICABANJUL
  """Africa/Bissau"""
  AFRICABISSAU
  """Africa/Blantyre"""
  AFRICABLANTYRE
  """Africa/Brazzaville"""
  AFRICABRAZZAVILLE
  """Africa/Bujumbura"""
  AFRICABUJUMBURA
  """Africa/Cairo"""
  AFRICACAIRO
  """Africa/Casablanca"""
  AFRICACASABLANCA
  """Africa/Ceuta"""
  AFRICACEUTA
  """Africa/Conakry"""
  AFRICACONAKRY
  """Africa/Dakar"""
  AFRICADAKAR
  """Africa/Dar_es_Salaam"""
  AFRICADARESSALAAM
  """Africa/Djibouti"""
  AFRICADJIBOUTI
  """Africa/Douala"""
  AFRICADOUALA
  """Africa/El_Aaiun"""
  AFRICAELAAIUN
  """Africa/Freetown"""
  AFRICAFREETOWN
  """Africa/Gaborone"""
  AFRICAGABORONE
  """Africa/Harare"""
  AFRICAHARARE
  """Africa/Johannesburg"""
  AFRICAJOHANNESBURG
  """Africa/Juba"""
  AFRICAJUBA
  """Africa/Kampala"""
  AFRICAKAMPALA
  """Africa/Khartoum"""
  AFRICAKHARTOUM
  """Africa/Kigali"""
  AFRICAKIGALI
  """Africa/Kinshasa"""
  AFRICAKINSHASA
  """Africa/Lagos"""
  AFRICALAGOS
  """Africa/Libreville"""
  AFRICALIBREVILLE
  """Africa/Lome"""
  AFRICALOME
  """Africa/Luanda"""
  AFRICALUANDA
  """Africa/Lubumbashi"""
  AFRICALUBUMBASHI
  """Africa/Lusaka"""
  AFRICALUSAKA
  """Africa/Malabo"""
  AFRICAMALABO
  """Africa/Maputo"""
  AFRICAMAPUTO
  """Africa/Maseru"""
  AFRICAMASERU
  """Africa/Mbabane"""
  AFRICAMBABANE
  """Africa/Mogadishu"""
  AFRICAMOGADISHU
  """Africa/Monrovia"""
  AFRICAMONROVIA
  """Africa/Nairobi"""
  AFRICANAIROBI
  """Africa/Ndjamena"""
  AFRICANDJAMENA
  """Africa/Niamey"""
  AFRICANIAMEY
  """Africa/Nouakchott"""
  AFRICANOUAKCHOTT
  """Africa/Ouagadougou"""
  AFRICAOUAGADOUGOU
  """Africa/Porto-Novo"""
  AFRICAPORTONOVO
  """Africa/Sao_Tome"""
  AFRICASAOTOME
  """Africa/Timbuktu"""
  AFRICATIMBUKTU
  """Africa/Tripoli"""
  AFRICATRIPOLI
  """Africa/Tunis"""
  AFRICATUNIS
  """Africa/Windhoek"""
  AFRICAWINDHOEK
  """America/Adak"""
  AMERICAADAK
  """America/Anchorage"""
  AMERICAANCHORAGE
  """America/Anguilla"""
  AMERICAANGUILLA
  """America/Antigua"""
  AMERICAANTIGUA
  """America/Araguaina"""
  AMERICAARAGUAINA
  """America/Argentina/Buenos_Aires"""
  AMERICAARGENTINABUENOSAIRES
  """America/Argentina/Catamarca"""
  AMERICAARGENTINACATAMARCA
  """America/Argentina/ComodRivadavia"""
  AMERICAARGENTINACOMODRIVADAVIA
  """America/Argentina/Cordoba"""
  AMERICAARGENTINACORDOBA
  """America/Argentina/Jujuy"""
  AMERICAARGENTINAJUJUY
  """America/Argentina/La_Rioja"""
  AMERICAARGENTINALARIOJA
  """America/Argentina/Mendoza"""
  AMERICAARGENTINAMENDOZA
  """America/Argentina/Rio_Gallegos"""
  AMERICAARGENTINARIOGALLEGOS
  """America/Argentina/Salta"""
  AMERICAARGENTINASALTA
  """America/Argentina/San_Juan"""
  AMERICAARGENTINASANJUAN
  """America/Argentina/San_Luis"""
  AMERICAARGENTINASANLUIS
  """America/Argentina/Tucuman"""
  AMERICAARGENTINATUCUMAN
  """America/Argentina/Ushuaia"""
  AMERICAARGENTINAUSHUAIA
  """America/Aruba"""
  AMERICAARUBA
  """America/Asuncion"""
  AMERICAASUNCION
  """America/Atikokan"""
  AMERICAATIKOKAN
  """America/Atka"""
  AMERICAATKA
  """America/Bahia"""
  AMERICABAHIA
  """America/Bahia_Banderas"""
  AMERICABAHIABANDERAS
  """America/Barbados"""
  AMERICABARBADOS
  """America/Belem"""
  AMERICABELEM
  """America/Belize"""
  AMERICABELIZE
  """America/Blanc-Sablon"""
  AMERICABLANCSABLON
  """America/Boa_Vista"""
  AMERICABOAVISTA
  """America/Bogota"""
  AMERICABOGOTA
  """America/Boise"""
  AMERICABOISE
  """America/Buenos_Aires"""
  AMERICABUENOSAIRES
  """America/Cambridge_Bay"""
  AMERICACAMBRIDGEBAY
  """America/Campo_Grande"""
  AMERICACAMPOGRANDE
  """America/Cancun"""
  AMERICACANCUN
  """America/Caracas"""
  AMERICACARACAS
  """America/Catamarca"""
  AMERICACATAMARCA
  """America/Cayenne"""
  AMERICACAYENNE
  """America/Cayman"""
  AMERICACAYMAN
  """America/Chicago"""
  AMERICACHICAGO
  """America/Chihuahua"""
  AMERICACHIHUAHUA
  """America/Ciudad_Juarez"""
  AMERICACIUDADJUAREZ
  """America/Coral_Harbour"""
  AMERICACORALHARBOUR
  """America/Cordoba"""
  AMERICACORDOBA
  """America/Costa_Rica"""
  AMERICACOSTARICA
  """America/Creston"""
  AMERICACRESTON
  """America/Cuiaba"""
  AMERICACUIABA
  """America/Curacao"""
  AMERICACURACAO
  """America/Danmarkshavn"""
  AMERICADANMARKSHAVN
  """America/Dawson"""
  AMERICADAWSON
  """America/Dawson_Creek"""
  AMERICADAWSONCREEK
  """America/Denver"""
  AMERICADENVER
  """America/Detroit"""
  AMERICADETROIT
  """America/Dominica"""
  AMERICADOMINICA
  """America/Edmonton"""
  AMERICAEDMONTON
  """America/Eirunepe"""
  AMERICAEIRUNEPE
  """America/El_Salvador"""
  AMERICAELSALVADOR
  """America/Ensenada"""
  AMERICAENSENADA
  """America/Fort_Nelson"""
  AMERICAFORTNELSON
  """America/Fort_Wayne"""
  AMERICAFORTWAYNE
  """America/Fortaleza"""
  AMERICAFORTALEZA
  """America/Glace_Bay"""
  AMERICAGLACEBAY
  """America/Godthab"""
  AMERICAGODTHAB
  """America/Goose_Bay"""
  AMERICAGOOSEBAY
  """America/Grand_Turk"""
  AMERICAGRANDTURK
  """America/Grenada"""
  AMERICAGRENADA
  """America/Guadeloupe"""
  AMERICAGUADELOUPE
  """America/Guatemala"""
  AMERICAGUATEMALA
  """America/Guayaquil"""
  AMERICAGUAYAQUIL
  """America/Guyana"""
  AMERICAGUYANA
  """America/Halifax"""
  AMERICAHALIFAX
  """America/Havana"""
  AMERICAHAVANA
  """America/Hermosillo"""
  AMERICAHERMOSILLO
  """America/Indiana/Indianapolis"""
  AMERICAINDIANAINDIANAPOLIS
  """America/Indiana/Knox"""
  AMERICAINDIANAKNOX
  """America/Indiana/Marengo"""
  AMERICAINDIANAMARENGO
  """America/Indiana/Petersburg"""
  AMERICAINDIANAPETERSBURG
  """America/Indiana/Tell_City"""
  AMERICAINDIANATELLCITY
  """America/Indiana/Vevay"""
  AMERICAINDIANAVEVAY
  """America/Indiana/Vincennes"""
  AMERICAINDIANAVINCENNES
  """America/Indiana/Winamac"""
  AMERICAINDIANAWINAMAC
  """America/Indianapolis"""
  AMERICAINDIANAPOLIS
  """America/Inuvik"""
  AMERICAINUVIK
  """America/Iqaluit"""
  AMERICAIQALUIT
  """America/Jamaica"""
  AMERICAJAMAICA
  """America/Jujuy"""
  AMERICAJUJUY
  """America/Juneau"""
  AMERICAJUNEAU
  """America/Kentucky/Louisville"""
  AMERICAKENTUCKYLOUISVILLE
  """America/Kentucky/Monticello"""
  AMERICAKENTUCKYMONTICELLO
  """America/Knox_IN"""
  AMERICAKNOXIN
  """America/Kralendijk"""
  AMERICAKRALENDIJK
  """America/La_Paz"""
  AMERICALAPAZ
  """America/Lima"""
  AMERICALIMA
  """America/Los_Angeles"""
  AMERICALOSANGELES
  """America/Louisville"""
  AMERICALOUISVILLE
  """America/Lower_Princes"""
  AMERICALOWERPRINCES
  """America/Maceio"""
  AMERICAMACEIO
  """America/Managua"""
  AMERICAMANAGUA
  """America/Manaus"""
  AMERICAMANAUS
  """America/Marigot"""
  AMERICAMARIGOT
  """America/Martinique"""
  AMERICAMARTINIQUE
  """America/Matamoros"""
  AMERICAMATAMOROS
  """America/Mazatlan"""
  AMERICAMAZATLAN
  """America/Mendoza"""
  AMERICAMENDOZA
  """America/Menominee"""
  AMERICAMENOMINEE
  """America/Merida"""
  AMERICAMERIDA
  """America/Metlakatla"""
  AMERICAMETLAKATLA
  """America/Mexico_City"""
  AMERICAMEXICOCITY
  """America/Miquelon"""
  AMERICAMIQUELON
  """America/Moncton"""
  AMERICAMONCTON
  """America/Monterrey"""
  AMERICAMONTERREY
  """America/Montevideo"""
  AMERICAMONTEVIDEO
  """America/Montreal"""
  AMERICAMONTREAL
  """America/Montserrat"""
  AMERICAMONTSERRAT
  """America/Nassau"""
  AMERICANASSAU
  """America/New_York"""
  AMERICANEWYORK
  """America/Nipigon"""
  AMERICANIPIGON
  """America/Nome"""
  AMERICANOME
  """America/Noronha"""
  AMERICANORONHA
  """America/North_Dakota/Beulah"""
  AMERICANORTHDAKOTABEULAH
  """America/North_Dakota/Center"""
  AMERICANORTHDAKOTACENTER
  """America/North_Dakota/New_Salem"""
  AMERICANORTHDAKOTANEWSALEM
  """America/Nuuk"""
  AMERICANUUK
  """America/Ojinaga"""
  AMERICAOJINAGA
  """America/Panama"""
  AMERICAPANAMA
  """America/Pangnirtung"""
  AMERICAPANGNIRTUNG
  """America/Paramaribo"""
  AMERICAPARAMARIBO
  """America/Phoenix"""
  AMERICAPHOENIX
  """America/Port-au-Prince"""
  AMERICAPORTAUPRINCE
  """America/Port_of_Spain"""
  AMERICAPORTOFSPAIN
  """America/Porto_Acre"""
  AMERICAPORTOACRE
  """America/Porto_Velho"""
  AMERICAPORTOVELHO
  """America/Puerto_Rico"""
  AMERICAPUERTORICO
  """America/Punta_Arenas"""
  AMERICAPUNTAARENAS
  """America/Rainy_River"""
  AMERICARAINYRIVER
  """America/Rankin_Inlet"""
  AMERICARANKININLET
  """America/Recife"""
  AMERICARECIFE
  """America/Regina"""
  AMERICAREGINA
  """America/Resolute"""
  AMERICARESOLUTE
  """America/Rio_Branco"""
  AMERICARIOBRANCO
  """America/Rosario"""
  AMERICAROSARIO
  """America/Santa_Isabel"""
  AMERICASANTAISABEL
  """America/Santarem"""
  AMERICASANTAREM
  """America/Santiago"""
  AMERICASANTIAGO
  """America/Santo_Domingo"""
  AMERICASANTODOMINGO
  """America/Sao_Paulo"""
  AMERICASAOPAULO
  """America/Scoresbysund"""
  AMERICASCORESBYSUND
  """America/Shiprock"""
  AMERICASHIPROCK
  """America/Sitka"""
  AMERICASITKA
  """America/St_Barthelemy"""
  AMERICASTBARTHELEMY
  """America/St_Johns"""
  AMERICASTJOHNS
  """America/St_Kitts"""
  AMERICASTKITTS
  """America/St_Lucia"""
  AMERICASTLUCIA
  """America/St_Thomas"""
  AMERICASTTHOMAS
  """America/St_Vincent"""
  AMERICASTVINCENT
  """America/Swift_Current"""
  AMERICASWIFTCURRENT
  """America/Tegucigalpa"""
  AMERICATEGUCIGALPA
  """America/Thule"""
  AMERICATHULE
  """America/Thunder_Bay"""
  AMERICATHUNDERBAY
  """America/Tijuana"""
  AMERICATIJUANA
  """America/Toronto"""
  AMERICATORONTO
  """America/Tortola"""
  AMERICATORTOLA
  """America/Vancouver"""
  AMERICAVANCOUVER
  """America/Virgin"""
  AMERICAVIRGIN
  """America/Whitehorse"""
  AMERICAWHITEHORSE
  """America/Winnipeg"""
  AMERICAWINNIPEG
  """America/Yakutat"""
  AMERICAYAKUTAT
  """America/Yellowknife"""
  AMERICAYELLOWKNIFE
  """Antarctica/Casey"""
  ANTARCTICACASEY
  """Antarctica/Davis"""
  ANTARCTICADAVIS
  """Antarctica/DumontDUrville"""
  ANTARCTICADUMONTDURVILLE
  """Antarctica/Macquarie"""
  ANTARCTICAMACQUARIE
  """Antarctica/Mawson"""
  ANTARCTICAMAWSON
  """Antarctica/McMurdo"""
  ANTARCTICAMCMURDO
  """Antarctica/Palmer"""
  ANTARCTICAPALMER
  """Antarctica/Rothera"""
  ANTARCTICAROTHERA
  """Antarctica/South_Pole"""
  ANTARCTICASOUTHPOLE
  """Antarctica/Syowa"""
  ANTARCTICASYOWA
  """Antarctica/Troll"""
  ANTARCTICATROLL
  """Antarctica/Vostok"""
  ANTARCTICAVOSTOK
  """Arctic/Longyearbyen"""
  ARCTICLONGYEARBYEN
  """Asia/Aden"""
  ASIAADEN
  """Asia/Almaty"""
  ASIAALMATY
  """Asia/Amman"""
  ASIAAMMAN
  """Asia/Anadyr"""
  ASIAANADYR
  """Asia/Aqtau"""
  ASIAAQTAU
  """Asia/Aqtobe"""
  ASIAAQTOBE
  """Asia/Ashgabat"""
  ASIAASHGABAT
  """Asia/Ashkhabad"""
  ASIAASHKHABAD
  """Asia/Atyrau"""
  ASIAATYRAU
  """Asia/Baghdad"""
  ASIABAGHDAD
  """Asia/Bahrain"""
  ASIABAHRAIN
  """Asia/Baku"""
  ASIABAKU
  """Asia/Bangkok"""
  ASIABANGKOK
  """Asia/Barnaul"""
  ASIABARNAUL
  """Asia/Beirut"""
  ASIABEIRUT
  """Asia/Bishkek"""
  ASIABISHKEK
  """Asia/Brunei"""
  ASIABRUNEI
  """Asia/Calcutta"""
  ASIACALCUTTA
  """Asia/Chita"""
  ASIACHITA
  """Asia/Choibalsan"""
  ASIACHOIBALSAN
  """Asia/Chongqing"""
  ASIACHONGQING
  """Asia/Chungking"""
  ASIACHUNGKING
  """Asia/Colombo"""
  ASIACOLOMBO
  """Asia/Dacca"""
  ASIADACCA
  """Asia/Damascus"""
  ASIADAMASCUS
  """Asia/Dhaka"""
  ASIADHAKA
  """Asia/Dili"""
  ASIADILI
  """Asia/Dubai"""
  ASIADUBAI
  """Asia/Dushanbe"""
  ASIADUSHANBE
  """Asia/Famagusta"""
  ASIAFAMAGUSTA
  """Asia/Gaza"""
  ASIAGAZA
  """Asia/Harbin"""
  ASIAHARBIN
  """Asia/Hebron"""
  ASIAHEBRON
  """Asia/Ho_Chi_Minh"""
  ASIAHOCHIMINH
  """Asia/Hong_Kong"""
  ASIAHONGKONG
  """Asia/Hovd"""
  ASIAHOVD
  """Asia/Irkutsk"""
  ASIAIRKUTSK
  """Asia/Istanbul"""
  ASIAISTANBUL
  """Asia/Jakarta"""
  ASIAJAKARTA
  """Asia/Jayapura"""
  ASIAJAYAPURA
  """Asia/Jerusalem"""
  ASIAJERUSALEM
  """Asia/Kabul"""
  ASIAKABUL
  """Asia/Kamchatka"""
  ASIAKAMCHATKA
  """Asia/Karachi"""
  ASIAKARACHI
  """Asia/Kashgar"""
  ASIAKASHGAR
  """Asia/Kathmandu"""
  ASIAKATHMANDU
  """Asia/Katmandu"""
  ASIAKATMANDU
  """Asia/Khandyga"""
  ASIAKHANDYGA
  """Asia/Kolkata"""
  ASIAKOLKATA
  """Asia/Krasnoyarsk"""
  ASIAKRASNOYARSK
  """Asia/Kuala_Lumpur"""
  ASIAKUALALUMPUR
  """Asia/Kuching"""
  ASIAKUCHING
  """Asia/Kuwait"""
  ASIAKUWAIT
  """Asia/Macao"""
  ASIAMACAO
  """Asia/Macau"""
  ASIAMACAU
  """Asia/Magadan"""
  ASIAMAGADAN
  """Asia/Makassar"""
  ASIAMAKASSAR
  """Asia/Manila"""
  ASIAMANILA
  """Asia/Muscat"""
  ASIAMUSCAT
  """Asia/Nicosia"""
  ASIANICOSIA
  """Asia/Novokuznetsk"""
  ASIANOVOKUZNETSK
  """Asia/Novosibirsk"""
  ASIANOVOSIBIRSK
  """Asia/Omsk"""
  ASIAOMSK
  """Asia/Oral"""
  ASIAORAL
  """Asia/Phnom_Penh"""
  ASIAPHNOMPENH
  """Asia/Pontianak"""
  ASIAPONTIANAK
  """Asia/Pyongyang"""
  ASIAPYONGYANG
  """Asia/Qatar"""
  ASIAQATAR
  """Asia/Qostanay"""
  ASIAQOSTANAY
  """Asia/Qyzylorda"""
  ASIAQYZYLORDA
  """Asia/Rangoon"""
  ASIARANGOON
  """Asia/Riyadh"""
  ASIARIYADH
  """Asia/Saigon"""
  ASIASAIGON
  """Asia/Sakhalin"""
  ASIASAKHALIN
  """Asia/Samarkand"""
  ASIASAMARKAND
  """Asia/Seoul"""
  ASIASEOUL
  """Asia/Shanghai"""
  ASIASHANGHAI
  """Asia/Singapore"""
  ASIASINGAPORE
  """Asia/Srednekolymsk"""
  ASIASREDNEKOLYMSK
  """Asia/Taipei"""
  ASIATAIPEI
  """Asia/Tashkent"""
  ASIATASHKENT
  """Asia/Tbilisi"""
  ASIATBILISI
  """Asia/Tehran"""
  ASIATEHRAN
  """Asia/Tel_Aviv"""
  ASIATELAVIV
  """Asia/Thimbu"""
  ASIATHIMBU
  """Asia/Thimphu"""
  ASIATHIMPHU
  """Asia/Tokyo"""
  ASIATOKYO
  """Asia/Tomsk"""
  ASIATOMSK
  """Asia/Ujung_Pandang"""
  ASIAUJUNGPANDANG
  """Asia/Ulaanbaatar"""
  ASIAULAANBAATAR
  """Asia/Ulan_Bator"""
  ASIAULANBATOR
  """Asia/Urumqi"""
  ASIAURUMQI
  """Asia/Ust-Nera"""
  ASIAUSTNERA
  """Asia/Vientiane"""
  ASIAVIENTIANE
  """Asia/Vladivostok"""
  ASIAVLADIVOSTOK
  """Asia/Yakutsk"""
  ASIAYAKUTSK
  """Asia/Yangon"""
  ASIAYANGON
  """Asia/Yekaterinburg"""
  ASIAYEKATERINBURG
  """Asia/Yerevan"""
  ASIAYEREVAN
  """Atlantic/Azores"""
  ATLANTICAZORES
  """Atlantic/Bermuda"""
  ATLANTICBERMUDA
  """Atlantic/Canary"""
  ATLANTICCANARY
  """Atlantic/Cape_Verde"""
  ATLANTICCAPEVERDE
  """Atlantic/Faeroe"""
  ATLANTICFAEROE
  """Atlantic/Faroe"""
  ATLANTICFAROE
  """Atlantic/Jan_Mayen"""
  ATLANTICJANMAYEN
  """Atlantic/Madeira"""
  ATLANTICMADEIRA
  """Atlantic/Reykjavik"""
  ATLANTICREYKJAVIK
  """Atlantic/South_Georgia"""
  ATLANTICSOUTHGEORGIA
  """Atlantic/St_Helena"""
  ATLANTICSTHELENA
  """Atlantic/Stanley"""
  ATLANTICSTANLEY
  """Australia/ACT"""
  AUSTRALIAACT
  """Australia/Adelaide"""
  AUSTRALIAADELAIDE
  """Australia/Brisbane"""
  AUSTRALIABRISBANE
  """Australia/Broken_Hill"""
  AUSTRALIABROKENHILL
  """Australia/Canberra"""
  AUSTRALIACANBERRA
  """Australia/Currie"""
  AUSTRALIACURRIE
  """Australia/Darwin"""
  AUSTRALIADARWIN
  """Australia/Eucla"""
  AUSTRALIAEUCLA
  """Australia/Hobart"""
  AUSTRALIAHOBART
  """Australia/LHI"""
  AUSTRALIALHI
  """Australia/Lindeman"""
  AUSTRALIALINDEMAN
  """Australia/Lord_Howe"""
  AUSTRALIALORDHOWE
  """Australia/Melbourne"""
  AUSTRALIAMELBOURNE
  """Australia/North"""
  AUSTRALIANORTH
  """Australia/NSW"""
  AUSTRALIANSW
  """Australia/Perth"""
  AUSTRALIAPERTH
  """Australia/Queensland"""
  AUSTRALIAQUEENSLAND
  """Australia/South"""
  AUSTRALIASOUTH
  """Australia/Sydney"""
  AUSTRALIASYDNEY
  """Australia/Tasmania"""
  AUSTRALIATASMANIA
  """Australia/Victoria"""
  AUSTRALIAVICTORIA
  """Australia/West"""
  AUSTRALIAWEST
  """Australia/Yancowinna"""
  AUSTRALIAYANCOWINNA
  """Brazil/Acre"""
  BRAZILACRE
  """Brazil/DeNoronha"""
  BRAZILDENORONHA
  """Brazil/East"""
  BRAZILEAST
  """Brazil/West"""
  BRAZILWEST
  """Canada/Atlantic"""
  CANADAATLANTIC
  """Canada/Central"""
  CANADACENTRAL
  """Canada/Eastern"""
  CANADAEASTERN
  """Canada/Mountain"""
  CANADAMOUNTAIN
  """Canada/Newfoundland"""
  CANADANEWFOUNDLAND
  """Canada/Pacific"""
  CANADAPACIFIC
  """Canada/Saskatchewan"""
  CANADASASKATCHEWAN
  """Canada/Yukon"""
  CANADAYUKON
  """CET"""
  CET
  """Chile/Continental"""
  CHILECONTINENTAL
  """Chile/EasterIsland"""
  CHILEEASTERISLAND
  """CST6CDT"""
  CST6CDT
  """Cuba"""
  CUBA
  """EET"""
  EET
  """Egypt"""
  EGYPT
  """Eire"""
  EIRE
  """EST"""
  EST
  """EST5EDT"""
  EST5EDT
  """Etc/GMT"""
  ETCGMT
  """Etc/GMT+0"""
  ETCGMTPLUS0
  """Etc/GMT+1"""
  ETCGMTPLUS1
  """Etc/GMT+10"""
  ETCGMTPLUS10
  """Etc/GMT+11"""
  ETCGMTPLUS11
  """Etc/GMT+12"""
  ETCGMTPLUS12
  """Etc/GMT+2"""
  ETCGMTPLUS2
  """Etc/GMT+3"""
  ETCGMTPLUS3
  """Etc/GMT+4"""
  ETCGMTPLUS4
  """Etc/GMT+5"""
  ETCGMTPLUS5
  """Etc/GMT+6"""
  ETCGMTPLUS6
  """Etc/GMT+7"""
  ETCGMTPLUS7
  """Etc/GMT+8"""
  ETCGMTPLUS8
  """Etc/GMT+9"""
  ETCGMTPLUS9
  """Etc/GMT-0"""
  ETCGMTMINUS0
  """Etc/GMT-1"""
  ETCGMTMINUS1
  """Etc/GMT-10"""
  ETCGMTMINUS10
  """Etc/GMT-11"""
  ETCGMTMINUS11
  """Etc/GMT-12"""
  ETCGMTMINUS12
  """Etc/GMT-13"""
  ETCGMTMINUS13
  """Etc/GMT-14"""
  ETCGMTMINUS14
  """Etc/GMT-2"""
  ETCGMTMINUS2
  """Etc/GMT-3"""
  ETCGMTMINUS3
  """Etc/GMT-4"""
  ETCGMTMINUS4
  """Etc/GMT-5"""
  ETCGMTMINUS5
  """Etc/GMT-6"""
  ETCGMTMINUS6
  """Etc/GMT-7"""
  ETCGMTMINUS7
  """Etc/GMT-8"""
  ETCGMTMINUS8
  """Etc/GMT-9"""
  ETCGMTMINUS9
  """Etc/GMT0"""
  ETCGMT0
  """Etc/Greenwich"""
  ETCGREENWICH
  """Etc/UCT"""
  ETCUCT
  """Etc/Universal"""
  ETCUNIVERSAL
  """Etc/UTC"""
  ETCUTC
  """Etc/Zulu"""
  ETCZULU
  """Europe/Amsterdam"""
  EUROPEAMSTERDAM
  """Europe/Andorra"""
  EUROPEANDORRA
  """Europe/Astrakhan"""
  EUROPEASTRAKHAN
  """Europe/Athens"""
  EUROPEATHENS
  """Europe/Belfast"""
  EUROPEBELFAST
  """Europe/Belgrade"""
  EUROPEBELGRADE
  """Europe/Berlin"""
  EUROPEBERLIN
  """Europe/Bratislava"""
  EUROPEBRATISLAVA
  """Europe/Brussels"""
  EUROPEBRUSSELS
  """Europe/Bucharest"""
  EUROPEBUCHAREST
  """Europe/Budapest"""
  EUROPEBUDAPEST
  """Europe/Busingen"""
  EUROPEBUSINGEN
  """Europe/Chisinau"""
  EUROPECHISINAU
  """Europe/Copenhagen"""
  EUROPECOPENHAGEN
  """Europe/Dublin"""
  EUROPEDUBLIN
  """Europe/Gibraltar"""
  EUROPEGIBRALTAR
  """Europe/Guernsey"""
  EUROPEGUERNSEY
  """Europe/Helsinki"""
  EUROPEHELSINKI
  """Europe/Isle_of_Man"""
  EUROPEISLEOFMAN
  """Europe/Istanbul"""
  EUROPEISTANBUL
  """Europe/Jersey"""
  EUROPEJERSEY
  """Europe/Kaliningrad"""
  EUROPEKALININGRAD
  """Europe/Kiev"""
  EUROPEKIEV
  """Europe/Kirov"""
  EUROPEKIROV
  """Europe/Kyiv"""
  EUROPEKYIV
  """Europe/Lisbon"""
  EUROPELISBON
  """Europe/Ljubljana"""
  EUROPELJUBLJANA
  """Europe/London"""
  EUROPELONDON
  """Europe/Luxembourg"""
  EUROPELUXEMBOURG
  """Europe/Madrid"""
  EUROPEMADRID
  """Europe/Malta"""
  EUROPEMALTA
  """Europe/Mariehamn"""
  EUROPEMARIEHAMN
  """Europe/Minsk"""
  EUROPEMINSK
  """Europe/Monaco"""
  EUROPEMONACO
  """Europe/Moscow"""
  EUROPEMOSCOW
  """Europe/Nicosia"""
  EUROPENICOSIA
  """Europe/Oslo"""
  EUROPEOSLO
  """Europe/Paris"""
  EUROPEPARIS
  """Europe/Podgorica"""
  EUROPEPODGORICA
  """Europe/Prague"""
  EUROPEPRAGUE
  """Europe/Riga"""
  EUROPERIGA
  """Europe/Rome"""
  EUROPEROME
  """Europe/Samara"""
  EUROPESAMARA
  """Europe/San_Marino"""
  EUROPESANMARINO
  """Europe/Sarajevo"""
  EUROPESARAJEVO
  """Europe/Saratov"""
  EUROPESARATOV
  """Europe/Simferopol"""
  EUROPESIMFEROPOL
  """Europe/Skopje"""
  EUROPESKOPJE
  """Europe/Sofia"""
  EUROPESOFIA
  """Europe/Stockholm"""
  EUROPESTOCKHOLM
  """Europe/Tallinn"""
  EUROPETALLINN
  """Europe/Tirane"""
  EUROPETIRANE
  """Europe/Tiraspol"""
  EUROPETIRASPOL
  """Europe/Ulyanovsk"""
  EUROPEULYANOVSK
  """Europe/Uzhgorod"""
  EUROPEUZHGOROD
  """Europe/Vaduz"""
  EUROPEVADUZ
  """Europe/Vatican"""
  EUROPEVATICAN
  """Europe/Vienna"""
  EUROPEVIENNA
  """Europe/Vilnius"""
  EUROPEVILNIUS
  """Europe/Volgograd"""
  EUROPEVOLGOGRAD
  """Europe/Warsaw"""
  EUROPEWARSAW
  """Europe/Zagreb"""
  EUROPEZAGREB
  """Europe/Zaporozhye"""
  EUROPEZAPOROZHYE
  """Europe/Zurich"""
  EUROPEZURICH
  """Factory"""
  FACTORY
  """GB"""
  GB
  """GB-Eire"""
  GBEIRE
  """GMT"""
  GMT
  """GMT+0"""
  GMTPLUS0
  """GMT-0"""
  GMTMINUS0
  """GMT0"""
  GMT0
  """Greenwich"""
  GREENWICH
  """Hongkong"""
  HONGKONG
  """HST"""
  HST
  """Iceland"""
  ICELAND
  """Indian/Antananarivo"""
  INDIANANTANANARIVO
  """Indian/Chagos"""
  INDIANCHAGOS
  """Indian/Christmas"""
  INDIANCHRISTMAS
  """Indian/Cocos"""
  INDIANCOCOS
  """Indian/Comoro"""
  INDIANCOMORO
  """Indian/Kerguelen"""
  INDIANKERGUELEN
  """Indian/Mahe"""
  INDIANMAHE
  """Indian/Maldives"""
  INDIANMALDIVES
  """Indian/Mauritius"""
  INDIANMAURITIUS
  """Indian/Mayotte"""
  INDIANMAYOTTE
  """Indian/Reunion"""
  INDIANREUNION
  """Iran"""
  IRAN
  """Israel"""
  ISRAEL
  """Jamaica"""
  JAMAICA
  """Japan"""
  JAPAN
  """Kwajalein"""
  KWAJALEIN
  """Libya"""
  LIBYA
  """localtime"""
  LOCALTIME
  """MET"""
  MET
  """Mexico/BajaNorte"""
  MEXICOBAJANORTE
  """Mexico/BajaSur"""
  MEXICOBAJASUR
  """Mexico/General"""
  MEXICOGENERAL
  """MST"""
  MST
  """MST7MDT"""
  MST7MDT
  """Navajo"""
  NAVAJO
  """NZ"""
  NZ
  """NZ-CHAT"""
  NZCHAT
  """Pacific/Apia"""
  PACIFICAPIA
  """Pacific/Auckland"""
  PACIFICAUCKLAND
  """Pacific/Bougainville"""
  PACIFICBOUGAINVILLE
  """Pacific/Chatham"""
  PACIFICCHATHAM
  """Pacific/Chuuk"""
  PACIFICCHUUK
  """Pacific/Easter"""
  PACIFICEASTER
  """Pacific/Efate"""
  PACIFICEFATE
  """Pacific/Enderbury"""
  PACIFICENDERBURY
  """Pacific/Fakaofo"""
  PACIFICFAKAOFO
  """Pacific/Fiji"""
  PACIFICFIJI
  """Pacific/Funafuti"""
  PACIFICFUNAFUTI
  """Pacific/Galapagos"""
  PACIFICGALAPAGOS
  """Pacific/Gambier"""
  PACIFICGAMBIER
  """Pacific/Guadalcanal"""
  PACIFICGUADALCANAL
  """Pacific/Guam"""
  PACIFICGUAM
  """Pacific/Honolulu"""
  PACIFICHONOLULU
  """Pacific/Johnston"""
  PACIFICJOHNSTON
  """Pacific/Kanton"""
  PACIFICKANTON
  """Pacific/Kiritimati"""
  PACIFICKIRITIMATI
  """Pacific/Kosrae"""
  PACIFICKOSRAE
  """Pacific/Kwajalein"""
  PACIFICKWAJALEIN
  """Pacific/Majuro"""
  PACIFICMAJURO
  """Pacific/Marquesas"""
  PACIFICMARQUESAS
  """Pacific/Midway"""
  PACIFICMIDWAY
  """Pacific/Nauru"""
  PACIFICNAURU
  """Pacific/Niue"""
  PACIFICNIUE
  """Pacific/Norfolk"""
  PACIFICNORFOLK
  """Pacific/Noumea"""
  PACIFICNOUMEA
  """Pacific/Pago_Pago"""
  PACIFICPAGOPAGO
  """Pacific/Palau"""
  PACIFICPALAU
  """Pacific/Pitcairn"""
  PACIFICPITCAIRN
  """Pacific/Pohnpei"""
  PACIFICPOHNPEI
  """Pacific/Ponape"""
  PACIFICPONAPE
  """Pacific/Port_Moresby"""
  PACIFICPORTMORESBY
  """Pacific/Rarotonga"""
  PACIFICRAROTONGA
  """Pacific/Saipan"""
  PACIFICSAIPAN
  """Pacific/Samoa"""
  PACIFICSAMOA
  """Pacific/Tahiti"""
  PACIFICTAHITI
  """Pacific/Tarawa"""
  PACIFICTARAWA
  """Pacific/Tongatapu"""
  PACIFICTONGATAPU
  """Pacific/Truk"""
  PACIFICTRUK
  """Pacific/Wake"""
  PACIFICWAKE
  """Pacific/Wallis"""
  PACIFICWALLIS
  """Pacific/Yap"""
  PACIFICYAP
  """Poland"""
  POLAND
  """Portugal"""
  PORTUGAL
  """PRC"""
  PRC
  """PST8PDT"""
  PST8PDT
  """ROC"""
  ROC
  """ROK"""
  ROK
  """Singapore"""
  SINGAPORE
  """SystemV/AST4"""
  SYSTEMVAST4
  """SystemV/AST4ADT"""
  SYSTEMVAST4ADT
  """SystemV/CST6"""
  SYSTEMVCST6
  """SystemV/CST6CDT"""
  SYSTEMVCST6CDT
  """SystemV/EST5"""
  SYSTEMVEST5
  """SystemV/EST5EDT"""
  SYSTEMVEST5EDT
  """SystemV/HST10"""
  SYSTEMVHST10
  """SystemV/MST7"""
  SYSTEMVMST7
  """SystemV/MST7MDT"""
  SYSTEMVMST7MDT
  """SystemV/PST8"""
  SYSTEMVPST8
  """SystemV/PST8PDT"""
  SYSTEMVPST8PDT
  """SystemV/YST9"""
  SYSTEMVYST9
  """SystemV/YST9YDT"""
  SYSTEMVYST9YDT
  """Turkey"""
  TURKEY
  """UCT"""
  UCT
  """Universal"""
  UNIVERSAL
  """US/Alaska"""
  USALASKA
  """US/Aleutian"""
  USALEUTIAN
  """US/Arizona"""
  USARIZONA
  """US/Central"""
  USCENTRAL
  """US/East-Indiana"""
  USEASTINDIANA
  """US/Eastern"""
  USEASTERN
  """US/Hawaii"""
  USHAWAII
  """US/Indiana-Starke"""
  USINDIANASTARKE
  """US/Michigan"""
  USMICHIGAN
  """US/Mountain"""
  USMOUNTAIN
  """US/Pacific"""
  USPACIFIC
  """US/Samoa"""
  USSAMOA
  """UTC"""
  UTC
  """W-SU"""
  WSU
  """WET"""
  WET
  """Zulu"""
  ZULU
}

"""The unique setting of a field."""
enum Uniqueness {
  """The value of the field is not required to be unique."""
  NONE
  """
  The value of the field must be unique, but only in the context of other values entered into this field specifically.
  """
  LOCAL
  """The field must be unique amongst all other fields of the same type."""
  GLOBAL
}

"""The system of units."""
enum Units {
  """Metric."""
  METRIC
  """Imperial."""
  IMPERIAL
}
```
