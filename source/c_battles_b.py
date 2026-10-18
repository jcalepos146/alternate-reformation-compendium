from c_battles import B

H = "hist"
RC, CR, GN, OT = "roman-catholic", "cranmerian", "gnesio-catholic", "sunni"

# ----------------------------------------------------------- Before the divergence bites (1500-1530)
B("vedrosha", "Battle of Vedrosha", H, "14 July 1500", 1500,
  "Muscovite victory over Lithuania that opens the long border war.",
  ["Ivan III's army routs the Lithuanian host and captures its hetman. Orsha in 1514 reverses the tide."],
  "Near Dorogobuzh", "Muscovy against Lithuania", "Muscovite victory", faith=["russian-orthodox"])
B("ravenna", "Battle of Ravenna", H, "11 April 1512", 1512,
  "French victory in the War of the Holy League, won at huge cost.",
  ["Gaston de Foix wins and dies. The French lose Italy within months, which Marignano ([[marignano]]) then restores."],
  "Ravenna, Italy", "France against the Holy League", "French victory; Foix killed", faith=[RC])
B("flodden", "Battle of Flodden", H, "9 September 1513", 1513,
  "English victory in which James IV of Scotland is killed.",
  ["The Scottish king falls with much of his nobility, leaving an infant James V. Scotland comes to the reforming age under regencies."],
  "Northumberland", "England against Scotland", "English victory", faith=[CR])
B("orsha", "Battle of Orsha", H, "8 September 1514", 1514,
  "Lithuanian–Polish victory over Muscovy.",
  ["Konstanty Ostrogski ([[ostrozky]]) wins a great victory, though Vasili III had already taken Smolensk."],
  "Orsha, Belarus", "Lithuania and Poland against Muscovy", "Lithuanian victory", faith=["russian-orthodox", "eastern-orthodox"])
B("chaldiran", "Battle of Chaldiran", H, "23 August 1514", 1514,
  "Ottoman musketry beats Safavid cavalry.",
  ["Selim I ([[selim-i]]) wins against Ismail ([[ismail-i]]) and takes Tabriz briefly. The frontier between Sunni and Twelver states is fixed for centuries."],
  "North-west Iran", "Ottoman Empire against Safavid Persia", "Ottoman victory", faith=[OT, "shia"])
B("marj-dabiq", "Battle of Marj Dabiq", H, "24 August 1516", 1516,
  "Ottoman victory that opens Syria.",
  ["The Mamluk sultan dies on the field; Aleppo and Damascus fall."],
  "Near Aleppo", "Ottoman Empire against the Mamluks", "Ottoman victory", faith=[OT])
B("ridaniya", "Battle of Ridaniya", H, "22 January 1517", 1517,
  "Ottoman victory that ends the Mamluk Sultanate.",
  ["Cairo falls and the caliphate passes to the Ottoman house."],
  "Near Cairo", "Ottoman Empire against the Mamluks", "Ottoman victory", faith=[OT])
B("tenochtitlan", "Fall of Tenochtitlan", H, "May–August 1521", 1521,
  "Spanish and allied conquest of the Aztec capital.",
  ["Cortés ([[hernan-cortes]]) and thousands of allies take the city. New Spain follows, and the Roman communion's western edge opens."],
  "Mexico", "Spain and allied peoples against the Aztecs", "Spanish victory", faith=[RC, "traditional-religions"])
B("rhodes", "Siege of Rhodes", H, "1522", 1522,
  "Suleiman takes the island from the Knights of St John.",
  ["The Knights go to Malta, where they hold in 1565 ([[malta]])."],
  "Rhodes", "Ottoman Empire against the Knights", "Ottoman victory", faith=[OT, RC])
B("bicocca", "Battle of Bicocca", H, "27 April 1522", 1522,
  "Imperial arquebusiers beat the Swiss in French pay.",
  ["Frundsberg's Landsknechts ([[frundsberg]]) are present. The Swiss lose their name for invincibility; Zwingli does not live to preach against the mercenary trade ([[marignano]])."],
  "Near Milan", "Empire and Spain against France and the Swiss", "Imperial victory", faith=[RC])
B("mohacs", "Battle of Mohács", H, "29 August 1526", 1526,
  "Ottoman victory that kills the king of Hungary.",
  ["Louis II ([[louis-ii-hungary]]) drowns in retreat. Hungary splits into Habsburg, Ottoman and eastern parts."],
  "Southern Hungary", "Ottoman Empire against Hungary", "Ottoman victory", faith=[OT, RC])
