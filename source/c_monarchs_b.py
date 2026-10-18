from common import M

# ------------------------------------------------------------ Empire, Germany, Scandinavia
M("frederick-the-wise", "Frederick the Wise", "hist", "Elector of Saxony 1486–1525", 1517,
  "Luther’s protector at Wittenberg.",
  ["Frederick shields Luther after Worms in 1521 (the divergence at Marignano in 1515 does not touch him). He dies in 1525 and his brother John succeeds."],
  ["gnesio-catholic", "cranmerian"], "Elector of Saxony", "Frederick III, Elector of Saxony", y2=1525)

M("philip-of-hesse", "Philip of Hesse", "hist", "Landgrave 1509–67", 1530,
  "Co-leader of the Schmalkaldic League.",
  ["Philip is captured after the League’s collapse ([[schmalkaldic-war]]). His Hesse becomes a Philippist territory in the Cranmerian communion."],
  ["cranmerian"], "Landgrave of Hesse", "Philip I, Landgrave of Hesse", y2=1567)

M("christian-iii", "Christian III of Denmark", "hist", "1534–59", 1537,
  "King who introduced Bugenhagen’s church order to Denmark-Norway.",
  ["Christian establishes the evangelical church in 1537 under Bugenhagen’s order ([[johannes-bugenhagen]]). Denmark-Norway sits in the Philippist–Cranmerian communion."],
  ["cranmerian"], "King of Denmark-Norway", "Christian III of Denmark", y2=1559)

M("gustav-vasa", "Gustav I of Sweden", "hist", "1523–60", 1523,
  "Founder of the Vasa monarchy.",
  ["Gustav breaks with Rome at Västerås in 1527 but keeps the bishops. The Swedish succession through Petrus Magni ([[petrus-magni]]) is the line that makes Sweden’s Gnesio-Catholic bishops valid."],
  ["gnesio-independent"], "King of Sweden", "Gustav I of Sweden", y2=1560)

M("matthias", "Matthias", "hist", "Emperor 1612–19", 1612,
  "Rudolf’s brother and successor, who granted the Letter of Majesty.",
  ["Matthias confirms Bohemian rights in 1609–11 ([[letter-of-majesty]]) and leaves the succession to Ferdinand."],
  ["roman-catholic"], "Holy Roman Emperor", "Matthias, Holy Roman Emperor", y2=1619)

M("ferdinand-iii", "Ferdinand III", "hist", "Emperor 1637–57", 1637,
  "Emperor at the end of the German war.",
  ["Ferdinand signs the settlement of 1648 ([[peace-1648]]) after Nördlingen and the Swedish campaigns."],
  ["roman-catholic"], "Holy Roman Emperor", "Ferdinand III, Holy Roman Emperor", y2=1657)

M("leopold-i", "Leopold I", "hist", "Emperor 1658–1705", 1658,
  "Emperor of the Hungarian reconquest.",
  ["Leopold rules through [[vienna-1683]] and Karlowitz ([[karlowitz]])."],
  ["roman-catholic"], "Holy Roman Emperor", "Leopold I, Holy Roman Emperor", y2=1705)

M("louis-ii-hungary", "Louis II of Hungary", "hist", "1516–26", 1526,
  "Last Jagiellon king of Hungary, killed at Mohács.",
  ["His death at [[mohacs]] ends the independent kingdom and opens the Habsburg and Ottoman partition."],
  ["roman-catholic"], "King of Hungary and Bohemia", "Louis II of Hungary", y2=1526)

M("frederick-iii-palatine", "Frederick III, Elector Palatine", "hist", "1559–76", 1563,
  "Patron of the Heidelberg Catechism.",
  ["Frederick turns the Palatinate Reformed and commissions the catechism of 1563 ([[heidelberg-catechism]]). He keeps the Palatinate within the Cranmerian communion's Reformed wing."],
  ["cranmerian"], "Elector Palatine", "Frederick III, Elector Palatine", y2=1576)

# ------------------------------------------------------------ France
M("henry-ii-france", "Henry II of France", "hist", "1547–59", 1547,
  "King who ends the Italian wars at Cateau-Cambrésis.",
  ["Henry fights Charles V and Philip II ([[metz-1552]], [[saint-quentin]]) and makes peace in 1559 ([[cateau-cambresis]]). He dies in a joust that year."],
  ["gallican-church"], "King of France", "Henry II of France", y2=1559)

M("henry-iii", "Henry III of France and Poland", "hist", "Poland 1573–75; France 1574–89", 1573,
  "Elected king of Poland, then returned to France.",
  ["Henry swore the Henrician articles guaranteeing toleration in 1573 ([[warsaw-confederation]]) and left in 1574 to take the French crown."],
  ["gallican-church"], "King of France, King of Poland", "Henry III of France", y2=1589)

