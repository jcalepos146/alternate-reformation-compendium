from common import E

R = "Real person."
RH = "Real person in a hypothetical role."
INV = "Invented figure."

# ================================================================ Roman communion

E("julius-ii", "person", "Julius II", "hist", "pope 1503–13", 1503, "The pope who convened Lateran V in 1512.",
  ["Julius II opens the Fifth Lateran Council in 1512 and holds the Papal States together by war. The timeline’s reform agenda starts under him, before any evangelical movement exists."],
  faith=["roman-catholic"], office="Pope", basis=R, y2=1513)

E("leo-x", "person", "Leo X", "hist", "pope 1513–21", 1513, "Medici pope who closes Lateran V and signs the Bologna concordat with France.",
  ["Leo X closes the Lateran Council in 1517 and concludes the [[concordat-of-bologna]] with Francis I in 1516. His court is the target of every later complaint about curial abuses."],
  faith=["roman-catholic"], office="Pope", basis=R, y2=1521)

E("paul-iii", "person", "Paul III", "hist", "pope 1534–49", 1534, "The pope under whom Trent opens, and under whom the softened Session 6 passes.",
  ["Paul III summons the Council of Trent, which opens in 1545. In this timeline its Session 6 in 1547 allows imputed righteousness, and the council is suspended in 1549. He is the last pope in the project’s canon before Urban VIII."],
  faith=["roman-catholic"], office="Pope", basis=R, y2=1549)

E("urban-viii", "person", "Urban VIII", "canon", "pope 1623–44", 1623, "The pope in 1635, shown on the map at Rome.",
  ["Urban VIII sits at Rome while France leads the war against the Habsburgs and Bohemia is returned to Rome in its Utraquist rite. He is the holder of the pope seat on the 1635 map."],
  faith=["roman-catholic"], office="Pope", basis=R, y2=1644)

E("reginald-pole", "person", "Reginald Pole", "prop", "1500–58", 1545, "English cardinal and papal legate, proposed as an architect of the softened Session 6.",
  ["Pole was one of the legates at Trent’s opening and belonged to the Spirituali, the circle that sought a settlement with the evangelicals. In this timeline he is proposed as a driving voice for imputed righteousness in 1547, which is a role history did not give him."],
  faith=["roman-catholic"], office="Cardinal", basis=RH)

E("giovanni-morone", "person", "Giovanni Morone", "prop", "1509–80", 1547, "Cardinal of the Spirituali, proposed as Pole’s ally in 1547.",
  ["Morone was a diplomat of the reforming wing and was later suspected of heresy by the hardliners. Here he is proposed as a negotiator who carries the Session 6 compromise through the council."],
  faith=["roman-catholic"], office="Cardinal", basis=RH)

E("gasparo-contarini", "person", "Gasparo Contarini", "hist", "1483–1542", 1541, "Venetian cardinal and head of the Spirituali, whose Regensburg formula on justification anticipates Session 6.",
  ["Contarini negotiated the formula on double justification at Regensburg in 1541 and died the next year. His text is the model for the compromise that the council adopts in 1547 in this timeline, though he does not live to see it."],
  faith=["roman-catholic"], office="Cardinal", basis=R)

E("cajetan", "person", "Thomas de Vio, Cardinal Cajetan", "hist", "1469–1534", 1518, "Dominican theologian and legate to Germany.",
  ["Cajetan was the senior Thomist of the age and Rome’s legate at Augsburg in 1518. His death in 1534 predates the council. The Thomist rigour he stands for is the main resistance to the Session 6 compromise."],
  faith=["roman-catholic"], office="Cardinal", basis=R)

# ================================================================ Gallican

E("pierre-d-epinac", "person", "Pierre d’Épinac", "canon", "Archbishop of Lyon 1574–99", 1574, "First effective Primate of Lyon.",
  ["D’Épinac gives the Lyon primacy real content: appeals from the French sees, the right to convene the national synod, and a first claim on the Rhineland. He works with the king against the Guise family’s ambitions in the church."],
  faith=["gallican-church"], office="Primate of Lyon", basis=R + " First effective Primate here; the role is canon, the precise acts are proposed.", y2=1599)