B("vienna-1529", "First Siege of Vienna", H, "September–October 1529", 1529,
  "Suleiman's first failed attempt on the Habsburg capital.",
  ["Autumn rains and poor supply end the siege in three weeks."],
  "Vienna", "Habsburgs against the Ottoman Empire", "Siege lifted", faith=[RC, OT])

# ----------------------------------------------------------- Radical Reformation and the north
B("counts-feud", "The Count's Feud", H, "1534–36", 1534,
  "Danish civil war that brings Christian III to the throne.",
  ["The war ends with the victory of Christian III ([[christian-iii]]) and the evangelical order of 1537."],
  "Denmark", "Christian III against Lübeck and the Catholic nobility", "Christian III victorious", faith=[CR])
B("tunis-1535", "Conquest of Tunis", H, "1535", 1535,
  "Charles V takes Tunis from Barbarossa.",
  ["Andrea Doria's fleet ([[andrea-doria]]) carries the Emperor's expedition."],
  "Tunis", "Empire against the Ottomans' corsair client", "Imperial victory", faith=[RC, OT])
B("preveza", "Battle of Preveza", H, "28 September 1538", 1538,
  "Ottoman naval victory over a Christian league.",
  ["Barbarossa ([[barbarossa]]) beats Doria ([[andrea-doria]]) and holds the Mediterranean until Lepanto."],
  "Gulf of Arta, Greece", "Ottoman Empire against the Holy League", "Ottoman victory", faith=[OT, RC])
B("pinkie", "Battle of Pinkie Cleugh", H, "10 September 1547", 1547,
  "English victory over Scotland during the 'Rough Wooing'.",
  ["The Protectorate of Edward VI ([[edward-vi]]) wins but cannot hold the ground. Scotland turns to France."],
  "East Lothian", "England against Scotland", "English victory", faith=[CR])

# ----------------------------------------------------------- After the Interim
B("metz-1552", "Siege of Metz", H, "1552–53", 1552,
  "France holds Metz against Charles V.",
  ["Henry II ([[henry-ii-france]]) takes the three bishoprics with German princes' help; Charles fails to retake Metz."],
  "Metz", "France against the Empire", "French victory", faith=[RC])
B("eger-1552", "Siege of Eger", H, "1552", 1552,
  "A small Hungarian garrison holds against the Ottomans.",
  ["István Dobó ([[istvan-dobo]]) holds the fortress for weeks."],
  "Eger, Hungary", "Habsburg Hungary against the Ottomans", "Siege lifted", faith=[RC, OT])
B("saint-quentin", "Battle of Saint-Quentin", H, "10 August 1557", 1557,
  "Spanish victory over France.",
  ["Philip II's army ([[philip-ii]]) wins but cannot take Paris."],
  "Picardy", "Spain against France", "Spanish victory", faith=[RC])
B("gravelines", "Battle of Gravelines", H, "13 July 1558", 1558,
  "Egmont's cavalry defeat the French; the war ends at Cateau-Cambrésis.",
  ["The victory forces France to settle ([[cateau-cambresis]])."],
  "Gravelines", "Spain against France", "Spanish victory", faith=[RC])
B("dreux", "Battle of Dreux", "prop", "19 December 1562", 1562,
  "The first pitched battle of the French wars of religion.",
  ["In history the Huguenots lost. Here Poissy ([[poissy]]) succeeds, and a clash like Dreux, if it happens at all, is one that the Guise party ([[guise-party]]) provokes. Whether it should be a battle here is open."],
  "Dreux", "Royal army and Guise against Huguenots", "Open",
  faith=[RC, CR], open_q=["Whether the wars start at all after a successful Poissy."])
B("malta", "Great Siege of Malta", H, "1565", 1565,
  "The Knights hold Malta against the Ottomans.",
  ["The siege is lifted in September. It is the high point of Hospitaller resistance."],
  "Malta", "Knights of St John against the Ottomans", "Siege lifted", faith=[RC, OT])
B("szigetvar", "Siege of Szigetvár", H, "1566", 1566,
  "Zrinski's last stand ([[zrinski]]) in which Suleiman dies.",
  ["Suleiman dies during the siege; Selim II ([[selim-ii]]) takes the throne."],
  "Szigetvár, Hungary", "Habsburg Croatia against the Ottomans", "Ottoman victory, at great cost", faith=[RC, OT])
