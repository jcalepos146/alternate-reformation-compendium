from common import E

R = "Real person."
RH = "Real person in a hypothetical role."

# ---------------------------------------------------------------- The Habsburg world

E("charles-v", "monarch", "Charles V", "hist", "Emperor 1519–56", 1519, "Habsburg emperor whose victory at Mühlberg shapes the Interim.",
  ["Charles holds Spain, the Netherlands, Naples and the Empire. He defeats the Schmalkaldic League at [[muhlberg]] in 1547 and imposes the [[augsburg-interim]], whose rejection by the Gnesio party and compromise by the Philippists cleave the Wittenberg movement."],
  faith=["roman-catholic"], office="Holy Roman Emperor", basis=R, y2=1556)

E("ferdinand-i", "monarch", "Ferdinand I", "hist", "Emperor 1556–64", 1556, "Habsburg king of Bohemia and Hungary, Charles V’s brother.",
  ["Ferdinand holds Bohemia, Silesia, Moravia and Royal Hungary. Hungary is partitioned three ways in his reign, with Ottoman Buda and John Sigismund’s eastern kingdom."],
  faith=["roman-catholic"], office="Holy Roman Emperor", basis=R, y2=1564)

E("maximilian-ii", "monarch", "Maximilian II", "hist", "Emperor 1564–76", 1564, "Tolerant emperor whose reign keeps the ambiguous Augsburg settlement workable.",
  ["The peace of 1555 never said which Augsburg Confession it protected. Maximilian’s tolerance keeps that quiet until 1576, when his death opens the way for the crisis."],
  faith=["roman-catholic"], office="Holy Roman Emperor", basis=R, y2=1576)

E("rudolf-ii", "monarch", "Rudolf II", "hist", "Emperor 1576–1612", 1576, "Withdrawn emperor whose neglect lets the confessional dispute fester.",
  ["Rudolf’s reign sees the Bohemian union of 1575 bear fruit and the Long Turkish War ([[long-turkish-war]]). Bohemia is Gnesio-Catholic under a Roman Catholic king."],
  faith=["roman-catholic"], office="Holy Roman Emperor", basis=R, y2=1612)

E("ferdinand-ii", "monarch", "Ferdinand II", "hist", "Emperor 1619–37", 1619, "Habsburg emperor deposed as king of Bohemia in 1619 and restored at White Mountain.",
  ["Ferdinand’s defeat of the estates ([[white-mountain]]) returns Bohemia to Rome by 1635, with the Utraquist rite in union with Rome as the moderates’ price."],
  faith=["roman-catholic", "utraquist-rite"], office="Holy Roman Emperor", basis=R, y2=1637)

E("philip-ii", "monarch", "Philip II of Spain", "hist", "1556–98", 1556, "Spanish king whose officials tolerate Baianist Louvain.",
  ["Philip holds Spain, the Spanish Netherlands, Naples and Milan. He fights the revolt of the Low Countries ([[dutch-revolt]])."],
  faith=["roman-catholic"], office="King of Spain", basis=R, y2=1598)

E("philip-iv", "monarch", "Philip IV of Spain", "hist", "1621–65", 1621, "Spanish king and king of Portugal in the Iberian Union in 1635.",
  ["Philip IV holds Castile, Aragon, Portugal, Naples, Milan and the Netherlands. In 1635 his troops seize the Elector of Trier."],
  faith=["roman-catholic"], office="King of Spain", basis=R, y2=1665)

# ---------------------------------------------------------------- France

E("francis-i", "monarch", "Francis I of France", "hist", "1515–47", 1515, "King who signs the Concordat of Bologna with Rome.",
  ["Victor at Marignano in 1515, where Zwingli dies ([[marignano]]), Francis then concludes the [[concordat-of-bologna]]. It gives the Crown nomination of bishops and is the legal foundation of the Gallican settlement."],
  faith=["gallican-church"], office="King of France", basis=R, y2=1547)