M("louis-xiv", "Louis XIV", "hist", "1643–1715", 1661,
  "The Sun King, in a France that never revoked Nantes.",
  ["In our history Louis revoked the edict of toleration in 1685. Here the Gallican–Augustinian settlement protects the Cranmerian Huguenots, so there is no revocation and no flight. His quarrels are with Rome ([[gallican-articles-1682]]) and the Dutch."],
  ["gallican-church"], "King of France", "Louis XIV", y2=1715)

M("mary-queen-of-scots", "Mary, Queen of Scots", "hist", "1542–67", 1561,
  "Catholic queen, deposed in 1567, whose fall clears the way for a reforming crown in Scotland.",
  ["Mary returns to Scotland in 1561 and faces [[knox]]. She is deposed in 1567. How the crown then ends up in a reformist rather than Kirk hands, with the Kirk underground, is open."],
  ["roman-catholic"], "Queen of Scotland", "Mary, Queen of Scots", y2=1587)

M("mary-i-england", "Mary I of England", "prop", "1553–58", 1553,
  "Queen of a Cranmerian England, whose reign is not fixed in canon.",
  ["Mary succeeded Edward in history and restored Rome. In this timeline a pan-Protestant Communion is already formed around Cranmer by 1552, and the settlement's survival of her accession is open."],
  ["cranmerian", "roman-catholic"], "Queen of England", "Mary I of England",
  open_q=["Whether Mary reigns, and what she does to the Communion."], y2=1558)

M("charles-ii", "Charles II of England", "prop", "1660–85", 1660,
  "Proposed king of the Royalist restoration.",
  ["Canon places a Royalist restoration by 1660 under a rival Stuart and a conservative French-aligned monarchy. Charles II is the historical figure for that restoration."],
  ["cranmerian", "byzantinists"], "King of England (proposed)", "Charles II of England",
  open_q=["Whether Charles or Rupert is the rival Stuart."], y2=1685)

M("james-ii", "James II and VII", "prop", "1685–88", 1685,
  "Proposed last Stuart king before the Dutch union.",
  ["James II was deposed in 1688 in history. Here the Dutch succession is dated 1688–89, so he fits as the monarch it replaces."],
  ["cranmerian"], "King of England (proposed)", "James II of England", y2=1688,
  open_q=["Whether the Dutch succession is by right or by force."])

# ------------------------------------------------------------ Poland, Hungary, Transylvania
M("sigismund-i", "Sigismund I the Old", "hist", "Poland 1506–48", 1506,
  "King of Poland-Lithuania before the Reformation reaches the Commonwealth.",
  ["Sigismund fought the Teutonic Order, which becomes the Prussian duchy under Albert in 1525."],
  ["roman-catholic"], "King of Poland", "Sigismund I the Old", y2=1548)

M("sigismund-ii-augustus", "Sigismund II Augustus", "hist", "Poland 1548–72", 1548,
  "Last Jagiellon, who keeps Poland open to evangelicals.",
  ["Sigismund II presides over the Polish Reformation and the union of Lublin (1569), then the Consensus of Sandomierz ([[consensus-of-sandomierz]])."],
  ["roman-catholic", "cranmerian"], "King of Poland", "Sigismund II Augustus", y2=1572)

M("stephen-bathory", "Stephen Báthory", "hist", "Poland 1576–86", 1576,
  "Transylvanian-born king who beat Ivan IV.",
  ["Báthory leads the campaigns that end in the Livonian settlement ([[pskov]], [[livonian-war]]). He guarantees toleration."],
  ["roman-catholic"], "King of Poland", "Stephen Báthory", y2=1586)

M("john-ii-casimir", "John II Casimir", "hist", "Poland 1648–68", 1648,
  "King during the Rising and the Deluge.",
  ["John Casimir rules through [[zboriv]], [[berestechko]] and [[deluge]]."],
  ["roman-catholic"], "King of Poland", "John II Casimir Vasa", y2=1668)

M("john-iii-sobieski", "John III Sobieski", "hist", "Poland 1674–96", 1674,
  "The Polish king who relieved Vienna.",
  ["Sobieski leads the relief army at [[vienna-1683]]."],
  ["roman-catholic"], "King of Poland", "John III Sobieski", y2=1696)

# ------------------------------------------------------------ Russia
M("vasili-iii", "Vasili III", "hist", "Grand Prince 1505–33", 1514,
  "Grand prince who took Smolensk.",
  ["Vasili wins Smolensk in 1514 after [[orsha]] and [[vedrosha]] set the border with Lithuania."],
  ["russian-orthodox"], "Grand Prince of Moscow", "Vasili III of Russia", y2=1533)