B("jarnac-moncontour", "Jarnac and Moncontour", "prop", "March and October 1569", 1569,
  "Royal victories in the third French war.",
  ["Historically Condé's uncle fell at Jarnac, and Coligny ([[coligny]]) was beaten at Moncontour. Here he survives to lead the moderates into settlement."],
  "Poitou", "Crown against the Huguenots", "Open", faith=[CR, RC], open_q=["Whether the third war takes place."])
B("molodi", "Battle of Molodi", H, "July–August 1572", 1572,
  "Muscovite victory over the Crimean Tatars.",
  ["Ivan IV's army ([[ivan-iv]]) ends the Tatar threat to Moscow."],
  "South of Moscow", "Muscovy against Crimea", "Muscovite victory", faith=["russian-orthodox"])
B("three-kings", "Battle of the Three Kings", H, "4 August 1578", 1578,
  "Moroccan victory in which Sebastian of Portugal dies.",
  ["Three kings die and Portugal passes to Philip II ([[sebastian-of-portugal]])."],
  "Alcácer Quibir, Morocco", "Morocco against Portugal", "Moroccan victory", faith=[RC, OT])
B("wenden", "Battle of Wenden", H, "October 1578", 1578,
  "Polish–Lithuanian–Swedish victory over Muscovy in Livonia.",
  ["The victory is a step toward the Livonian settlement ([[livonian-war]])."],
  "Livonia", "Poland-Lithuania and Sweden against Muscovy", "Allied victory", faith=[GN])
B("pskov", "Siege of Pskov", H, "1581–82", 1581,
  "Báthory's army fails to take Pskov.",
  ["The siege ([[stephen-bathory]]) ends in the truce of Yam-Zapolsky. The Livonian war closes ([[livonian-war]])."],
  "Pskov", "Poland-Lithuania against Muscovy", "Siege fails; truce", faith=["russian-orthodox"])
B("fall-of-antwerp", "Fall of Antwerp", "canon", "1584–85", 1585,
  "Farnese takes Antwerp and fixes the north–south line.",
  ["Alexander Farnese ([[alexander-farnese]]) starves the city. The southern provinces return to Spain, the north holds ([[dutch-revolt]])."],
  "Antwerp", "Spain against the Dutch rebels", "Spanish victory", faith=[RC, CR])
B("coutras", "Battle of Coutras", "prop", "20 October 1587", 1587,
  "Henry of Navarre's cavalry victory.",
  ["In history, Navarre's victory was the first Huguenot battlefield win. Whether it happens here is open, since Poissy changed the party lines."],
  "Guyenne", "Navarre against royal forces", "Open", faith=[CR, RC], open_q=["Whether the war of the three Henrys happens."])
B("armada", "The Spanish Armada", H, "July–August 1588", 1588,
  "The failed invasion of England.",
  ["Drake and Howard ([[francis-drake]], [[charles-howard]]) harass the fleet, and storms finish it."],
  "English Channel", "England against Spain", "English victory", faith=[CR, RC])
B("ivry", "Battle of Ivry", "prop", "14 March 1590", 1590,
  "Henry IV's victory over the League.",
  ["A battle between the Crown and the Catholic League ([[catholic-league]]) happens if the succession crisis of 1589 does."],
  "Normandy", "Henry IV against the League", "Open", faith=[RC, CR], open_q=["Whether the League and the war of succession occur."])
B("tondibi", "Battle of Tondibi", H, "1591", 1591,
  "Moroccan musketeers beat the Songhai.",
  ["Ahmad al-Mansur's army crosses the Sahara."],
  "Mali", "Morocco against Songhai", "Moroccan victory", faith=[OT, "traditional-religions"])
B("sisak", "Battle of Sisak", H, "22 June 1593", 1593,
  "Habsburg victory that begins the Long Turkish War.",
  ["The war that follows ([[long-turkish-war]]) lasts thirteen years."],
  "Croatia", "Habsburg Croatia against the Ottomans", "Habsburg victory", faith=[RC, OT])
B("mezokeresztes", "Battle of Mezőkeresztes", H, "26 October 1596", 1596,
  "Ottoman victory in the Long Turkish War.",
  ["Mehmed III wins after a near rout of the Ottomans."],
  "Hungary", "Ottoman Empire against the Habsburgs", "Ottoman victory", faith=[OT, RC])
B("nieuwpoort", "Battle of Nieuwpoort", H, "2 July 1600", 1600,
  "Maurice of Nassau's victory over Spain.",
  ["Maurice ([[maurice-of-nassau]]) wins on the Flemish coast and secures the Republic."],
  "Flanders", "Dutch Republic against Spain", "Dutch victory", faith=[CR])