E("alphonse-de-richelieu", "person", "Alphonse de Richelieu", "canon", "Archbishop of Lyon 1628–53", 1628, "Cardinal and Primate of the Gauls in 1635, brother of the king’s minister.",
  ["Alphonse de Richelieu is Primate when France leads the war against the Habsburgs as protector of the Lyon-aligned churches. His brother runs royal policy, and the office gains weight across the Rhine."],
  faith=["gallican-church", "gnesio-lyon"], office="Primate of Lyon", basis=R, y2=1653)

E("tournon", "person", "Cardinal François de Tournon", "hist", "1489–1562", 1561, "Senior cardinal at Poissy, who opposed Beza.",
  ["Tournon presided over the Roman side at Poissy and resisted the Reformed speakers. The fact that Poissy partly succeeds in this timeline needs an explanation, and his death in 1562 is one of the hinges."],
  faith=["gallican-church"], office="Cardinal", basis=R,
  open_q=["What explains Poissy’s success despite Tournon’s opposition."])

E("cardinal-of-lorraine", "person", "Charles, Cardinal of Lorraine", "hist", "1524–74", 1561, "Guise archbishop of Reims, rival for primatial authority.",
  ["Charles of Lorraine held Reims with its own primatial claims and represented the Guise party in the church. The king’s support for Lyon is meant partly as a counterweight to him."],
  faith=["gallican-church"], office="Cardinal", basis=R)

E("baius", "person", "Michael Baius", "hist", "1513–89", 1567, "Louvain theologian whose Augustinian teaching Rome censures only lightly.",
  ["Baius taught that fallen nature cannot do good without grace and that concupiscence is sinful. Here Rome censures him lightly and Louvain and Ghent remain Baianist strongholds."],
  faith=["roman-catholic", "gallican-church"], office="Teacher", basis=R)

E("jansen", "person", "Cornelius Jansen", "prop", "1585–1638", 1636, "Louvain Augustinian and bishop of Ypres, proposed as the school’s next great voice.",
  ["Jansen’s Augustinus appeared after his death in 1640 in our history. He is proposed here as a Baianist successor writing for a Roman communion that has never closed the Augustinian question."],
  faith=["roman-catholic"], office="Teacher", basis=RH)

# ================================================================ Gnesio-Catholic

E("flacius", "person", "Matthias Flacius Illyricus", "canon", "1520–75", 1550, "Leader of the Gnesio-Lutherans and printer of the case against the Interims from besieged Magdeburg.",
  ["Flacius rejects the Augsburg and Leipzig Interims and prints the case from Magdeburg. His line of teaching becomes the Gnesio-Catholic church’s inheritance. He dies the same year as the Bohemian union that fixes the church’s name."],
  faith=["gnesio-catholic"], office="Teacher", basis=R)

E("amsdorf", "person", "Nikolaus von Amsdorf", "hist", "1483–1565", 1548, "Luther’s ally and the first evangelical bishop of Naumburg, Gnesio leader.",
  ["Amsdorf holds that the Interims betray the Reformation and is the senior churchman of Ernestine Thuringia. His consecration in 1542 is the kind of episcopal precedent the Gnesio-Catholics later invoke."],
  faith=["gnesio-catholic"], office="Bishop", basis=R)

E("john-frederick-i", "monarch", "John Frederick I of Saxony", "hist", "1503–54", 1547, "Elector who loses his title at Mühlberg and leaves the Ernestines in Thuringia.",
  ["Captured at [[muhlberg]], John Frederick loses the electorate to Maurice. His heirs keep the Thuringian lands, the future Gnesio heartland."],
  faith=["gnesio-catholic"], office="Prince", basis=R)