E("charles-ix", "monarch", "Charles IX of France", "hist", "1560–74", 1561, "Boy-king under whom Poissy convenes.",
  ["Poissy ([[poissy]]) meets in his reign under the regency of Catherine de’ Medici. St Bartholomew’s either does not happen or stays a local massacre in this timeline."],
  faith=["gallican-church"], office="King of France", basis=R, y2=1574)

E("henry-iv", "monarch", "Henry IV of France", "canon", "1589–1610", 1589, "Navarrese king who converts to the Gallican church and protects the Cranmerian Huguenots.",
  ["Henry converts in 1589 (the historical ‘Paris is worth a Mass’), protects the Cranmerian Huguenots by edict, and is assassinated in 1610 as in history. He was about to march on Jülich when he was stabbed, so the Jülich crisis lands on a France without him."],
  faith=["gallican-church"], office="King of France", basis=R, y2=1610)

E("louis-xiii", "monarch", "Louis XIII of France", "hist", "1610–43", 1610, "King under whom France leads the war against the Habsburgs.",
  ["With Richelieu as minister and his brother Alphonse as Primate of Lyon, Louis occupies Lorraine and much of Alsace and takes up the protectorate of the Lyon-aligned churches. La Rochelle falls in 1628 ([[la-rochelle]])."],
  faith=["gallican-church"], office="King of France", basis=R, y2=1643)

# ---------------------------------------------------------------- Scandinavia and the Baltic

E("gustavus-adolphus", "monarch", "Gustavus Adolphus", "canon", "King of Sweden 1611–32", 1611, "Swedish king who dies at Lützen in 1632.",
  ["He intervenes in the German war and dies at [[lutzen]]. Sweden is left under a regency, and France leads the anti-Habsburg side as protector of the Lyon-aligned churches."],
  faith=["gnesio-independent"], office="King of Sweden", basis=R, y2=1632)

E("charles-ix-sweden", "monarch", "Charles IX of Sweden", "canon", "regent from 1599, king 1604–11", 1599, "Duke Charles, who deposes Sigismund and defends the Uppsala settlement.",
  ["Charles deposes his nephew by 1599 as defender of the Uppsala settlement. He is Gnesio-Catholic in office, but suspected of Cranmerian sympathies, so the crown and church may diverge later."],
  faith=["gnesio-independent"], office="King of Sweden", basis=R, y2=1611,
  open_q=["How far a Cranmerian-leaning king strains the Gnesio-Catholic church."])

E("sigismund-iii", "monarch", "Sigismund III", "hist", "Poland 1587–1632; Sweden 1592–99", 1587, "Roman Catholic king of Poland, deposed in Sweden.",
  ["Sigismund fights Charles of Sweden after being deposed in 1599, and presses the Polish tolerant settlement from the Jesuit side. He is the main threat to Polish toleration."],
  faith=["roman-catholic"], office="King of Poland", basis=R, y2=1632)

E("wladyslaw-iv", "monarch", "Władysław IV", "hist", "King of Poland 1632–48", 1632, "King who keeps Smolensk at Polyanovka in 1634.",
  ["Władysław gains Smolensk at [[polyanovka]]. Toleration survives under him and later through the Deluge."],
  faith=["roman-catholic"], office="King of Poland", basis=R, y2=1648)

E("christian-iv", "monarch", "Christian IV of Denmark", "hist", "1588–1648", 1588, "King of Denmark-Norway in the Cranmerian communion.",
  ["Hemmingsen’s teaching puts Christian’s kingdom in the Cranmerian camp. His Danish holdings include Schleswig-Holstein with the Gottorp duke."],
  faith=["cranmerian"], office="King of Denmark-Norway", basis=R, y2=1648)

# ---------------------------------------------------------------- England