B("kircholm", "Battle of Kircholm", H, "27 September 1605", 1605,
  "Polish hussars crush the Swedes.",
  ["Chodkiewicz ([[chodkiewicz]]) wins against Charles IX of Sweden ([[charles-ix-sweden]]). The Vasa quarrel continues."],
  "Livonia", "Poland-Lithuania against Sweden", "Polish victory", faith=[RC, GN])
B("klushino", "Battle of Klushino", H, "4 July 1610", 1610,
  "Żółkiewski destroys the Muscovite army and enters Moscow.",
  ["Żółkiewski ([[zolkiewski]]) wins and the Polish occupation begins ([[polish-occupation-moscow]]). Vasily Shuisky ([[vasily-shuisky]]) falls."],
  "Smolensk region", "Poland-Lithuania against Muscovy and Sweden", "Polish victory", faith=[RC, "russian-orthodox"])
B("smolensk-1609", "Siege of Smolensk", H, "1609–11", 1609,
  "Sigismund III's long siege.",
  ["Smolensk falls in 1611 ([[sigismund-iii]]). The fortress is lost in 1654."],
  "Smolensk", "Poland-Lithuania against Muscovy", "Polish victory", faith=[RC])

# ----------------------------------------------------------- Thirty Years' War and after
B("hormuz", "Capture of Hormuz", H, "1622", 1622,
  "Persian and English forces take the Portuguese fortress.",
  ["Abbas I ([[abbas-i]]) ends Portuguese control of the Gulf."],
  "Strait of Hormuz", "Persia and England against Portugal", "Allied victory", faith=["shia"])
B("stadtlohn", "Battle of Stadtlohn", H, "6 August 1623", 1623,
  "Tilly destroys the army of Christian of Brunswick.",
  ["Tilly ([[tilly]]) finishes the Palatine war."],
  "Westphalia", "Catholic League against Brunswick", "League victory", faith=[RC, CR])
B("lutter", "Battle of Lutter", H, "27 August 1626", 1626,
  "Tilly beats Christian IV of Denmark.",
  ["Christian IV ([[christian-iv]]) is forced out of the war."],
  "Lower Saxony", "Catholic League against Denmark", "League victory", faith=[RC, CR])
B("stralsund-1628", "Siege of Stralsund", H, "1628", 1628,
  "Wallenstein fails to take the Baltic port.",
  ["Wallenstein ([[wallenstein]]) lifts the siege and Gustavus Adolphus ([[gustavus-adolphus]]) lands in 1630."],
  "Stralsund", "Empire against Stralsund, Sweden and Denmark", "Siege lifted", faith=[GN])
B("sack-of-magdeburg", "Sack of Magdeburg", H, "20 May 1631", 1631,
  "Imperial troops burn the Gnesio city.",
  ["Tilly's army ([[tilly]]) takes the city. Magdeburg, the Gnesio refusal of the Interim ([[siege-magdeburg]]), becomes its martyr. The sack drives the north to Sweden."],
  "Magdeburg", "Empire and League against Magdeburg", "City destroyed", faith=[GN])
B("wittstock", "Battle of Wittstock", H, "4 October 1636", 1636,
  "Banér's victory over the Imperial-Saxon army.",
  ["Banér ([[johan-baner]]) restores Sweden's position after Nördlingen ([[nordlingen]])."],
  "Brandenburg", "Sweden against Saxony and the Empire", "Swedish victory", faith=[GN])
B("baghdad-1638", "Siege of Baghdad", H, "1638", 1638,
  "Murad IV retakes Baghdad from Persia.",
  ["Murad IV ([[murad-iv]]) wins the city that fixes the frontier."],
  "Baghdad", "Ottoman Empire against Persia", "Ottoman victory", faith=[OT, "shia"])

# The English War. Sides are the timeline's reverse: the king leads the reform, the establishment is Royalist.
B("edgehill", "Battle of Edgehill", "prop", "23 October 1642", 1642,
  "Proposed first pitched battle of the English War.",
  ["In history the king fought Parliament here. In this timeline the Royalists fight in the king's name against his reforming ministers ([[english-war]]), and Rupert ([[prince-rupert]]) leads their cavalry against Cromwell's ([[oliver-cromwell]]) troopers."],
  "Warwickshire", "Royalists against the Reforming Crown", "Indecisive", faith=[CR],
  open_q=["Whether this battle happens; canon fixes no battles."])