E("john-william-saxe-weimar", "monarch", "John William of Saxe-Weimar", "hist", "1530–73", 1567, "Ernestine duke whose line is broken by the Grumbach Feud.",
  ["His territory is split after [[grumbach-feud]], with Weimar and Jena staying Gnesio-Catholic and Gotha and Coburg becoming Philippist. The averted purge of Jena by Elector August in 1573 is a point the timeline must handle."],
  faith=["gnesio-independent"], office="Prince", basis=R,
  open_q=["How Elector August’s 1573 purge of Jena is averted."])

E("john-iii-sweden", "monarch", "John III of Sweden", "hist", "1537–92", 1576, "King whose Red Book of 1576 starts Sweden’s road to Gnesio-Catholicism.",
  ["John III’s liturgy, the Red Book ([[red-book]]), leans toward the ancient church. Sweden’s [[uppsala-synod]] of 1593 completes the work after his death."],
  faith=["gnesio-independent"], office="King", basis=R, y2=1592)

E("abraham-angermannus", "person", "Abraham Angermannus", "hist", "c.1540–99", 1593, "Archbishop of Uppsala who presides at the 1593 synod.",
  ["Angermannus leads the church that adopts the Uppsala settlement. Under his archbishopric the Swedish succession is secured for later Gnesio consecrations."],
  faith=["gnesio-independent"], office="Archbishop of Uppsala", basis=R + " His role at 1593 is historical.", y2=1599)

E("albert-of-prussia", "monarch", "Albert of Prussia", "hist", "1490–1568", 1525, "Last Grand Master and first Duke of Prussia, a Polish fief.",
  ["Albert secularises the Teutonic state in 1525 and founds Königsberg’s university. His church is caught up in [[osiander]]’s controversy, then becomes Gnesio-Catholic under Polish overlordship."],
  faith=["evangelical-unaligned", "gnesio-independent"], office="Prince", basis=R)

E("osiander", "person", "Andreas Osiander", "hist", "1498–1552", 1550, "Königsberg theologian whose dispute on justification divides Prussia.",
  ["The Osiandrian controversy is Prussia’s own quarrel, separate from the Philippist–Gnesio split. It keeps the duchy off the German map of parties."],
  faith=["evangelical-unaligned"], office="Teacher", basis=R)

E("wolfgang-wilhelm", "monarch", "Wolfgang Wilhelm of Palatinate-Neuburg", "canon", "1578–1653", 1613, "Prince who turns Gnesio-Catholic in 1613 to win French backing for Jülich.",
  ["Historically he converted to Rome to win Spanish support. Here he converts to the Gnesio-Catholic church under Lyon, takes Jülich and Berg at [[xanten]], and brings the Rhine under the Lyon orbit."],
  faith=["gnesio-lyon"], office="Prince", basis=R + " The conversion is the timeline’s parallel to the historical one.")

# ================================================================ Cranmerian

E("cranmer", "person", "Thomas Cranmer", "canon", "1489–1556", 1549, "Archbishop of Canterbury and convener of the international council at Lambeth.",
  ["Cranmer’s council sits at Lambeth from 1549, with the continental exiles in England ([[lambeth-council]]). His Communion is named for him. What becomes of him in 1556 is not settled in canon."],
  faith=["cranmerian"], office="Archbishop of Canterbury", basis=R + " His later fate is open.", y2=1556,
  open_q=["Whether Cranmer survives Mary’s reign or dies as in history."])

E("melanchthon", "person", "Philip Melanchthon", "hist", "1497–1560", 1548, "Philippist leader whose Leipzig Interim keeps doctrine and yields on ceremonies.",
  ["Melanchthon’s compromise at Leipzig is the origin of the Philippist party and of the name Cranmerian–Philippist Communion. His wing wins the contest with the Gnesio party."],
  faith=["cranmerian"], office="Teacher", basis=R)