E("henry-viii", "monarch", "Henry VIII", "hist", "1509–47", 1534, "King who makes the English church independent of Rome.",
  ["The royal supremacy begins under Henry. His son’s reign shapes the church that Cranmer’s council develops."],
  faith=["cranmerian"], office="King of England", basis=R, y2=1547)

E("edward-vi", "monarch", "Edward VI", "canon", "1547–53", 1547, "Boy-king of the Edwardian church and host of the Lambeth council.",
  ["The Church of England under Edward is the foundation of the Communion. Cranmer’s council meets at Lambeth during his reign."],
  faith=["cranmerian"], office="King of England", basis=R, y2=1553)

E("elizabeth-i", "monarch", "Elizabeth I", "hist", "1558–1603", 1558, "The last Tudor, whose death brings James VI of Scotland to the English throne.",
  ["The map’s notes imply she lives to 1603, and James inherits as in history. Her church’s settlement is canon-adjacent but its details are not written."],
  faith=["cranmerian"], office="Queen of England", basis=R, y2=1603)

E("james-vi-i", "monarch", "James VI and I", "canon", "Scotland 1567; England 1603–25", 1603, "A Scottish king, born into the Kirk but a reformist, who inherits the senior see of the Cranmerian communion.",
  ["James is raised in the Kirk, but the Kirk is by his reign an underground church whose members are leaving for the New World. He remains a reformist: supreme governor of the church in the Cranmerian communion on both sides of the border, leaning toward the reforming line that his son turns into a programme."],
  faith=["hardline-reformed", "cranmerian"], office="King of England and Scotland", basis=R, y2=1625)

E("charles-i-england", "monarch", "Charles I (the reforming king)", "canon", "1625–", 1625, "A king who favours a more democratic, low-church Church of England and economic liberalisation.",
  ["In our history Charles I defended bishops and the royal prerogative. Here the roles are reversed: the king leads the reforming cause and the opposition raises the old constitution. The establishment, the nobility and the Navy lean toward Royalism. A West Country group goes further and argues for an autocratic monarchy on Roman and Byzantine lines ([[byzantinists]]).",
   "By 1635 the second Stuart king is making low-church reform a programme, and war follows around 1640–42 ([[english-war]])."],
  faith=["cranmerian"], office="King of England", basis=R + " The reforming role is the timeline’s reversal.",
  open_q=["How the king’s reign ends: the war’s course after 1642 is not yet fixed."])

E("william-iii", "monarch", "William III of Orange", "prop", "Stadholder 1672–; England c.1688–89", 1688, "Proposed head of a Dutch dynasty in England.",
  ["Canon says a conservative, French-aligned monarchy ends in union under a Dutch dynasty around 1688–89, by marriage and succession, with the date tentative. William of Orange, the historical stadholder, is the natural candidate for the throne."],
  faith=["cranmerian"], office="King of England (proposed)", basis=RH,
  open_q=["Whether the Dutch succession happens in 1688–89 or another year."])

# ---------------------------------------------------------------- Germany

E("maurice-of-saxony", "monarch", "Maurice of Saxony", "hist", "Elector 1547–53", 1547, "Albertine duke who takes the electorate from the Ernestines.",
  ["Maurice besieges Magdeburg in 1550–51 ([[siege-magdeburg]]) and becomes the Philippist electorate’s founder."],
  faith=["cranmerian"], office="Elector of Saxony", basis=R, y2=1553)

E("john-george-i", "monarch", "John George I of Saxony", "hist", "Elector 1611–56", 1611, "Cranmerian elector who leaves the war at Prague in 1635.",
  ["Saxony and Brandenburg make peace with the Emperor at Prague that year, leaving France and Sweden against the Habsburgs."],
  faith=["cranmerian"], office="Elector of Saxony", basis=R, y2=1656)