M("fyodor-i", "Fyodor I", "hist", "Tsar 1584–98", 1584,
  "Tsar whose reign sees the patriarchate founded.",
  ["Fyodor's brother-in-law Boris Godunov runs the state, and Job becomes the first patriarch in 1589."],
  ["russian-orthodox"], "Tsar of Russia", "Feodor I of Russia", y2=1598)

M("vasily-shuisky", "Vasily IV Shuisky", "hist", "Tsar 1606–10", 1606,
  "Boyar tsar of the Time of Troubles.",
  ["Vasily is overthrown in 1610; the Poles enter Moscow ([[klushino]])."],
  ["russian-orthodox"], "Tsar of Russia", "Vasili IV of Russia", y2=1610)

M("false-dmitry-i", "False Dmitry I", "hist", "Tsar 1605–06", 1605,
  "Pretender backed by Poland.",
  ["Dmitry took Moscow in 1605 and was killed in 1606. His Latin ties help turn Moscow against Rome."],
  ["russian-orthodox", "roman-catholic"], "Tsar of Russia", "False Dmitry I", y2=1606)

M("alexis-of-russia", "Alexis of Russia", "hist", "Tsar 1645–76", 1645,
  "Tsar of the Kievan-Moscow union and the Nikon-era reforms.",
  ["Alexis accepts Pereiaslav in 1654 ([[pereiaslav]]). His court absorbs the Kievan scholars."],
  ["russian-orthodox"], "Tsar of Russia", "Alexis of Russia", y2=1676)

M("peter-i", "Peter I of Russia", "prop", "1682–1725", 1700,
  "Proposed ruler who modernises Russia's church.",
  ["Peter I abolished the patriarchate in 1721 in history. Here he is a possible ruler in the 1700 snapshot, with Prokopovich ([[feofan-prokopovich]]) as his churchman."],
  ["russian-orthodox"], "Tsar of Russia", "Peter the Great", y2=1725,
  open_q=["Whether Peter reforms the church as in history."])

# ------------------------------------------------------------ Ottoman and Persian
M("selim-i", "Selim I", "hist", "Sultan 1512–20", 1514,
  "Conqueror of Persia's west and the Mamluks.",
  ["Selim wins [[chaldiran]], [[marj-dabiq]] and [[ridaniya]] and takes Egypt and the caliphal claim."],
  ["sunni"], "Ottoman Sultan", "Selim I", y2=1520)

M("ismail-i", "Ismail I", "hist", "Shah 1501–24", 1501,
  "Founder of Safavid Persia and the Twelver state.",
  ["Ismail makes Twelver Shia the state religion. He loses to Selim at [[chaldiran]]."],
  ["shia"], "Shah of Persia", "Ismail I", y2=1524)

M("tahmasp-i", "Tahmasp I", "hist", "Shah 1524–76", 1524,
  "Safavid shah who ruled fifty-two years.",
  ["Tahmasp hosts the Mughal refugee Humayun and invites clerics like [[al-karaki]]."],
  ["shia"], "Shah of Persia", "Tahmasp I", y2=1576)

M("selim-ii", "Selim II", "hist", "Sultan 1566–74", 1566,
  "Sultan of Lepanto, with Sokollu running the state.",
  ["Selim rebuilds the fleet after [[lepanto]] under [[sokollu-mehmed]]."],
  ["sunni"], "Ottoman Sultan", "Selim II", y2=1574)

M("mehmed-iv", "Mehmed IV", "hist", "Sultan 1648–87", 1683,
  "Sultan during the failed siege of Vienna.",
  ["Mehmed IV rules through [[vienna-1683]] and is deposed in 1687."],
  ["sunni"], "Ottoman Sultan", "Mehmed IV", y2=1687)

# ------------------------------------------------------------ Iberia
M("philip-iii", "Philip III of Spain", "hist", "1598–1621", 1598,
  "Spanish king of the Twelve Years' Truce.",
  ["Philip III signs the truce with the Dutch in 1609."],
  ["roman-catholic"], "King of Spain", "Philip III of Spain", y2=1621)

M("sebastian-of-portugal", "Sebastian of Portugal", "hist", "1557–78", 1578,
  "King killed at Alcácer Quibir.",
  ["His death at [[three-kings]] ends the Aviz dynasty and opens the path to Philip II."],
  ["roman-catholic"], "King of Portugal", "Sebastian of Portugal", y2=1578)

M("christina-of-sweden", "Christina of Sweden", "prop", "1632–54", 1644,
  "Queen of Sweden.",
  ["Christina was raised Gnesio and abdicated in 1654 in history. Here the Swedish church is Gnesio-Catholic, so her conversion to Rome has weight."],
  ["gnesio-independent", "roman-catholic"], "Queen of Sweden", "Christina, Queen of Sweden", y2=1654,
  open_q=["Whether Christina abdicates and converts here."])