E("bucer", "person", "Martin Bucer", "hist", "1491–1551", 1549, "Strasbourg reformer, exile in England and mediating voice at Lambeth.",
  ["Bucer’s mediating theology on the Eucharist suits the Communion’s breadth. He dies at Cambridge in 1551, before the council ends."],
  faith=["cranmerian"], office="Teacher", basis=R)

E("a-lasco", "person", "Jan Łaski (John à Lasco)", "hist", "1499–1560", 1550, "Polish reformer, superintendent of the stranger churches in London.",
  ["Łaski links England, Poland and the Low Countries. The Poles’ later entry into the Communion at [[consensus-of-sandomierz]] follows his line."],
  faith=["cranmerian"], office="Superintendent", basis=R)

E("vermigli", "person", "Peter Martyr Vermigli", "hist", "1499–1562", 1550, "Italian exile at Oxford, theologian of the Lambeth council.",
  ["Vermigli teaches at Oxford and helps draft the Communion’s confession. He is the Italian voice in a council of exiles."],
  faith=["cranmerian"], office="Teacher", basis=R)

E("hemmingsen", "person", "Niels Hemmingsen", "canon", "1513–1600", 1575, "Danish theologian never removed from his chair, so Denmark-Norway joins the Communion.",
  ["Hemmingsen’s teaching puts Denmark-Norway in the Cranmerian–Philippist camp rather than the Gnesio. His survival as a leading voice is the reason for the Scandinavian split between Denmark and Sweden."],
  faith=["cranmerian"], office="Teacher", basis=R)

E("bullinger", "person", "Heinrich Bullinger", "canon", "1504–75", 1550, "Zurich’s leader after Leo Jud, a moderate whose Second Helvetic Confession brings in the Hungarian Reformed.",
  ["With Zwingli dead at Marignano, Zurich reforms late under [[leo-jud]] and Bullinger and leans Philippist. Bullinger’s confession is adopted in Hungary, bringing its Reformed into the Communion."],
  faith=["cranmerian"], office="Antistes of Zurich", basis=R + " His moderate role is canon.")

E("leo-jud", "person", "Leo Jud", "canon", "1482–1542", 1530, "Zwingli’s friend who leads Zurich’s late, moderate reform.",
  ["With Zwingli gone, Jud and then Bullinger reform Zurich a few years late, leaning toward Lutheran views on the Eucharist. Zurich, Basel and moderate Bern join Cranmer."],
  faith=["cranmerian"], office="Pastor", basis=R)

E("brenz", "person", "Johannes Brenz", "hist", "1499–1570", 1548, "Württemberg’s reformer, who resisted the Interim and shapes the Communion’s Lutheran right wing.",
  ["Brenz hid from Spanish garrisons in 1548. His Württemberg ends up the Communion’s Lutheran right wing, with a teaching on the bodily presence that sits uneasily beside Reformed-leaning churches."],
  faith=["cranmerian"], office="Teacher", basis=R)

E("frederick-v", "person", "Frederick V, Elector Palatine", "canon", "1596–1632", 1619, "Cranmerian prince elected king of Bohemia in 1619.",
  ["Elected as a Cranmerian king for a Gnesio-Catholic kingdom, he loses both crowns and the Palatinate to Bavaria after [[white-mountain]]. He dies in 1632. The Lower Palatinate is occupied in 1635."],
  faith=["cranmerian"], office="Prince", basis=R, y2=1632)

E("laud", "person", "William Laud", "prop", "1573–1645", 1633, "Proposed Archbishop of Canterbury from 1633 and chief of the Royalist establishment.",
  ["In our history Laud pushed a high-church line and was executed in 1645. Here the king favours a low-church settlement, so a Laud-style primate is the natural head of the establishment party that lines up with the nobility and the Navy. Canterbury is the senior see of the Communion in the 1635 map but its holder is not named in canon."],
  faith=["cranmerian"], office="Archbishop of Canterbury", basis=RH,
  open_q=["Who holds Canterbury in 1635, and how the king handles an archbishop who opposes him."])