E("george-william-brandenburg", "monarch", "George William of Brandenburg", "hist", "Elector 1619–40", 1619, "Cranmerian elector who also rules Gnesio-Catholic Prussia.",
  ["Brandenburg takes Cleves and Mark at [[xanten]], and the duke of Prussia as Polish vassal rules a Gnesio-Catholic church. The Prussian church under a Cranmerian elector is a standing contradiction."],
  faith=["cranmerian"], office="Elector of Brandenburg", basis=R, y2=1640)

E("maximilian-i-bavaria", "monarch", "Maximilian I of Bavaria", "hist", "1597–1651", 1620, "Head of the Catholic League, who takes the Palatinate.",
  ["Maximilian’s army wins [[white-mountain]] and he gains the Upper Palatinate."],
  faith=["roman-catholic"], office="Elector of Bavaria", basis=R, y2=1651)

# ---------------------------------------------------------------- East and South

E("michael-romanov", "monarch", "Michael Romanov", "hist", "Tsar 1613–45", 1613, "First Romanov tsar, whose father Filaret rules the church.",
  ["Michael’s father Filaret returns from Polish captivity and becomes patriarch in 1619. The catechism of 1627 comes under this dual rule."],
  faith=["russian-orthodox"], office="Tsar of Russia", basis=R, y2=1645)

E("suleiman", "monarch", "Suleiman I", "hist", "Sultan 1520–66", 1520, "Ottoman sultan who partitions Hungary and conquers Iraq and Yemen.",
  ["Suleiman’s empire takes Rhodes in 1522, Buda in 1541 and Iraq and Yemen by 1550. Ebussuud sets his legal order."],
  faith=["sunni"], office="Ottoman Sultan", basis=R, y2=1566)

E("murad-iv", "monarch", "Murad IV", "hist", "Sultan 1623–40", 1623, "Ottoman sultan who retakes Baghdad in 1638.",
  ["Persia holds Baghdad from 1623 to 1638. Murad’s empire shown in the 1635 map is at war with the Safavids."],
  faith=["sunni"], office="Ottoman Sultan", basis=R, y2=1640)

E("abbas-i", "monarch", "Shah Abbas I", "hist", "Shah 1588–1629", 1588, "Safavid shah who takes Hormuz and Baghdad.",
  ["Abbas holds Hormuz from 1622 and Baghdad from 1623, and builds a Twelver Shia state."],
  faith=["shia"], office="Shah of Persia", basis=R, y2=1629)

E("ahmad-al-mansur", "monarch", "Ahmad al-Mansur", "hist", "Sultan of Morocco 1578–1603", 1591, "Saadian sultan who conquers Songhai in 1591.",
  ["His conquest yields the Pashalik of Timbuktu. After his death the Saadian realm splits between Fez and Marrakesh."],
  faith=["sunni"], office="Sultan of Morocco", basis=R, y2=1603)

E("john-sigismund", "monarch", "John Sigismund Zápolya", "hist", "1540–71", 1568, "King of the eastern Hungarian lands and sponsor of the Edict of Torda.",
  ["John Sigismund protects Unitarian preaching at [[torda]] in 1568. Eastern Hungary becomes the Principality of Transylvania."],
  faith=["unitarian"], office="Prince of Transylvania", basis=R)

E("gabriel-bethlen", "monarch", "Gabriel Bethlen", "hist", "Prince of Transylvania 1613–29", 1619, "Cranmerian prince whose bid for Bohemia was one option in 1619.",
  ["Bethlen was an Ottoman vassal who intervened in the Bohemian war. The estates elect Frederick V rather than him in this timeline."],
  faith=["cranmerian"], office="Prince of Transylvania", basis=R, y2=1629)

E("george-rakoczi-i", "monarch", "George I Rákóczi", "hist", "Prince of Transylvania 1630–48", 1630, "Prince of Transylvania in 1635.",
  ["Rákóczi rules Transylvania as an Ottoman vassal. The principality recognises Roman, Cranmerian and Unitarian churches."],
  faith=["cranmerian"], office="Prince of Transylvania", basis=R, y2=1648)