B("lansdown", "Battle of Lansdown", "prop", "5 July 1643", 1643,
  "Proposed West Country battle.",
  ["Grenville ([[bevil-grenville]]) falls at Lansdown. West Country forces and Hopton ([[ralph-hopton]]) are the Byzantinist wing."],
  "Near Bath", "Royalists against the Reforming Crown", "Open", faith=["byzantinists"],
  open_q=["Whether the West Country goes to the Royalists."])
B("marston-moor", "Battle of Marston Moor", "prop", "2 July 1644", 1644,
  "Proposed northern battle.",
  ["In history this was the Parliamentary victory that broke the north. Here the Reforming Crown's army under Fairfax and Cromwell ([[thomas-fairfax]]) could win it, since Montrose ([[montrose]]) carries the Royalist case in Scotland."],
  "Yorkshire", "Reforming Crown against Royalists", "Open", faith=[CR])
B("naseby", "Battle of Naseby", "prop", "14 June 1645", 1645,
  "Proposed decisive battle of the first stage.",
  ["The canon says the Royalists win the war and restore by 1660. Naseby could be the Royalist victory instead."],
  "Northamptonshire", "Royalists against the Reforming Crown", "Open", faith=[CR],
  open_q=["Who wins the decisive field battle."])
B("preston-1648", "Battle of Preston", "prop", "17–19 August 1648", 1648,
  "Proposed second-stage battle.",
  ["The 1648 map shows the war. Here Preston would be the battle where the Royalists, now backing a rival Stuart, strike against the crown."],
  "Lancashire", "Open", "Open", faith=[CR])
B("rocroi", "Battle of Rocroi", H, "19 May 1643", 1643,
  "French victory over the Spanish tercios.",
  ["Condé ([[conde]]) wins at twenty-one."],
  "Ardennes", "France against Spain", "French victory", faith=[RC, "gallican-church"])
B("jankau", "Battle of Jankau", H, "6 March 1645", 1645,
  "Swedish victory over the Imperial army in Bohemia.",
  ["Torstensson ([[lennart-torstensson]]) opens the road to Vienna."],
  "Bohemia", "Sweden against the Empire", "Swedish victory", faith=[GN])

# ----------------------------------------------------------- Eastern Europe, Ottoman wars
B("zboriv", "Battle of Zboriv", H, "1649", 1649,
  "Khmelnytsky and the Tatars force the Polish king to settle.",
  ["John Casimir ([[john-ii-casimir]]) grants autonomy to the Cossack Hetmanate."],
  "Ukraine", "Cossacks against Poland-Lithuania", "Compromise", faith=["eastern-orthodox"])
B("berestechko", "Battle of Berestechko", H, "1651", 1651,
  "Polish victory against the Cossacks.",
  ["The Tatars desert Khmelnytsky ([[bohdan-khmelnytsky]]). He turns to Moscow in 1654."],
  "Ukraine", "Poland-Lithuania against Cossacks and Tatars", "Polish victory", faith=["eastern-orthodox"])
B("jasna-gora", "Siege of Jasna Góra", H, "1655", 1655,
  "Częstochowa holds out against Sweden.",
  ["The defence turns Polish opinion against Sweden ([[deluge]])."],
  "Częstochowa", "Poland against Sweden", "Siege lifted", faith=[RC])
B("warsaw-1656", "Battle of Warsaw", H, "28–30 July 1656", 1656,
  "Swedish–Brandenburg victory over the Poles.",
  ["Charles X Gustav wins on the field but cannot keep the country ([[deluge]])."],
  "Warsaw", "Sweden and Brandenburg against Poland", "Swedish victory", faith=[GN])
B("vienna-1683", "Battle of Vienna", H, "12 September 1683", 1683,
  "Relief of the siege by a Polish-Imperial army.",
  ["Sobieski ([[john-iii-sobieski]]) leads the relief and Kara Mustafa ([[kara-mustafa]]) is beaten. It begins [[great-turkish-war]]."],
  "Vienna", "Habsburg Empire and Poland against the Ottomans", "Allied victory", faith=[RC, OT])
B("zenta", "Battle of Zenta", H, "11 September 1697", 1697,
  "Prince Eugene destroys the Ottoman army.",
  ["The victory leads to the peace of Karlowitz ([[karlowitz]])."],
  "Zenta, Hungary", "Habsburgs against the Ottomans", "Habsburg victory", faith=[RC, OT])