E("comenius", "person", "Jan Amos Comenius", "prop", "1592–1670", 1632, "Bishop of the Unity of the Brethren, a teacher in exile after the defeat of Bohemia.",
  ["Comenius is the last bishop of the Unity in our history and a pedagogue with a European reputation. In this timeline the Brethren belong to the Cranmerian Communion, and he is the obvious voice of the Bohemian exiles."],
  faith=["unity-brethren"], office="Bishop of the Unity", basis=RH)

# ================================================================ Hardline Reformed

E("calvin", "person", "John Calvin", "canon", "1509–64", 1541, "Reformer of Geneva and architect of the hardline Reformed churches.",
  ["The timeline keeps Calvin and Geneva. With no Zwingli, Reformed theology runs through Bucer, Oecolampadius and Calvin. Geneva, with Vaud, becomes the hardline core that refuses Cranmer’s settlement."],
  faith=["hardline-reformed"], office="Pastor of Geneva", basis=R)

E("beza", "person", "Theodore Beza", "canon", "1519–1605", 1561, "Calvin’s successor, who confronts Tournon at Poissy.",
  ["Beza leads the Company of Pastors at Geneva and speaks for the Reformed at [[poissy]], where his case partly succeeds. Geneva remains the centre of the hardline churches after his death."],
  faith=["hardline-reformed"], office="Pastor of Geneva", basis=R, y2=1605)

E("knox", "person", "John Knox", "hist", "1514–72", 1560, "Scottish reformer and architect of the Kirk.",
  ["Knox’s Kirk is hardline Reformed and stays outside Cranmer’s settlement. It does not hold the state: it survives as an underground church, and many of its people go to the New World. James’s accession in 1603 therefore brings a reformist king, not a Kirk, to the senior see of the Communion."],
  faith=["hardline-reformed"], office="Minister", basis=R)

E("andrew-melville", "person", "Andrew Melville", "hist", "1545–1622", 1580, "Scottish presbyterian leader who fights for the Kirk against royal bishops.",
  ["Melville’s presbyterian order sits against the royal bishops. After 1603 his party is driven underground under James ([[james-vi-i]]), and its remnant carries presbyterian order to the New World."],
  faith=["hardline-reformed"], office="Teacher", basis=R)

E("jeanne-d-albret", "monarch", "Jeanne d’Albret", "hist", "1528–72", 1560, "Calvinist queen of Navarre, protector of Béarn.",
  ["Her Béarn remains a hardline refuge long after the Huguenot movement is crushed elsewhere."],
  faith=["hardline-reformed"], office="Prince", basis=R)

# ================================================================ Bohemia

E("harrach", "person", "Ernst Adalbert von Harrach", "canon", "Archbishop of Prague 1623–67", 1623, "Archbishop of Prague when the Utraquist rite is restored to Roman communion.",
  ["Harrach is the leader of the Roman side in Bohemia after White Mountain and the first archbishop of the Utraquist rite in union with Rome."],
  faith=["utraquist-rite"], office="Archbishop of Prague", basis=R, y2=1667)

E("budovec", "person", "Wenceslas Budovec", "hist", "1547–1621", 1618, "Leader of the Bohemian estates, executed in 1621.",
  ["Budovec is the Unity’s lay champion of the Letter of Majesty and the estates’ rights. His death after [[white-mountain]] marks the end of the Bohemian revolt."],
  faith=["unity-brethren", "gnesio-catholic"], office="Estates leader", basis=R)

E("thurn", "person", "Matthias Thurn", "hist", "1567–1640", 1618, "Commander of the Bohemian estates’ army and leader of the Defenestration.",
  ["Thurn leads the estates’ military side of the revolt of 1618 ([[defenestration-1618]]) and escapes after White Mountain."],
  faith=["gnesio-catholic"], office="Commander", basis=R)

# ================================================================ Orthodox and Eastern

E("ivan-iv", "monarch", "Ivan IV", "hist", "1530–84", 1570, "Tsar who starts the Western-Rite experiment in the 1570s.",
  ["After a debate in 1570 with the Brethren minister Jan Rokyta, Ivan grants a charter to settled deportees of Dorpat. It begins as an experiment and becomes the Western-Rite church."],
  faith=["western-rite-orthodox"], office="Tsar", basis=R, y2=1584)

E("job", "person", "Patriarch Job", "hist", "c.1525–1607", 1589, "First Patriarch of Moscow (1589–1605).",
  ["Under Job the Western-Rite church becomes a vicariate under the new Patriarchate."],
  faith=["russian-orthodox"], office="Patriarch of Moscow", basis=R, y2=1605)

E("godunov-boris", "monarch", "Boris Godunov", "hist", "c.1551–1605", 1598, "Tsar whose Westernising policy organises the Western-Rite church.",
  ["Around 1598–1604 Godunov’s policy gives the Western-Rite church its own primate. The church’s fate is tied to the Time of Troubles that follows his death."],
  faith=["western-rite-orthodox"], office="Tsar", basis=R, y2=1605)

E("filaret", "person", "Patriarch Filaret", "canon", "c.1553–1633", 1619, "Patriarch of Moscow and father of the tsar, author of the 1627 catechism.",
  ["Filaret’s hostility is aimed at Rome rather than at Lutherans. After the Polish occupation of Moscow he adopts the Gnesio-flavoured catechism ([[filaret-catechism]]) as an anti-Latin weapon. In our history he demanded the rebaptism of Latin converts in 1620; here chrismation is the rule for the Western-Rite church."],
  faith=["russian-orthodox"], office="Patriarch of Moscow", basis=R, y2=1633)

E("joasaph-i", "person", "Patriarch Joasaph I", "canon", "Patriarch of Moscow 1634–40", 1634, "Patriarch of Moscow in 1635, with Filaret’s catechism in force.",
  ["Joasaph inherits the catechism’s controversy. His seat is shown on the 1635 map with its resistance centred at Kiev."],
  faith=["russian-orthodox"], office="Patriarch of Moscow", basis=R, y2=1640)

E("jeremias-ii", "person", "Jeremias II of Constantinople", "hist", "c.1536–95", 1589, "Ecumenical Patriarch who consecrates the first Patriarch of Moscow.",
  ["Jeremias visits Moscow in 1588–89 and agrees to the Patriarchate. The Greek patriarchs’ later condemnation of Moscow’s catechism has this relationship behind it."],
  faith=["eastern-orthodox"], office="Ecumenical Patriarch", basis=R)

E("cyril-lucaris", "person", "Cyril Lucaris", "canon", "1572–1638", 1620, "Ecumenical Patriarch in 1635, a Reformed-leaning scholar whose confession of 1629 split the Greeks.",
  ["Lucaris sent the Codex Alexandrinus to Charles I in 1627 and issued a Calvin-leaning confession in 1629. He is the model for the Greek reaction to the Russian catechism, and the model for the English Byzantinists’ dream of a Greek ally."],
  faith=["eastern-orthodox"], office="Ecumenical Patriarch", basis=R, y2=1638)

E("peter-mohyla", "person", "Peter Mohyla", "canon", "1596–1647", 1633, "Orthodox Metropolitan of Kiev from 1633, leader of resistance to the catechism.",
  ["In our history Mohyla was the Latinising reformer of the Kiev church. Here he is the bastion against Moscow’s Lutheran formulas, and the mirror image of that earlier figure."],
  faith=["eastern-orthodox"], office="Metropolitan of Kiev (Orthodox)", basis=R, y2=1647)

E("hypatius-pociej", "person", "Hypatius Pociej", "hist", "1541–1613", 1596, "Principal architect of the Union of Brest.",
  ["Pociej negotiates the union of 1596 ([[brest]]) and becomes the first Uniate metropolitan of Kiev."],
  faith=["ruthenian-uniate"], office="Metropolitan of Kiev (Uniate)", basis=R, y2=1613)

E("josyf-rutsky", "person", "Josyf Rutsky", "canon", "Uniate Metropolitan of Kiev 1613–37", 1613, "Uniate Metropolitan of Kiev in 1635.",
  ["Rutsky holds Kiev beside Peter Mohyla’s Orthodox church. His seat is on the 1635 map."],
  faith=["ruthenian-uniate"], office="Metropolitan of Kiev (Uniate)", basis=R, y2=1637)

E("gedeon-balaban", "person", "Gedeon Balaban", "canon", "Orthodox bishop of Lviv", 1596, "Bishop of Lviv who refuses the union.",
  ["Balaban’s Lviv, with its brotherhood, is one of the centres of resistance to Brest. The map marks him as refusing the union."],
  faith=["eastern-orthodox"], office="Bishop of Lviv", basis=R)

E("ostrozky", "person", "Konstanty Ostrozky", "hist", "1526–1608", 1580, "Ruthenian magnate and patron of the Ostroh circle.",
  ["Ostrozky’s academy and press at Ostroh make him the lay champion of Orthodoxy against the union."],
  faith=["eastern-orthodox"], office="Patron", basis=R)

# ================================================================ Anabaptists, Unitarians

E("menno-simons", "person", "Menno Simons", "hist", "1496–1561", 1540, "Dutch organiser of the peaceable Anabaptists.",
  ["The Mennonites carry the radical tradition into the Low Countries. Their communities are shown as dots."],
  faith=["anabaptist"], office="Elder", basis=R)

E("ferenc-david", "person", "Ferenc Dávid", "hist", "1520–79", 1568, "First Unitarian bishop of Transylvania.",
  ["With John Sigismund’s backing he wins recognition for antitrinitarian preaching at Torda ([[torda]]). The Unitarian Church of Transylvania follows him."],
  faith=["unitarian"], office="Bishop of Kolozsvár", basis=R)

E("faustus-socinus", "person", "Faustus Socinus", "hist", "1539–1604", 1580, "Italian theologian of the Polish Brethren.",
  ["Socinus carries the antitrinitarian tradition to Poland and gives the Polish Brethren their theology."],
  faith=["polish-brethren"], office="Teacher", basis=R)

# ================================================================ Islam and Judaism

E("ebussuud", "person", "Ebussuud Efendi", "hist", "1490–1574", 1545, "Ottoman Şeyhülislam who aligns state and religious law.",
  ["Ebussuud serves from 1545 to 1574 and sets the legal order of Suleiman’s empire."],
  faith=["sunni"], office="Şeyhülislam", basis=R, y2=1574)

E("shaykh-bahai", "person", "Shaykh Bahai", "hist", "1547–1621", 1600, "Safavid scholar and statesman under Shah Abbas.",
  ["Shaykh Bahai is the leading scholar of Abbas’s court and a voice of Twelver Shia orthodoxy."],
  faith=["shia"], office="Scholar", basis=R)

E("joseph-karo", "person", "Joseph Karo", "hist", "1488–1575", 1565, "Safed codifier of Jewish law.",
  ["Karo’s Shulchan Aruch is published in 1565. With Moses Isserles’s glosses from Kraków it unites Sephardic and Ashkenazi practice."],
  faith=["judaism"], office="Codifier", basis=R)

E("maharal", "person", "Judah Loew (the Maharal)", "hist", "c.1520–1609", 1580, "Prague rabbi and teacher.",
  ["The Maharal’s Prague sits in the Bohemian crown lands through the revolt of 1618 and its aftermath, with the Jewish community among the city’s large dots on the map."],
  faith=["judaism"], office="Rabbi of Prague", basis=R)

E("susenyos", "monarch", "Susenyos of Ethiopia", "hist", "1572–1632", 1622, "Emperor who converts to Rome in 1622 and abdicates in 1632.",
  ["His Catholic experiment divides the Ethiopian church and ends with abdication."],
  faith=["miaphysite"], office="Emperor", basis=R, y2=1632)
